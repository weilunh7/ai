import gymnasium as gym
import time
import random

env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset(seed=42)

def choose_action(observation):
   pos,v,ang,rot = observation
   # 0 -> 左移 ; 1 -> 右移
   #if pos > 1 :
   #   if ang < 0 : return 1
   #   if ang > 0 : return 0
   if ang < -0.1 : return 1
   if ang > 0.1 : return 0
   if pos > 1 : return 1
   if pos < -1 :return 0
   return random.randint(0, 1)

for _ in range(200):
   start = time.time()
   env.render()
   action = choose_action(observation)  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)
   print('observation=', observation)
   if terminated or truncated:
      observation, info = env.reset()
      end = time.time()
      print("執行時間：%f 秒" % (end - start))
      print('done')

env.close()