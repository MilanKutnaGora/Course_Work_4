from abc import ABC, abstractmethod


class GetVacanciesByAPI(ABC):

    @abstractmethod
    def get_city_id(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass