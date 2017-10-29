
python plot_simple.py "26_percent" "Transmission Probability(in %)" "Percentage(%)" "Percentage of Nodes Reached(Incomplete Broadcast) starting from Node 26 vs Transmission Probability(Outside Class)"
python plot_simple.py "26_time" "Transmission Probability(in %)" "Time" "Time to complete broadcast starting from Node 26 vs Transmission Probability(Outside Class)"
python plot_simple.py "26_ginny" "Transmission Probability(in %)" "Ginny Coefficient" "Ginny Coefficient starting from Node 26 vs Transmission Probability(Outside Class)"
python plot_errorbar.py "avg_percent" "Transmission Probability(in %)" "Percentage" "Average Percentage of Nodes Reached(Incomplete Broadcast) for 100 random nodes vs Transmission Probability(Outside Class)" 0 102
python plot_errorbar.py "avg_time" "Transmission Probability(in %)" "Time" "Average Time for 100 random nodes vs Transmission Probability(Outside Class)" 0 74 
python plot_errorbar.py "avg_ginny" "Transmission Probability(in %)" "Ginny Coefficient Value" "Average Ginny Coefficient for 100 random nodes vs Transmission Probability(Outside Class)" 0 101