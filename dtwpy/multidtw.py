import multiprocessing as mp
import itertools
import numpy as np

from .dtw import dtw

def _dtw_wrapper(arg):
    args, kwargs = arg
    return dtw(*args,**kwargs)

def dtw_distances(signals, **kwargs):
    n_jobs = kwargs.pop('n_jobs',1)
    n_jobs = mp.cpu_count() if n_jobs == -1 else n_jobs
    N = len(signals)
    dist_matrix = np.zeros([N,N])
    indexes = range(N)
    params = zip(itertools.combinations(signals,2),itertools.repeat(kwargs))
    with mp.Pool(processes=n_jobs) as pool:
        distances = pool.map(_dtw_wrapper, params)
    for (i,j), d in zip(itertools.combinations(indexes,2),distances):
        dist_matrix[(i,j)] = d
        dist_matrix[(j,i)] = d
    return dist_matrix

def dtw_medoid(signals,**kwargs):
    dist_matrix = dtw_matrix(signals,**kwargs)
    medoid_index = np.argmin(np.sum(dist_matrix,axis=0))
    return medoid_index