

def balancedBrackets(string):

    # let's compare the end most characters to each other
    # we can either do this recursively or we can do this ... iteratively
    # if it fails at any point, exit out of the loop and fail
    # wow, the first test case would actually fail me immediately

    # we can use some sort of stack data structure to do all of this junk
    closing_brackets_hash = {'{': '}', '(': ')', '[': ']'}
    psuedo_stack = []
    print(closing_brackets_hash)

    for stupid_bracket in string:

        if stupid_bracket in closing_brackets_hash:  # dude thats insane thats so cool fuck c
            # check the next guy and see if its the same as the first guy
            psuedo_stack.append(stupid_bracket)
        elif closing_brackets_hash[psuedo_stack.pop()] != stupid_bracket:
            return False

    if len(psuedo_stack) == 0:
        return True
    # i just want to compare the next bracket to the stupid bracket


print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False
