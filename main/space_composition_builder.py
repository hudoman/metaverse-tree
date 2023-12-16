from typing import List
from items.spaces._map import space_class_map
from items._space import Space


class SpaceCompositionBuilder():

    _space_objs: List[Space] = []

    def __init__(self, spaces: List[str]):
        self._space_objs = []
        if not spaces:
            raise AssertionError("Empty spaces list.")
        
        self._index = 1
        for index, space_key in enumerate(spaces):
            self._space_objs.append(space_class_map[space_key](index))

        self._space_objs.sort(key=lambda x: x._priority)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._space_objs):
            space = self._space_objs[self._index]
            self._index += 1
            return space
        else:
            raise StopIteration
    
    def get_space_tree(self) -> List[Space]:
        return self._space_objs
    
    def build_space_tree(self) -> None:
        for current_space in self._space_objs:
            while current_space.has_available_door():
                try:
                    next_space = next(self)
                    next_space.set_parent(current_space)
                    current_space.add(next_space)
                except StopIteration:
                    break
