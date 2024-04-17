from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:

        def filter_rating_country(x: dict) -> bool:
            return x["rating_kinopoisk"] != "0" and x["rating_kinopoisk"] != "" and "," in x["country"]

        def rating_extract(x: dict) -> float:
            return float(x["rating_kinopoisk"])

        filtered_list_of_movies = list(filter(filter_rating_country, list_of_movies))
        ratings = list(map(rating_extract, filtered_list_of_movies))
        print((list_of_movies[4054]["country"]))
        sum_rating = reduce((lambda x, y: x + y), ratings)
        return sum_rating / len(ratings)
        pass

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def filter_rating_country(x: dict) -> bool:
            return x["rating_kinopoisk"] != "" and float(x["rating_kinopoisk"]) >= rating

        def count_i_extract(x: dict) -> int:
            count_in_name = 0
            for element in x["name"]:
                if element == "и":
                    count_in_name += 1
            return count_in_name

        filtered_list_of_movies = list(filter(filter_rating_country, list_of_movies))
        all_counts = list(map(count_i_extract, filtered_list_of_movies))
        if len(all_counts) > 0:
            answer = reduce((lambda x, y: x + y), all_counts)
        else:
            answer = 0
        return answer
        pass
