import os
import shutil
import tkinter as tkdeactivate
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
font_style = ("Microsoft JhengHei", 12)

def wherethefolder():  # 抓取c路徑位置
    files = filedialog.askdirectory()
    seq.set(files)

def rename_and_sort_images():
    try:
        # 獲取用戶指定的資料夾路徑
        folder_path = seq.get()
        print(folder_path)
        
        # 獲取用戶輸入的初始計數器值
        counter = int(counter_var.get())

        filename = str(fname.get())

        # 獲取資料夾中的所有符合條件的文件
        files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.mp4', '.jpg'))]

        # 如果沒有符合條件的文件，拋出錯誤
        if not files:
            raise ValueError("資料夾中沒有找到符合條件的文件 (png, jpg, mp4)")

        # 按照文件名排序
        files.sort()

        # 遍歷文件並重新命名
        for file in files:
            # 新的文件名格式為：flower_00000.png，其中 counter 是計數器的值，格式化為五位數
            new_name = f'{filename}_{counter:05d}.png'

            # 構建完整的文件路徑
            old_path = os.path.join(folder_path, file)
            new_path = os.path.join(folder_path, new_name)

            # 重新命名文件
            shutil.move(old_path, new_path)
            print(f'已重新命名: {file} 為 {new_name}')

            # 計數器加一
            counter += 1

        # 顯示成功消息
        messagebox.showinfo("成功", "文件重新命名和排序成功！")
        
    except ValueError as ve:
        messagebox.showerror("錯誤", f"出現錯誤：{str(ve)}")
        
    except Exception as e:
        messagebox.showerror("錯誤", f"出現錯誤：{str(e)}")

root = ctk.CTk()
root.geometry("300x280")
root.title("Renameit")

# 修改背景色
root.configure(fg_color='#EDEDF2')

root_frame = ctk.CTkFrame(root, fg_color='#EDEDF2')
root_frame.pack(fill='x', padx=10, pady=10)

photo = ctk.CTkImage(light_image=Image.open("Renameit/Assets/open-folder.png"))


# 抓取位置按鈕
btn_folderpath = ctk.CTkButton(root_frame,
                font=font_style,
                text="選取資料夾位置",
                text_color="#191B1D",
                fg_color="#FF8AEB",
                hover_color="#FFC3F5",
                image=photo,
                command=wherethefolder,
                height=35)
btn_folderpath.pack(padx=5, pady=10)

# 位置顯示框
seq = ctk.StringVar()  # 建立文字變數
seq.set('Filepath')  # 一開始設定沒有內容
entry_folder = ctk.CTkEntry(root_frame, textvariable=seq, border_width=0, text_color='#bdb5bc', font=("Calibri", 12))
entry_folder.pack(fill='x', padx=10, pady=5, ipadx=5, ipady=2)

root_frame2 = ctk.CTkFrame(root, fg_color='#EDEDF2')
root_frame2.pack(fill='x', padx=50, pady=0)

root_frame3 = ctk.CTkFrame(root, fg_color='#EDEDF2')
root_frame3.pack(fill='x', padx=50, pady=0)

# 新增名稱/ID號
fname = ctk.StringVar(value="seq")  # 設定初始值
fname_label = ctk.CTkLabel(root_frame2, text="序列名稱/ID : ", font=font_style)
fname_label.pack(side='left', padx=5, pady=5)
entry_fname = ctk.CTkEntry(root_frame2, textvariable=fname, border_width=0, text_color="#FF86C9", width=10)
entry_fname.pack(fill='x', padx=5, pady=5, ipadx=30, ipady=2)

# 新增計數器輸入框
counter_var = ctk.StringVar(value="00000")  # 設定初始值
counter_label = ctk.CTkLabel(root_frame3, text="初始計數器值 : ", font=font_style)
counter_label.pack(side='left', padx=5, pady=5)
entry_counter = ctk.CTkEntry(root_frame3, textvariable=counter_var, border_width=0, text_color="#FF86C9", width=10)
entry_counter.pack(fill='x', padx=5, pady=5, ipadx=30, ipady=2)

# 執行按鈕
btn_go = ctk.CTkButton(root,
                font=font_style,
                text="✮⋆｡✩ 執行 ｡°✩⋆°✮",
                text_color="#FFFFFF",
                fg_color="#1A1A1A",
                hover_color="#555555",
                command=rename_and_sort_images,
                height=35)
btn_go.pack(padx=5, pady=10)

root.mainloop()
