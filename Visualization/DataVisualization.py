import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


def generate_heatmap(data: pd.DataFrame, filename: str, vmin: float = 0.0, vmax: float = 100.0, 
                     title: str = ''):
    '''
    Generate a heatmap of winning probabilities for each player combination of color sequences.

    Args:
        data: DataFrame with the simulation data.
        filename: Filename for generated heatmap (without extension).
        vmin, vmax: Value bounds for the heatmap.
        title: Title to display on the generated heatmap.
    '''

    # Round total_games down to the nearest hundred
    # (To account for ties, and the fact that each variation has a diff number of ties)
    total_games = math.floor((data.iloc[0]['Player 1 Wins'] + data.iloc[0]['Player 2 Wins']) / 100) * 100

    # Update the title with the total games
    title += f'Player 1 Win Percentage (Total Non-Tie Games, Approx.: {total_games})'

    # mean() is redundant here
    # This mainly exists for readability later on
    probs = data[['Sequence 1', 'Sequence 2', 'Player 1 Win %']].groupby(['Sequence 1', 'Sequence 2']).mean()
    
    seqs = ['000', '001', '010', '011', '100', '101', '110', '111'] # All possible color sequences
    matrix = np.zeros((8,8)) # For storing probabilities

    # Fill matrix
    for p1_idx, p1_seq in enumerate(seqs):
        for p2_idx, p2_seq in enumerate(seqs):
            if p1_seq == p2_seq:
                # Make duplicate sequence pairs nan values (to be black on heatmap later)
                matrix[p1_idx][p2_idx] = np.nan
                continue
                
            matrix[p1_idx][p2_idx] = probs.loc[(p1_seq, p2_seq)].values[0]

    # Generate heatmap
    seqs = ['RRR', 'RRB', 'RBR', 'RBB', 'BRR', 'BRB', 'BBR', 'BBB'] # All possible color sequences (but in letters)
    plt.figure(figsize=(9,9))
    ax = sns.heatmap(np.flip(matrix, axis=0), 
                     annot=True, fmt='.2f', cmap='Blues',
                     vmin=vmin, vmax=vmax, cbar_kws={'format': '%.0f%%'},
                     xticklabels=seqs,
                     yticklabels=np.flip(seqs))
    ax.set_facecolor('black') # Make diagonal black
    for t in ax.texts: t.set_text(t.get_text() + "%") # Add % after each annotation text
    
    plt.title(title)
    plt.xlabel('Player 2 Sequence')
    plt.ylabel('Player 1 Sequence')
    
    # Save heatmap
    full_filename = f'figures/{filename}.png'
    ax.get_figure().savefig(full_filename)
    
    print(f'<> {full_filename} saved <>')
    
    return full_filename
