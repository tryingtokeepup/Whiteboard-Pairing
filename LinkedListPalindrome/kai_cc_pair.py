class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def isLinkedListPalindrome(node):

    iterator = node
    array = []


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)

a.next = b
b.next = c
c.next = d
d.next = e

w = ListNode(10)
x = ListNode(11)
y = ListNode(11)
z = ListNode(10)

w.next = x
x.next = y
y.next = z


print(isLinkedListPalindrome(a))   # should print true
# should print false since now the 'a' node is not included in the linked list
print(isLinkedListPalindrome(b))

print(isLinkedListPalindrome(w))   # should print true
