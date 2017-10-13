# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:52:42 2017

@author: Peter
"""

# Probability of actually having a disease given a positive test result.

# libraries; N.B. commented packages are not in use in present version.
import numpy as np
import matplotlib
# import scipy
# import bayespy

# close all plots
matplotlib.pyplot.close("all")

# Bayes' theorem P(A|B) = [P(B|A)P(A)]/[P(B)]
# P(A) = probability of actually having the disease
# P(B) = true positive test rate
A = float(input("Base rate P(A)? "))
B = float(input("P(B)? "))

PAB = float((B * A) / ((B * A) + (1 - B) * (1 - A)))
print("Probability of A, given B: ", PAB)

 # end program
 # second change