import tkinter as tk
from tkinter import ttk

class MemberReg :
    hobby_list = ["영화 시청", "음악 감상", "사진 찍기", "운동", "독서"]

    def __init__(self) :
        self.win = tk.Tk()
        self.win.title("회원 가입")
        self.buildGUI()

    def buildGUI(self) : # frame 관리 / frame : 이름, 학년, 취미의 전체 레이아웃 관리
        self.name_input_frame().grid(row = 0, column = 0, sticky = 'w')
        self.class_input_frame().grid(row = 1, column = 0, sticky = 'w')
        self.hobby_input_frame().grid(row = 2, column = 0, sticky = 'w')
        self.btn_input_frame().grid(row = 3, column = 0, sticky = 'e')

    def name_input_frame(self) :
        frame = ttk.Frame(self.win) # frame 선언

        self.text_label = ttk.Label(frame, text = '이름 : ')

        self.name = tk.StringVar()
        input_entry = ttk.Entry(frame, textvariable = self.name)

        self.text_label.grid(row = 0, column = 0) # grid : 격자형으로 frame안에서 세부적인 자리 잡기
        input_entry.grid(row = 0, column = 1)

        return frame

    def class_input_frame(self) :
        frame = ttk.Frame(self.win) # 한 줄 짜리 묶음 전체 (학년 입력 라벨 + 버튼들)

        self.text_label = ttk.Label(frame, text = '학년 : ')
        
        sub_frame = ttk.Frame(frame) # 서브프레임 설정 parameter : 이 프레임안에서 프레임 매서드로 선언 !
        self.grade = tk.IntVar()
        for i in range(1, 5) :
            grade_check = ttk.Radiobutton(sub_frame, text = f"{i}학년", value = i, variable = self.grade)
            # 서브프레임 안에 라디오 버튼을 넣겠습니다 !
            grade_check.pack(side = tk.LEFT) # 서브프레임 안에서 버튼을 왼쪽부터 쌓겠다

        self.text_label.grid(row = 0, column = 0) # 서브프레임안에 들어있지 않은 라벨 배치하고
        sub_frame.grid(row = 0, column = 1) # 서브프레임을 그 다음으로 배치
        
        return frame

    def hobby_input_frame(self) :
        frame = ttk.Frame(self.win)

        self.text_label = ttk.Label(frame, text = '취미 : ')

        sub_frame = ttk.Frame(frame)
        self.hobby = []
        for i in range(len(self.hobby_list)) :
            self.hobby.append(tk.IntVar())
            hobby_btn = ttk.Checkbutton(sub_frame, text = self.hobby_list[i], variable = self.hobby[i])
            hobby_btn.pack(side=tk.LEFT)

        self.text_label.grid(row = 0, column = 0) 
        sub_frame.grid(row = 0, column = 1)

        return frame

    def btn_input_frame(self) :
        frame = ttk.Frame(self.win)

        input_btn = ttk.Button(frame, text = '입력', command = self.input_btn_clicked)
        
        quit_btn = ttk.Button(frame, text = '종료', command = self.win.destroy)

        input_btn.pack(side = tk.LEFT)
        quit_btn.pack(side = tk.LEFT)

        return frame

    def input_btn_clicked(self) :
        print(f"{self.name.get()}")
        print(f"{self.grade.get()}")
        
        for i in range(len(self.hobby_list)) :
            if self.hobby[i].get() == 1 :
                print(f"{self.hobby_list[i]}")

res = MemberReg()
res.win.mainloop()