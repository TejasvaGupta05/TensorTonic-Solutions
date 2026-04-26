import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    abc=False
    if(x.ndim ==1) :
        x=x.reshape(1,-1)
        abc=True
    print(np.array(x).shape)
    ans = np.zeros(x.shape)
    for i in range(len(x)):
        max_val = np.max(x[i])
        sumo = 0
        print(i)
        for j in range(len(x[i])):
            sumo = sumo + np.exp(x[i][j]-max_val)
        
        for j in range(len(x[i])):
            print(np.exp(x[i][j])/sumo)
            ans[i][j] = (np.exp(x[i][j]-max_val)/sumo)
            print(ans[i][j])
    print(abc)
    if(abc==True):
        ans=ans.reshape(-1)
    return ans
    pass