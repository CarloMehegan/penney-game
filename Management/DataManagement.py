import numpy as np
import pandas as pd
import random
import itertools 
import os
from collections import defaultdict
import json
import random
import numpy as np
from time import time
from tqdm import tqdm


def load_process_simulations(file_path): 
    simulations = np.load(file_path)
    def int_to_bit(n):
        binary = bin(n)[2:] 
        return binary.zfill(52)
    binary_simulations = [int_to_bit(sim) for sim in simulations]             
    return binary_simulations

def variation1(deck, player1_sequence, player2_sequence):
    player1_cards = 0
    player2_cards = 0
    pile = 0
    
    for i in range(len(deck) - 2):
        current_sequence = deck[i:i+3]
        pile += 1
        if current_sequence == player1_sequence:
            player1_cards += pile
            pile = 0
        elif current_sequence == player2_sequence:
            player2_cards += pile
            pile = 0 
    return player1_cards, player2_cards


def variation2(deck, player1_sequence, player2_sequence):
    player1_tricks = 0
    player2_tricks = 0
    
    for i in range(len(deck) - 2):
        current_sequence = deck[i:i+3]
        if current_sequence == player1_sequence:
            player1_tricks += 1
        elif current_sequence == player2_sequence:
            player2_tricks += 1
    return player1_tricks, player2_tricks

def analyze_all_combinations(filename):
    all_sequences = [''.join(seq) for seq in itertools.product('01', repeat=3)]
    results_v1 = []
    results_v2 = []

    for p1 in all_sequences:
        for p2 in all_sequences:
            if p1 != p2:
                p1_wins_v1, p2_wins_v1 = 0,0
                p1_wins_v2, p2_wins_v2 = 0,0

                for game in filename:
                    p1_cards_v1, p2_cards_v1 = variation1(game, p1, p2)
                    if p1_cards_v1 > p2_cards_v1:
                        p1_wins_v1 += 1
                    elif p2_cards_v1 > p1_cards_v1:
                        p2_wins_v1 += 1
                
                    p1_cards_v2, p2_cards_v2 = variation2(game, p1, p2)
                    if p1_cards_v2 > p2_cards_v2:
                        p1_wins_v2 += 1
                    elif p2_cards_v2 > p1_cards_v2:
                        p2_wins_v2 += 1
                
                results_v1.append({'Sequence 1': p1, 'Sequence 2': p2, 
                                   'Player 1 Wins': p1_wins_v1, 'Player 2 Wins': p2_wins_v1, 
                                   'Player 1 Win %': round((p1_wins_v1/len(filename))*100,2),
                                   'Player 2 Win %': round((p2_wins_v1/len(filename))*100,2)})
                results_v2.append({'Sequence 1': p1, 'Sequence 2': p2, 
                                   'Player 1 Wins': p1_wins_v2, 'Player 2 Wins': p2_wins_v2, 
                                   'Player 1 Win %': round((p1_wins_v2/len(filename))*100,2),
                                   'Player 2 Win %': round((p2_wins_v2/len(filename))*100,2)})

    aggreg_df1 = pd.DataFrame(results_v1)
    aggreg_df2 = pd.DataFrame(results_v2)
    return aggreg_df1, aggreg_df2


def combine_past_data():
    #read in other csv files in data folder 
    #combine them with current df for each variation 
    #save updated csv files without overwriting
    
    
    