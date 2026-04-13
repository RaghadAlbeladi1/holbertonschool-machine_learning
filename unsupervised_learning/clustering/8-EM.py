#!/usr/bin/env python3
"""
Expectation-Maximization for a Gaussian Mixture Model
"""
import numpy as np
initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """
    Performs the expectation maximization for a GMM
    X: numpy.ndarray of shape (n, d) containing the data set
    k: positive integer, number of clusters
    iterations: maximum number of iterations
    tol: tolerance on the change in log likelihood for early stopping
    verbose: if True, prints log likelihood information
    Returns: pi, m, S, g, log_lh or None x5 on failure
    """
    if (not isinstance(X, np.ndarray) or X.ndim != 2 or
            not isinstance(k, int) or k <= 0 or
            not isinstance(iterations, int) or iterations <= 0 or
            not isinstance(tol, (int, float)) or tol < 0 or
            not isinstance(verbose, bool)):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    if pi is None or m is None or S is None:
        return None, None, None, None, None

    log_prev = 0.0
    for i in range(iterations + 1):
        g, log_lh = expectation(X, pi, m, S)
        if g is None or log_lh is None:
            return None, None, None, None, None

        if verbose and (i % 10 == 0):
            print("Log Likelihood after {} iterations: {}".format(
                i, round(log_lh, 5)))

        if i > 0 and abs(log_lh - log_prev) <= tol:
            break

        if i == iterations:
            break

        pi, m, S = maximization(X, g)
        if pi is None or m is None or S is None:
            return None, None, None, None, None

        log_prev = log_lh

    g, log_lh = expectation(X, pi, m, S)
    if g is None or log_lh is None:
        return None, None, None, None, None

    if verbose and (i % 10 != 0):
        print("Log Likelihood after {} iterations: {}".format(
            i, round(log_lh, 5)))

    return pi, m, S, g, log_lh
