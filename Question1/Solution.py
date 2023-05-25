import sys

# read input values
A, B, C, D = map(int, input().split()) # read the values of A, B, C, and D from input
n = int(input()) # read the number of customers, n, from input

# initialize the total sales to zero
total_sales = 0

# iterate through each customer
for i in range(n):
    # read the customer's data
    t, l = input().split() # read the customer's boarding time, t, and distance, l, from input
    hh, mm = map(int, t.split(':')) # extract the hour and minute values from the boarding time string
    distance = int(l) # convert the distance to an integer

    # calculate the fare
    fare = B # start with the flat rate fare

    if distance > A: # if the distance is greater than the minimum distance A
        extra_distance = distance - A # calculate the extra distance beyond A
        extra_fare = ((extra_distance - 1) // C + 1) * D # calculate the extra fare for the extra distance
        fare += extra_fare # add the extra fare to the total fare

    if hh >= 22: # if the boarding time is 22:00 or later
        fare *= 1.2 # apply a 20% increase to the fare

    total_sales += int(fare) # add the fare, rounded down to the nearest integer, to the total sales

# output the total sales
print(total_sales)
