import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a=np.asarray(a,dtype=float)
    b=np.asarray(b,dtype=float)
    num=np.dot(a,b)
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)
    denom=norm_a*norm_b
    if denom!=0:
        return float(num/denom)
    else:
        return 0.0