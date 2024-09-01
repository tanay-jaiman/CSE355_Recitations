from cse355_machine_design import NFA, registry

def example():

# L = {w in {0,1}* | w contains 101 or 11 as a substring}

    Q = {"q_0", "q_1", "q_2", "q_3"}
    Sigma = {"0", "1"}
    delta = {
        ("q_0", "0"): {"q_0"},
        ("q_0", "1"): {"q_0", "q_1"},
        ("q_1", "0"): {"q_2"},
        ("q_1", "_"): {"q_2"},
        ("q_2", "1"): {"q_3"},
        ("q_3", "0"): {"q_3"},
        ("q_3", "1"): {"q_3"}
    }
    q0 = "q_0"
    F = {"q_3"}

    return NFA(Q, Sigma, delta, q0, F)


if __name__ == "__main__":
    #example().display_state_diagram()
    #example().evaluate("010110", 1)
    #example().submit_as_answer(1)
    registry.export_submissions()