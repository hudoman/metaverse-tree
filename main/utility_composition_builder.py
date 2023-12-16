from typing import List, Any, Dict, Union
from items.utilities._map import all_utilities, utilities_by_category
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
    _real_space_utility_tree: Dict[str, Any] = {}
    _html_table: str = ""
    _filter: Dict[str, Any] = {}
    _picked_armories: List[Utility] = []
    _picked_forges: List[Utility] = []
    _picked_time_wardens: List[Utility] = []
    _combined_utilities: List[Utility] = []


    def __init__(self, space_tree: List[Space], filter: Dict[str, Any] = {}):
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
    
    def get_real_space_utility_tree(self) -> Dict[str, Any]:
        return self._real_space_utility_tree
    
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
        all_armories = utilities_by_category[Category.ARMORY]
        intersected = []
        intersected.extend(all_armories)
        random.shuffle(intersected)
        for _ in range(self.total_armories):
            picked_utility = random.choice(intersected)
            self._picked_armories.append(picked_utility)

    def pick_forges(self) -> None:
        all_forges = utilities_by_category[Category.FORGE]
        intersected = []
        intersected.extend(all_forges)
        random.shuffle(intersected)
        for _ in range(self.total_forges):
            picked_utility = random.choice(intersected)
            self._picked_forges.append(picked_utility)

    def pick_time_wardens(self) -> None:
        all_time_wardens = utilities_by_category[Category.TIME_WARDEN]
        intersected = []
        intersected.extend(all_time_wardens)
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
        zipped_utils = list(reduce(operator.concat, zipped_utils))
        self._combined_utilities = [util for util in zipped_utils if util is not None]

    def calculate_total_utilities(self) -> None:
        focus: Dict[str, Any] = self._filter.get("focus")
        if not focus:
            raise AssertionError("Missing utility focus.")
        total_points = (
            focus.get("forge", 0) +
            focus.get("armory", 0) +
            focus.get("time_warden", 0)
        )
        if total_points == 0:
            raise AssertionError("Add at least one of: forge, armory or time_warden focus.")

        focus_forge = self._filter["focus"]["forge"] / total_points
        focus_armory = self._filter["focus"]["armory"] / total_points
        focus_time_warden = self._filter["focus"]["time_warden"] / total_points
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
            difference = total_occupied - self.total_free_doors
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
        utility_id = 0
        for current_space in self._space_utility_tree:
            while current_space.has_available_door():
                try:
                    combined_utilities_iterator = iter(self)
                    utility_class = next(combined_utilities_iterator)
                    utility_obj = utility_class(utility_id, current_space.get_rarity())
                    utility_obj.set_parent(current_space)
                    current_space.add(utility_obj)
                    utility_id += 1
                except StopIteration:
                    break

    def generate_space_utility_html_table(self):
        # total_space = len(self._space_utility_tree)
        
        # total_cells_width = total_space * SPACE_CELLS_WIDTH
        # start_cell = round(total_cells_width / 2)


        self._html_table = '<style>table.generated-space-utility-pyramid {width: 100%;background-color: #ffffff;border-collapse: collapse;border-width: 2px;border-color: #ffcc00;\
  border-style: solid;\
  color: #000000;\
}\
\
table.generated-space-utility-pyramid td, table.generated-space-utility-pyramid th {\
  border-width: 2px;\
  border-color: #ffcc00;\
  border-style: solid;\
  padding: 3px;\
}\
\
table.generated-space-utility-pyramid thead {\
  background-color: #ffcc00;\
}\
</style>\
'
        self._html_table += '<table class="generated-space-utility-pyramid"><tbody>'

        self.iterate_real_tree(self._real_space_utility_tree)

        self._html_table += '</tbody></table>'


        file_html = open("index.html", "w")
        file_html.write(self._html_table)
        file_html.close()

        test=True
    
    def iterate_real_tree(self, tree: Dict[Union[Space, Utility], Dict[Union[Space, Utility], Any] ]):
        for space_or_utility, space_or_utility_children in tree.items():
            self._html_table += f'<tr><td>{space_or_utility}</td>'
            
            # if space_or_utility.get_category() == Category.SPACE:
            #     for _ in range(space_or_utility.get_total_doors()):
            #         self._html_table += '<td></td>'

            self._html_table += '</tr>'

            self._html_table += f'<tr>'
            for space_or_utility_child, _ in space_or_utility_children.items():
                self._html_table += f'<td>{space_or_utility_child}</td>'


            self._html_table += f'</tr>'

            # self.iterate_real_tree(space_or_utility_children)