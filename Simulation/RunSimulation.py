import numpy as np
import os
from tqdm import tqdm
from typing import List

def generate_simulation_results(num_iterations: int,
                                deck: str,
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
    
    # optionally, set seed for reproducibility
    
    # store results
    # Change with array instead of list, lot faster. 
    results = np.empty((num_iterations, 2), dtype=object)
    print(results.shape)
    for i in tqdm(range(num_iterations)):
        np.random.seed(seed+i)
        ndeck = np.random.choice(list(deck), len(deck), replace=False)
        results[i] = [seed+i, int(''.join(ndeck), 2)]  # append binary as integer
    
    return results
#q: getting an error in generate_simulation_results, ValueError at np.random.choice(deck, len(deck), replace=False). a must be 1-dimensional or an integer
#q: I think the issue is that the deck is a string, so we need to convert it to a list.
#q: is there a way to shuffle a string in place? 

def generate_sequence(
        seq: str,
        seed = 123,
    ):
    np.random.seed(seed)
    return np.random.choice(seq, len(seq), replace=False)
    

if __name__ == "__main__":
    # np.random.seed(42)
    red = '1' * 26
    black = '0' * 26
    deck = black + red
    # print(np.random.choice(deck, len(deck), replace=False))
    res = generate_simulation_results(1000000, deck, seed=1)
    print(res)
    print(res[-1])