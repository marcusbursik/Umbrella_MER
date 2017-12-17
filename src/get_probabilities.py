"""
Name: get_probabilities
Version: 0.3
Date: 24 November 2017
Author: Rose M. Rustowicz, Solene Pouget, Marcus Bursik
Concept: Solene Pouget, Emile Jansons, Marcus Bursik
Contact: Marcus Bursik mib@buffalo.edu
"""
import matplotlib.pyplot as plt
from scipy import stats		# used for t-test
import scipy				# used to generate random normal distribution
import numpy as np			# numpy for array operations

def get_probabilities(c, a, one_stdev_err, probabilities_txt_filename):
	"""
	[ output_txt_file ] = get_probabilities(c, a, one_stdev_err, probabilities_txt_filename)

	Description: This function generates a sample set of data from the
	 alpha value and its standard deviation and performs a series of 
	 t-tests to evaluate the probability that the data fits different
	 power law relationships (2/9, 5/9, 2/3, 3/4)

	Input:
	 'c' - The constant in y = cx^a, can be a vector of constant c's 
		if > 1 fit eqn
	 'a' - The power constant in y = cx^a, can be a vector of alphas 
		if > 1 fit eqn
	 'one_stdev_err' - An array of one standard deviation errors of a and c
	 'probabilities_txt_filename' - A filename that the probabilities will 
		be saved to in a results folder
	 
	Output:
	 output_txt_file - The text file output
	"""

	# Specify number of samples to draw from distribution of parameter values.
        # Small number (currently n = 100) is chosen to reflect generally small number of
        # times at which we have satellite acquisition.
        # Could be changed to actual number of satellite image pairs in analysis, but note
        # that no probability can be calculated for n < 2.
	n = 100
	# Specify exponents to test as strings
	strings = ['4/9', '10/9', '4/3', '3/2']
	# Specify exponents to test as floats, in the same order as above
	popmean_ar = np.array([4./9., 10./9., 4./3., 3./2.])
#	popmean_ar = np.array([2./9., 5./9., 2./3., 3./4.])

	# Open the .txt file for writing
	f = open(probabilities_txt_filename, 'w')

	# If alpha is a scalar of type float
	if (type(a) == np.float64) or (type(a) == np.float) or (type(a) == float):
		
		# Write the information to the .txt file
		f.write('c, constant = ' + str(c) + '\n')
		f.write('stdev in c = ' + str(one_stdev_err[0]) + ' \n')
		f.write('a, alpha = ' + str(a) + '\n')
		f.write('stdev in a = ' + str(one_stdev_err[1]) + '\n')

		# Test the population mean as the different probabilities
		for mean_idx in range(0,len(popmean_ar)):
			popmean = popmean_ar[mean_idx]
			
			# Pre-allocate space for t-statistics and probabilities
			t_stat = np.zeros(2)	
			prob = np.zeros(2)
			# Generate arrays from n samples, stddev, and expected value
			#  of a. Use the sample array and test the probabilities that 
			#  the distribution follows each power law value 
			for index in range(0,2):
				array = one_stdev_err[1]*scipy.random.standard_normal(n)+a
				# num_numbers = len(set(array))					
				hist, edges = np.histogram(array, bins=100)
				x = range(100)
				y = hist
                                # uncomment to see the histograms
				# plt.plot(x,y)
				# plt.show()

				t_stat[index], prob[index] = scipy.stats.ttest_1samp(array, popmean)
			
			# Write out the data to the .txt file

			prob_string = '1st run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[0])
			f.write(prob_string + '\n')
			prob_string = '2nd run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[1])
			f.write(prob_string + '\n')

			# Write if the probability values converged to two sig figs
			if np.absolute(prob[0] - prob[1]) < 0.1:
				f.write('Probability does converge to two significant figures. \n')
			else:
				f.write('Probability does not converge to two significant figures. \n')
	
			t_stat_string = '1st run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[0])
			f.write(t_stat_string + '\n')
			t_stat_string = '2nd run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[1])
			f.write(t_stat_string + '\n')
			f.write(t_stat_string + '\n')

	elif type(a) == np.ndarray:
		f.write('RESULTS FOR THE FIRST FIT:\n')

		f.write('c, constant = ' + str(c[0]) + '\n')
		f.write('stdev in c = ' + str(one_stdev_err[0,0]) + ' \n')
		f.write('a, alpha = ' + str(a[0]) + '\n')
		f.write('stdev in a = ' + str(one_stdev_err[0,1]) + '\n')

		for mean_idx in range(0,len(popmean_ar)):
			popmean = popmean_ar[mean_idx]
				
			t_stat = np.zeros(2)
			prob = np.zeros(2)
			for index in range(0,2):
				array = one_stdev_err[0,1]*scipy.random.standard_normal(n)+a[0]
				t_stat[index], prob[index] = scipy.stats.ttest_1samp(array, popmean)

                        prob_string = '1st run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[0])
                        f.write(prob_string + '\n')
			prob_string = '2nd run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[1])
			f.write(prob_string + '\n')
	
			if np.absolute(prob[0] - prob[1]) < 0.1:
				f.write('Probability does converge to two significant figures. \n')
			else:
				f.write('Probability does not converge to two significant figures. \n')

			t_stat_string = '1st run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[0])
			f.write(t_stat_string + '\n')
			t_stat_string = '2nd run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[1])
			f.write(t_stat_string + '\n')
			f.write(t_stat_string + '\n')

		f.write('\nRESULTS FOR THE SECOND FIT:\n')

		f.write('c, constant = ' + str(c[1]) + '\n')
		f.write('stdev in c = ' + str(one_stdev_err[1,0]) + ' \n')
		f.write('a, alpha = ' + str(a[1]) + '\n')
		f.write('stdev in a = ' + str(one_stdev_err[1,1]) + '\n')

		for mean_idx in range(0,len(popmean_ar)):
			popmean = popmean_ar[mean_idx]
			
			t_stat = np.zeros(2)
			prob = np.zeros(2)
			for index in range(0,2):
				array = one_stdev_err[1,1]*scipy.random.standard_normal(n)+a[1]
				t_stat[index], prob[index] = scipy.stats.ttest_1samp(array, popmean)

                        prob_string = '1st run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[0])
                        f.write(prob_string + '\n')
			prob_string = '2nd run: probability that alpha is '+ strings[mean_idx] + ' is ' + str(prob[1])
			f.write(prob_string + '\n')

			if np.absolute(prob[0] - prob[1]) < 0.1:
				f.write('Probability does converge to two significant figures. \n')
			else:
				f.write('Probability does not converge to two significant figures. \n')

			t_stat_string = '1st run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[0])
			f.write(t_stat_string + '\n')
			t_stat_string = '2nd run: t-statistic that alpha is ' + strings[mean_idx] + ' is ' + str(t_stat[0])
			f.write(t_stat_string + '\n')
			f.write(t_stat_string + '\n')
	
	# Close the .txt file now that all writing to it is complete
	f.close()

if __name__ == '__main__':
	c = 154
	a = 0.776
	one_stdev_err = [123.12, 0.0481]
	probabilities_txt_filename = 'probs_text.txt'

	get_probabilities(c, a, one_stdev_err, probabilities_txt_filename)
