import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

uw = pd.read_csv('https://github.com/aaiken1/fin-data-analysis-python/raw/main/data/zestimatesAndCutoffs_byGeo_uw_2017-10-10_forDataPage.csv')

profile = ProfileReport(uw, title="Pandas Profiling Report for UW Zillow Data")