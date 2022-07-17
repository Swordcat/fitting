from .FitModels import Fermi, Gaussian, InvCoshSq, Linear, Lorentzian, Oscillation, Polynomial, SinExpDecay, SinGaussDecay


REGISTERED_MODELS = [
    Fermi,
    Gaussian,
    InvCoshSq,
    Linear,
    Lorentzian,
    Oscillation,
    Polynomial(),
    SinExpDecay,
    SinGaussDecay
]


class ModelRegistry:
    def __init__(self, registered_models):
        self.models = {model.__name__: model for model in registered_models}

    def get(self, name):
        if name not in self.models:
            raise ValueError(f"Fitting model {name} not found")
        return self.models[name]


model_registry = ModelRegistry(REGISTERED_MODELS)
