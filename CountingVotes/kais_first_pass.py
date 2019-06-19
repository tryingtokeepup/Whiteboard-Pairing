def count_votes(arr):
    candidate_vote_tracker = {}
    current_winner_votes = 0
    current_winner = ''
    # so, basically, we have a bunch of candidates who have votes inside the array that is passed to us.
    # we need to iterate over the choosen candidates, and everytime they recieve a vote, if they don't have a count
    # initialize them into the counts hash table, with their name and how many votes they have recieved.
    for candidate in arr:
        # if the candidate is not in the array
        if candidate not in candidate_vote_tracker:
            candidate_vote_tracker[candidate] = 0
        # for all other cases, add to the candidate score

        candidate_vote_tracker[candidate] += 1

        if candidate_vote_tracker[candidate] > current_winner_votes:
            current_winner_votes = candidate_vote_tracker[candidate]
            # whoever is in the lead is the current presumed winner
            current_winner = candidate
        # however, we do have the condition that there are two or even more people tied
        elif candidate_vote_tracker[candidate] == current_winner_votes:
            # do a string comparison, whatever is first alphabetically wins... yeah, i know.
            if candidate > current_winner:
                current_winner = candidate

    return current_winner


print(count_votes([
    'veronica',
    'mary',
    'alex',
    'james',
    'mary',
    'michael',
    'alex',
    'michael',
]))

# should print 'michael'


# print(
#     count_votes([
#         'john',
#         'johnny',
#         'jackie',
#         'johnny',
#         'john',
#         'jackie',
#         'jamie',
#         'jamie',
#         'john',
#         'johnny',
#         'jamie',
#         'johnny',
#         'john',
#     ])
# )  # should print 'johnny'
