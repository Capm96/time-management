import unittest
import datetime
import kronos
from facade import DatabaseFacade
from archiver_csv import CsvArchiver

string_format_time = "%Y-%m-%d %H:%M:%S"


class CsvArchiverTest(unittest.TestCase):
    def test_archive(self):
        facade = DatabaseFacade()
        csv_archiver = CsvArchiver()
        csv_archiver.archive(facade)
