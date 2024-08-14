import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def rescorla_wagner(learning_rate, data):
    v = 0  # initial associative strength
    v_history = [v]  # to track the learning curve
    
    for _, row in data.iterrows():
        time_since_last_post = row['time_since_last_post']
        likes = row['likes']
        
        alpha = learning_rate(time_since_last_post)
        prediction_error = likes - v
        v = v + alpha * prediction_error
        v_history.append(v)
    
    return v_history

def sse(params, data):
    learning_rate = lambda t: params[0] / (1 + params[1] * t)
    predicted = rescorla_wagner(learning_rate, data)
    return np.sum((np.array(predicted[1:]) - data['likes'])**2)

# Simulate some data
np.random.seed(0)
n_posts = 100
time_since_last_post = np.random.exponential(scale=1, size=n_posts)
likes = np.random.poisson(lam=10, size=n_posts)
data = pd.DataFrame({'time_since_last_post': time_since_last_post, 'likes': likes})

# Estimate model parameters
initial_params = [0.1, 0.1]
result = minimize(sse, initial_params, args=(data,))
best_params = result.x
print(f"Best parameters: learning rate scale = {best_params[0]:.3f}, learning rate decay = {best_params[1]:.3f}")

# Define the best fitting learning rate function
best_learning_rate = lambda t: best_params[0] / (1 + best_params[1] * t)

# Assess model fit
predicted = rescorla_wagner(best_learning_rate, data)
plt.figure(figsize=(10, 6))
plt.plot(data['likes'], 'bo', label='Actual Likes')
plt.plot(predicted[1:], 'r-', label='Predicted')
plt.xlabel('Post Number')
plt.ylabel('Number of Likes')
plt.legend()
plt.show()

sse_best = sse(best_params, data)
mean_likes = np.mean(data['likes'])
total_variance = np.sum((data['likes'] - mean_likes)**2)
r_squared = 1 - (sse_best / total_variance)
print(f"Proportion of variance explained: {r_squared:.3f}")
