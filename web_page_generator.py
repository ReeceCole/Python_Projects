import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML,)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        

        def get_data():
            label.config(text= entry.get())
            entry = Entry(self, width=42)
            entry.place(relx= .5, rely= .5, anchor= CENTER)
            label = Label(win, text="")
            label.pack()
            self.lblDisplay(Frame, text= "{}", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)
    

    def defaultHTML(self):
        htmlText = "Stay tuned for amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

 
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
