def move_disk(start_peg, end_peg):
    print("from", start_peg, "to", end_peg)


def move_tower(n, start_peg=1, end_peg=2):
    if n == 1:
        move_disk(start_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg
        move_tower(n - 1, start_peg, spare_peg)
        move_disk(start_peg, spare_peg)
        move_tower(n - 1, spare_peg, end_peg)


move_tower(3)
