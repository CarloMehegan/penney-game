import numpy as np
import os
from tqdm import tqdm

def generate_simulation_results(num_iterations, output_filename, path=str):
    """
    Simulates shuffling a deck of red and black cards and saves the results as a .npy file.

    Parameters:
    - num_iterations: int, number of times to shuffle the deck and store the result
    - output_filename: str, name of the file to save results (without the .npy extension)
    - path: str, optional, the directory where the file will be saved (default is 'fake_data')
    """

    # Initialize deck
    red = ['0'] * 26
    black = ['1'] * 26
    deck = black + red
    
    np.random.seed(123)  # Optional: Set seed for reproducibility
    
    # Store results
    results = []
    for i in tqdm(range(num_iterations)):
        np.random.shuffle(deck)
        results.append(int(''.join(deck), 2))  # Append binary as integer
    
    # Ensure the directory exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Construct the full file path
    full_filename = os.path.join(path, output_filename + '.npy')
    
    # Save the results to a .npy file
    np.save(full_filename, results)
    
    print(f"Results saved to {full_filename}")
    return full_filename