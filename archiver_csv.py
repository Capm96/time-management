import abc
from archiver import Archiver


class CsvArchiver(Archiver):
    def archive(self, facade):
        """Print one CSV file per-day-of-data from time_management.db"""
        items = facade.get_all_items()
        for item in items:
            if item is not None:
                row = item.split(",")
                print(row[1])
