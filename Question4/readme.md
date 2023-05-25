# Description

Track Inc plans to recruit new employees for a labor shortage. They have decided to arrange a recruitment test.

There are two phases to this test. In the first phase, a paper test will be given to judge basic skills. In the second phase, interviews will take place to judge practical experience.

Each examinee is assigned an integer according to the order of their test application. The test results for examinee `i` are given with two integers, `Ai`,`Bi`. 

`Ai` is the skill score judged using the paper test and `Bi` is the skill score judged in the interview.

They decided to create a candidate list according to the test results. If a pair of nonidentical integers `(i,j)` satisfies `Ai≤Aj`	and `Bi≤Bj`
, examinee `i` will be eliminated from the candidate list. That is, candidate `i` will be judged inferior to candidate `j`. This operation is executed every time a set of skills for a new candidate is added to the list. If two candidates have identical skills, then one of the two candidates will be eliminated from the candidate list.

Your mission is to process the following two types of N queries.

`“1 a b”`: add an examinee with the skills of `(Ai,Bi)` to the candidate list

`“2”`: output the number of examinees in the current candidate list.

The first query is called the `“1 a b”` type query and the second one is called the `“2”` type query. Note that it is guaranteed that the first query will be the `“1 a b”` type and that there will be at least one `“2”` type query.

## Implementation:

### CLI:
Implement a command line application that receives standard input and writes the answer to its standard output.

### Input rule:
The program is executed as follows:
```
./myApp < input.in
```

The standard input format is as follows:
```
N
query1
.
.
.
queryN
```
	
The conditions are as follows:
```
1≤N≤10^5, integer
```
In a query of type `“1 a b”`: 1≤(a,b)≤10^9, integer

query1 is of the type `“1 a b”`

At least one `“2”` type query exists

## Output rule:
Print the output of the `“2”` type queries according to the input order separated by a new line.
 
## I/O examples:
### Example 1:
Standard input (00_sample1.in)
```
5
1 1 3
1 2 1
2
1 2 2
2
```

Standard output:
```
2
2
```

After processing queries 1 and 2, the candidate list has two examinees having the skills 1,3 and 2,1.

At query 4, an examinee having the skills 2,2 is added. Since 2,1 is inferior to 2,2, the examinee with the skills 2,1 is eliminated from the list. That is why the current candidate list has two examinees.

### Example 2
Standard input (00_sample2.in):
```
14
1 1 1
1 7 2
1 3 5
1 6 1
2
1 6 5
1 4 6
1 3 7
2
1 2 5
1 2 9
1 5 5
1 7 2
2
```

Standard output
```
2
4
5
```

## How to get stdin lines:
In main.py, there is a function called main, which gives stdin lines as lines.
```
def main(lines):
    # code to run
```
lines passed here is came from sys.stdin.

## How to output result:
You can use the standard print() method to output results to stdout.
```
print(result)
```

## Test cases json:
```
[
   {
      "input": "in/basic/00_sample1.in",
      "output": "out/basic/00_sample1.out",
      "description": "[基本実装] N が5である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 5"
   },
   {
      "input": "in/basic/00_sample2.in",
      "output": "out/basic/00_sample2.out",
      "description": "[基本実装] N が14である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 14"
   },
   {
      "input": "in/basic/10_basic1.in",
      "output": "out/basic/10_basic1.out",
      "description": "[基本実装] N が815である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 815"
   },
   {
      "input": "in/basic/10_basic2.in",
      "output": "out/basic/10_basic2.out",
      "description": "[基本実装] N が591である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 591"
   },
   {
      "input": "in/basic/10_basic3.in",
      "output": "out/basic/10_basic3.out",
      "description": "[基本実装] N が204である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 204"
   },
   {
      "input": "in/basic/10_basic4.in",
      "output": "out/basic/10_basic4.out",
      "description": "[基本実装] N が109である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 109"
   },
   {
      "input": "in/basic/10_basic5.in",
      "output": "out/basic/10_basic5.out",
      "description": "[基本実装] N が476である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 476"
   },
   {
      "input": "in/basic/10_basic6.in",
      "output": "out/basic/10_basic6.out",
      "description": "[基本実装] N が538である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 538"
   },
   {
      "input": "in/basic/10_basic7.in",
      "output": "out/basic/10_basic7.out",
      "description": "[基本実装] N が356である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 356"
   },
   {
      "input": "in/basic/10_basic8.in",
      "output": "out/basic/10_basic8.out",
      "description": "[基本実装] N が280である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 280"
   },
   {
      "input": "in/basic/10_basic9.in",
      "output": "out/basic/10_basic9.out",
      "description": "[基本実装] N が1000である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 1000"
   },
   {
      "input": "in/basic/10_basic10.in",
      "output": "out/basic/10_basic10.out",
      "description": "[基本実装] N が147である場合に正答できる",
      "description_en": "[Basic Case] Correct when N is 147"
   }
]
```
