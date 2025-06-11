import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class WordBook :

    dic_wordbook = {}

    def __init__(self) :
        self.win = tk.Tk()
        self.win.title("단어장")
        self.buildGUI()
        self.loadData()

    def buildGUI(self) :
        self.first_row_frame().grid(row = 0, column = 0, sticky = 'w')
        self.second_row_frame().grid(row = 1, column = 0, sticky = 'w')
        self.third_row_frame().grid(row = 2, column = 0, sticky = 'e')

    def loadData(self) :
        if not os.path.exists("words.txt") : # 파일 존재 여부 검사 : TRUE/FALSE 리턴
            with open("words.txt", "w", encoding = "utf-8") as file : # 파일이 없다면 빈 파일 생성
                pass
            return self.dic_wordbook
        
        with open("words.txt", "r", encoding = "utf-8") as file : # with open : close 걱정없이 파일을 알아서 열고닫는다
            for line in file :
                word = line.split(":") # 단어 뜻 분리 / split 매서드는 항상 리스트에 넣어서 리스트를 반환해준다
                for i in range(0, len(word)) :
                    word[i] = word[i].strip() # 공백제거
                key = word[0]
                value = word[1]
                self.dic_wordbook[key] = value

        return self.dic_wordbook
                
 
    def first_row_frame(self) :
        frame = ttk.Frame(self.win)

        self.text_label = tk.Label(frame, text = "단어 : ")

        self.input_var = tk.StringVar()
        self.text_entry = ttk.Entry(frame, textvariable = self.input_var)

        search_btn = ttk.Button(frame, text = '검색', command = self.search_word)

        add_btn = ttk.Button(frame, text = '추가', command = self.add_word)

        self.text_label.grid(row = 0, column = 0)
        self.text_entry.grid(row = 0, column = 1)
        search_btn.grid(row = 0, column = 2)
        add_btn.grid(row = 0, column = 3)

        return frame
    
    def second_row_frame(self) :
        frame = ttk.Frame(self.win)

        self.text_label = tk.Label(frame, text = '뜻 : ')

        self.meaning_var = tk.StringVar()
        self.meaning_entry = ttk.Entry(frame, textvariable = self.meaning_var)

        self.text_label.grid(row = 0, column = 0)
        self.meaning_entry.grid(row = 0, column = 1)

        return frame
    
    def third_row_frame(self) :
        frame = ttk.Frame(self.win)

        reset_btn = ttk.Button(frame, text = '초기화', command = self.reset_entry)

        quit_btn = ttk.Button(frame, text = '종료', command = self.win.destroy)

        reset_btn.pack(side = tk.LEFT)
        quit_btn.pack(side = tk.LEFT)

        return frame
    
    def search_word(self) :
        input = self.input_var.get()
        if input in self.dic_wordbook :
            self.meaning_var.set(f"{self.dic_wordbook[input]}")
        else :
            messagebox.showinfo('검색 오류', f"{self.input_var.get()}라는 단어는 없습니다 !")

    def add_word(self) :
        input = self.input_var.get()
        meaning = self.meaning_var.get()
        self.dic_wordbook[input] = meaning
        self.input_var.set('')
        self.meaning_var.set('')
        messagebox.showinfo('추가 확인', f"단어 {input}를 추가했습니다.")
    
    def reset_entry(self) :
        self.input_var.set('')
        self.meaning_var.set('')

test = WordBook()
test.win.mainloop()