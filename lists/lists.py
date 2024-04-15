class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if len(input_list) == 0:
            return input_list
        local_max = input_list[0]
        for elem in input_list:
            if elem > local_max:
                local_max = elem
        for elem in input_list:
            if elem > 0:
                elem = local_max
        return input_list
        pass

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def binary_search_recursive(arr: list[int], low: int, high: int, x: int) -> int:
            if high >= low:
                mid = (high + low) // 2
                if mid < len(arr) and arr[mid] == x:
                    return mid
                elif mid < len(arr) and arr[mid] > x:
                    return binary_search_recursive(arr, low, mid - 1, x)
                else:
                    return binary_search_recursive(arr, mid + 1, high, x)
            else:
                return -1
        a = binary_search_recursive(input_list, 0, len(input_list), query)
        return a
        pass
