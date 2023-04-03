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
    loc = 2 * x.mean() - a
    scale = np.sqrt(np.var(2 * x - a)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
