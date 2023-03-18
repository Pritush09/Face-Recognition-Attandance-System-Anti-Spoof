import tkinter as tk

import utils


class App:

    def __init__(self):
        self.main_window = tk.Tk() #TK() pe ctrl+Leftclick
        #width  x height
        self.main_window.geometry('1200x520+350+100')
        self.main_window.minsize(500,500)# Width x Height

        # this is is for the button for the user
        self.login_button_main_window = utils.get_button(self.main_window,'login','blue',self.login)
        self.Register_button_main_window = utils.get_button(self.main_window,'Register','black',self.Register,fg='black')




    def start(self):
        self.main_window.mainloop() # for every time we run the whole program mainloop is used

    def login(self):
        pass

    def Register(self):
        pass

if __name__ == '__main__':
    obj = App()
    obj.start()