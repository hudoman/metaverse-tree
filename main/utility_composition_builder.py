from typing import List, Any, Dict, Union
from items.utilities._map import (
    all_utilities, 
    utilities_by_category,
    armory_by_specialization_keyed,
    forge_by_specialization_keyed,
    time_warden_by_specialization_keyed
)
from items._space import Space
from items._utility import Utility
from items.enums import Category
import random
import operator
from functools import reduce
import itertools
from main.utils import dict_nested_set_value


class UtilityCompositionBuilder():

    _space_utility_tree: List[Space] = []
    _space_utility_tree_serialized: Dict[str, List[str]] = {}
    _real_space_utility_tree: Dict[str, Any] = {}
    _filter: Dict[str, Any] = {}
    _picked_armories: List[Utility] = []
    _picked_forges: List[Utility] = []
    _picked_time_wardens: List[Utility] = []
    _combined_utilities: List[Utility] = []


    def __init__(self, space_tree: List[Space], filter: Dict[str, Any] = {}):
        self._space_utility_tree = []
        self._space_utility_tree_serialized = {}
        self._real_space_utility_tree = {}
        self._filter = {}
        self._picked_armories = []
        self._picked_forges = []
        self._picked_time_wardens = []
        self._combined_utilities = []

        if not space_tree:
            raise AssertionError("Empty space tree.")
        
        self._space_utility_tree = space_tree
        self._filter = filter

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._combined_utilities):
            utility = self._combined_utilities[self._index]
            self._index += 1
            return utility
        else:
            raise StopIteration
        
    def get_utility_tree(self) -> List[Space]:
        return self._space_utility_tree

    def get_serialized_utility_tree(self) -> Dict[str, Any]:
        return self._space_utility_tree_serialized
        
    def get_real_space_utility_tree(self) -> Dict[str, Any]:
        return self._real_space_utility_tree
    
    def serialize_utility_tree(self) -> Dict[str, Any]:
        for space in self._space_utility_tree:
            space_key = space.get_string_key()
            self._space_utility_tree_serialized[space_key] = []
            for space_or_utility in space.get_composition():
                self._space_utility_tree_serialized[space_key].append(space_or_utility.get_string_key())
    
    def build_real_space_utility_tree(self) -> None:
        tree = {}
        is_first = True
        for space in self._space_utility_tree:
            if is_first:
                tree[space] = {}
                is_first = False
            else:
                dict_nested_set_value(tree, space, {})

            for space_or_utility in space.get_composition():
                dict_nested_set_value(tree, space_or_utility.get_parent(), {space_or_utility: {}})

        self._real_space_utility_tree = tree

    @property
    def total_free_doors(self) -> int:
        total = 0
        for current_space in self._space_utility_tree:
            total += current_space.available_doors()
        return total
    
    def pick_armories(self) -> None:
        filtered_armories: List[Utility] = []
        armories_filter : List[str] = self._filter.get("specialization", {}).get("armory")

        for armory_filter_key in armories_filter:
            filtered_armories.extend(armory_by_specialization_keyed[armory_filter_key])

        all_armories = utilities_by_category[Category.ARMORY]
        if filtered_armories:
            intersected = list(set(all_armories) & set(filtered_armories))
        else:
            intersected = list(set(all_armories))

        random.shuffle(intersected)
        for _ in range(self.total_armories):
            picked_utility = random.choice(intersected)
            self._picked_armories.append(picked_utility)

    def pick_forges(self) -> None:
        filtered_forges: List[Utility] = []
        forges_filter : List[str] = self._filter.get("specialization", {}).get("forge")

        for forge_filter_key in forges_filter:
            filtered_forges.extend(forge_by_specialization_keyed[forge_filter_key])

        all_forges = utilities_by_category[Category.FORGE]
        if filtered_forges:
            intersected = list(set(all_forges) & set(filtered_forges))
        else:
            intersected = list(set(all_forges))

        random.shuffle(intersected)
        for _ in range(self.total_forges):
            picked_utility = random.choice(intersected)
            self._picked_forges.append(picked_utility)

    def pick_time_wardens(self) -> None:
        filtered_time_wardens: List[Utility] = []
        time_wardens_filter : List[str] = self._filter.get("specialization", {}).get("time-warden")

        for time_warden_filter_key in time_wardens_filter:
            filtered_time_wardens.extend(time_warden_by_specialization_keyed[time_warden_filter_key])

        all_time_wardens = utilities_by_category[Category.TIME_WARDEN]
        if filtered_time_wardens:
            intersected = list(set(all_time_wardens) & set(filtered_time_wardens))
        else:
            intersected = list(set(all_time_wardens))

        random.shuffle(intersected)
        for _ in range(self.total_time_wardens):
            picked_utility = random.choice(intersected)
            self._picked_time_wardens.append(picked_utility)

    def init_process_filter(self) -> None:
        self.calculate_total_utilities()
        # self.apply_specialization_filter()
        # self.apply_bonuses_filter()
        self.pick_armories()
        self.pick_forges()
        self.pick_time_wardens()
        self.combine_utilities()

    def combine_utilities(self) -> None:
        # TODO:: apply ordering
        # self.filter_ordering()

        # Zipping lists 
        zipped_utils = list(itertools.zip_longest(self._picked_armories, self._picked_forges, self._picked_time_wardens))
        if zipped_utils:
            zipped_utils = list(reduce(operator.concat, zipped_utils))
            self._combined_utilities = [util for util in zipped_utils if util is not None]

    def calculate_total_utilities(self) -> None:
        focus: Dict[str, Any] = self._filter.get("focus")
        if not focus:
            raise AssertionError("Missing utility focus.")
        total_points = (
            int(focus.get("forge", 0)) +
            int(focus.get("armory", 0)) +
            int(focus.get("time_warden", 0))
        )
        if total_points == 0:
            raise AssertionError("Add at least one of: forge, armory or time_warden focus.")

        focus_forge = int(focus.get("forge", 0)) / total_points
        focus_armory = int(focus.get("armory", 0)) / total_points
        focus_time_warden = int(focus.get("time_warden", 0)) / total_points
        largest_focus = max([focus_forge, focus_armory, focus_time_warden])

        armories_float = self.total_free_doors * focus_armory
        forges_float = self.total_free_doors * focus_forge 
        time_wardens_float = self.total_free_doors * focus_time_warden
        self.total_armories: int = round(armories_float)
        self.total_forges: int = round(forges_float)
        self.total_time_wardens: int = round(time_wardens_float)

        total_occupied = (
            self.total_armories + 
            self.total_forges + 
            self.total_time_wardens
        )
        if total_occupied != self.total_free_doors:
            difference = self.total_free_doors - total_occupied
            if total_occupied > self.total_free_doors:
                if focus_armory == largest_focus:
                    self.total_armories -= difference
                elif focus_forge == largest_focus:
                    self.total_forges -= difference
                elif focus_time_warden == largest_focus:
                    self.total_time_wardens -= difference

            if total_occupied < self.total_free_doors:
                if focus_armory == largest_focus:
                    self.total_armories += difference
                elif focus_forge == largest_focus:
                    self.total_forges += difference
                elif focus_time_warden == largest_focus:
                    self.total_time_wardens += difference
            
    def fill_space_with_random_utility(self):
        random.shuffle(all_utilities)
        for current_space in self._space_utility_tree:
            while current_space.has_available_door():
                random_utility = random.choice(all_utilities)
                utility_obj = random_utility(current_space.get_id(), current_space.get_rarity())
                utility_obj.set_parent(current_space)
                current_space.add(utility_obj)

    def fill_space_with_picked_combined_utility(self):
        utility_id = len(self._space_utility_tree) + 1
        combined_utilities_iterator = iter(self)

        for current_space in self._space_utility_tree:
            while current_space.has_available_door():
                try:
                    utility_class = next(combined_utilities_iterator)
                    utility_obj = utility_class(utility_id, current_space.get_rarity())
                    utility_obj.set_parent(current_space)
                    current_space.add(utility_obj)
                    utility_id += 1
                except StopIteration:
                    break
