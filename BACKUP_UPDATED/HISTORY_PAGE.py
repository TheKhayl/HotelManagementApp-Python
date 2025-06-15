from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry




class History:
    def __init__(self, root, return_to_main):
        self.root = root
        self.return_to_main = return_to_main
        self.root.title("EASY HOTEL MANAGEMENT  ")
        self.root.geometry("1670x1050+0+0")

        # Title Bar Frame
        title_frame = Frame(self.root, bd=20, relief=RIDGE, bg="black")
        title_frame.pack(side=TOP, fill=X)


        back_btn = Button(title_frame, text="Main Menu", command=self.go_back_to_main,
                          font=("times new roman", 22, "bold"), bg="black", fg="red", width=18, )
        back_btn.pack(side="bottom", padx=0, pady=10)


        lbltitle = Label(title_frame, text="Hotel Management System", fg="tan", bg="Black",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, padx=100)
        #=======A=============================Dataframe=================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=200,width=1670,height=770)


        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("times new roman",25,"bold"),text="History")
        DataframeLeft.place(x=10,y=5,width=1610,height=720)





        #=============================Search button=======================================
        lblsearchBy=Label(DataframeLeft, font=("times new roman", 14, "bold"),text="Search By:",bg="red",fg="white")
        lblsearchBy.grid(row=0,column=0, sticky=W,padx=2)

        comsearchTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                    font=("arial", 14, "bold"), width=20)
        comsearchTablet['values'] = ("Name", "Bed Type", "Mobile No.", "Room No.","Address")
        comsearchTablet.current(0)
        comsearchTablet.grid(row=0, column=1,padx=2)
        comsearchTablet.configure(justify="center")

        textsearch = Entry(DataframeLeft, font=("times new roman", 14, "bold"), width=20,)
        textsearch.grid(row=0, column=2,padx=2)
        textsearch.configure(justify="center")

        btn_Search=Button(DataframeLeft, text="Search", font=("times new roman", 12, "bold"), bg="green", fg="white",
                          width=15)
        btn_Search.grid(row=0, column=5,padx=2)

        btn_Show= Button(DataframeLeft, text="Show All", font=("times new roman", 12, "bold"), bg="green", fg="white",
                            width=15)
        btn_Show.grid(row=0, column=6)


        #=======================Show Data =======================

        details_table=Frame(DataframeLeft,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=1570,height=590)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        # =======================Show Data =======================

        details_table = Frame(DataframeLeft, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=1570, height=590)

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

        # Set column widths
        for col in self.history_table["columns"]:
            self.history_table.column(col, width=120)

        self.history_table.pack(fill=BOTH, expand=1)

    def go_back_to_main(self):
        self.root.destroy()             # Close the current checkout window
        self.return_to_main()           # Call the main menu function





