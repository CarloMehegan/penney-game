import numpy as np
import os
from tqdm import tqdm

def generate_simulation_results(num_iterations: int,
                                output_filename: str,
                                seed = 123,
                                path: str = "data"
                               ) -> str:
    """
    Simulates shuffling a deck of red and black cards and saves the results as a .npy file.

    Parameters:
    - num_iterations: int, number of times to shuffle the deck and store the result
    - output_filename: str, name of the file to save results (without the .npy extension)
    - seed: optional, seed for reproducibility (default is 123)
    - path: str, optional, the directory where the file will be saved (default is 'fake_data')
    """

    # initialize deck
    red = ['0'] * 26
    black = ['1'] * 26
    deck = black + red
    
    np.random.seed(seed)  # optionally, set seed for reproducibility
    
    # store results
    results = []
    for i in tqdm(range(num_iterations)):
        np.random.shuffle(deck)
        results.append(int(''.join(deck), 2))  # append binary as integer
    
    # ensure the directory exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # construct the full file path
    full_filename = os.path.join(path, output_filename + '.npy')
    
    # save the results to a .npy file
    np.save(full_filename, results)
    
    print(f"Shuffled decks saved to {full_filename}")
    return full_filename