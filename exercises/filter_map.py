from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции,).
        Если первый элемент кортежа истина, то результат добавляется в список.

        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        :param func: Функция, применяемая к каждому элементу списка.
        :param input_array: Исходный список.
        :return: Отфильтрованный список.
        """
        modified_input_array = map(func, input_array)
        return [item[1] for item in modified_input_array if item[0]]
