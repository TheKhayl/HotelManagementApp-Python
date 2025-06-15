from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry



# frame for title
class Manage:
    def __init__(self, root, return_to_main):
        self.root = root
        self.return_to_main = return_to_main
        self.root.title("EASY HOTEL MANAGEMENT  ")
        self.root.geometry("1670x1050+0+0")

        # Title Bar Frame
        title_frame = Frame(self.root, bd=20, relief=RIDGE, bg="black")
        title_frame.pack(side=TOP, fill=X)

        # Back to Menu Button (aligned left inside the title bar)
        back_btn = Button(title_frame, text="Main Menu", command=self.go_back_to_main,
                          font=("times new roman", 22, "bold"), bg="black", fg="red", width=18, )
        back_btn.pack(side="bottom", padx=0, pady=10)

        # Main Title Label (centered after the button)
        lbltitle = Label(title_frame, text="Hotel Management System", fg="tan", bg="Black",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, padx=100)
        #=======A=============================Dataframe=================================

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=200,width=1670,height=770)

        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("times new roman",25,"bold"),text="Manage")
        DataframeLeft.place(x=10,y=5,width=1610,height=720)



        #=============================Search button=======================================
        btn_Edit=Button(DataframeLeft, text="Edit", font=("times new roman", 12, "bold"), bg="green", fg="white",
                          width=15, command=self.edit_data)
        btn_Edit.grid(row=0, column=5,padx=2)

        btn_Delete= Button(DataframeLeft, text="Delete", font=("times new roman", 12, "bold"), bg="green", fg="white",
                            width=15, command=self.delete_data)
        btn_Delete.grid(row=0, column=0,sticky=E)

        #=======================Show Data =======================
        details_table=Frame(DataframeLeft,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=1570,height=590)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

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

        # Sample data
        self.history_table.insert("", END, values=("Juan Dela Cruz", "09171234567", "Manila", "ID123", "2000",
                                                   "Filipino", "Male", "Queen", "Suite", "101", "2024-06-01",
                                                   "2024-06-05", "14:00", "12:00"))

    # Function to edit data
    def edit_data(self):
        selected = self.history_table.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a row to edit.")
            return

        values = self.history_table.item(selected, 'values')
        popup = Toplevel()
        popup.title("Edit Information")
        popup.geometry("450x550")

        entries = []
        labels = self.history_table["columns"]

        for i, label in enumerate(labels):
            Label(popup, text=label.upper(), font=("times new roman", 12, "bold")).grid(row=i, column=0, padx=10, pady=5, sticky=W)
            entry = Entry(popup, width=40)
            entry.insert(0, values[i])
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries.append(entry)

        def save_edit():
            new_values = [e.get() for e in entries]
            self.history_table.item(selected, values=new_values)
            popup.destroy()

        Button(popup, text="Save Changes", command=save_edit, width=20, bg="green", fg="white",
               font=("times new roman", 12, "bold")).grid(row=len(labels), columnspan=2, pady=20)

    # Function to delete data
    def delete_data(self):
        selected = self.history_table.focus()
        if not selected:
            messagebox.showwarning("Warning", "Please select a row to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
        if confirm:
            self.history_table.delete(selected)


    def go_back_to_main(self):
        self.root.destroy()
        self.return_to_main()





