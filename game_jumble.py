from tkinter import *
import random
class Game:
    def __init__(self, master):
        self.i=0
        self.words=["bodyguard","castle","you","narcos","daredevil","fargo","seinfeld","firefly","spartacus","homeland","punisher","revenge","house","dexter","californication","ozark","mindhunter","limitless","order","dark","riverdale","lucifer","suits","sherlock","dynasty","titans","gotham","immortals","blacklist"]
        self.master = master
        master.title("Jumble Game")
        self.score = 0
        self.entered_string = ""
        self.correct = ""
        self.score_label_text = IntVar()
        self.score_label_text.set(self.score)
        self.score_label = Label(master, textvariable=self.score_label_text)

        self.jumble_label_text = IntVar()
        self.jumble_label_text.set("")
        self.get_word()
        self.jumble_label = Label(master, textvariable=self.jumble_label_text)
        self.label = Label(master, text="Score:")
        self.jumble = Label(master, text = "The jumbled word is - ") 
        self.entry = Entry(master)
        self.check_button = Button(master, text="Next word", command=lambda: self.update("check"))
        self.quit_button = Button(master, text="Quit", command=lambda: self.update("quit"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        
        # LAYOUT
        
        self.label.grid(row=0, column=0, sticky=W)
        self.score_label.grid(row=0, column=3, columnspan=2, sticky=E)
        self.jumble_label.grid(row = 1, column = 2)
        self.entry.grid(row=3,columnspan=3,sticky = W+E)
        self.jumble.grid(row=1, column =0)
        self.check_button.grid(row=4, column=0)
        self.quit_button.grid(row=4, column=1)
        self.reset_button.grid(row=4, column=3, sticky=W+E)
    def update(self, method): #Word is checked and score is updated here
        if self.i<10: 
            self.entered_string = self.entry.get()
            if method == "check":
                if((self.correct) == (self.entered_string)):
                    self.score += 1
            elif method == "quit":
                quit();
            else: # reset
                self.score = 0
            self.score_label_text.set(self.score)
            self.get_word()
            self.entry.delete(0, END)
            self.i=self.i+1
            
        else:
            quit();
    def get_word(self): #Jumbling takes place here
        word=random.choice(self.words)
        self.correct=word
        self.words.remove(word)
        jumble=""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]
        self.jumble_label_text.set(jumble)
root = Tk()
my_gui = Game(root)
root.mainloop()
