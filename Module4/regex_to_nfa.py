from cse355_machine_design import NFA, registry


def regex_to_nfa_example():

    # L = 0010* U (101)*

    Q = {"q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"}

    Sigma = {"0", "1"}

    delta = {
        ("q0", "_"): {"q1", "q2"},
        ("q1", "0"): {"q3"},
        ("q3", "0"): {"q4"},
        ("q4", "1"): {"q5"},
        ("q5", "0"): {"q5"},

        ("q2", "1"): {"q6"},
        ("q6", "0"): {"q7"},
        ("q7", "1"): {"q2"}
    }

    q0 = "q0"
    F = {"q2", "q5"}

    return NFA(Q, Sigma, delta, q0, F)