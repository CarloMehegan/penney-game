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


def load_process_simulations(path): 
    simulations = np.load(path)
    def int_to_bit(n):
        binary = bin(n)[2:] 
        return binary.zfill(52)
    binary_simulations = [int_to_bit(sim) for sim in simulations]             
    return binary_simulations

def variation1(deck, player1_sequence, player2_sequence):
    player1_cards = 0
    player2_cards = 0
    pile = 0
    i = 0
    
    while i < len(deck) - 2:
        current_sequence = deck[i:i+3]
        pile += 1
        if current_sequence == player1_sequence:
            player1_cards += pile
            pile = 0
            i += 3
        elif current_sequence == player2_sequence:
            player2_cards += pile
            pile = 0 
            i += 3
        else:
            i += 1
    return player1_cards, player2_cards


def variation2(deck, player1_sequence, player2_sequence):
    player1_tricks = 0
    player2_tricks = 0
    i = 0
    
    while i < len(deck) - 2:
        current_sequence = deck[i:i+3]
        if current_sequence == player1_sequence:
            player1_tricks += 1
            i += 3
        elif current_sequence == player2_sequence:
            player2_tricks += 1
            i += 3
        else:
            i += 1
    return player1_tricks, player2_tricks


def analyze_all_combinations(filename):
    all_sequences = ['{:03b}'.format(i) for i in range(8)]  # Generate sequences as '000', '001', etc.
    results_v1 = []
    results_v2 = []

    for p1 in all_sequences:
        for p2 in all_sequences:
            if p1 != p2:
                p1_wins_v1, p2_wins_v1 = 0, 0
                p1_wins_v2, p2_wins_v2 = 0, 0

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
                
                results_v1.append({
                    'Sequence 1': p1, 
                    'Sequence 2': p2, 
                    'Player 1 Wins': p1_wins_v1, 
                    'Player 2 Wins': p2_wins_v1, 
                    'Player 1 Win %': round((p1_wins_v1/(p1_wins_v1 + p2_wins_v1))*100, 2)
                })
                results_v2.append({
                    'Sequence 1': p1, 
                    'Sequence 2': p2, 
                    'Player 1 Wins': p1_wins_v2, 
                    'Player 2 Wins': p2_wins_v2, 
                    'Player 1 Win %': round((p1_wins_v2/(p1_wins_v2 + p2_wins_v2))*100, 2) 
                })

    aggreg_df1 = pd.DataFrame(results_v1)
    aggreg_df2 = pd.DataFrame(results_v2)

    # Ensure 'Sequence 1' and 'Sequence 2' are treated as strings
    aggreg_df1['Sequence 1'] = aggreg_df1['Sequence 1'].astype(str)
    aggreg_df1['Sequence 2'] = aggreg_df1['Sequence 2'].astype(str)
    aggreg_df2['Sequence 1'] = aggreg_df2['Sequence 1'].astype(str)
    aggreg_df2['Sequence 2'] = aggreg_df2['Sequence 2'].astype(str)

    return aggreg_df1, aggreg_df2

#issue would be in these following functions 

def combine_past_data(existing_var1, existing_var2, var1_output_name, var2_output_name, folder='data'):
    variation1_combined = existing_var1.copy() if existing_var1 is not None else pd.DataFrame()
    variation2_combined = existing_var2.copy() if existing_var2 is not None else pd.DataFrame()
    
    if not variation1_combined.empty:
        variation1_combined.set_index(['Sequence 1', 'Sequence 2'], inplace=True)
    if not variation2_combined.empty:
        variation2_combined.set_index(['Sequence 1', 'Sequence 2'], inplace=True)
    
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder, filename)
            df = pd.read_csv(file_path, dtype={'Sequence 1': str, 'Sequence 2': str})
            
            # Ensure all sequences are 3 digits
            df['Sequence 1'] = df['Sequence 1'].apply(lambda x: x.zfill(3))
            df['Sequence 2'] = df['Sequence 2'].apply(lambda x: x.zfill(3))
            
            df.set_index(['Sequence 1', 'Sequence 2'], inplace=True)
            
            if 'variation1' in filename.lower():
                variation1_combined = update_dataframe(variation1_combined, df)
            elif 'variation2' in filename.lower():
                variation2_combined = update_dataframe(variation2_combined, df)
            else:
                print(f"File {filename} doesn't match any variation pattern.")
    
    variation1_combined.reset_index(inplace=True)
    variation2_combined.reset_index(inplace=True)       
    
    variation1_combined.to_csv(f'{var1_output_name}.csv', index=False)
    variation2_combined.to_csv(f'{var2_output_name}.csv', index=False)
                
    return variation1_combined, variation2_combined

def update_dataframe(existing_df, new_df):
    if existing_df.empty:
        return new_df
    
    common_columns = existing_df.columns.intersection(new_df.columns)
    
    existing_df.update(new_df[common_columns])
    
    total_games = existing_df['Player 1 Wins'] + existing_df['Player 2 Wins']
    existing_df['Player 1 Win %'] = (existing_df['Player 1 Wins'] / total_games * 100).round(2)                    
    
    return existing_df



    

    