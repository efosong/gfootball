from . import *
import numpy as np

# TODO how to set a random seed?
def build_scenario(builder):
    builder.config().game_duration = 400
    builder.config().deterministic = False
    builder.config().offsides = False
    builder.config().end_episode_on_score = True
    builder.config().end_episode_on_out_of_play = True
    builder.config().end_episode_on_possession_change = True
    
    # Defence Team
    builder.SetTeam(Team.e_Left)
    builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK, controllable=False)
    # Left Back
    spawn_box_LB = [-0.33, -0.05], [-0.75, -0.33]
    location_LB = np.random.uniform(*spawn_box_LB)
    builder.AddPlayer(*location_LB, e_PlayerRole_LB)
    # Right Back
    spawn_box_RB = [-0.33, 0.05], [-0.75, 0.33]
    location_RB = np.random.uniform(*spawn_box_RB)
    builder.AddPlayer(*location_RB, e_PlayerRole_RB)
        
    # Attack Team
    builder.SetTeam(Team.e_Right)
    builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK, controllable=False)
    # Left Mid
    spawn_box_LM = [0, -0.05], [0.3, -0.33]
    location_LM = np.random.uniform(*spawn_box_LM)
    builder.AddPlayer(*location_LM, e_PlayerRole_LM)
    # Right Mid
    spawn_box_RM = [0, 0.05], [0.3, 0.33]
    location_RM = np.random.uniform(*spawn_box_RM)
    builder.AddPlayer(*location_RM, e_PlayerRole_RM)
    # Spawn the ball
    # choose one of the attackers to give the ball at random
    if np.random.random() > 0.5:
        location_ball = -(location_LM[0]+0.05), -location_LM[1]
    else:
        location_ball = -(location_RM[0]+0.05), -location_RM[1]
    builder.SetBallPosition(*location_ball)