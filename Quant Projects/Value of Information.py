def expected_value(action, p_good):
    if action == "A":
        return p_good * 10 + (1 - p_good) * (-5)
    if action == "B":
        return p_good * 2 + (1 - p_good) * 1


def optimal_action(p_good):
    ev_a = expected_value("A", p_good)
    ev_b = expected_value("B", p_good)
    return "A" if ev_a >= ev_b else "B"


def posterior(p_prior, signal_good, q):
    if signal_good:
        return (q * p_prior) / (q * p_prior + (1 - q) * (1 - p_prior))
    else:
        return ((1 - q) * p_prior) / ((1 - q) * p_prior + q * (1 - p_prior))


def value_of_information(p_prior, q):
    base_action = optimal_action(p_prior)
    base_ev = expected_value(base_action, p_prior)

    p_good_signal = posterior(p_prior, True, q)
    p_bad_signal = posterior(p_prior, False, q)

    ev_with_signal = (
        p_prior * expected_value(optimal_action(p_good_signal), p_good_signal)
        + (1 - p_prior) * expected_value(optimal_action(p_bad_signal), p_bad_signal)
    )

    return ev_with_signal - base_ev


if __name__ == "__main__":
    p_prior = float(input("Enter prior probability of good state (0–1): "))
    q = float(input("Enter signal accuracy q (0–1): "))

    if not (0 < p_prior < 1):
        raise ValueError("p_prior must be between 0 and 1")

    if not (0 < q < 1):
        raise ValueError("q must be between 0 and 1")

    # Normalize anti-informative signals
    flipped = False
    if q < 0.5:
        q = 1 - q
        flipped = True

    voi = value_of_information(p_prior, q)

    print("\nRESULT")
    print("Prior probability:", p_prior)
    print("Effective signal accuracy:", round(q, 3))
    if flipped:
        print("Note: signal was anti-informative and has been inverted")
    print("Value of information:", round(voi, 4))