# dtwpy

DTWpy is a open source Python3 library for fast and parallel computation of Dynamic Time Warping distances and alignments of time series.

This project is a standalone version of the [mlpy](https://github.com/lukauskas/mlpy/tree/master/mlpy/dtw) implementation for Dynamic Time Warping.

Building on top of that implementation, wrapper functions are provided for ease of use.

The package includes a easy to use plotting library for pairwise time series alignment and cost visualization.

#Installation

The package requires Python >=3.3 since it uses the [multiprocessing](https://docs.python.org/3.5/library/multiprocessing.html) package to release the GIL.

The implementation also requires `Cython` so if you do not have it installed you will need to run

```
pip install Cython
```

To compile the dependencies you will have to run the following command

```
python setup_dtw.py build_ext --inplace
```

#Tutorial

A demo showcasing the behavior of the different DTW functions and some time benchmarks is shown [here](http://nbviewer.jupyter.org/github/JJGO/dtw/blob/master/dtw_demo.ipynb)
