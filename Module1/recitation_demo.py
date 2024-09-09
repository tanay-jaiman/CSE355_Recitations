from cse355_machine_design import DFA, registry

def example():
    Q = {"q0", "q1", "q2", "q3", "q4"}
    Sigma = {"a", "b"}
    Delta = {
        ("q0", "a") : "q1",
        ("q0", "b") : "q4",
        ("q1", "a") : "q4",
        ("q1", "b") : "q2",
        ("q2", "a") : "q3",
        ("q2", "b") : "q4",
        ("q3", "a") : "q3",
        ("q3", "b") : "q3",
        ("q4", "a") : "q4",
        ("q4", "b") : "q4"
    }
    start_state = "q0"
    final_set_of_states = {"q3"}

    return DFA(Q, Sigma, Delta, start_state, final_set_of_states)