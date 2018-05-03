from gym.envs.registration import register

register(
    id='grid-v0',
    entry_point='gym_grid.envs:GridEnv',
)

register(
    id='grid-v1',
    entry_point='gym_grid.envs:GridEnvB',
)

register(
    id='grid-v2',
    entry_point='gym_grid.envs:GridEnvC',
)