import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 224851402 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    a = 0.071
    loc = a / 2
    return max(x) / 2 + loc, \
           max(x) / (2 * alpha ** (1/len(x))) + loc
