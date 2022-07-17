import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 40, 1000)
y = fitting.FitModels.Exponential.generate_noisy_data(1, x, 10, 1, 1)
f = fitting.Fitting(fitting.FitModels.Exponential())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()
