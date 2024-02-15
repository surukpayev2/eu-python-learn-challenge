class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        local_max = input_list[0]
        for i in range(1, len(input_list)):
            if input_list[i] > local_max:
                local_max = input_list[i]
        for i in range(len(input_list)):
            if input_list[i] > 0:
                input_list[i] = local_max
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
