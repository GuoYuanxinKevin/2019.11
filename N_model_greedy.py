import numpy as np 
import matplotlib.pyplot as plt

rho = 0.95
lambda_1 = 1.3*rho
lambda_2 = 0.4*rho
m_1 = 1
m_2 = 1/2
m_3 = 1
nu = lambda_1 + lambda_2 + m_1 + m_2 + m_3

V = dict()
action = dict()
V_temp = dict()

for i in range(101):
    for j in range(101):
        V[(i,j)] = 0
        action[(i,j)] = 0
        V_temp[(i,j)] = 0


for iteration in range(20000):
    for i in range(0,101):
        for j in range(0,101):
            if i == 0 and j == 0:
                V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
            elif i == 0:
                if V[(i,j)] < V[(i,j-1)]:
                    action[(i,j)] = 1
                    if j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
            elif j == 0:
                if V[(i-1,j)] < V[(i,j)]:
                    action[(i,j)] = 1
                    if i == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if i == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j)]/nu
            else:
                if (m_2 * V[(i-1,j)] + m_3 * V[(i,j)]) < (m_2 * V[(i,j)] + m_3 * V[(i,j-1)]):
                    action[(i,j)] = 1
                    if i == 100 and j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    elif i == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    elif j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + (m_1+m_2)*V[(i-1,j)]/nu + (m_3)*V[(i,j)]/nu
                else:
                    action[(i,j)] = 2
                    if i == 100 and j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    elif i == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    elif j == 100:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    else:
                        V_temp[(i,j)] = i + j + lambda_1*V[(i+1,j)]/nu + lambda_2*V[(i,j+1)]/nu + m_1*V[(i-1,j)]/nu + m_2*V[(i,j)]/nu + m_3*V[(i,j-1)]/nu
                    
    a = V_temp[(0,0)]
    for i in range(0,101):
        for j in range(0,101):
            V[(i,j)] = V_temp[(i,j)] - a

state = (0,0)
event_list = ['arr_1','arr_2','comp_1','comp_2','comp_3']
V = 0
avg_cost_list = []
for i in range(5000000):
    event = np.random.choice(event_list,p=[lambda_1/nu,lambda_2/nu,m_1/nu,m_2/nu,m_3/nu])
    if event == 'arr_1':
        state = (state[0]+1,state[1])
    elif event == 'arr_2':
        state = (state[0],state[1]+1)
    elif event == 'comp_1' and state[0]>0:
        state = (state[0]-1,state[1])
    elif event == 'comp_2':
        if state[0] > 100 and state[1] > 100:
            if action[(100,100)] == 1:
                state = (state[0]-1,state[1])
        elif state[0] > 100:
            if action[(100,state[1])] == 1:
                state = (state[0]-1,state[1])
        elif state[1] > 100:
            if action[(state[0],100)] == 1:
                state = (state[0]-1,state[1])
        elif action[state] == 1:
            state = (state[0]-1,state[1])
    elif event == 'comp_3':
        if state[0] > 100 and state[1] > 100:
            if action[(100,100)] == 2:
                state = (state[0],state[1]-1)
        elif state[0] > 100:
            if action[(100,state[1])] == 2:
                state = (state[0],state[1]-1)
        elif state[1] > 100:
            if action[(state[0],100)] == 2:
                state = (state[0],state[1]-1)
        elif action[state] == 2:
            state = (state[0],state[1]-1)
    V += (state[0] + state[1])
    avg_V = V/(i+1)
    avg_cost_list.append(avg_V)

def MCMC_fixed_policy(alpha,rho):
    lambda_1 = 1.3*rho
    lambda_2 = 0.4*rho
    m_1 = 1
    m_2 = 2
    m_3 = 1
    nu = lambda_1 + lambda_2 + 1/m_1 + 1/m_2 + 1/m_3
    event_list = ['arr_1','arr_2','comp_1','comp_2','comp_3']
    state = [0,0]
    V = 0
    avg_cost_list = []
    for i in range(5000000):
        event = np.random.choice(event_list,p=[lambda_1/nu,lambda_2/nu,1/(m_1*nu),1/(m_2*nu),1/(m_3*nu)])
        if event == 'arr_1' and state[0] <= 100:
            state[0] += 1
        elif event == 'arr_2' and state[1] <= 100:
            state[1] += 1
        elif event == 'comp_1' and state[0]>0:
            state[0] -= 1
        elif event == 'comp_2' and state[0]>alpha:
            state[0] -= 1
        elif event == 'comp_3' and state[1]>0 and state[0] <= alpha:
            state[1] -= 1
        V += (state[0] + state[1])
        avg_V = V/(i+1)
        avg_cost_list.append(avg_V)
    return avg_cost_list

plt.plot(avg_cost_list, label='greedy', lw=2)
policy_10_95 = MCMC_fixed_policy(10,0.95)
plt.plot(policy_10_95, label='fixed:alpha=10', lw=2)
plt.legend()
plt.title('rho=0.95')
plt.show()
            
            
