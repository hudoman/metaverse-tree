from main.space_composition_builder import SpaceCompositionBuilder
from main.utility_composition_builder import UtilityCompositionBuilder
from items.spaces._map import space_class_map
from items.utilities._map import all_utilities
from items.enums import Rarity
import json

class MetaverseUtilityView():
    
    def get_object(self, request):
        try:
            owned_space = ["space_tiny_common"]

            focus_dict = json.loads(request.get("focus", '{}'))
            specialization_dict = json.loads(request.get("specialization", '{}'))
            filter = {
                "focus" : focus_dict,
                "specialization": specialization_dict
            }

            spaces_dict = json.loads(request.get("spaces", '{}'))
            for space_key, space_value in spaces_dict.items():
                space_count = space_value.get("count", 0)
                for _ in range(space_count):
                    owned_space.append(space_key)

            space_comp_builder = SpaceCompositionBuilder(owned_space)
            space_comp_builder.build_space_tree()
            space_tree = space_comp_builder.get_space_tree()

            utility_comp_builder = UtilityCompositionBuilder(space_tree, filter)
            utility_comp_builder.init_process_filter()
            utility_comp_builder.fill_space_with_picked_combined_utility()
            utility_comp_builder.serialize_utility_tree()
            return utility_comp_builder.get_serialized_utility_tree()
        except AssertionError as error:
            raise error

    def get(self, request):
        # request

        request = {
            "focus" : {focus_dict},
            "specialization": {specialization_dict}
        }

        space_utility_tree = self.get_object(request)
        return space_utility_tree
    

class ItemsMetadataView():


    def get_object(self):
        try:
            index = 1
            space_and_utilities_serialized = {}

            for space in space_class_map.values():
                space_obj = space(index)
                space_and_utilities_serialized.update(
                    {space_obj.get_string_repr(): vars(space_obj)}
                )
                index += 1

            for rarity in Rarity:
                for utility in all_utilities:
                    utility_obj = utility(index, rarity)
                    space_and_utilities_serialized.update(
                        {utility_obj.get_string_repr(): vars(utility_obj)}
                    )
                    index += 1

            return space_and_utilities_serialized
        except AssertionError as error:
            raise Exception('Exception occured during metadata load. Error: ') from error

    def get(self):
        space_utility_tree = self.get_object()
        return space_utility_tree