import tkinter as tk
import cv2
import utils
from PIL import Image,ImageTk

class App:

    def __init__(self):
        self.main_window = tk.Tk() #TK() pe ctrl+Leftclick
        #width  x height
        self.main_window.geometry('1200x520')
        #self.main_window.minsize(500,500)# Width x Height

        # this is is for the button for the user
        self.login_button_main_window = utils.get_button(self.main_window,'login','blue',self.login)
        self.Register_button_main_window = utils.get_button(self.main_window,'Register','black',self.Register)

        # placing the button on the window
        self.login_button_main_window.place(x=750, y=300)
        self.Register_button_main_window.place(x=750,y=400)

        # putting the label # this img label which will be there but will only show if u pack it this is the hardcore rule of tkinter
        self.webcam_label  = utils.get_img_label(self.main_window)
        self.webcam_label.place(x=0,y=0,width=700,height=500)

        self.add_webcam(self.webcam_label)


    def add_webcam(self,label):

        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

# we did not read the image dirrectly from the cv because it has some problem in opening the jpg file
    # so we use pillow in order to do as it has func called ImageTK

    def process_webcam(self):
        ret , frame = self.cap.read()
        self.recent_frame = frame
        # converting to format which other than cv2 undertstand from BGR to RGB
        img_ = cv2.cvtColor(self.recent_frame,cv2.COLOR_BGR2RGB)

        #npw converting the array image read by tha cv2 to pillow format
        self.recent_Pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.recent_Pil)# here converting in which the tk will understand
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20,self.process_webcam)





    def start(self):
        self.main_window.mainloop() # for every time we run the whole program mainloop is used

    def login(self):
        pass

    def Register(self):
        pass

if __name__ == '__main__':
    obj = App()
    obj.start()