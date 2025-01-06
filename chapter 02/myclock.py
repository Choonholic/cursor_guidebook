import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # 1초마다 시간 업데이트

# 메인 윈도우 생성
root = tk.Tk()
root.title("현재 시각")
root.geometry("300x100")  # 윈도우 크기를 더 크게 설정

# 시간 표시를 위한 레이블 생성
label = tk.Label(root, font=('Helvetica', 48), fg='black')
label.pack()

update_time()  # 시간 업데이트 함수 호출
root.mainloop()  # 이벤트 루프 시작