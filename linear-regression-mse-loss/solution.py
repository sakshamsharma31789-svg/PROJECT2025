import numpy as np


def mse_loss(input: np.ndarray, target: np.ndarray, reduction: str = "mean") -> float | np.ndarray:
    """
    input:     shape matching target, any shape
    target:    shape matching input, any shape
    reduction: 'mean' | 'sum' | 'none'

    Returns:
        a Python float when reduction is 'mean' or 'sum';
        an array shaped like input when reduction is 'none'
    """
    mse = (input-target)**2
    if reduction == 'mean' :
        return float(np.mean(mse))
    elif reduction == 'sum':
        return float(np.sum(mse))
    elif reduction == "none":
        return mse
    else:
        raise ValueError(f"invalid reduction {reduction}")
        
        

    
    pass
