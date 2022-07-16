import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 100)
y = fitting.FitModels.Polynomial(order=3)().generate_noisy_data(50, x, 0.5, 1.7, 0.3, 0.1)
f = fitting.Fitting(fitting.FitModels.Polynomial(order=3)())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()
