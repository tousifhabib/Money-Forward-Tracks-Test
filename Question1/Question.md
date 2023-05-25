# Description:
Let's create a program to calculate the total daily sales of a taxi.
A taxi fare can be calculated according to the following rules:
There is a flat rate of B yen when a customer gets in the taxi.
After a minimum of A meters, there is an additional rate of D yen for every C meters
For example, when the distance is longer than A meters but A+C meters or shorter, the additional rate is D yen.
In general, when the distance is longer than A+Ci meters but A+C(i+1) meters or shorter, the additional rate is (i+1)D yen (1≤i, i is an integer).
Taxi fares are calculated from the flat rate and the additional rate as follows.
If the boarding time is earlier than 22:00, the fare is the sum of the flat rate and the additional rate.
If the boarding time is 22:00 or later, the fare is 120% of the sum of the flat rate and the additional rate.
The fare is rounded down to the nearest integer in yen.
n sets of boarding time and distance data are given. Please calculate the total daily sales by adding up all of the fares.

## Implementation Details
### CLI
Please implement a CLI application that takes the input value as an argument and outputs the result to standard output. For details, see the "CLI application template" section at the bottom of this page.
### Input rules
The format of the standard input is as follows:
```
 ./myApp < input.in
```

The format of input.in is as follows:
```
A B C D
n
t1 l1
⋮
tn ln
```
	
On the first line, the integers A,B,C,D are given. On the second line, the number of customers n is given. On the following n lines, the boarding time ti and distance li (meters) of each customer are given.
`t` is given as a single string, as follows:
```
aa:bb
```

`aa` shows the hours and `bb` shows the minutes.
The hours and minutes are each expressed as two digits, as follows:
`02:06`

### Restrictions:
```
1≤A,B,C,D≤10^4, integer
0≤n≤10^4, integer
00:00≤ti≤23:59 (1≤i≤n)
1≤li≤10^5, integer (1≤i≤n)
```

### Example 1:
```
$ ./myApp < 00_example_01.in 
00_example_01.in:
1000 600 250 100
2
10:25 1500
23:40 2001
```
#### Standard Output:
```
2120
```
The first customer fare is 800 yen and the second customer fare is 1320 yen. The total sales are 2120 yen. 

### Example 2:
```
$ ./myApp < 00_example_02.in 
00_example_02.in:
1 9999 2 9999
0
```
Standard Output:
```
0
```
In some cases the taxi will have had no fares for the day. 