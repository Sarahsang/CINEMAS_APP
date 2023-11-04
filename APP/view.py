import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("Movie Booking")

# 从数据库导入数据
movies = {}

current_movie = "Movie 1"  # 当前选择的电影
current_index = 0  # 当前日期索引

# 更新显示的日期场次
def update_sessions(date_sessions):
    # 清空当前的场次
    for widget in session_frame.winfo_children():
        widget.destroy()
    
    # 加载新的场次信息
    for session in date_sessions:
        hall, time = session
        session_label = tk.Label(session_frame, text=f"{hall}: {time}")
        session_label.pack()

# 改变日期的函数
def change_date(delta):
    global current_index
    current_index += delta
    
    # 循环日期
    if current_index >= len(movies[current_movie]):
        current_index = 0
    elif current_index < 0:
        current_index = len(movies[current_movie]) - 1

    date, sessions = movies[current_movie][current_index]
    date_label.config(text=f"{current_movie} {date}")
    update_sessions(sessions)

# 创建页面上方的标签
header_label = tk.Label(root, text="Make a Booking", font=("Arial", 24))
header_label.pack(side="top", fill="x", pady=10)
# 创建 电影的详细信息的框架 显示电影的详细信息
header_label = tk.Label(root, text="movie1", font=("Arial", 20))
header_label.pack(side="top", fill="x", pady=20)

# 创建日期和场次的框架
date_session_frame = tk.Frame(root)
date_session_frame.pack(fill="both", expand=True)

# 日期标签
date_label = tk.Label(date_session_frame, text="", font=("Arial", 18))
date_label.pack(side="top", pady=5)

# 场次的框架
session_frame = tk.Frame(date_session_frame)
session_frame.pack(fill="both", expand=True)

# 左右按钮
left_button = tk.Button(date_session_frame, text="<", command=lambda: change_date(-1))
left_button.pack(side="left", fill="y")

right_button = tk.Button(date_session_frame, text=">", command=lambda: change_date(1))
right_button.pack(side="right", fill="y")

# 创建返回按钮
back_button = tk.Button(root, text="Back")
back_button.pack(side="bottom", fill="x", pady=10)

# 初始化场次显示
change_date(0)

# 运行主循环
root.mainloop()
