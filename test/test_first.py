import unittest
from dataclasses import dataclass
from typing import List, Dict



@dataclass
class Movie(object):
    imdb_id: str

@dataclass
class Library(object):
    movies: List[Movie]

    def find_movie(self, imdb_id):
        return next(filter(lambda movie: movie.imdb_id == imdb_id, self.movies))
    

class MyTestCase(unittest.TestCase):
    def test_finds_movie_by_id(self):
        imdb_id = "tt1234"
        movie = Movie(imdb_id)
        library = Library([movie])

        self.assertEqual(imdb_id, library.find_movie(imdb_id).imdb_id)
