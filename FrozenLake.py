import gym
from gym.envs.registration import register
import sys, tty, termios

class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(3)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

inKey = _Getch()

#MACiROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
arrow_keys = {
	'\x1b[A': UP,
	'\x1b[B': DOWN,
	'\x1b[C': RIGHT,
	'\x1b[D': LEFT}

# Register FrozenLake with is_slippery False
register(
	id='FrozenLake-v3',
	entry_point='gym.envs.toy_text:FrozenLakeEnv',
	kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make("FrozenLake-v3")
observation = env.reset()
env.render() # show the initial board

while True:
	# Choose an action from keyborard
	key = inKey()
	if key not in arrow_keys.keys():
		print("Game aborted!")
		break

	action = arrow_keys[key]
	state, reward, done, info = env.step(action)
	env.render() # S/how the board after action

	print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

	if done:
		print("Finished with reward", reward)
		break

