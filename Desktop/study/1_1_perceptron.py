#!/usr/bin/env python
# coding: utf-8

# # Perceptron

# ## 1. AND

# In[22]:

import numpy as np

def AND(x1, x2):
    W, b = np.array([0.5, 0.5]), -0.7
    x = np.array([x1, x2])
    tmp = np.sum(W*x) + b
    if tmp <= 0:
        return -1
    else:
        return 1
    
print('--- 퍼셉트론으로 구현한 AND 게이트 ---')

for xs in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    y = AND(xs[0], xs[1])
    print(xs, ' : ', y)


# ## 2. NAND

# In[31]:


def NAND(x1, x2):
    W, b = np.array([-0.5, -0.5]), 0.7
    x = np.array([x1, x2])
    tmp = np.sum(W*x) + b
    if tmp <= 0:
        return -1
    else:
        return 1
    
print('--- 퍼셉트론으로 구현한 NAND 게이트 ---')

for xs in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    y = NAND(xs[0], xs[1])
    print(xs, ' : ', y)


# ## 3. OR

# In[34]:


def OR(x1, x2):
    W, b = np.array([0.5, 0.5]), 0.2
    x = np.array([x1, x2])
    tmp = np.sum(W*x) + b
    if tmp <= 0:
        return -1
    else:
        return 1

print('--- 퍼셉트론으로 구현한 OR 게이트 ---')

for xs in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    y = OR(xs[0], xs[1])
    print(xs, ' : ', y)


# ## 4. XOR

# In[35]:


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

for xs in [(-1,-1), (-1,1), (1,-1), (1,1)]:
    y = XOR(xs[0], xs[1])
    print(xs, ' : ', y)