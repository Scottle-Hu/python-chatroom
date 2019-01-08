from tkinter import *
from tkinter.messagebox import showinfo
import sys

# 公共变量
root = Tk()
var = StringVar()


# 鼠标点击事件
def press_btn():
    showinfo(title="entry内容", message="entry value: " + var.get())


# 打开新窗体
def openNew():
    root.destroy()
    global root2
    root2 = Tk()
    root2.title('new window')
    root2.geometry('600x400')
    Button(root2, text="关闭窗口", command=root2.destroy).pack()
    global listVar
    global listbox
    listVar = StringVar()
    listbox = Listbox(root2, selectmode=SINGLE, listvariable=listVar)
    for i in range(10):
        listbox.insert(END, i)
    print(listVar.get())
    listbox.bind('<ButtonRelease-1>', printSelection)
    listbox.pack(side=LEFT)
    Button(root2, text="删除所选", command=deleteList).pack(side=LEFT)
    scFrame = Frame(root2, height=300)
    lb = Listbox(scFrame)
    for i in range(20):
        lb.insert(END, i)
    sc = Scrollbar(scFrame, orient=VERTICAL)
    sc['command'] = lb.yview
    lb['yscrollcommand'] = sc.set
    scFrame.pack(side=RIGHT)
    lb.pack(side=LEFT, fill=BOTH)
    sc.pack(side=RIGHT, fill=Y)


def printSelection(event):
    for i in listbox.curselection():
        print(listbox.get(i))


def getCheckbutton():
    print("多选框对应的值：")
    for v in cbVar:
        print(v.get())


def deleteList():
    for i in listbox.curselection():
        listbox.delete(i)


if __name__ == "__main__":
    root.title('test gui')
    root.geometry('800x600')
    root.resizable(height=False, width=False)

    # label
    label = Label(root, text="a label", bg="lightblue", fg="red", font=("Arial", 12), width=10, height=3)
    label.pack(side=LEFT)

    # frame
    frame = Frame(root, bg="green")
    frame_L = Frame(frame, bg="blue", width=15, height=15)
    label_L_1 = Label(frame_L, text="左上标签", bg="red", width=10, height=5)
    label_L_2 = Label(frame_L, text="左下标签", bg="red", width=10, height=5)
    label_L_1.pack()
    label_L_2.pack()
    frame_R = Frame(frame, bg="red", width=15, height=15)
    label_R_1 = Label(frame_R, text="右上标签", bg="red", width=10, height=5)
    label_R_2 = Label(frame_R, text="右下标签", bg="red", width=10, height=5)
    label_R_1.pack()
    label_R_2.pack()
    frame_L.pack(side=LEFT)
    frame_R.pack(side=RIGHT)
    frame.pack(side=TOP)

    # entry
    entry = Entry(root, textvariable=var, bg="#e3e3e3", fg="blue", width=30)
    entry.pack(side=BOTTOM)
    var.set("this is a entry.")

    # button
    btn = Button(root, text="获取entry文本", command=press_btn)
    btn.pack(side=RIGHT)

    # 打开新窗口的按钮测试
    btn_open = Button(root, text="打开新窗体", command=openNew)
    btn_open.pack()

    root.mainloop()
