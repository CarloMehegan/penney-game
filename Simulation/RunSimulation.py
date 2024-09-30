import numpy as np
import os
from tqdm import tqdm
from typing import List

def generate_simulation_results(num_iterations: int,
                                seq: str,
                                seed = 123,
                               ) -> List[List[int]]:
    """
    Simulates shuffling a deck of red and black cards and saves the results as a .npy file.

    Parameters:
    - num_iterations: int, number of times to shuffle the deck and store the result
    - output_filename: str, name of the file to save results (without the .npy extension)
    - seed: optional, seed for reproducibility (default is 123)
    - path: str, optional, the directory where the file will be saved (default is 'fake_data')
    """

    # initialize deck
    red = ['1'] * 26
    black = ['0'] * 26
    deck = black + red
    
    # optionally, set seed for reproducibility
    
    # store results
    # Change with array instead of list, lot faster. 
    results = np.empty((num_iterations, 2), dtype=object)
    print(results.shape)
    for i in tqdm(range(num_iterations)):
        np.random.seed(seed+i)
        ndeck = np.random.choice(deck, len(deck), replace=False)
        results[i] = [seed+i, int(''.join(ndeck), 2)]  # append binary as integer
    
    # # ensure the directory exists
    # if not os.path.exists(path):
    #     os.makedirs(path)
    
    # # construct the full file path
    # full_filename = os.path.join(path, output_filename + '.npy')
    
    # # save the results to a .npy file
    # np.save(full_filename, results)
    
    # print(f"Shuffled decks saved to {full_filename}")
    return results

if __name__ == "__main__":
    # np.random.seed(42)
    red = '1' * 26
    black = '0' * 26
    deck = black + red
    # print(np.random.choice(deck, len(deck), replace=False))
    res = generate_simulation_results(1000, deck, seed=1)
    print(res)
    print(res[-1])