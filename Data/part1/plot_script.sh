
python plot_simple.py "26_percent" "K" "Percentage(%)" "Percentage of Nodes Reached(Incomplete Broadcast) starting from Node 26 vs K"
python plot_simple.py "26_time" "K" "Time" "Time required to Complete Broadcast starting from Node 26 vs K"
python plot_simple.py "26_nodesreached" "K" "Nodes Reached" "Number of Copies Made while Simulation starting from Node 26 vs K"
python plot_errorbar.py "avg_percent" "K" "Percentage" "Average Percentage of Nodes Reached(Incomplete Broadcast) for 100 random nodes vs K" 0 99
python plot_errorbar.py "avg_time" "K" "Time" "Average Time for 100 random nodes vs K" 47 99 
