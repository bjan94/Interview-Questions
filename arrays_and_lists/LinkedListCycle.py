from common.Node import ListNode


class Solver:
    """
    Given a linked list, determine if it has a cycle in it.

    Follow up:
    Can you solve it without using extra space?
    """

    def list_has_cycle(self, head):
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


def main():
    solver = Solver()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = head.next

    print(solver.list_has_cycle(head))


if __name__ == "__main__":
    main()

e