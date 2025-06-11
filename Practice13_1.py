import tkinter as tk
from tkinter import ttk

class Temperature :
    def __init__(self) :
        self.win = tk.Tk()
        self.win.title("온도 변환기 - 1단계")
        self.buildGUI()

    def buildGUI(self) :
        self.text_label1 = ttk.Label(self.win, text = '화씨')
        self.text_label2 = ttk.Label(self.win, text = '섭씨')

        self.input_F = tk.StringVar(value = 0.0)
        self.input_C = tk.StringVar(value = 0.0)

        input_F_temp = ttk.Entry(self.win, justify = tk.RIGHT, width = 11, textvariable = self.input_F)

        input_C_temp = ttk.Entry(self.win, justify = tk.RIGHT, width = 11, textvariable = self.input_C)

        btn_F_to_C = ttk.Button(self.win, text = "화씨 → 섭씨", command = self.F_to_C)
        
        btn_C_to_F = ttk.Button(self.win, text = "섭씨 → 화씨", command = self.C_to_F)
        
        reset_btn = ttk.Button(self.win, text = "초기화", command = self.clear)

        quit_btn = ttk.Button(self.win, text = '종료', command = self.win.destroy)

        self.text_label1.grid(row = 0, column = 0)
        input_C_temp.grid(row = 0, column = 1)
        self.text_label2.grid(row = 0, column = 2)
        input_F_temp.grid(row = 0, column = 3)
        btn_F_to_C.grid(row = 1, column = 0)
        btn_C_to_F.grid(row = 1, column = 1)
        reset_btn.grid(row = 1, column = 2)
        quit_btn.grid(row = 1, column = 3)



    def F_to_C(self) :
        get_F = float(self.input_F.get()) # 변수를 꺼낼 때 get함수 필수
        result_C = (get_F - 32) / 1.8
        self.input_C.set(f"{result_C:.2f}")

    def C_to_F(self) :
        get_C = float(self.input_C.get())
        result_F = (get_C * 1.8) + 32
        self.input_F.set(f"{result_F:.2f}")

    def clear(self) :
        clear1 = self.input_F.set('0.0')
        clear2 = self.input_C.set('0.0')

level = Temperature()
level.win.mainloop()