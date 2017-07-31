import tkinter as tk
#from tkinter import Tk, ttk
from player import Player
from getwild import GetWild

import time
import random
import copy

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

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.correction_num = 0
        self.sum_quiz_num = 0

        for F in (StartPage, IntroPage, ResultPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def is_end(self):
        if(self.correction_num >= 5 or self.sum_quiz_num >= 10):
            return True
        else:
            return False


    def show_frame(self, page_name, arg=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "IntroPage" and arg:
            frame.create_quiz(arg)


class StartPage(tk.Frame):
    # TODO スタートするまでGe wild Gewildを言い続ける　5問正解しないとまたGewildループに入る
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Get Wild イントロ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("IntroPage", "play"))
        button2.pack()


class IntroPage(tk.Frame):
    answer_wild = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="どのGet Wildでしょうか", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.btn_play = tk.Button(self, text="Play wild", command= self.play)

        # if(self.btn_play.winfo_exists() == False):
        self.btn_play.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.selections = []
        # self.selection_texts = []
        for var in range(0, 4):
            # btn_text = tk.StringVar()
            # btn_text.set("-------------AAA")
            # self.selection_texts.append(btn_text)
            btn = tk.Button(self, text="-------------AAA")
            # btn = tk.Button(self, textvariable=btn_text)
            # self.selections[i].command =
            self.selections.append(btn)
            btn.pack()

        self.create_quiz("init")


    def create_quiz(self, arg):
        #import pdb; pdb.set_trace()

        wilds = []
        self.answer_wild = select_answer_wild()
        # import pdb; pdb.set_trace()
        if(arg != "init"):
            self.play()

        correct_answer = "%s %s" % (self.answer_wild.title, self.answer_wild.artist)
        wilds.append(self.answer_wild)

        for wild in select_choices_wild():
            wilds.append(wild)
        random.shuffle(wilds)

        i = 0
        for wild in wilds:
            answer = "%s %s" % (wild.title, wild.artist)
            self.selections[i].config(text= answer)
            self.selections[i].config(command= (lambda ans_str=answer: self.ans(ans_str)))
            i += 1

    # 回答する
    def ans(self, answer):
        # TODO 正解不正解をと正しい答えを次のページに受け渡す
        print(answer)
        if(answer == self.answer_wild.title + " " + self.answer_wild.artist):
            print("正解！！")
            self.controller.correction_num += 1
        else:
            print("不正解")

        self.controller.sum_quiz_num += 1

        if(self.controller.is_end()):
            self.controller.show_frame("ResultPage", "play")
        else:
            self.controller.show_frame("IntroPage", "play")

        return "answer"

    def play(self):
        print(self.answer_wild.title + " " + self.answer_wild.artist)
        a=Player('getwilds')
        a.playWild(self.answer_wild.file_name, self.answer_wild.firs_get_wild_seek)


class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

# # ------------
# def onBackButton():
#     a=Player('getwilds')
#     answer_wild = select_answer_wild()
#     # 適当な終了処理
#     if answer_wild is None:
#         print("AAAAAAAAAa")
#         return
#     else:
#         print(answer_wild.title + " " + answer_wild.artist)
#         print("------------")
#         for wild in select_choices_wild():
#             print(wild.title + " " + wild.artist)
#         print("============")
#
#         a.playWild(answer_wild.file_name, answer_wild.firs_get_wild_seek)
# # ------------
#
# root = Tk()
#
# #-----------------
# root.title("日本語Get Wild")
#
# # フルスクリーン化
# #root.attributes("-fullscreen", True)
# root.geometry("400x300")
#
# #ボタン
# btnframe = ttk.Frame(root)
# btn = ttk.Button(btnframe, text='にほんごでOk ', command=onBackButton)
#
# btnframe.grid()
# btn.grid()
# #------
# root.mainloop()
