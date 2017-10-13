# -*- coding: utf-8 -*-

# libraries; N.B. commented packages are not in use in present version.
import numpy as np
import matplotlib
# import scipy
# import bayespy

# Probability of actually having a disease given a positive test result.

def main():
    # close all plots
    matplotlib.pyplot.close("all")

    # Bayes' theorem P(A|B) = [P(B|A)P(A)]/[P(B)]
    # P(A) = probability of actually having the disease
    # P(B) = true positive test rate
    A = float(input("Base rate P(A)? "))
    B = float(input("P(B)? "))
    
    PAB = float((B * A) / ((B * A) + (1 - B) * (1 - A)))
    print("Probability of A, given B: ", PAB)

if __name__ == '__main__':
    main()