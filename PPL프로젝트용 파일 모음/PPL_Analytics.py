import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#표 한글, 음수표현 처리
import matplotlib
import matplotlib.font_manager as fm
font_location = 'C:/Windows/Fonts/malgun.ttf'
font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font',family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

ABC = pd.read_excel('ppl_all_brand_category.xlsx')
AP = pd.read_excel('ppl_all_product.xlsx')
# ...
# 진행중 -> 우선 ipynb의 시각화 강화가 먼저.


# cmd에서의 실행 확인을 위한 py파일
# ...