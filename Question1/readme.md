# Overview
This program calculates the total daily sales of a taxi based on the fare rules. It takes input from the command line interface, reads the values of A, B, C, D, and n, and then iterates through n customers' data. For each customer, it calculates the fare based on their boarding time and distance traveled and adds the fare to the total sales. Finally, it outputs the total sales.

# Input
The input values are read from the command line interface. The first line contains the values of A, B, C, and D separated by space. The second line contains the number of customers, n. The next n lines contain the data for each customer, consisting of their boarding time (hh:mm) and distance traveled.

# Calculation
The program calculates the fare for each customer based on the following rules:

There is a flat rate of B yen when a customer gets in the taxi.
After a minimum of A meters, there is an additional rate of D yen for every C meters.
The additional rate increases by D yen for every additional C meters traveled.
If the boarding time is earlier than 22:00, the fare is the sum of the flat rate and the additional rate.
If the boarding time is 22:00 or later, the fare is 120% of the sum of the flat rate and the additional rate.
The fare is rounded down to the nearest integer in yen.
For each customer, the program first extracts the hour and minute values from the boarding time string and converts the distance to an integer. It then calculates the fare based on the above rules and adds it to the total sales.

# Output
The program outputs the total sales rounded down to the nearest integer in yen.

# Example
Let's consider the first example provided in the prompt:

```
A, B, C, D = 1000, 600, 250, 100
n = 2
customers = [('10:25', 1500), ('23:40', 2001)]
```
For the first customer, the program calculates the fare as follows:

The distance traveled (1500) is greater than the minimum distance A (1000), so there is an additional fare.
The extra distance beyond A is 500.
The extra fare for the extra distance is ((500-1)//250 + 1) * 100 = 300.
The total fare is the sum of the flat rate and the extra fare, which is 600 + 300 = 800.
For the second customer, the program calculates the fare as follows:

The distance traveled (2001) is greater than the minimum distance A (1000), so there is an additional fare.
The extra distance beyond A is 1001.
The extra fare for the extra distance is ((1001-1)//250 + 1) * 100 = 500.
The total fare is the sum of the flat rate and the extra fare, which is 600 + 500 = 1100.

The boarding time is 23:40, which is later than 22:00, so the fare is increased by 20%.
The increased fare is 1.2 * 1100 = 1320.
The total sales are the sum of the fares for both customers, which is 800 + 1320 = 2120 yen.
