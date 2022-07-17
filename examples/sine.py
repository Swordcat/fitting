import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)
y = fitting.FitModels.Oscillation.generate_noisy_data(0.1, x, 0.8, 0.1, 0.1, 5)
f = fitting.Fitting(fitting.FitModels.Oscillation())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()


x = np.linspace(0, 40, 1000)
y = fitting.FitModels.SinExpDecay.generate_noisy_data(0.1, x, 0.8, 0.1, 0.1, 5, 8)
f = fitting.Fitting(fitting.FitModels.SinExpDecay())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()

x = np.linspace(0, 40, 1000)
y = fitting.FitModels.SinGaussDecay.generate_noisy_data(0.1, x, 1.6, 0.1, 0.1, 5, 14)
f = fitting.Fitting(fitting.FitModels.SinGaussDecay())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()