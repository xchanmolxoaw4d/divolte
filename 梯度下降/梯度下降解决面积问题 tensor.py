import  numpy as np
import math
from    matplotlib import pyplot as plt
import  torch

def f(r):
    g = 9*torch.tan(r)+9*torch.tan(3/4*math.pi-r)
    return g
def drawfig(f):

    x = torch.linspace(1.1/4*math.pi,0.99/2*math.pi,100)
    y = f(x)
    plt.plot(x,y)
    plt.show()

r = torch.tensor([1.16/4*np.pi], requires_grad=True)
optimizer = torch.optim.Adam([r], lr=1e-4)
for step in range(10000):
    pred = f(r)  #1 向前
    optimizer.zero_grad() #归0
    pred.backward()  #向后
    optimizer.step()  #下一步
    if step % 200 == 0:
        print (f'step {step}: r = {r.tolist()}, f(r) = {pred.item()}')
drawfig(f)
