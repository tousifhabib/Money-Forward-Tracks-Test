# Hash API CLI Program
This program is a CLI (Command-Line Interface) application that calls an API endpoint to generate a hash value for a given string. The API endpoint is hosted at http://challenge-server.code-check.io/ and has the following specification:

## API Specification
* Endpoint: /api/hash
* HTTP Method: GET
* Parameters(Query):
 * q: A string to generate a hash value (Required)
* Response: A JSON object with the following keys:
 * q: The given parameter q
* hash: Generated hash value

When the API is executed successfully, 200 OK is returned in the JSON format. When the program fails to run the API (when parameter q is not selected), 400 Bad Request is returned in the JSON format. The generated hash value will always be the same value for the same parameter q.

## Implementation
The implementation of the program uses TypeScript and the Axios library to make HTTP requests to the API endpoint. The program follows the following steps:

1. Define interfaces for request and response objects:
 * HashRequest: contains the q parameter to be passed in the request.
 * HashResponse: contains the q parameter and the generated hash value in the response.
2. Define an async function generateHash(q: string): Promise<string> that makes an HTTP GET request to the API endpoint with the q parameter as a query parameter. The function extracts the hash value from the response object and returns it.
3. Define the main function that takes command line arguments and calls generateHash with the q parameter. The function checks if the q parameter is missing and handles errors that occur while calling the API.
4. Call the main function with command line arguments (process.argv).

The generateHash function uses the Axios library to make an HTTP GET request to the API endpoint. The axios.get method is used to make the request with the q parameter as a query parameter. The response.data.hash property is used to extract the hash value from the response object and return it.

The main function uses process.argv to extract the q parameter from the command line arguments. If the q parameter is missing, the function logs an error message and exits the process with an exit code of 1. If the API request fails, the function handles the error and logs an appropriate error message before exiting the process with an exit code of 1.

Finally, the main function is called with process.argv to run the program with the command line arguments.

## Running the Program
To run the program, open a terminal window and navigate to the directory containing the main.ts file. Then, run the following command:
```
$ npx ts-node main.ts <q_parameter>
```
Replace <q_parameter> with the string to generate a hash value for. The program will make an HTTP GET request to the API endpoint with the q parameter and log the generated hash value to the console.

Example:
```
$ npx ts-node main.ts hoge
ac0030f68eee4280a8cff568b36dc7e8944880fcab1eadd9220c6c583939baf8
```