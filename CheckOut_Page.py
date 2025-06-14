from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry




class checkout:
    def __init__(self, root, return_to_main):
        self.root = root
        self.return_to_main = return_to_main
        self.root.title("EASY HOTEL MANAGEMENT  ")
        self.root.geometry("1670x1050+0+0")

        # Title Bar Frame
        title_frame = Frame(self.root, bd=20, relief=RIDGE, bg="black")
        title_frame.pack(side=TOP, fill=X)

        # --- Top Part: Title ---
        title_label_frame = Frame(title_frame, bg="black")
        title_label_frame.pack(side=TOP, fill=X)

        lbltitle = Label(title_label_frame, text="Hotel Management System", fg="tan", bg="black",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(pady=0)

        -
        title_button_frame = Frame(title_frame, bg="black")
        title_button_frame.pack(side=BOTTOM, fill=X)

        back_btn = Button(title_button_frame, text="Main Menu", command=self.go_back_to_main,
                          font=("times new roman", 22, "bold"), bg="black", fg="red", width=18)
        back_btn.pack(side=BOTTOM, padx=0, pady=10)  # Aligned left

        #=============================Dataframe=================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=200,width=1670,height=770)

        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                 font=("times new roman",25,"bold"),text="Check Out")
        DataframeLeft.place(x=10,y=0,width=1610,height=720)



        #=============================Search Fields & Button=======================================

        search_name = Entry(DataframeLeft, font=("times new roman", 14, "bold"), width=20)
        search_name.grid(row=0, column=2, padx=2)
        search_name.configure(justify="center")

        roomno = Entry(DataframeLeft, font=("times new roman", 14, "bold"), width=20)
        roomno.grid(row=0, column=3, padx=2)
        roomno.configure(justify="center")

        checkout_date = Entry(DataframeLeft, font=("times new roman", 14, "bold"), width=20)
        checkout_date.grid(row=0, column=4, padx=2)
        checkout_date.configure(justify="center")

        checkout_time = Entry(DataframeLeft, font=("times new roman", 14, "bold"), width=20)
        checkout_time.grid(row=0, column=5, padx=2)
        checkout_time.configure(justify="center")



        def confirm_checkout():
            selected = self.history_table.focus()
            if not selected:
                messagebox.showwarning("Warning", "Please select a record to check out.")
                return

            result = messagebox.askyesno("Confirmation", "Are you sure you want to check out?")
            if result:
                self.history_table.delete(selected)
                messagebox.showinfo("Success", "Checked out successfully.")
            else:
                messagebox.showinfo("Cancelled", "Check out cancelled.")

        btn_Search = Button(DataframeLeft, text="Check Out", font=("times new roman", 12, "bold"), bg="green",
                            fg="white",
                            width=15, command=confirm_checkout)
        btn_Search.grid(row=0, column=6, padx=2)

        #=======================Show Data =======================
        details_table = Frame(DataframeLeft, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=1570, height=600)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.history_table = ttk.Treeview(details_table,
                                          columns=("name", "mobile", "address", "id", "price",
                                                   "nationality", "gender", "bed", "room_type",
                                                   "room_no", "checkin_date", "checkout_date",
                                                   "checkin_time", "checkout_time"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.history_table.xview)
        scroll_y.config(command=self.history_table.yview)

        self.history_table.heading("name", text="Name")
        self.history_table.heading("mobile", text="Mobile No.")
        self.history_table.heading("address", text="Address")
        self.history_table.heading("id", text="ID Proof")
        self.history_table.heading("price", text="Price")
        self.history_table.heading("nationality", text="Nationality")
        self.history_table.heading("gender", text="Gender")
        self.history_table.heading("bed", text="Bed Type")
        self.history_table.heading("room_type", text="Room Type")
        self.history_table.heading("room_no", text="Room No.")
        self.history_table.heading("checkin_date", text="Check-in Date")
        self.history_table.heading("checkout_date", text="Check-out Date")
        self.history_table.heading("checkin_time", text="Check-in Time")
        self.history_table.heading("checkout_time", text="Check-out Time")

        self.history_table['show'] = 'headings'

        for col in self.history_table["columns"]:
            self.history_table.column(col, width=120)

        self.history_table.pack(fill=BOTH, expand=1)

        self.history_table.insert("", END, values=("Juan Dela Cruz", "09171234567", "Manila", "ID123", "2000",
                                                   "Filipino", "Male", "Queen", "Suite", "101", "2024-06-01",
                                                   "2024-06-05", "14:00", "12:00"))

        #=======================Row Click Handler =======================
        def get_cursor(event=""):
            selected_row = self.history_table.focus()
            data = self.history_table.item(selected_row)
            row = data['values']
            if row:
                search_name.delete(0, END)
                roomno.delete(0, END)
                checkout_date.delete(0, END)
                checkout_time.delete(0, END)

                search_name.insert(0, row[0])  # Name
                roomno.insert(0, row[9])       # Room No.

                now = datetime.datetime.now()
                checkout_date.insert(0, now.strftime("%Y-%m-%d"))
                checkout_time.insert(0, now.strftime("%H:%M:%S"))

        self.history_table.bind("<ButtonRelease-1>", get_cursor)


    def go_back_to_main(self):
        self.root.destroy()  # Close the current checkout window
        self.return_to_main()  # Call the main menu function



