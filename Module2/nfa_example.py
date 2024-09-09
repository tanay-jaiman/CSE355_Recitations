from cse355_machine_design import NFA, registry

def example_nfa():
    Q = {"q0", "q1", "q2", "q3"}
    Sigma = {"0", "1"}
    Delta = {
        ("q0", "0") : {"q0"},
        ("q0", "1") : {"q0", "q1"},
        ("q1", "0") : {"q2"},
        ("q1", "_") : {"q2"},
        ("q2", "1") : {"q3"},
        ("q3", "0") : {"q3"},
        ("q3", "1") : {"q3"}
    }

    start_state = "q0"
    F = {"q3"}

    return NFA(Q, Sigma, Delta, start_state, F)