from common.Node import ListNode

class Solver:
    """
    Reverse a singly linked list.

    Example:

    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL
    Follow up:

    A linked list can be reversed either iteratively or recursively. Could you implement both?
    """
    def reverse_singly_linked_list(self, head):
        prev = None

        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


def main():
    solver = Solver()

    first = ListNode(1)
    head = first
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)

    print(solver.reverse_singly_linked_list(first))


if __name__ == "__main__":
    main()
