import abc


class BaseExternalApiInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_info(self):
        raise NotImplementedError
