import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)
y = fitting.FitModels.Fermi.generate_noisy_data(0.1, x, 0.8, 2, 0.1, 5)
f = fitting.Fitting(fitting.FitModels.Fermi())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()
