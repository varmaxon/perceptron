import pyautogui as pag
import numpy as np
import random
import pandas as pd


class Dataset:
    def __init__(self, dataset_size):
        self.df = pd.DataFrame(columns=['x', 'y', 'result'])
        self.width = pag.size().width
        self.height = pag.size().height
        self.__generate(dataset_size)

    def __define_result(self, x, y):
        if (x < self.width / 2) and (y < self.height / 2):
            return 'LU'
        elif (x < self.width / 2) and (y >= self.height / 2):
            return 'LD'
        elif (x >= self.width / 2) and (y < self.height / 2):
            return 'RU'
        elif (x >= self.width / 2) and (y >= self.height / 2):
            return 'RD'
    
    def __generate(self, dataset_size):
        for i in range(dataset_size):
            x = random.randrange(0, 1920 + 1)
            y = random.randrange(0, 1080 + 1)

            self.df = self.df._append(
                {'x': x, 'y': y, 'result': self.__define_result(x, y)},
                ignore_index = True)


dataset = Dataset(10)
print(dataset.df)
