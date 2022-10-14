# 跳出訊息視窗
import tkinter as tk
from tkinter.constants import E, N, NE, W
import json

with open('note.json', encoding="utf-8") as f:
    data = json.load(f)
    f.close()


def onOK():
    data.append({
        "NAME": NAMEbox.get(),
        "CONTENT": contentbox.get()
    })
    with open('note.json', 'w', encoding="utf8") as file:  # utf-8解碼文正常文字
        json.dump(data, file, ensure_ascii=False)
    file.close()



window = tk.Tk()
window.title('視窗')
window.geometry("300x100+250+150")

# 標示文字
NAME = tk.Label(window, text='名稱')
content = tk.Label(window, text='內容')

# 輸入欄位
NAMEbox = tk.Entry(window, width=30)
contentbox = tk.Entry(window, width=30)

# 按鈕
button = tk.Button(window, text="OK", command=onOK)


# grid版面調整區域
NAME.grid(row=0, column=0, sticky=E, padx=0, pady=2)  # 路徑
content.grid(row=1, column=0, sticky=E, padx=0, pady=2)  # 尋找
NAMEbox.grid(row=0, column=1, sticky=W, padx=30,  pady=2)  # 路徑box
contentbox.grid(row=1, column=1, sticky=W, padx=30, pady=2)  # 尋找box
button.grid(row=2, column=1, padx=5, pady=2)  # 轉換按鈕


window.mainloop()
