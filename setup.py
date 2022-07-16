from setuptools import setup, find_packages

setup(name='fitting',
      version='0.0.1',
      description='Basic wrapper around scipy.optimize.curve_fit to make fitting to supported functions easier',
      url='N/A',
      author='Brandur Thorgrimsson',
      author_email='Brandur_thorn@me.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'numpy',
            'scipy',
            'dataclasses_json',
            'matplotlib'
      ],
      package_dir={'fitting': 'fitting'},
      zip_safe=False)