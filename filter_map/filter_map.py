from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        filtered_array = []
        for element in input_array:
            flag, value = func(element)
            if flag:
                filtered_array.append(value)
        return filtered_array

        pass
