# fitting
Updated 07/17/2022 by B. Thorgrimsson.

### Dependencies

See **requirements.txt** for the full list. To install all of them, run:

```
pip3 install -r requirements.txt
````

## What's This Package For?

This package is a lightweight wrapper around **scipy.optimize.curve_fit**. 
It's main feature is that for supported fit functions it will automatically 'guess' the initall fitting parameters. 
This package is not available online and should be installed directly from the source folder using
```
pip3 install .
````
To check if everything is working run:
```
pytest
````
Some plotting tests are skipped by default, they can be run with:
```
pytest --run-plotting
````

## What Is In The Repo?

### examples
These are examples showing how to use each supported fitting method as well as how to save figures and results.

    
### fitting

This folder contains the package source code

#### fitting.FitModels

This folder contains the different models supported by the package. Currently supported are
```
Exponential
Fermi
Gaussian
InvCoshSq (Coulomb peaks)
Linear
Lorentzian
Oscillation
SinExpDecay (Sinusoidial Oscillation with exponential decay envelope)
SinGaussDecay (Sinusoidial Oscillation with Gaussian decay envelope)
Polynomial (general n-th order polynomial fitting)
````
Each fit model can be fit directly e.g.
```
popt, perr, pcov = fitting.FitModels.Linear.fit(x,y)
````
Inital guesses are automatically determined but can be overwritten
```
popt, perr, pcov = fitting.FitModels.Linear.fit(x,y, guess=[1,0])
````
Note: the Polynomial model additionally takes an order argument that determine the order of polynomial to be fit
```
popt, perr, pcov = fitting.FitModels.Polynomial(order=3).fit(x,y)
````
#### fitting.Fitting (in file fitting.fit)
class for fitting data to a models that also has minimal support for plotting, saving figures and results. 
This class can be instantiated either with an instance of the model or with a string

```
f = fitting.Fitting(fitting.FitModel.Linear(), guess=None, bounds=None)
````
or
```
f = fitting.Fitting('linear', guess=None, bounds=None)
````
the string is not case-sensitive. 
If guess/bounds are None they automatically determined.
Note instantiating the Fitting class with the string 'Polynomial' results in a 2nd order Polynomial. 
This can be changed by calling the 'set_order' of the model i.e.

```
f = fitting.Fitting('polynomial', guess=None, bounds=None)
f.model.get_order(4)
````
is equivalent to 
```
f = fitting.Fitting(fitting.FitModel.Polynomial(order=4)(), guess=None, bounds=None)
````
Instances of the Fitting class can be used to fit data with
```
popt, perr, pcov = f.fit(x,y)
````
to then plot data and save figure (including raw data, inital guess and final fit)
```
f.plot(x,y, save=True)
````
This will save the figure to the current working directory with the model name as filename.
To get greater control over the location the figure is saved to use the following
```
f.plot(x,y, show=False, save=False)
f.save_figure(xlabel='my x label', ylabel='my y label', title = 'my title', 
              path = 'abs/path/to/file/directory', name = 'figure_name'
````
to save results with error values as a json file
```
f.save_results(path='', name='')
````
if path and name are not supplied current working directory and model name are used
    