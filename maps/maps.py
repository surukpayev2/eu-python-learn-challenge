from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        from functools import reduce
        def filter_rating_country(x):
            return x["rating_kinopoisk"] != "0" and x["rating_kinopoisk"] != "" and "," in x["country"]

        def rating_extract(x):
            return float(x["rating_kinopoisk"])

        filtered_list_of_movies = list(filter(filter_rating_country, list_of_movies))
        ratings = list(map(rating_extract, filtered_list_of_movies))
        print((list_of_movies[4054]["country"]))
        sum_rating = reduce((lambda x, y: x + y), ratings)
        return sum_rating/len(ratings)
        pass

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        pass
