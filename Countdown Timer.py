import time
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from threading import *

# Hour list
hour_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# Minute List
min_sec_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #window designs
        self.title("Countdown Timer")
        self.iconbitmap('icon.ico')
        self.configure(bg="#e83535")
        #setting app screen size--------------------------------------------------
        app_width = 480
        app_height = 320

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)

        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        self.resizable(False, False) #disabling resisizing the app window

        self.pause = False

        #button frame
        self.button_frame = Frame(self, bg="#e83535",width=240, height=40)
        self.button_frame.place(x=230, y=160)

        #time frame
        self.time_frame = Frame(self, bg="#e83535", width=480, height=120).place(x=0, y=210)

        #Labels
        time_label = Label(self, text="COUNTDOWN TIMER",font=("Arial",20, "bold"), bg='#e83535',fg='#000')
        time_label.place(x=95, y=30)

        hour_label = Label(self, text="Hour",font=("Arial",10,"bold"), bg='#e83535', fg='#000')
        hour_label.place(x=35, y=85)

        minute_label = Label(self, text="Minute",font=("Arial",10,"bold"), bg='#e83535', fg='#000')
        minute_label.place(x=185, y=85)

        second_label = Label(self, text="Second",font=("Arial",10,"bold"), bg='#e83535', fg='#000')
        second_label.place(x=335, y=85)
       
        # ===========================================
        # Combobox for hours
        self.hour = IntVar()
        self.hour_combobox = ttk.Combobox(self,width=8,height=10,textvariable=self.hour,font=("arial",15))
        self.hour_combobox['values'] = hour_list
        self.hour_combobox.current(0)
        self.hour_combobox.place(x=35,y=110)

        # Combobox for minutes
        self.minute = IntVar()
        self.minute_combobox = ttk.Combobox(self,width=8,height=10,textvariable=self.minute,font=("arial",15))
        self.minute_combobox['values'] = min_sec_list
        self.minute_combobox.current(0)
        self.minute_combobox.place(x=185,y=110)

        # Combobox for seconds
        self.second = IntVar()
        self.second_combobox = ttk.Combobox(self,width=8,height=10,textvariable=self.second,font=("arial",15))
        self.second_combobox['values'] = min_sec_list
        self.second_combobox.current(0)
        self.second_combobox.place(x=335,y=110)
        # ===========================================

        #buttons
        #set button
        set_button = Button(self, text='Set',font=("Arial",12,"bold"),width=5, bg="#b0ab25", fg="black",command=self.Get_Time)
        set_button.place(x=60, y=160)
        
        #cancel button
        cancel_button = Button(self, text='Cancel', font=("Arial",12,"bold"), bg="#b0ab25", fg="black",command=self.Cancel)
        cancel_button.place(x=140, y=160)

    def Get_Time(self):
        self.time_display = Label(self.time_frame,font=('Helvetica', 20 , "bold"),bg = '#e83535', fg = 'yellow')
        self.time_display.place(x=115, y=210)

        try:
            # total time in seconds
            h = (int(self.hour_combobox.get())*3600)
            m = (int(self.minute_combobox.get())*60)
            s = (int(self.second_combobox.get()))
            self.time_left = h + m + s

            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!','Please select a right time to set')
            else:
                # Start Button
                start_button = Button(self.button_frame, text='Start',font=("Arial",12,"bold"), bg="#b0ab25", fg="#000",command=self.Threading)
                start_button.place(x=20, y=0)

                # Pause Button
                pause_button = Button(self.button_frame, text='Pause',font=("Arial",12,"bold"), bg="#b0ab25", fg="#000",
                command=self.pause_time)
                pause_button.place(x=100, y=0)

        except ValueError as ve:
            messagebox.showerror("Error!",f"Error due to {ve}")

    def Cancel(self):
        self.pause = True
        self.destroy()

    def Threading(self):
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    def start_time(self):
        self.pause = False
        while self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)

            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
            self.time_display.update()

            time.sleep(1)
            self.time_left = self.time_left -1

            if self.time_left <= 0:
                messagebox.showinfo('Time Over','Press OK to close')
                self.clear_screen()

            if self.pause == True:
                break
    
    def clear_screen(self):
        for item in self.button_frame.winfo_children():
            item.destroy()
        
        self.time_display.destroy()
    
    def pause_time(self):
        self.pause = True

        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()

if __name__ == "__main__":
    obj = App()
    obj.mainloop()