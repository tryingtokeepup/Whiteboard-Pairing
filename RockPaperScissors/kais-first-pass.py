# Write a function called `rockPaperScissors` that will take as input an integer `n`. Your function should output all of the possible combinations of the three plays 'rock', 'paper', or 'scissors' up to the given integer `n`.


# initialize some array

# each one of these possibilities, as we reach n permutations???, we have to recursively call the function on it for that time???


# for every possible choice, we need to append every possible choice
def recursive_tomfoolery(plays_left, array):

    array.append('r')
    array.append('s')
    array.append('p')

    return array


def crazy_rps(n):
    rps_array = []
    plays = ['r', 'p', 's']

    # base case of done? keep recusively calling until we are done
    if n == 0 {

        return rps_array
    }
    else {
        # inside rps_array, make three new arrays, with r, p and s as the initial values of said new arrays
        for play in plays:

            recursive_tomfoolery(rps_array)
            n - 1
    }
