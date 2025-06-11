import tkinter as tk # 모듈 불러오기
from tkinter import ttk # 위젯 불러오기

def display_options(widget) : # 전달된 위젯의 설정가능한 모든 옵션을 출력하는 함수
    config = widget.configure()
    for key, value in config.items() :
        print(f"{key:15s}\t{value}")

def buildGUI() : # 배치 순서 = pack()코드의 순서

    global text_label1
    global text_label2
    global name

    name = tk.StringVar() # 엔트리 위젯에 문자열 저장
    input_entry = ttk.Entry(win, textvariable = name)
    

    sty = ttk.Style()
    sty.configure("wg.TLabel", foreground = 'white', background = 'green', font = ('맑은 고딕', 20))

    text_label1 = ttk.Label(win, text = "안녕하세요")

    text_label2 = ttk.Label(win)
    text_label2.configure(text = "반갑습니다")

    input_btn = ttk.Button(win, text = '입력', command = input_btn_handler) # 변경 커맨드 / 함수로 설정
    quit_btn = ttk.Button(win, text = '종료', command = win.destroy) # 종료 커맨드

    text_label1.pack() # 화면에 위젯을 배치하는 레이아웃 매서드
    text_label2.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler() :
    text_label2.configure(text = '무엇을 원하시나요, ' + name.get()) # 반갑습니다가 변경
    name.set('')

win = tk.Tk() # 윈도우 객체 생성
win.title("기본 위젯 예시")
buildGUI() # GUI 위젯 구성 실행
win.mainloop() # 이벤트 루프 실행
