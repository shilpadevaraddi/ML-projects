from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class pipeStep(BaseEstimator, TransformerMixin):
    def __init__(self, step_func):
        self.step_func = step_func
    def fit(self, *args):
        return self
    def transform(self, X):
        return self.step_func(X)
    
    
def dataSlicing(data):
    return data[['odor','gill-size','spore-print-color','stalk-color-below-ring']]

def dataOhe(df):
    data = pd.get_dummies(df, drop_first = True)
    return data