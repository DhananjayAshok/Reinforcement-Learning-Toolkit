#Core Imports Here
##############################################################################################

class Action(object):
    """Abstract base action class"""
    def get_action_space():
        """
        Returns a list of all possible actions
        Not always applicable
        """
        raise NotImplementedError

    def print(self):
        return str(self)

# Implement Your Custom Classes Below
##############################################################################################
import numpy as np


class TicTacToe3DAction(Action):
    def get_action_space():
        """
        Returns the list of actions with numbers from 1 through 9
        """
        return [TicTacToe3DAction(i) for i in range(1, 10)]
    
    def __init__(self, inp):
        Action.__init__(self)
        self.act = inp

    def __str__(self):
        return str(self.act)

