from abc import ABC, abstractmethod
from neutrino_api.controllers.base_controller import BaseController
from typing import List


class EnricherTemplate(ABC):

    @staticmethod
    @abstractmethod
    def enrich(controller: BaseController, data_list: List[str]):
        pass
