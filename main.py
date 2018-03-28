import numpy as np
# from random import random
# import statsmodels.api as smapi
# from statsmodels.formula.api import ols
# import statsmodels.graphics as smgraphics

def reject_outliers2(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def reject_outliers(data, m=2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / mdev if mdev else 0.
    return data[s < m]


if __name__ == '__main__':
    # load data in array
    for i in range(1, 2):
        data = np.loadtxt('data/{}.txt'.format(i))
            # first line is position
            # position[i] =
            # # ignore second line
            # # starting with third line force_x=[0] adc_x=[1] force_y=[2] adc_y=[3]
            # # write all data from the file
            # # Delete outliners
            #
            # # Make fit #
            # regression = ols("data ~ x", data=dict(data=y, x=x)).fit()
            # # Find outliers #
            # test = regression.outlier_test()
            # outliers = ((x[i], y[i]) for i, t in enumerate(test.icol(2)) if t < 0.5)
            # print 'Outliers: ', list(outliers)
            # # Figure #
            # figure = smgraphics.regressionplots.plot_fit(regression, 1)
            # # Add line #
            # smgraphics.regressionplots.abline_plot(model_results=regression, ax=figure.axes[0])
            # # Find parameters for linear equation from data fitting
            # [x_a, x_b] = np.polyfit(arr_adc_x, arr_force_x, 1)
            # [y_a, y_b] = np.polyfit(arr_adc_y, arr_force_y, 1)
        print data
