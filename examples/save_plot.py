import fitting
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 1000)
y = fitting.FitModels.Lorentzian.generate_noisy_data(0.1, x, 0.8, 2, 0.1, 5)
f = fitting.Fitting(fitting.FitModels.Lorentzian())
popt, perr, pcov = f.fit(x, y, plot=False)
f.plot(x, y, show=True, save=False)
# as no path is supplied the figure is save to the current working directory
f.save_figure('x label (units)', 'y label (units)', 'title')