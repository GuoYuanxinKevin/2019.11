import numpy as np 
import matplotlib.pyplot as plt

rho = 0.8
lambda_1 = 1.3*rho
lambda_2 = 0.4*rho
m_1 = 1
m_2 = 1/2
m_3 = 1
nu = lambda_1 + lambda_2 + m_1 + m_2 + m_3

V = dict()
action = dict()
V_temp = dict()

for i in range(31):
    for j in range(31):
        V[(i,j)] = 0
        action[(i,j)] = 0
        V_temp[(i,j)] = 0


for iteration in range(1000):
    for i in range(0,31):
        for j in range(0,31):
            if i == 0 and j == 0:
                V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
            elif i == 0:
                if V[(i,j)] < V[(i,j-1)]:
                    action[(i,j)] = 1
                    if j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
            elif j == 0:
                if V[(i-1,j)] < V[(i,j)]:
                    action[(i,j)] = 1
                    if i == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if i == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j)]/nu
            else:
                if (m_2 * V[(i-1,j)] + m_3 * V[(i,j)]) < (m_2 * V[(i,j)] + m_3 * V[(i,j-1)]):
                    action[(i,j)] = 1
                    if i == 30 and j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    elif i == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    elif j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if i == 30 and j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    elif i == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    elif j == 30:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    
    a = V_temp[(0,0)]
    for i in range(0,31):
        for j in range(0,31):
            V[(i,j)] = V_temp[(i,j)] - a


for i in range(1,30):
    for j in range(1,30):
        print(i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu - V[(i,j)])
                    

                
