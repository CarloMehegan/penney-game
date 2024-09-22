from Management import DataManagement
from Simulation import RunSimulation
from Visualization import DataVisualization
import numpy as np
import importlib
importlib.reload(DataManagement)
importlib.reload(RunSimulation)
importlib.reload(DataVisualization)

def add_new_sims(iterations, output_filename, seed):
	#creating deck simulations
	sim = RunSimulation.generate_simulation_results(
		iterations,
		output_filename, 
		seed, 
		path='data'
	)
	
	#loading and processing simulations between players
	processed_sims_total = DataManagement.load_process_simulations(sim)
	Variation1, Variation2 = DataManagement.analyze_all_combinations(processed_sims_total)

	#combine new data with past data
	v1_combined, v2_combined = DataManagement.combine_past_data(
		Variation1,
		Variation2,
		'variation1.csv',
		'variation2.csv',
		folder='data'
	)

	#create heatmap with data
	visualization1 = DataVisualization.generate_heatmap(v1_combined, 'Variation1')
	visualization2 = DataVisualization.generate_heatmap(v2_combined, 'Variation2')