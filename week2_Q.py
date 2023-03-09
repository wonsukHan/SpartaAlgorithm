class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head
        cnt = 0
        while cur is not None:
            cur = cur.next
            cnt += 1
        ans = self.head
        for i in range(cnt - k):
            ans = ans.next
        return ans


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    for i in range(len(orders)):
        if not available(menus, orders[i]):
            return False
    return True


def available(menus, order):
    menus.sort()
    while len(menus) != 1:
        if menus[len(menus) // 2] > order:
            menus = menus[:len(menus) // 2]
        elif menus[len(menus) // 2] < order:
            menus = menus[len(menus) // 2:]
        elif menus[len(menus) // 2] == order:
            return True
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)


numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current):
    cnt = 0
    if len(array) == 0:
        if target == current:
            return 1
        return 0
    cnt += get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:], target, current + array[0])
    cnt += get_count_of_ways_to_target_by_doing_plus_or_minus(array[1:], target, current - array[0])
    return cnt


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0))  # 5를 반환해야 합니다!