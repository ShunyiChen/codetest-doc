from cProfile import label
from struct import pack
from tkinter import *
from tkinter import messagebox 

class Application(Frame):
    """一个经典的GUI"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    
    def createWidget(self):
        self.btn01 = Button(self)
        self.btn01["text"] = "Generate"
        self.btn01.pack()
        self.btn01["command"] = self.generate

        # 创建一个退出按钮
        self.btnQuit = Button(self, text="Quit", command=self.quit)
        self.btnQuit.pack()

        self.label01 = Label(self, text="直流电", width=10, height=2,
                            bg="blue",fg="white", font=("宋体",18))
        self.label01.pack()

    def generate(self):
        print("Start generating documents")

    def quit(self):
        root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title("GUI")
    root.geometry("500x300+400+200")
    app = Application(master=root)
    root.mainloop()




# button = Button(root)
# button["text"] = "CLOSE"
# button.pack()




# root = Tk()
# root.title("GUI")
# root.geometry("500x300+400+200")

# button = Button(root)
# button["text"] = "CLOSE"
# button.pack()


# def handleClose(e):
#     print("关闭")
#     messagebox.showinfo("Close", "ddddddddddd")

# button.bind("<Button-1>", handleClose)

# root.mainloop()