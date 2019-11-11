import numpy as np 
import matplotlib.pyplot as plt


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

#time = list(range(1,10001))
policy_5_95 = MCMC_fixed_policy(5,0.95)
policy_10_95 = MCMC_fixed_policy(10,0.95)
policy_15_95 = MCMC_fixed_policy(15,0.95)
policy_20_95 = MCMC_fixed_policy(20,0.95)
policy_5_9 = MCMC_fixed_policy(5,0.9)
policy_10_9 = MCMC_fixed_policy(10,0.9)
policy_15_9 = MCMC_fixed_policy(15,0.9)
policy_20_9 = MCMC_fixed_policy(20,0.9)
policy_5_8 = MCMC_fixed_policy(5,0.8)
policy_10_8 = MCMC_fixed_policy(10,0.8)
policy_15_8 = MCMC_fixed_policy(15,0.8)
policy_20_8 = MCMC_fixed_policy(20,0.8)


plt.subplot(131)
plt.plot(policy_5_95, label='alpha=5', lw=2)
plt.plot(policy_10_95, label='alpha=10', lw=2)
plt.plot(policy_15_95, label='alpha=15', lw=2)
plt.plot(policy_20_95, label='alpha=20', lw=2)
plt.legend()
plt.title('rho=0.95')

plt.subplot(132)
plt.plot(policy_5_9, label='alpha=5', lw=2)
plt.plot(policy_10_9, label='alpha=10', lw=2)
plt.plot(policy_15_9, label='alpha=15', lw=2)
plt.plot(policy_20_9, label='alpha=20', lw=2)
plt.legend()
plt.title('rho=0.9')

plt.subplot(133)
plt.plot(policy_5_8, label='alpha=5', lw=2)
plt.plot(policy_10_8, label='alpha=10', lw=2)
plt.plot(policy_15_8, label='alpha=15', lw=2)
plt.plot(policy_20_8, label='alpha=20', lw=2)
plt.legend()
plt.title('rho=0.8')

plt.show()


