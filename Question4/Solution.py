import sys


def add_candidate(candidates, a, b):
    # add the candidate to the list
    candidates.append((a, b))

    # sort the list by interview score in decreasing order, then by paper test score in decreasing order
    candidates.sort(key=lambda c: (-c[1], -c[0]))

    # iterate over the list to eliminate any candidates that are inferior to a previous candidate in the list
    i = 0
    while i < len(candidates) - 1:
        # check if the paper test score and interview score of the candidate at index i+1 are both lower than or equal to those of the candidate at index i
        if candidates[i][0] >= candidates[i + 1][0] and candidates[i][1] >= candidates[i + 1][1]:
            # delete the candidate at index i+1, since it is inferior to the one at index i
            del candidates[i + 1]
        else:
            # move on to the next candidate
            i += 1

    # return the updated candidate list
    return candidates


def count_candidates(candidates):
    # count the number of candidates still in the list
    count = 0
    for c in candidates:
        count += 1

    # return the count
    return count


def main(lines):
    # read in the number of queries
    n = int(lines[0])

    # initialize an empty list of candidates
    candidates = []

    # process each query
    for i in range(1, n + 1):
        # read in the query type and parameters using map
        query = list(map(int, lines[i].split()))

        if query[0] == 1:
            # if the query is of type 1, call add_candidate with the candidate list and the skill scores
            candidates = add_candidate(candidates, query[1], query[2])
        elif query[0] == 2:
            # if the query is of type 2, call count_candidates with the candidate list and print the result
            print(count_candidates(candidates))


# read in the standard input and pass it to the main function
main(sys.stdin.readlines())