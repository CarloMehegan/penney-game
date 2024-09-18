how do i finish up the sim part? whats left?

what we currently store
- how each p1 and p2 variation scores, counting the wins

what do we need to store from each simulation?
- random seed
- deck
- how each p1 and p2 variation scores
- how many points they get
- how many tricks they get
- how many games played for each variation

what do we need for heatmaps?
- p1's average points for each variation
- p1's average tricks for each variation
- p1's win ratio for each variation

what does data management need to do?
- take the simulated game data, and get the averages and ratios for the heatmaps
- if we already have games parsed, we should be able to take new sims and parse only those and append the new data

what does viz need to do?
- read the average/ratio numbers and make the heatmaps

what does sim need to do?
- get all that data into json or probably numpy format
- check for previous data, and if it exists, append to that. if it doesnt exist, create a new file

how do we bring these things together?
- create three interface functions
	- 1. `new_sims(seed, iterations)`
	- 2. `parse_sims()`
	- 3. `make_heatmap(type_of_heatmap)`
- maybe `parse_sims` always runs after `new_sims`; do we need to store unparsed data?
- wrap all three into a python script that takes a command line argument
	- `python penney.py --new-sims=1000`
		- "running sims... done!"
		- "parsing data... done!"
		- "creating heatmap.. done!"
		- "view heatmap in assets/.."
	- and then the heatmap would show up in files
