import sys
sys.path.append("C:\\Users\\hudec\\Dev\\items-composition\\")
from space_composition_builder import SpaceCompositionBuilder
from utility_composition_builder import UtilityCompositionBuilder
from items.utilities.forges import AForge
from items.enums import Rarity
import copy
owned_space = ["space_starter"]

owned_space.extend([
    "space_rare_small_0",
    "space_rare_small_0",
    "space_legendary_large_0",
    "space_rare_small_0",
    "space_epic_small_0",
    "space_rare_small_0",
    "space_rare_small_0",
    "space_rare_small_0",
    "space_epic_small_0",
    "space_epic_small_0"
])

space_comp_builder = SpaceCompositionBuilder(owned_space)
space_comp_builder.build_space_tree()
space_tree = space_comp_builder.get_space_tree()

utility_comp_builder = UtilityCompositionBuilder(copy.deepcopy(space_tree))
utility_comp_builder.fill_space_with_random_utility()
utility_tree1 = utility_comp_builder.get_utility_tree()

filter = {
    "focus" : {
        "forge": 10,
        "armory": 50,
        "time_warden": 99,
    }
}
utility_comp_builder2 = UtilityCompositionBuilder(copy.deepcopy(space_tree), filter)
utility_comp_builder2.init_process_filter()
utility_comp_builder2.fill_space_with_picked_combined_utility()
utility_comp_builder2.build_real_space_utility_tree()

utility_comp_builder2.generate_space_utility_html_table()
real_tree = utility_comp_builder2.get_real_space_utility_tree()
test=True
