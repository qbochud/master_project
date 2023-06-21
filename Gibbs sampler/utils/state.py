"""Abstract class representing a state of the Markov process. The
        concrete class must be implemented on a case by cse basis
Author: Michel Bierlaire
Date: Sat Nov  6 14:29:24 2021
"""

from abc import abstractmethod

class State:
    """Abstract class representing a state of the Markov process. The
        concrete class must be implemented on a case by cse basis
    """

    @abstractmethod
    def indicators(self):
        """Returns the indicators associated with the state

        :return: array of indicators
        :rtype: numpy.array()
        """

    @abstractmethod
    def next_state(self):
        """Returns the next state generated by the user defined Markov
            process.  the forward and the backward transition
            probabilities.

        :return: state, pij, pji
        :rtype: State, float, float

        """

    @abstractmethod
    def logweight(self):
        """log of the unnormalized target sampling
            probability.

        :return: log of the weight
        :rtype: float
        """