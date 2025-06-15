import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = {}

    flattend_matrix = np.array(list)
    matrix = flattend_matrix.reshape(3, 3)
    
    # calculate mean
    mean_rows = matrix.mean(axis=0).tolist()
    mean_cols = matrix.mean(axis=1).tolist()
    mean_flat = flattend_matrix.mean().tolist()

    # calculate variance
    variance_rows = matrix.var(axis=0).tolist()
    variance_cols = matrix.var(axis=1).tolist()
    variance_flat = matrix.var().tolist()

    # std deviation
    std_dev_rows = matrix.std(axis=0).tolist()
    std_dev_cols = matrix.std(axis=1).tolist()
    std_dev_flat = matrix.std().tolist()

    # max
    max_rows = matrix.max(axis=0).tolist()
    max_cols = matrix.max(axis=1).tolist()
    max_flat = matrix.max().tolist()

    # min
    min_rows = matrix.min(axis=0).tolist()
    min_cols = matrix.min(axis=1).tolist()
    min_flat = matrix.min().tolist()

    # sum
    sum_rows = matrix.sum(axis=0).tolist()
    sum_cols = matrix.sum(axis=1).tolist()
    sum_flat = matrix.sum().tolist()
    
    calculations['mean'] = [mean_rows, mean_cols, mean_flat]
    calculations['variance'] = [variance_rows, variance_cols, variance_flat]
    calculations['standard deviation'] = [std_dev_rows, std_dev_cols, std_dev_flat]
    calculations['max'] = [max_rows, max_cols, max_flat]
    calculations['min'] = [min_rows, min_cols, min_flat]
    calculations['sum'] = [sum_rows, sum_cols, sum_flat]

    return calculations