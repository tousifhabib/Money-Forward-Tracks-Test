import axios, { AxiosError, AxiosResponse } from 'axios';

// Define interfaces for request and response objects
interface HashRequest {
  q: string;
}

interface HashResponse {
  q: string;
  hash: string;
}

// Call the hash API and return the generated hash value
async function generateHash(q: string): Promise<string> {
  // Make an HTTP GET request to the API with the q parameter as a query parameter
  const response: AxiosResponse<HashResponse> = await axios.get('http://challenge-server.code-check.io/api/hash', {
    params: {
      q: q,
    },
  });
  // Extract the hash value from the response object and return it
  return response.data.hash;
}

// Main function takes command line arguments and calls generateHash
function main(argv: string[]) {
  // Extract the q parameter from argv
  const q = argv[2];
  // Check if q parameter is missing
  if (!q) {
    console.error('Error: parameter q is missing');
    process.exit(1);
  }
  // Call generateHash with q parameter and print the resulting hash value to standard output
  generateHash(q)
    .then((hash) => {
      console.log(hash);
    })
    .catch((error: AxiosError) => {
      // Handle errors that occur while calling the API
      if (error.response) {
        console.error(`HTTP error ${error.response.status}: ${error.response.data}`);
      } else {
        console.error(`Network error: ${error.message}`);
      }
      process.exit(1);
    });
}

// Call main function with command line arguments
main(process.argv);