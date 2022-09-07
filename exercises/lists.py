class ListExercise:
    @staticmethod
    def max_value(input_list: list[int]) -> int:
        max_value = input_list[0]

        for value in input_list:
            if value > max_value:
                max_value = value

        return max_value

    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return []

        max_value_item = ListExercise.max_value(input_list)

        return list(map(lambda x: max_value_item if x > 0 else x, input_list))

    @staticmethod
    def recursive_search(input_list: list[int], query: int, min: int = 0, max: int = 0) -> int:
        if min > max:
            return -1

        mid = (min + max) // 2

        if input_list[mid] == query:
            return mid
        elif input_list[mid] > query:
            return ListExercise.recursive_search(input_list, query, min, mid - 1)
        else:
            return ListExercise.recursive_search(input_list, query, mid + 1, max)

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        min, max = 0, len(input_list) - 1

        return ListExercise.recursive_search(input_list, query, min, max)
