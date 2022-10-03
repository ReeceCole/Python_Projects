import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn2 = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customText)
        self.btn2.grid(row=2, padx=(10,10) , pady=(10,10), column=0)
        self.btn.grid(row=2, padx=(10,10) , pady=(10,10), column=1)
        self.entry = Entry(self.master, width=42)
        self.entry.grid(row=1, padx=(10,10) , pady=(10,10), columnspan=2)
        self.label = Label(self.master, text="")
        self.label.grid()
        self.lblDisplay = Label(self.master, text= "Enter custom text or click the Default HTML page button").grid(row=0, padx=(10,10) , pady=(10,10), columnspan=2)
        
    
    def defaultHTML(self):
        htmlText = "Stay tuned for amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        htmlText = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

 
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
