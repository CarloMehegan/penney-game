import numpy as np
import os
from tqdm import tqdm

def generate_simulation_results(num_iterations, output_filename):
    
    data_folder = os.path.join("..", "data")

    # Initialize deck
    red = ['0'] * 26
    black = ['1'] * 26
    deck = black + red
    
    np.random.seed(123) 
    

    results = []
    for _ in tqdm(range(num_iterations)):
        np.random.shuffle(deck)
        results.append(int(''.join(deck), 2))  
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    
    full_filename = os.path.join(data_folder, output_filename + '.npy')
    
    np.save(full_filename, results)
    
    print(f"Results saved to {full_filename}")
    return full_filename

