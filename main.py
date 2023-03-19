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

        # this is for making the instance of the label function so we can capture the video
        self.webcam_label  = utils.get_img_label(self.main_window)
        self.webcam_label.place(x=0,y=0,width=700,height=500)

        self.add_webcam(self.webcam_label)


    def add_webcam(self,label):

        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        # we this this becz we cant simply take the input every time so we call the function by this function
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
        self.register_new_window = tk.Toplevel(self.main_window)
        self.register_new_window.geometry('1200x520')
        #button
        self.accept_button = utils.get_button(self.register_new_window,'Accept','red',self.Accept)
        self.accept_button.place(x=750, y=300)
        self.tryagain_button = utils.get_button(self.register_new_window, 'Try Again', 'green', self.Try_Again)
        self.tryagain_button.place(x=750, y=400)

        self.capture_label = utils.get_img_label(self.register_new_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        # we want to add a image not to capture the video inorder to save the image of the user
        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = utils.get_entry_text(self.register_new_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = utils.get_text_label(self.register_new_window,'Please, Input username:')
        self.text_label_register_new_user.place(x=750, y=70)

    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.recent_Pil)  # here converting in which the tk will understand
        label.imgtk = imgtk
        label.configure(image=imgtk)

        # we copied frames as we gonna use  opencv to save the image from the capture to our folder
        self.register_new_user_capture = self.recent_frame.copy()




    def Accept(self):
        # this for my directory u may have different directory
        # directory me save ho raha C:\\Users\\mynam\\FACE  RECOGNITION ATTANDANCE SYSTEM\\known people
        name = self.entry_text_register_new_user.get(1.0,"end-1c")# this text is to get the message from the box where the user wrote his or her name
        # saving the image into the database
        cv2.imwrite('C:\\Users\\mynam\\FACE  RECOGNITION ATTANDANCE SYSTEM\\known people\\{}.jpg'.format(name),self.register_new_user_capture)

        utils.msg_box("Success!","You were registered successfully!")

        self.register_new_window.destroy()

    def Try_Again(self):
        self.register_new_window.destroy()


if __name__ == '__main__':
    obj = App()
    obj.start()