import unittest
from dataclasses import dataclass
from typing import List, Dict
from unittest.mock import MagicMock



class EmailSystem:
    def sendMail(self, template, distribution_list, info):
        pass

@dataclass
class Movie(object):
    imdb_id: str
    info: Dict


class InfoSource:
    def fetch_info(self, imdb_id):
        pass

@dataclass
class InfoSourceStub(InfoSource):
    info: str

    def fetch_info(self, imdb_id):
        return self.info


# Movie(1, {'plm':'asd'})

@dataclass
class Library(object):
    movies: List[Movie]
    info_source: InfoSource
    emails: EmailSystem

    def find_movie(self, imdb_id):
        return next(filter(lambda movie: movie.imdb_id == imdb_id, self.movies))
    
    def donate(self, imdb_id):
        movie = Movie(imdb_id, self.info_source.fetch_info(imdb_id))
        self.movies.append(movie)
        self.emails.sendMail("New Movie", "All Members", movie.info)


class MyTestCase(unittest.TestCase):
    def test_finds_movie_by_id(self):
        imdb_id = "tt1234"
        movie = Movie(imdb_id, None)
        library = Library([movie], None, None)
        self.assertEqual(imdb_id, library.find_movie(imdb_id).imdb_id)

    def test_adds_movie_to_library_with_movie_info(self):
        imdb_id = "tt1234"
        info = {
            'title' : 'The Abyss',
            'year' : 1989,
            'rating' : 7.6
            }

        library = Library([],  InfoSourceStub(info), EmailSystem())
        library.donate(imdb_id)
        movie = library.find_movie(imdb_id)

        self.assertDictEqual(info, movie.info)


    def test_emails_about_new_movie(self):
        info = {}
        emails = EmailSystem()
        emails.sendMail = MagicMock()
        library = Library([], InfoSourceStub(info), emails)
        library.donate("tt1234")
        emails.sendMail.assert_called_with("New Movie", "All Members", info)
