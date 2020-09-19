from draw_part import *
from game_work_part import *


def do_all_stuff(x, y):
    global m
    global game_list
    if not someone_wins(game_list)[0] and not is_it_a_draw(game_list):
        put_x, put_y = get_clever_coords(x, y)[0], get_clever_coords(x, y)[1]

        try:
            if game_list[position_in_game_list(put_x, put_y)[0]][position_in_game_list(put_x, put_y)[1]] == 0:
                game_list[position_in_game_list(put_x, put_y)[0]][position_in_game_list(put_x, put_y)[1]] = (m % 2) + 1
                if m % 2 == 0:
                    Cross(put_x, put_y, "red", 95).show()
                else:
                    Circle(put_x, put_y, 95, "blue").show()
                m += 1

            if someone_wins(game_list)[0]:
                player_wins(someone_wins(game_list)[1])
            elif is_it_a_draw(game_list):
                it_is_a_draw()

        except TypeError:
            pass

    elif someone_wins(game_list)[0]:
        player_wins(someone_wins(game_list)[1])

    else:
        it_is_a_draw()


home()
ht()
speed(0)
Board3(0, 0, "black", 300).show()

onscreenclick(do_all_stuff)

mainloop()
