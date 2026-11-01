import math


def perplexity_dashboard(losses: list[float]) -> tuple[float, float]:
    """
    losses: a list of N per-token negative log-likelihood values.

    H = mean(losses)
    PPL = e^H

    Return (mean_loss, perplexity). Exponentiate the MEAN, never the sum.
    """
    mean_of_the_losses = sum(losses)/len(losses)
    PPL = math.exp(mean_of_the_losses)
    return mean_of_the_losses,PPL
    pass
