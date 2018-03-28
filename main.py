import numpy as np
import statsmodels.api as smapi
from statsmodels.formula.api import ols
import statsmodels.graphics as smgraphics

def reject_outliers2(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]


def reject_outliers(data, m=2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d / mdev if mdev else 0.
    return data[s < m]

def fit_data_without_outliers(x, y):
    # Make fit for x data
    regression = ols("data ~ x", data=dict(data=y, x=x)).fit()
    # Find outliers #
    test = regression.outlier_test()
    outliers = ((y[j], x[j]) for j, t in enumerate(test.icol(2)) if t < 0.5)
    print 'Outliers: ', list(outliers)
    # Figure #
    figure = smgraphics.regressionplots.plot_fit(regression, 1)
    # Add line #
    smgraphics.regressionplots.abline_plot(model_results=regression, ax=figure.axes[0])



if __name__ == '__main__':
    # load data in array
    positions = np.loadtxt('data/positions.txt')
    for i in range(1, 2):

        position = positions[i-1]
        # 1st and 2nd column data from file are x-direction data
        # 3rd and 4th column are y-direction data
        data_x = np.loadtxt('data/{}.txt'.format(i), usecols=(0, 1))
        data_y = np.loadtxt('data/{}.txt'.format(i), usecols=(2, 3))

        force_x = data_x[:, 0]
        adc_x = data_x[:, 1]
        force_y = data_y[:, 0]
        adc_y = data_y[:, 1]

        fit_data_without_outliers(adc_x, force_x)

        # Find parameters for linear equation from data fitting
        [x_a, x_b] = np.polyfit(adc_x, force_x, 1)
        [y_a, y_b] = np.polyfit(adc_y, force_y, 1)

