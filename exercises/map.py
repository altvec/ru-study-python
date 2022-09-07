from typing import Union


class MapExercise:
    @staticmethod
    def movies_rated_by_kinoposik(movies: list[dict], rating: Union[float, int] = 0) -> list:
        return [
            movie
            for movie in movies
            if movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) > rating
        ]

    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        rated_movies = MapExercise.movies_rated_by_kinoposik(list_of_movies)
        selected_movies = list(filter(lambda m: len(m["country"].split(",")) >= 2, rated_movies))
        ratings = [float(movie["rating_kinopoisk"]) for movie in selected_movies]

        return sum(ratings) / len(selected_movies)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        rated_movies = MapExercise.movies_rated_by_kinoposik(list_of_movies, rating)

        return sum(map(lambda m: m["name"].count("и"), rated_movies))
