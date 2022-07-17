import fitting
import numpy as np

x = np.linspace(-20, 20, 1000)
y = fitting.FitModels.Lorentzian.generate_noisy_data(0.1, x, 0.8, 2, 0.1, 5)
f = fitting.Fitting(fitting.FitModels.Lorentzian())
popt, perr, pcov = f.fit(x, y, plot=False)
f.save_result()