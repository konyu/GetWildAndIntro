from tkinter import Tk, ttk
from player import Player
from getwild import GetWild

import random

get_wild_list = GetWild.class_method()
#get_wild_length = len(get_wild_list)

def unplayed_list():
    unplyed_list = list(filter(lambda x: x.played == False, get_wild_list))
    if len(unplyed_list) == 0:
        return None
    else:
        return unplyed_list

def select_answer_wild():
    # for wild in get_wild_list:
    #     print(wild.played)
    answer_wild = random.choice(unplayed_list())
    answer_wild.played = True
    return answer_wild

def select_choices_wild():
    choices_wild = random.sample(unplayed_list(), 3)
    return choices_wild

# ------------
def onBackButton():
    a=Player('getwilds')
    answer_wild = select_answer_wild()
    # 適当な終了処理
    if answer_wild is None:
        print("AAAAAAAAAa")
        return
    else:
        print(answer_wild.title + " " + answer_wild.artist)
        print("------------")
        for wild in select_choices_wild():
            print(wild.title + " " + wild.artist)
        print("============")

        a.playWild(answer_wild.file_name, answer_wild.firs_get_wild_seek)
# ------------

root = Tk()

#-----------------
root.title("日本語Get Wild")

# フルスクリーン化
#root.attributes("-fullscreen", True)
root.geometry("400x300")

#ボタン
btnframe = ttk.Frame(root)
btn = ttk.Button(btnframe, text='にほんごでOk ', command=onBackButton)

# Static1 = ttk.Label(text='test')
# Static1.pack()


btnframe.grid()
btn.grid()

#------
root.mainloop()
