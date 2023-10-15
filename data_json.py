from abc import ABC, abstractmethod

class VacanciesInFileJson(ABC):

    @abstractmethod
    def save_to_json(self):
        pass

    @abstractmethod
    def get_json(self):
        pass

    @abstractmethod
    def delete_from_json(self):
        pass

    @abstractmethod
    def formatting_output_data(self, input_list):
        pass

