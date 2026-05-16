import random
import matplotlib.pyplot as plt
price = 100
price_list_history = []
price_list_history.append(price)
for i in range(1000):
    simulation_price = 100
    for j in range(365):
        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            simulation_price = simulation_price*1.01
        else:
            simulation_price = simulation_price*0.99
    price_list_history.append(simulation_price)
plt.hist(price_list_history)
plt.show()