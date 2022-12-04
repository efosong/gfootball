# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from . import *


def build_scenario(builder):
    builder.config().game_duration = 1024
    builder.config().right_team_difficulty = 0.05
    builder.config().deterministic = False
    builder.config().offsides = False
    builder.config().end_episode_on_out_of_play = True

    first_team = Team.e_Left
    second_team = Team.e_Right

    builder.SetTeam(first_team)
    builder.AddPlayer(-1.00, 0.00, e_PlayerRole_GK, controllable=False)
    builder.AddPlayer(0.00, 0.02, e_PlayerRole_RM)
    builder.AddPlayer(0.00, -0.02, e_PlayerRole_LM)
    builder.AddPlayer(-0.60, -0.25, e_PlayerRole_LB)
    builder.AddPlayer(-0.60, 0.25, e_PlayerRole_CB)

    builder.SetTeam(second_team)
    builder.AddPlayer(-1.00, 0.00, e_PlayerRole_GK, controllable=False)
    builder.AddPlayer(-0.10, 0.08, e_PlayerRole_RM)
    builder.AddPlayer(-0.10, -0.08, e_PlayerRole_CF)
    builder.AddPlayer(-0.60, -0.25, e_PlayerRole_LB)
    builder.AddPlayer(-0.60, 0.25, e_PlayerRole_CB)
