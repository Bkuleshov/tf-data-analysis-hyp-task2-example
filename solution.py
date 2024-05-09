import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 818742406 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
  return ks_2samp(x, y).pvalue < 0.05
