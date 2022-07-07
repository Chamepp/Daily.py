from tkinter.ttk import Combobox
from tkinter import Tk, Button, filedialog, messagebox, Label, Menu
from PIL import ImageGrab
from cv2 import VideoWriter, VideoWriter_fourcc, cvtColor, resize, COLOR_BGR2RGB
from ctypes import windll
import time
import numpy as np


# Start Class
class WindowRecorder:
    def __init__(self):
        self.__app = Tk()
        self.__app.title(app_name)
        self.__app.geometry(app_window_size)
        self.__app.resizable(0, 0)
        self.__is_recording=False
        self.__frame_per_sec=fps_combo_box[default_cmbox_value]


    # Create Context
    def create_context(self):
        self.__btn_start_stop = Button(self.__app, text=btn_start_txt, width=btn_start_width, command=self.start_recording, bg='green', fg='white', bd=0)
        self.__btn_start_stop.pack(pady=10)
        
        self.__btn_exit=Button(self.__app, text=btn_exit_txt, width=btn_close_width, command=self.destroy, fg='white', bg='blue', bd=0)
        self.__btn_exit.pack()
        
        ''' Combo Box '''
        self.__cmb_box=Combobox(self.__app, values=fps_combo_box, width=5)
        self.__cmb_box.pack(side='right', padx=5, pady=5)
        cmb_label = Label(self.__app, text='fps')
        cmb_label.pack(side='right')
        self.__cmb_box.current(default_cmbox_value)
        self.__cmb_box.bind('<<ComboboxSelected>>', self.on_select_listener)

        ''' Timer label '''
        self.__timer=Label(text='00:00:00')
        self.__timer.pack(side='left', padx=5)
        
        ''' Root Menu '''
        self.__root_menu = Menu(master=self.__app)
        self.__app.config(menu=self.__root_menu)

        ''' File Menu '''
        self.__file_menu = Menu(self.__root_menu, tearoff=0)
        self.__file_menu.add_command(label='About', command=self.about)
        self.__file_menu.add_command(label='Contact us', command=self.contact_us)
        self.__file_menu.add_separator()
        self.__file_menu.add_command(label='Exit', command=self.destroy)

        self.__root_menu.add_cascade(label='Menu', menu=self.__file_menu)


    # Start Application       
    def start(self):
        self.__app.mainloop()

    # Recording Operation
    def start_recording(self):
        self.__is_recording=True
        self.__temp_video_frames = list()
        self.__btn_start_stop.configure(text=btn_close_txt, command=self.stop, bg='red')
        self.__cmb_box['state']='disabled'
        self.count=0
        self.min=0
        self.sec=0
        self.__app.iconify()
        self.record_frames()
        
    # Stop Recording Operation
    def stop(self):
        self.__is_recording=False
        file = filedialog.asksaveasfile(defaultextension="*.*", filetypes=[('mp4', '.mp4'),])
        if file:
            if file.name:
                print(file.name)
                shape = self.__temp_video_frames[0].shape
                print(shape)
                fourcc = VideoWriter_fourcc(*codec)
                video_writer = VideoWriter(file.name, fourcc, self.__frame_per_sec, (shape[1], shape[0]), True)
                if self.__temp_video_frames:
                    for frame in self.__temp_video_frames:
                        video_writer.write(frame)
                    del self.__temp_video_frames
                video_writer.release()
        self.__btn_start_stop.configure(text=btn_start_txt, command=self.start_recording, bg='green')
        self.__cmb_box['state']='normal'

    # Closing Application
    def destroy(self):
        self.__app.destroy()

    # Extract Frames
    def record_frames(self):
        screen = np.array(ImageGrab.grab())
        screen = cvtColor(screen, COLOR_BGR2RGB)
        screen = resize(screen, video_res)
        self.__temp_video_frames.append(screen)
        self.count += 1
        dur = (self.count / self.__frame_per_sec) 
        self.min = int(dur / 60)
        self.sec = dur % 60
        self.__timer['text']=time.strftime('%H:%M:%S', time.gmtime(self.min*60 + self.sec))
        if self.__is_recording:
            self.__app.after(call_record_after, self.record_frames)
      
    # Selection Controller
    def on_select_listener(self, event=None):
        if event:
            self.__frame_per_sec=int(event.widget.get())


    # Details
    def about(self):
        messagebox.showinfo('About', about_msg)
        

if __name__=='__main__':

    # Execute
    user_32 = windll.user32
    user_32.SetProcessDPIAware()

    app = WindowRecorder()
    app.create_context()
    app.start()
