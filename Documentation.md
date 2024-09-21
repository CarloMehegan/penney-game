# Project Penney

## Overview
Penney's Game is played by two players and one deck of cards. Each player chooses a three-card sequence of colors (i.e. Red or Black) and cards are drawn face-up until one of the selected sequences appear (i.e. RRR, or BRB). Penney's game has two variations. 

The first variation tallies the total number of cards from the initial draw until a chosen sequence appears. All cards in the pile are given to the player whose sequence appears. This is repeated until the deck runs out; any cards remaining in the pile at the end are not tallied.

The second variation counts the number of "tricks" a player scores in a game. Each time a player's sequence appears, their number of tricks increases by 1, repeated until the deck runs out.

Below, you may read the documentation on how our group approached simulating the game, managing/storing our data, and visualizing our data as a heatmap. The project includes four files:

- `RunSimulation.py`
- `DataManagement.py`
- `DataVisualization.py`
- `RunEverything.ipynb`

## RunSimulation.py
The RunSimulation file will simulate the shuffling of decks of cards and save the results as a `.npy` file.

`generate_simulation_results(num_iter, output_filename, path)`

Parameters:
- `num_iter` (`int`): the number of decks to create
- `output_filename` (`str`): the file to save the decks in
- `path` (`str`, optional): the path to save the file in. Defaults to `'data'`

Functionality:
- Creates decks of red and black cards, represented by 52 bits, where `0` is red and `1` is black.
- The 52 bits are shuffled, to represent a random deck with 26 black and 26 red cards.
- Saves the decks as integers and stores them in a `.npy` file.


---

## DataManagement.py
The DataManagement file has several functions associated with storing and processing data for visualization purposes.

`load_process_simulations(path)
`

Parameter:
- `path` (`str`): the path for the

  
Functionality:
- Loads simulation data from specified file
- Converts each integer in file to 52-bit binary string
- Returns a list of the binary strings


`variation1`

Parameters:
- `deck` (`str`): deck of cards as binary sequence
- `player1_sequence` (`str`): 3-bit sequence for player 1
- `player2_sequence` (`str`): 3-bit sequence for player 2

Functionality:
- Initialize card counts and pile size
- Iterates through the deck to check for matches with player sequences
- If match is found, matching player receives cards in pile
- Returns `player1_cards, player2_cards`: the number of **cards** collected by each player

`variation2`

Parameters:
- `deck` (`str`): deck of cards as binary sequence
- `player1_sequence` (`str`): 3-bit sequence for player 1
- `player2_sequence` (`str`): 3-bit sequence for player 2

Functionality:
- Initialize trick counters for both players
- Iterates through deck to check for matches with player sequences
- When a match is found, matching player scores one trick
- Returns `player1_tricks, player2_tricks`: number of **tricks** won by each player


`analyze_all_combinations`

Parameter:
- `simulations`: list of binary strings representing games

Functionality:
- Generates all possible player 1 and player 2 sequence combinations 
- For each unique pair of sequences it simulations both variations of the game for each deck in simulations, counts wins for each player in both variations, and calculates win percentages
- Compiles results into two DataFrames, one for each variation


**combine_past_data**

Parameters:
- `existing_var1` (`pandas.DataFrame`): Existing data for variation 1 for new simulations. 
- `existing_var2` (`pandas.DataFrame`): Existing data for variation 2 for new simulations. 
- `var1_output_name` (`str`): Name for output CSV file for combination of all variation 1 win counts. 
- `var2_output_name` (`str`): Name for output CSV file for combination of all vacation 2 win counts. 
- `folder` (`str`, optional): Path to the folder containing the CSV files to process. Default is `data`.

  
Functionality:
- Initializes combined DataFrames for each variation using existing data
- Sets ‘Sequence 1’ and ‘Sequence 2’ as index
- Iterates through CSV files in folder: reads each CSV, ensures sequences are 3 digits long, determines which variation the file belongs to, updates corresponding combined DataFrame using `update_dataframe` function
- Resets index of combined DataFrames
- Saves updated DataFrames to CSV files 
- Returns the two updated DataFrames 


`update_dataframe`


Parameters:
- `existing_df` (`pandas.DataFrame`): Existing DataFrame to be updated
- `new_df` (`pandas.DataFrame`): DataFrame containing data to be merged


Functionality:
- If the existing DataFrame is empty, it returns the new DataFrame
- Finds common columns between existing and new DataFrames
- Updates existing DataFrame with values from common columns in new DataFrame
- Recalculates the ‘Player 1 Win %’ based on updated win counts 
- Returns updated DataFrame with merged data and recalculated win percentages 



---

## DataVisualization.py


The DataVisualization file helps with generating and saving heatmaps for the probability of player 1 winning for every possible combination of color card sequences. 

`generate_heatmap`

Parameters:
- `data`: This is the DataFrame that contains the total results
- `filename`: Name of the file where the heatmap is saved
- `vmin`, `vmax`: Win percentage value bounds for the color scale in the heatmap
- `title`: Title text of the heatmap 


Functionality:

- Takes dataframe of the total Penney's game simulation
- Creates 8 by 8 matrix comparing Player 1 and Player 2
- Fills the matrix with each of the winning probabilities
- The heatmap is created after visualizing the annotated 8 by 8 matrix
- The dark diagonal on the heatmap is set for the sequences that match
- The heatmap is labeled with proper percentages of player 1 wins for each sequence 
- Darker colors represent a higher winning probability; lighter colors represent a lower winning probability

---

## RunEverything.ipynb
The RunEverything notebook allows you, the FLB, to simply run a few lines of code and produce two heatmaps, along with the corresponding data frames.
