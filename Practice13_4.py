import tkinter as tk
from tkinter import ttk
from tkinter import messagebox # 결과창을 윈도우창으로 띄우고싶다면 사용

# main idea = 체크박스에서 여러 개의 체크 여부 관리 : 리스트를 생성하고 반복문에서 intvar()로 반복적으로 체크 여부인 0과 1 저장 / 필요할 때 .get()으로 꺼내쓰기

class PlayerInfo :
    list_class = ["1학년", "2학년", "3학년", "4학년"]
    list_hobby = ["영화 시청", "음악 감상", "사진 찍기", "운동", "독서"]
    hobby_checklist = []

    def __init__(self) :
        self.win = tk.Tk()
        self.win.title("회원 가입")
        self.buildGUI()

    def buildGUI(self) :
        self.name_label = ttk.Label(self.win, text = "이름 : ")

        self.name_input = tk.StringVar()
        self.name_entry = ttk.Entry(self.win, textvariable = self.name_input)

        self.class_label = ttk.Label(self.win, text = "학년 : ")
        self.class_var = tk.StringVar()
        for i in range(len(self.list_class)) :
            class_check = ttk.Radiobutton(self.win, text = self.list_class[i], value = self.list_class[i], variable = self.class_var) 
            class_check.grid(row = 1 , column = 1 + i, sticky='w')
            # text : 윈도우 창에서 보일 체크박스의 이름
            # value : 버튼이 선택되었을 때 variable에 저장될 값
            # variable : 여러 버튼을 묶어주는 공유 변수, 어떤 버튼이 선택되었는지 저장

        self.hobby_label = ttk.Label(self.win, text = "취미 : ")
        for i in range(len(self.list_hobby)) : # IntVar()로 0과1 생성
            var = tk.IntVar()
            hobby_check = ttk.Checkbutton(self.win, text = self.list_hobby[i], variable = var)
            hobby_check.grid(row = 2 , column = 1 + i, sticky='w')
            self.hobby_checklist.append(var)

        self.input_btn = ttk.Button(self.win, text = "입력", command = self.input_info)

        self.quit_btn = ttk.Button(self.win, text = "종료", command = self.win.destroy)

        self.name_label.grid(row = 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)
        self.class_label.grid(row = 1, column = 0)
        self.hobby_label.grid(row = 2, column = 0)
        self.input_btn.grid(row = 3, column = 2)
        self.quit_btn.grid(row = 3, column = 3)

    def input_info(self) :
        print(f"{self.name_input.get()}") # 변수를 호출할 때 .get() 함수 필수
        class_str = self.class_var.get()
        only_int = int(class_str[0])
        print(f"{only_int}")
        for i in range(len(self.list_hobby)) :
            if self.hobby_checklist[i].get() == 1 :
                print(f"{self.list_hobby[i]}")

print_info = PlayerInfo()
print_info.win.mainloop()