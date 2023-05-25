# Description

An API has been implemented on the following host.
http://challenge-server.code-check.io/

Make a CLI program that calls the hash API implemented on this host!

## Implementation:

### API Specification:

The specification of the API is as follows.

Endpoint: `/api/hash`

HTTP Method: `GET`

Parameters(Query):
`q`: A string to generate a hash value (Required)

### Response:

The format is in JSON having the following 2 keys:
`q`: The given parameter `q`

`hash`: Generated hash value

When the API is executed successfully, 200 OK is returned in the JSON format
When the program fails to run the API (when parameter q is not selected), 400 Bad Request is returned in the JSON format.

The generated hash value will always be the same value for the same parameter `q`.

Example: 
```
{"q":"hoge", "hash":"ac0030f68eee4280a8cff568b36dc7e8944880fcab1eadd9220c6c583939baf8"}
```

## CLI
Implement a command line application that receives command line arguments and writes the answer to its standard output. For details, see the “Command line application template” section at the bottom of the page. 

## Input Rules:
1. Your CLI application should have one value as an argument.
2. The argument is parameter q of the API.
3. The argument is composed of ASCII characters (control characters are omitted).
4. The length of the argument is between 1 and 100 characters.

## Output Rules:
1. Print the generated hash value to standard output.
2. Use the given parameter `q` to run the API.
3. You are able to use any library to run the API.


## Standard output: 
```
$ ./myApp hoge
ac0030f68eee4280a8cff568b36dc7e8944880fcab1eadd9220c6c583939baf8
```

## How to get input parameters:
In main.py, there is a function called main, which gives command line arguments as argv.

```
def main(argv):
    # code to run
```
    
argv passed here is came from `sys.argv`. Script name information is excluded in argv of main method. 

## How to read a file:
If the input data is a file, use the open function.
```
f = open(v)
line = f.readline()

while line:
    print(line.replace('\n',''))
    line = f.readline()

f.close()
```

## How to output result:

You can use the standard print() method to output results to stdout.
```
print(result)
```