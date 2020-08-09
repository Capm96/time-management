import abc


class Archiver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def archive(self, facade):
        """Print one file-per-day-of-data from time_management.db"""
