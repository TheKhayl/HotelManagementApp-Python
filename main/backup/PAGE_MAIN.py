from tkinter import *
from tkinter import messagebox
from CheckOut_Page import checkout
from Manage_Page import Manage
from AddBooking import ClientRregistration
from HISTORY_PAGE import History
from PIL import Image, ImageTk


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy Hotel Management System")
        self.root.geometry("1670x1050+0+0")
        self.booking_history = []

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hotel Management System", fg="Green", bg="Black",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =======A=============================Dataframe=================================

        Dataframe1 = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe1.place(x=0, y=120, width=685, height=850)


        Dataframe2 = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe2.place(x=985, y=120, width=685, height=850)



        # LEFT FRAME
        Dataframe1 = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe1.place(x=0, y=120, width=685, height=850)

        # Load and display image in LEFT frame
        self.hotel_image_left = Image.open(
            r"C:\Users\admin\OneDrive\Desktop\Tkinther.HOTEL\Hotel_Management Image\room1.jpg")
        self.hotel_image_left = self.hotel_image_left.resize((645, 810))
        self.hotel_photo_left = ImageTk.PhotoImage(self.hotel_image_left)

        image_label_left = Label(Dataframe1, image=self.hotel_photo_left)
        image_label_left.pack()

        # RIGHT FRAME
        Dataframe2 = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe2.place(x=985, y=120, width=685, height=850)


        self.hotel_image_right = Image.open(
            r"C:\Users\admin\OneDrive\Desktop\Tkinther.HOTEL\Hotel_Management Image\room2.jpg.crdownload")
        self.hotel_image_right = self.hotel_image_right.resize((645, 810))
        self.hotel_photo_right = ImageTk.PhotoImage(self.hotel_image_right)

        image_label_right = Label(Dataframe2, image=self.hotel_photo_right)
        image_label_right.pack()

        # ==================================== Navigation Button Frame ====================================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE, bg="black")
        Buttonframe.place(x=685, y=120, width=300, height=850)  # Adjusted width for vertical layout

        # Optional: Title on top of button column
        left_title = Label(Buttonframe, text="MAIN MENU", font=("times new roman", 20, "bold"), fg="red", bg="black")
        left_title.pack(side=TOP, pady=40)

        # Vertical Navigation Buttons
        btn_home = Button(Buttonframe, text="Home", command=self.show_home,
                          font=("times new roman", 14, "bold"), bg="black", fg="green", width=20)
        btn_home.pack(side=TOP, pady=50)

        btn_customer = Button(Buttonframe, text="Registration", command=self.show_customer,
                              font=("times new roman", 14, "bold"), bg="black", fg="green", width=20)
        btn_customer.pack(side=TOP, pady=50)

        btn_history = Button(Buttonframe, text="History", command=self.show_history,
                             font=("times new roman", 14, "bold"), bg="black", fg="green", width=20)
        btn_history.pack(side=BOTTOM, pady=50)

        btn_manage = Button(Buttonframe, text="Manage", command=self.show_manage,
                            font=("times new roman", 14, "bold"), bg="black", fg="green", width=20)
        btn_manage.pack(side=BOTTOM, pady=50)

        btn_checkout = Button(Buttonframe, text="Check Out", command=self.show_checkout,
                              font=("times new roman", 14, "bold"), bg="black", fg="green", width=20)
        btn_checkout.pack(side=BOTTOM, pady=50)



        #self.home_label.place(x=400, y=300)

    def show_checkout(self):
        self.root.withdraw()  # Hide the main window

        def reopen_main():
            self.root.deiconify()  # Show main window again

        new_window = Toplevel(self.root)
        checkout(new_window, return_to_main=reopen_main)

        def on_close():
            new_window.destroy()
            self.root.deiconify()

        new_window.protocol("WM_DELETE_WINDOW", on_close)

    def show_manage(self):
        self.root.withdraw()

        def reopen_main():
            self.root.deiconify()

        new_window = Toplevel(self.root)
        Manage(new_window, return_to_main=reopen_main)

        def on_close():
            new_window.destroy()
            self.root.deiconify()

        new_window.protocol("WM_DELETE_WINDOW", on_close)

    def show_customer(self):
        self.root.withdraw()

        def reopen_main():
            self.root.deiconify()

        new_window = Toplevel(self.root)
        ClientRregistration(new_window, return_to_main=reopen_main)

        def on_close():
            new_window.destroy()
            self.root.deiconify()

        new_window.protocol("WM_DELETE_WINDOW", on_close)

    def show_history(self):
        self.root.withdraw()

        def reopen_main():
            self.root.deiconify()

        new_window = Toplevel(self.root)
        History(new_window, return_to_main=reopen_main)

        def on_close():
            new_window.destroy()
            self.root.deiconify()

        new_window.protocol("WM_DELETE_WINDOW", on_close)

    def show_home(self):
        messagebox.showinfo("Home", "This is the Home Page of Easy Hotel Management System")


if __name__ == "__main__":
    root = Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
