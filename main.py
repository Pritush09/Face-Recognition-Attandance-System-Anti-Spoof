import tkinter as tk
import cv2
import utils


class App:

    def __init__(self):
        self.main_window = tk.Tk() #TK() pe ctrl+Leftclick
        #width  x height
        self.main_window.geometry('1200x520+350+100')
        self.main_window.minsize(500,500)# Width x Height

        # this is is for the button for the user
        self.login_button_main_window = utils.get_button(self.main_window,'login','blue',self.login)
        self.Register_button_main_window = utils.get_button(self.main_window,'Register','black',self.Register)

        # placing the button on the window
        self.login_button_main_window.place(x=750, y=300)
        self.Register_button_main_window.place(x=750,y=400)

        # putting the label # this img label which will be there but will only show if u pack it this is the hardcore rule of tkinter
        self.webcam_label  = utils.get_img_label(self.main_window)
        self.webcam_label.place(x=10,y=0,width=700,height=600)

        self.add_webcam(self.webcam_label)


    def add_webcam(self,label):

        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)



    def start(self):
        self.main_window.mainloop() # for every time we run the whole program mainloop is used

    def login(self):
        pass

    def Register(self):
        pass

if __name__ == '__main__':
    obj = App()
    obj.start()