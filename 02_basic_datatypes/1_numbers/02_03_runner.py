'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
#10 miles is 16 kilometers, need to find the average time to complete 1 mile for the runner and convert
#running pace is run time divided by distance

run_time = 30.3 # minutes and seconds it took to run the 10 miles
run_distance_kms = 16 # I converted this outside of the calculation - see above but I could include it easily

pace_in_kms = run_time / run_distance_kms

print(pace_in_kms)