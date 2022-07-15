from .FitModels.base import BaseFitModel
import numpy as np
from scipy.optimize import curve_fit

class Fitting:
    def __init__(self, model: BaseFitModel):
        self.model = model

