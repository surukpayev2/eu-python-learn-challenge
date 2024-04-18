from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        filtered_array = []
        for element in input_array:
            a = func(element)
            if a[0]:
                filtered_array.append(a[1])
        return filtered_array

        pass
