from typing import Any, Dict, List


def dict_nested_search(passed_dict, search_key):
    "Recursive search for dict values"
    if search_key in passed_dict: 
        return passed_dict[search_key]
    
    for _, value in passed_dict.items():
        if isinstance(value,dict):
            item = dict_nested_search(value, search_key)
            if item is not None:
                return item
    

def dict_nested_set_value(passed_dict: Dict[Any, Any], lookup_key, update_value: Dict[str, Any]):
    "Recursive search and update dict values"
    if lookup_key in passed_dict: 
        passed_dict[lookup_key].update(update_value)

    for _, value in passed_dict.items():
        if isinstance(value,dict):
            item = dict_nested_set_value(value, lookup_key, update_value)
            if item is not None:
                return item