import numpy as np


def fit_data_without_outliers(x, y):
    return np.polyfit(x, y, 1)


arr_a_x = []
arr_b_x = []
arr_a_y = []
arr_b_y = []

if __name__ == '__main__':

    positions = np.loadtxt('data/positions.txt')
    for i in range(1, 36):

        # 1st and 2nd column data from file are x-direction data
        # 3rd and 4th column are y-direction data
        data_x = np.loadtxt('data/{}.txt'.format(i), usecols=(0, 1))
        data_y = np.loadtxt('data/{}.txt'.format(i), usecols=(2, 3))

        force_x = data_x[:, 0]
        adc_x = data_x[:, 1]
        force_y = data_y[:, 0]
        adc_y = data_y[:, 1]

        # Find parameters for linear equation from data fitting
        a_x, b_x = fit_data_without_outliers(adc_x, force_x)
        a_y, b_y = fit_data_without_outliers(adc_y, force_y)

        # write data in array
        arr_a_x.append(a_x)
        arr_b_x.append(b_x)
        arr_a_y.append(a_y)
        arr_b_y.append(b_y)

    file_x = open('data_analysis_results_x.txt', 'a')
    # loop through each item in the list and write it to the output file
    for (pos, a, b) \
            in zip(positions, arr_a_x, arr_b_x):
        file_x.write('{} {} {} \n'.format(str(pos), str(a), str(b)))
    file_x.write('\n \n')
    file_x.close()

    file_y = open('data_analysis_results_y.txt', 'a')
    # loop through each item in the list and write it to the output file
    for (pos, a, b) \
            in zip(positions, arr_a_y, arr_b_y):
        file_y.write('{} {} {} \n'.format(str(pos), str(a), str(b)))
    file_y.write('\n \n')
    file_y.close()








