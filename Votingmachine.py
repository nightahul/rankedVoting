# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 01:09:24 2014

@author: rahul
"""
from Ballot import Ballot


class Votingmachine:
    def __init__(self, filename):
        '''initialises the voting machine'''
        self.ballots = self.ballotGenerator(filename)
        self.number_of_rounds = 0 #number of rounds of counting to determine the winner
        self.candidate_names = self.candidates()
        self.winner = self.find_winner()
        print 'Election is won by',self.winner
        
    def ballotGenerator(self, filename):
        ballotList = []
        with open(filename, 'r') as f:
            for line in f:
                linesplit = line.split(',')
                linesplit = [name.strip() for name in linesplit]
                ballotList.append(Ballot(linesplit))
        return ballotList
        
    def candidates(self):
        candidate_names = set()
        for ballot in self.ballots:
            for name in ballot.candidates:
                candidate_names.add(name)
        return candidate_names
        
    def count_votes(self):
        votes = dict()
        for candidate in self.candidate_names:
            if candidate in Ballot.eliminated_candidates:
                continue
            votes[candidate] = 0
        for ballot in self.ballots:
            candidate = ballot.next_voted_candidate()
            if candidate is not None:
                votes[candidate]+=1
        return votes
        
    def find_max(self, votes):
        try:
            best_candidate = max(votes, key = lambda x:votes.get(x))
        except:
            best_candidate = None
        return best_candidate
        
    def find_min(self, votes):
        return min(votes, key = lambda x:votes.get(x))
        
    def find_winner(self):
        winning_votes = len(self.ballots)/2 +1
        num_rounds = 0
        while True:
            num_rounds+=1
            votes = self.count_votes()
            print votes
            best_candidate = self.find_max(votes)
            if best_candidate is None:
                break
            if votes[best_candidate] >=winning_votes:
                self.number_of_rounds = num_rounds
                return best_candidate
            else:
                worst_candidate = self.find_min(votes)
                '''
                there may be more than one candidates with minimum votes but
                worst returns only one
                delete all those candidates
                '''
                worst_votes = votes[worst_candidate]
                for candidate in votes:
                    if votes[candidate]==worst_votes:
                        Ballot.eliminate_candidate(candidate)
                        
            
            
                