# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 01:12:28 2014

@author: rahul
"""

class Ballot:
    '''A Ballot object contains a ranked list of candidates'''
    eliminated_candidates = set()
    
    @classmethod
    def eliminate_candidate(cls, candidate):
        cls.eliminated_candidates.add(candidate)
        
    def __init__(self, candidate_list):
        self.candidates = candidate_list
    
    def next_voted_candidate(self):
        '''function that returns the non eliminated candidate next in rank'''
        for candidate in self.candidates:
            if candidate in Ballot.eliminated_candidates:
                continue
            else:
                return candidate
                
    
    
    