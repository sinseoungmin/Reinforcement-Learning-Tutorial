import tensorflow as tf
import gym
from gym.envs.registration import register
import readchar

# macros
LEFT = 0
DOWN = 1
RIGHT = 2
UP =3

# key mapping
arrow_keys = {
    '\x1b[A': UP,
    '\x1b[B': DOWN,
    '\x1b[C': RIGHT,
    '\x1b[D': LEFT,
}

register(
    id = 'FrozenLake-v3',
    entry_point = 'gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')
env.render()

state = env.reset()
while True:
    # choose an action from keyboard
    key = readchar.readkey()
    if key not in arrow_keys.keys():
        print(key)
        print('game aborted!')
        break

    action = arrow_keys[key]
    state, reward, done, info = env.step(action)
    env.render()
    print('state: ', state, 'action: ', action, 'reward: ', reward, 'info: ', info)

    if done:
        print('finished with reward: ', reward)
        break