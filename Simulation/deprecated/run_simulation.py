import numpy as np
from tqdm import tqdm

red = ['0'] * 26
black = ['1'] * 26
deck = black + red

np.random.seed(123)

results = []
for i in tqdm(range(1000000)):
    np.random.shuffle(deck)
    results += [int(''.join(deck),2)]

np.save('results', results)
