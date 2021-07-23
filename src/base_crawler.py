# encoding=utf-8
# Author: Yu-Lun Chiang
# Description: Base crawler for polymorphism

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class BaseCrawler(ABC):
    @abstractmethod
    def getInfo(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def results(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def readJson(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def writeJson(self):
        raise NotImplementedError
