# Network-Broadcast-on-a-time-varying-ad-hoc-network

The project analyzes an ***ad-hoc*** network run during a four to five day conference setting.

**Assumptions:**
1. Exchange of data is ***bidirectional*** upon any sighting in the trace.
2. Whenever nodes sight each other, the sighting is long enough for complete transfer of data in both directions.
3. In part 1, each node transmits to the first K ***unique neighbours*** it sights.
4. The transmission probability space is such that ***x%+y% = 100%***

*Note on directories:*

1. ***doc***: Contains analysis of part 1,2 and 3.
2. ***Data***: Contains scripts, data, plots for all experiments that was run for the assignment.
3. ***src***: Contains *raw scripts*. More on execution below.
4. ***Problem Statement***: Contains 2 files. *Second statement* was attempted.

*Note on execution of scripts:*

Change directory to *src/* folder using `cd src`

To run script for part 1, type in ***Unix Bash***:
```
python algo1.py <script_name> <Parameter_K> <Source_node>
```

To run script for part 2, type in ***Unix Bash***:
```
python algo2.py <Top_S%> <Bottom_L%> <Transmission_Prob_to_super_nodes(%)> <Transmission_Prob_to_Oridinary_nodes(%)> <Source_Node>
```

To run script for part 3, type in ***Unix Bash***:
```
python algo3.py <Transmission Prob.(X in %)> <Transmission Porb(Y in %)> <Source_Node>
```



