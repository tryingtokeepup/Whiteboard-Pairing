import math


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# we will recieve some sort of sorted array of ints as input
# we also have to be careful, and ... make sure its sort of balanced, as we need to return a minimum height tree
# dont worry TOO much about 2nd condition
# this exposes the fact that i dont remember binary trees at all


def main(arr):
    if len(arr) == 1:
        return "yo, hey man"

    middle_of_array = len(arr) // 2
    # i want to figure out what the middle value is
    head_node = BinaryTreeNode(arr[len(arr) // 2])
    left_array = arr[:middle_of_array]
    head_node.left = main(left_array)
    right_array = arr[middle_of_array:]
    head_node.right = main(right_array)

    return head_node

# Helper function to validate that the created tree is a valid BST


def is_BST(root):
    node_and_bounds_stack = []
    node_and_bounds_stack.append(
        {"node": root, "lower_bound": -math.inf, "upper_bound": math.inf})

    while node_and_bounds_stack != []:
        node_and_bounds = node_and_bounds_stack.pop()
        node = node_and_bounds["node"]

        lower_bound = node_and_bounds["lower_bound"]
        upper_bound = node_and_bounds["upper_bound"]

        if node.value <= lower_bound or node.value >= upper_bound:
            return False

        if node.left != None:
            node_and_bounds_stack.append(
                {"node": node.left, "lower_bound": lower_bound, "upper_bound": node.value})

        if node.right != None:
            node_and_bounds_stack.append(
                {"node": node.right, "lower_bound": node.value, "upper_bound": upper_bound})

    return True


test_array = [1, 2, 3, 4, 5, 6, 7]
print(main(test_array))
