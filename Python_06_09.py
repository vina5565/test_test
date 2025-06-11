import tkinter as tk
from tkinter import ttk

class MyWindow : 
    def __init__(self) :
        self.win = tk.Tk() # 윈도우 창 객체 생성
        self.win.title("버튼 위젯 예 - OOP") # 윈도우 창 타이틀
        self.buildGUI() 

    def buildGUI(self) :
        self.text_label = ttk.Label(self.win, text = "안녕하세요") # 텍스트 출력 라벨

        self.name = tk.StringVar() # 사용자 입력 저장 변수

        input_entry = ttk.Entry(self.win, textvariable = self.name) # 사용자 입력 칸 생성 (윈도창과 연결, self.name과 연결)

        input_btn = ttk.Button(self.win, text = '입력', command = self.input_btn_handler) # 버튼 생성, 명령어 설정

        quit_btn = ttk.Button(self.win, text = '종료', command = self.win.destroy) # 버튼 설정, 명령어 설정

        self.text_label.pack()
        input_entry.pack()
        input_btn.pack()
        quit_btn.pack() #패킹

    def input_btn_handler(self) :
        self.text_label.configure(text = '반가워요, ' + self.name.get()) # 특정 라벨의 텍스트를 구성 / 저장된 입력 변수 가져오기
        self.name.set('') # 입력 후 칸 초기화


hello = MyWindow()
hello.win.mainloop()