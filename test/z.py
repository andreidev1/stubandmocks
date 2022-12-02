from dataclasses import dataclass
from typing import List



@dataclass
class Movie:
    imdb_id: str

@dataclass
class Library(object):
    movies: List[Movie]

    def find_movie(self, imdb_id):
        return next(filter(lambda movie: movie.imdb_id == imdb_id, self.movies))



library = Library([Movie('tt1234')])
print(library.find_movie('tt1234').imdb_id)