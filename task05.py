def use_list_comprehensions(list_in):
    try:
        list_out = [int(i) for i in list_in]
    except:
        print(-1)
        return
    print("Четные:", [x for x in list_out if x % 2 == 0])
    print("Нечетные:", [x for x in list_out if x % 2 == 1])
    print("Меньше 0:", [x for x in list_out if x < 0])


def use_map_filter(list_in):
    try:
        list_out = list(map(lambda x: int(x), list_in))
    except:
        print(-1)
        return
    print("Четные:", list(filter(lambda x: x % 2 == 0, list_out[::])))
    print("Нечетные:", list(filter(lambda x: x % 2 == 1, list_out[::])))
    print("Меньше 0:", list(filter(lambda x: x < 0, list_out[::])))


if __name__ == '__main__':
    list_in = input().split(' ')
    use_list_comprehensions(list_in)
    use_map_filter(list_in)
