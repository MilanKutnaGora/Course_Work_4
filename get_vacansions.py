from abc import ABC, abstractmethod

class GetVacancies(ABC):
    @abstractmethod
    def get_all_vac_info(self):
        pass

    @abstractmethod
    def get_vac_by_min_salary(self, salary_minimum):
        pass

    @abstractmethod
    def get_top_n_vacancies_by_sal(self, vac_count):
        pass

    @abstractmethod
    def get_vac_by_keyword(self, keyword):
        pass

    @abstractmethod
    def get_valid_vacancies_with_salary(self):
        pass