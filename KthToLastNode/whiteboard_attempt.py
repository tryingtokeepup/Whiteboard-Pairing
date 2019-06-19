class ListNode:
    def __init__(self, value):
        self.value = value

        self.next = None

# code starts here


# def kthToLastNodeNotWorking(k, head):
#     starting_node = head
#     # i need a trailing node
#     trail_node = head

#     # i know that if k is less than 1, thats a problem
#     if k < 1:
#         return print(f"Yo, check your k value. It's got to be at least 1")
#     else:
#         while not starting_node.next = None:
#             starting_node = starting.node.next
#             trail_node = trail_node.next
#             for i in range(k - 1):
#                 pass


def kthToLastNode(k, head):
    if k < 1:
        raise Exception(
            f"Impossible to find less than first to last node: {k}")

    leftNode = head
    rightNode = head

    # move rightNode to the kth node
    for i in range(k - 1):
        # but along the way, if a rightNode doesn't have a next,
        # then k is greater than the length of the list and there
        # can't be a kth-to-last node! we'll raise an error
        if not rightNode.next:
            raise Exception(
                f"k is larger than the length of the linked list: {k}")

        rightNode = rightNode.next

    # starting with leftNode on the head,
    # move leftNode and rightNode down the list,
    # maintaining a distance of k between them,
    # until rightNode hits the end of the list
    while rightNode.next:
        leftNode = leftNode.next
        rightNode = rightNode.next

    # since leftNode is k nodes behind rightNode,
    # leftNode is now the kth to last node!
    return leftNode.value


a = ListNode("Australian Sheperd")
b = ListNode("Beagle")
c = ListNode("Cairne Terrier")
d = ListNode("Dobermann")
e = ListNode("English Mastiff")

a.next = b
b.next = c
c.next = d
d.next = e

# Some tests
print(kthToLastNode(2, a))   # should print 'Dobermann'
print(kthToLastNode(5, a))   # should print 'Australian Sheperd'
print(kthToLastNode(3, c))   # should print 'Cairne Terrier'
