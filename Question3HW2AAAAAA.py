#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:54:19 2018

@author: Aslan
"""

class Node:
    """ base class """
    def __init__(self, name, cost, healthindex):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost
        self.healthindex= healthindex

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs, healthindex):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, cost, healthindex)
        self.futureNodes = future_nodes
        self.probs = probs
        self.healthindex = healthindex

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost

    def get_expected_healthindex(self):

        exp_healthindex = self.healthindex  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_healthindex += self.probs[i]*node.get_expected_healthindex()
            i += 1
        return exp_healthindex


class TerminalNode(Node):

    def __init__(self, name, cost, healthindex):
        Node.__init__(self, name, cost, healthindex)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost

    def get_expected_healthindex(self):
        return self.healthindex


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes, healthindex):
        Node.__init__(self, name, cost, healthindex)
        self.futureNode = future_nodes

    def get_expected_costsDN(self):
        """ returns the expected costs of future nodes"""
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes = node.get_expected_cost()
        return outcomes
#I guess you'd probably only need this if you had to find D1 HUI? Looks like we don't need it but may be good
#to have the function available
    def get_expected_utilityDN(self):
        outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcomes = node.get_expected_utility()

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

#the utility probs  are at the end
C2 = ChanceNode('C2', 15, [T1, T2], [0.1, 0.9], 0.2)
C1 = ChanceNode('C1', 0, [C2, T3], [0.4, 0.6], 0.7)
C3 = ChanceNode('C3', 2, [T4, T5], [0.2, 0.8], 0.1)
D1 = DecisionNode('D1', 0, [C1, C3], 0)


print('The Decision Node expected cost is' )
print (D1.get_expected_costsDN())
#we want the expected cost of C1/C3
print('The C1 Node expected cost is')
print(C1.get_expected_cost())
print('The C3 Node expected cost is')
print(C3.get_expected_cost())
#we want the HUI score for C1/C3
print('The C1 Node expected health index score is')
print(C1.get_expected_healthindex())
print('The C3 Node expected health index score is')
print(C3.get_expected_healthindex())

