from gym.envs.registration import register

register(
    id='Safexp-PointGoal3-v0',
    entry_point='utils.point:Env',
    max_episode_steps=1000,
    reward_threshold=10000.0,
)

register(
    id='Safexp-CarGoal3-v0',
    entry_point='utils.car:Env',
    max_episode_steps=1000,
    reward_threshold=10000.0,
)
