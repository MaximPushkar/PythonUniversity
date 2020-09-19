def someone_wins(l):
    ans = [False, None]
    for i in range(3):
        if [l[i][0], l[i][1], l[i][2]] == [1, 1, 1]:
            ans = [True, "1"]
        elif [l[i][0], l[i][1], l[i][2]] == [2, 2, 2]:
            ans = [True, "2"]
        elif [l[0][i], l[1][i], l[2][i]] == [1, 1, 1]:
            ans = [True, "1"]
        elif [l[0][i], l[1][i], l[2][i]] == [2, 2, 2]:
            ans = [True, "2"]
    if [l[0][0], l[1][1], l[2][2]] == [1, 1, 1]:
        ans = [True, "1"]
    elif [l[0][0], l[1][1], l[2][2]] == [2, 2, 2]:
        ans = [True, "2"]
    elif [l[0][2], l[1][1], l[2][0]] == [1, 1, 1]:
        ans = [True, "1"]
    elif [l[0][2], l[1][1], l[2][0]] == [2, 2, 2]:
        ans = [True, "2"]
    return ans


def is_it_a_draw(l):
    for i in range(3):
        if l[i].count(0) != 0:
            return False
    return True


def get_clever_coords(x, y):
    put_x, put_y = None, None

    if abs(x) <= 50:
        put_x = 0
    elif 150 > x > 50:
        put_x = 100
    elif -150 < x < -50:
        put_x = -100

    if abs(y) <= 50:
        put_y = 0
    elif 150 > y > 50:
        put_y = 100
    elif -150 < y < -50:
        put_y = -100

    return put_x, put_y


def position_in_game_list(put_x, put_y):
    if put_x is None or put_y is None:
        return [None, None]
    else:
        if put_x == 0:
            column_number = 1
        elif put_x == -100:
            column_number = 0
        else:
            column_number = 2

        if put_y == 0:
            line_number = 1
        elif put_y == -100:
            line_number = 2
        else:
            line_number = 0

        return [line_number, column_number]


m = 0
game_list = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
winner = [False, None]
