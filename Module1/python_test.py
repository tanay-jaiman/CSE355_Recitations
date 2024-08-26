from cse355_machine_design import DFA, registry

# Create a function that returns a DFA
def example():
	Q = {"q_0", "q_1", "q_2", "q_3", "q_4"} # Set of States
	Sigma = {"a", "b"} # Alphabet set
	Delta = {
				("q_0", "a") : "q_1",
				("q_0", "b") : "q_4",	
				("q_1", "a") : "q_4",
				("q_1", "b") : "q_2",		
				("q_2", "a") : "q_3",
				("q_2", "b") : "q_4",	
				("q_3", "a") : "q_3",
				("q_3", "b") : "q_3",	
				("q_4", "a") : "q_4",
				("q_4", "b") : "q_4",
			} # Transition function
	q_0 = "q_0" # Start state
	F = {"q_3"} # Final set

	# return DFA
	return DFA(Q, Sigma, Delta, q_0, F)


