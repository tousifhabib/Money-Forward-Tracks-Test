import sys
import requests

API_URL = "http://challenge-server.code-check.io/api/hash"

def generate_hash(q):
    params = {"q": q}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["hash"]
    elif response.status_code == 400:
        error_data = response.json()
        error_msg = error_data.get("message", "Error: Bad Request")
        print(error_msg, file=sys.stderr)
        sys.exit(1)
    else:
        print("Error: API request failed", file=sys.stderr)
        sys.exit(1)

def main(argv):
    if len(argv) != 2:
        print("Error: Missing argument q", file=sys.stderr)
        sys.exit(1)

    q = argv[1]
    result = generate_hash(q)
    print(result)

if __name__ == "__main__":
    main(sys.argv)