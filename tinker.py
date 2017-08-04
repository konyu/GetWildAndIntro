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

        for F in (StartPage, IntroPage, ResultPage, MiddlePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def is_end(self):
        if(self.correction_num >= 5 or self.sum_quiz_num >= 10):
            return True
        else:
            return False


    def show_frame(self, page_name, arg=None, ans=None):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "IntroPage":
            frame.create_quiz(arg)
        elif page_name == "ResultPage":
            frame.show_result()
        elif page_name == "MiddlePage":
            frame.show_result(arg, ans)


class StartPage(tk.Frame):
    # TODO スタートするまでGe wild Gewildを言い続ける　5問正解しないとまたGewildループに入る
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Get Wild and Intro", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Start", font=tkfont.Font(size=20),
                            command=lambda: controller.show_frame("IntroPage", "play"))
        button2.pack(fill='both', expand=1)


class IntroPage(tk.Frame):
    answer_wild = None
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="どのGet Wildでしょうか", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)

        self.btn_play = tk.Button(self, text="Replay", command= self.play, font=tkfont.Font(size=15))

        # if(self.btn_play.winfo_exists() == False):
        self.btn_play.pack()

        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()

        self.selections = []
        # self.selection_texts = []
        for var in range(0, 4):
            # btn_text = tk.StringVar()
            # btn_text.set("-------------AAA")
            # self.selection_texts.append(btn_text)
            btn = tk.Button(self, text="-------------", pady=10, font=tkfont.Font(size=12))
            # btn = tk.Button(self, textvariable=btn_text)
            # self.selections[i].command =
            self.selections.append(btn)
            btn.pack(fill='both', expand=1)

        self.create_quiz("init")


    def create_quiz(self, arg):
        #import pdb; pdb.set_trace()

        wilds = []
        self.answer_wild = select_answer_wild()
        # import pdb; pdb.set_trace()

        correct_answer = "%s %s" % (self.answer_wild.title, self.answer_wild.artist)
        wilds.append(self.answer_wild)

        for wild in select_choices_wild():
            wilds.append(wild)
        random.shuffle(wilds)

        i = 0
        for wild in wilds:
            answer = "%s %s" % (wild.title, wild.artist)
            text = "%s\n%s" % (wild.title, wild.artist)
            self.selections[i].config(text= text)
            self.selections[i].config(command= (lambda ans_str=answer: self.ans(ans_str)))
            i += 1

        if(arg != "init"):
            self.play()
            # import pdb; pdb.set_trace()
            # else:

    # 回答する
    def ans(self, answer):
        result = "correct"
        print(answer)
        if(answer == self.answer_wild.title + " " + self.answer_wild.artist):
            print("正解！！")
            result = "correct"
            self.controller.correction_num += 1
        else:
            result = "incorrect"
            print("不正解")

        self.controller.sum_quiz_num += 1
        print(result)
        if(self.controller.is_end()):
            self.controller.show_frame("ResultPage")
        else:
            self.controller.show_frame("MiddlePage", result, answer)

        return "answer"

    def play(self):
        print(self.answer_wild.title + " " + self.answer_wild.artist)
        a=Player('getwilds')
        a.playWild(self.answer_wild.file_name, self.answer_wild.firs_get_wild_seek)

class MiddlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=10)

        self.label2 = tk.Label(self, text="正解は", font=controller.title_font)
        self.label2.pack(side="top", fill="x", pady=10)
        #
        self.label3 = tk.Label(self, text="", font=controller.title_font)
        self.label3.pack(side="top", fill="both", pady=10)

        self.label4 = tk.Label(self, text="でした", font=controller.title_font)
        self.label4.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Next", font=tkfont.Font(size=15),
                           command=lambda: controller.show_frame("IntroPage"))
        button.pack(fill='both', expand=1)

    def show_result(self, result, ans):
        text = "%s問中%s正解" % (self.controller.sum_quiz_num, self.controller.correction_num)
        if(result == "correct"):
            self.label.config(text=("正解！！！" + text) , fg="blue")
        elif(result == "incorrect"):
            self.label.config(text=("不正解！！"+ text), fg="red")
        dst = ans.replace(' ', '\n')
        self.label3.config(text=dst)


class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="結果発表", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.label2 = tk.Label(self, text="", font=controller.title_font)
        self.label2.pack(side="top", fill="x", pady=10)

        self.label3 = tk.Label(self, text="", font=controller.title_font)
        self.label3.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="スタートに戻る",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def show_result(self):
        result = "You are just Mild. ¯\_(ツ)_/¯ "
        if(self.controller.correction_num >= 5):
            result = "You are WILD!!!"
        self.label2.config(text=result)
        # import pdb; pdb.set_trace()

        detail = "%s/%s正解" % (self.controller.correction_num, self.controller.sum_quiz_num)
        self.label3.config(text=detail)

        self.controller.correction_num = 0
        self.controller.sum_quiz_num = 0


if __name__ == "__main__":
    app = SampleApp()
    # app.overrideredirect(True)
    # app.overrideredirect(False)
    app.attributes('-fullscreen',True)
    app.mainloop()
    # app.geometry("400x300")
    #app.attributes("-fullscreen", True)


# #-----------------
# root.title("日本語Get Wild")
#
# # フルスクリーン化
# #root.attributes("-fullscreen", True)
# root.geometry("400x300")
