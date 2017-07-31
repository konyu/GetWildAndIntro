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
        for F in (StartPage, IntroPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name, arg=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if arg:
            frame.create_quiz(arg)


class StartPage(tk.Frame):
    # TODO スタートするまでGe wild Gewildを言い続ける　5問正解しないとまたGewildループに入る
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Get Wild イントロ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # button1 = tk.Button(self, text="Play wild", command= self.play)

        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("IntroPage", "play"))
        # button1.pack()
        button2.pack()


class IntroPage(tk.Frame):
    answer_wild = None
    # TODO 画面切り替わり時に音声再生
    # TODO ボタンの大きさをグリッド表示にする
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
        # 既存のボタンを削除する
        # for btn in self.selections:
        #     btn.destroy()
        # self.selections = []
        # for btn in tk.Frame.buttons:
        #     btn.destroy() #config(state=tk.DISABLED)
        # self.binst.destroy()
        #         remove.grid(row=r,column=6,sticky='w')
        #
        # remove.grid_forget()
        # pack_forget() [
        #import pdb; pdb.set_trace()

        wilds = []
        self.answer_wild = select_answer_wild()
        # import pdb; pdb.set_trace()
        if(arg != "init"):
            self.play()

        correct_answer = "%s %s" % (self.answer_wild.title, self.answer_wild.artist)
        wilds.append(self.answer_wild)

        for wild in select_choices_wild():
            # print("!" + wild.title + " " + wild.artist)
            # answer = "%s %s" % (wild.title, wild.artist)
            wilds.append(wild)
        random.shuffle(wilds)

        # for wild in wilds:
        #     # print(wild)
        #     # print(wild.title + " " + wild.artist)
        #     answer = "%s %s" % (wild.title, wild.artist)
        #
        #     # answer = str(copy.deepcopy(wild))
        #     print(answer)
        #     btn = tk.Button(self, text=answer, command = lambda ans=answer : self.ans(ans))
        #     btn.pack()
        #     self.selections.append(btn)

        i = 0
        for wild in wilds:
            answer = "%s %s" % (wild.title, wild.artist)
            self.selections[i].config(text= answer)
            self.selections[i].config(command= (lambda ans_str=answer: self.ans(ans_str)))
            i += 1

        # for i in range(0, 4):
        #     # self.selection_texts[i].set(wilds[i])
        #     # self.selections[i].textvariable.set(wilds[i])
        #     ans_str = wilds[copy.deepcopy(i)]
        #     #ans_str = copy.deepcopy(i)
        #
        #     self.selections[i].config(text= ans_str)
        #     self.selections[i].config(command= (lambda : self.ans(ans_str)))
            #self.selections[i].pack()

        # btn = tk.Button(self, text="%s %s" % (self.answer_wild.title, self.answer_wild.artist), command= lambda : self.ans(correct_answer))
        # # btn.pack()
        # self.selections.append(btn)
        #
        # for wild in select_choices_wild():
        #     print(wild.title + " " + wild.artist)
        #     answer = "%s %s" % (wild.title, wild.artist)
            # btn = tk.Button(self, text=answer, command = lambda : self.ans(answer))
            # selections.append(btn)

        # random.shuffle(selections)
        # for btn in selections:
        #     btn.pack()


    # 回答する
    def ans(self, answer):
        # TODO 正解不正解をと正しい答えを次のページに受け渡す
        print(answer)
        if(answer == self.answer_wild.title + " " + self.answer_wild.artist):
            print("正解！！")
            self.controller.show_frame("IntroPage", "play")
        else:
            print("不正解")
        return "answer"

    def play(self):
        print(self.answer_wild.title + " " + self.answer_wild.artist)
        a=Player('getwilds')
        a.playWild(self.answer_wild.file_name, self.answer_wild.firs_get_wild_seek)


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
