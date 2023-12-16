import sys
sys.path.append("C:\\Users\\hudec\\Dev\\items-composition\\")

from main.utils import dict_nested_search, dict_nested_set_value

dictionary = {
    "key1" : {
        "key2": {
            "key3": {

            }
        },
        "key45" : {
            "keeeey43": {
                "test": 432423
            }

        }
    },
    "somekeeey": {

    }
}

dict_nested_set_value(dictionary, "keeeey43", {"da": 32})

val = dict_nested_search(dictionary, "keeddddeey43")
test=True