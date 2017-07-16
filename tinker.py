import tkinter as tk
#from tkinter import Tk, ttk
from player import Player
from getwild import GetWild

import time
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
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play wild",
                            command= self.play)

        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

    def play(self):
        answer_wild = select_answer_wild()
        a=Player('getwilds')
        a.playWild(answer_wild.file_name, answer_wild.firs_get_wild_seek)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

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
