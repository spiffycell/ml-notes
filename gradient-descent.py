#!/usr/bin/python

import numpy as np


def gradient_descent(inputs, outputs):

    # initial values for slope, intercept
    slope = 0.32528735632182293
    intercept = -4.1586206896548035
   
    # THESE ARE THE VALUES YOU MAY NEED TO RECALIBRATE TO ZERO-IN ON THE GLOBAL MINIMA
    # number of steps taken along the curve (towards the mse minima)
    index = 1000000
    # size of the steps taken along the curve
    learn_rate = 0.00093
    
    
    for i in range(index):
        
        # calculate predicted output
        outputs_pred = slope * inputs + intercept
        
        # calculate MSE
        n = len(inputs)
        mse = (1/n) * sum([val**2 for val in (outputs - outputs_pred)])
      

        # calculate partial derivatives to help mark next point on curve
        # calculate derivative of slope
        deriv_slope = -(2/n) * sum(inputs * (outputs - outputs_pred))
        # calculate derivative of intercept
        deriv_intercept = -(2/n) * sum(outputs - outputs_pred)
        
        # recalibrate current values
        slope = slope - learn_rate * deriv_slope
        intercept = intercept - learn_rate * deriv_intercept
        
        print("slope: {}, intercept: {}, MSE: {}, index: {}".format(slope, intercept, mse, i))


def init():

    inputs = np.array([15, 18, 31, 34, 52])
    outputs = np.array([1, 2, 4, 8, 13])

    gradient_descent(inputs, outputs)


if __name__ == "__main__":
    init()
