import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10, 20, 100)
y = fitting.FitModels.Linear.generate_noisy_data(4, x, 5, 11)
f = fitting.Fitting(fitting.FitModels.Linear())
popt, perr, pcov = f.fit(x, y, plot=True)
plt.show()
