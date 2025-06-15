from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkcalendar import DateEntry





class ClientRregistration:
    def __init__(self, root, return_to_main):
        self.root = root
        self.return_to_main = return_to_main
        self.root.title("EASY HOTEL MANAGEMENT  ")
        self.root.geometry("1670x1050+0+0")
        self.booking_history = []

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


        DataframeLeft=LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                 font=("times new roman",25,"bold"),text="CLIENT REGISTRATION")
        DataframeLeft.place(x=10,y=5,width=1610,height=720)






        # ====================================Data Frame left=================================

        lblNameTablet=Label(DataframeLeft,text="Name: ", font=("times new roman", 16, "bold"),padx=50,pady=50)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        textName=Entry(DataframeLeft,font=("times new roman", 12, "bold"),width=35)
        textName.grid(row=0,column=1)

        lblmobTablet = Label(DataframeLeft, text="Mobile No. ", font=("times new roman", 16, "bold"), padx=50, pady=50)
        lblmobTablet.grid(row=1, column=0, sticky=W)
        textmob = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35,)
        textmob.grid(row=1, column=1)

        lbladdTablet = Label(DataframeLeft, text="Address: ", font=("times new roman", 16, "bold"), padx=50, pady=50)
        lbladdTablet.grid(row=2, column=0, sticky=W)
        textadd = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35, )
        textadd.grid(row=2, column=1)

        lblidTablet = Label(DataframeLeft, text="ID Proof: ", font=("times new roman", 16, "bold"), padx=50, pady=50)
        lblidTablet.grid(row=3, column=0, sticky=W)
        textid = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35, )
        textid.grid(row=3, column=1)

        lblpriceTablet = Label(DataframeLeft, text="Price: ", font=("times new roman", 16, "bold"), padx=50, pady=50)
        lblpriceTablet.grid(row=4, column=0, sticky=W)
        textprice = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35, )
        textprice.grid(row=4, column=1)

        # ====================================  Nationality =================================

        lblnatTablet = Label(DataframeLeft, text="Nationality: ", font=("times new roman", 16, "bold"), padx=50,
                             pady=25)
        lblnatTablet.grid(row=0, column=3, sticky=W)

        comnatTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                    font=("arial", 12, "bold"), width=30)
        comnatTablet['values'] = ("Filipino", "Bisaya", "Ilongo", "Pangasinense")
        comnatTablet.current(0)
        comnatTablet.grid(row=0, column=4)
        comnatTablet.configure(justify="center")
        # ==================================== Gender =================================
        lblgenTablet = Label(DataframeLeft, text="Gender: ", font=("times new roman", 16, "bold"), padx=50,
                             pady=25)
        lblgenTablet.grid(row=1, column=3, sticky=W)

        comgenTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                    font=("arial", 12, "bold"), width=30)
        comgenTablet['values'] = ("Male", "Female", "BAWAL BADING")
        comgenTablet.current(0)
        comgenTablet.grid(row=1, column=4)
        comgenTablet.configure(justify="center")

        # ==================================== BED TYPE =================================

        lblbedTablet = Label(DataframeLeft, text="Bed Type: ", font=("times new roman", 16, "bold"), padx=50,
                             pady=25)
        lblbedTablet.grid(row=2, column=3, sticky=W)

        combedTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                    font=("arial", 12, "bold"), width=30)
        combedTablet['values'] = ("Queen", "King", "Suite")
        combedTablet.current(0)
        combedTablet.grid(row=2, column=4)
        combedTablet.configure(justify="center")

        # ==================================== ROOM TYPE =================================

        lblRTTablet = Label(DataframeLeft, text="Room Type: ", font=("times new roman", 16, "bold"), padx=50,
                             pady=25)
        lblRTTablet.grid(row=3, column=3, sticky=W)

        comRTTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                    font=("arial", 12, "bold"), width=30)
        comRTTablet['values'] = ("Single MOM", "Double Room", "Triple Room")
        comRTTablet.current(0)
        comRTTablet.grid(row=3, column=4)
        comRTTablet.configure(justify="center")
        # ==================================== ROOM ID =================================

        lblidTablet = Label(DataframeLeft, text="Room No.: ", font=("times new roman", 16, "bold"), padx=50,
                            pady=25)
        lblidTablet.grid(row=4, column=3, sticky=W)

        comidTablet = ttk.Combobox(DataframeLeft, state="readonly",
                                   font=("arial", 12, "bold"), width=30)
        comidTablet['values'] = ("69", "1002", "1003")
        comidTablet.current(0)
        comidTablet.grid(row=4, column=4)
        comidTablet.configure(justify="center")


        # ================================= Check-in Date ============================
        lbl_checkin = Label(DataframeLeft, text="Check-in Date: ", font=("times new roman", 16, "bold"), padx=25,
                            pady=0)
        lbl_checkin.grid(row=0, column=5, sticky=W)
        checkin_date = DateEntry(DataframeLeft, width=32, font=("times new roman", 12, "bold"), background="darkblue",
                                 foreground="white", borderwidth=2)
        checkin_date.grid(row=0, column=6)
        checkin_date.configure(justify="center")

        #=================================== Check-out Date =============================
        lbl_checkout = Label(DataframeLeft, text="Check-out Date: ", font=("times new roman", 16, "bold"), padx=25,
                             pady=25)
        lbl_checkout.grid(row=2, column=5, sticky=W)
        checkout_date = DateEntry(DataframeLeft, width=32, font=("times new roman", 12, "bold"), background="darkblue",
                                  foreground="white", borderwidth=2)
        checkout_date.grid(row=2, column=6)
        checkout_date.configure(justify="center")

        # =================================== Check-in Time ==============================
        lbl_checkin_time = Label(DataframeLeft, text="Check-in Time: ", font=("times new roman", 16, "bold"), padx=25,
                                 pady=0)
        lbl_checkin_time.grid(row=1, column=5, sticky=W)

        # Hour Combobox
        checkin_hour = ttk.Combobox(DataframeLeft, values=[f"{i:02}" for i in range(1, 13)], width=5,
                                    font=("times new roman", 12, "bold"), state="readonly")
        checkin_hour.current(0)
        checkin_hour.grid(row=1, column=6, sticky=W, padx=0)
        checkin_hour.configure(justify="center")

        # Minute Combobox
        checkin_minute = ttk.Combobox(DataframeLeft, values=[f"{i:02}" for i in range(0, 60, 5)], width=5,
                                      font=("times new roman", 12, "bold"), state="readonly")
        checkin_minute.current(0)
        checkin_minute.grid(row=1, column=6, sticky=E, padx=100)
        checkin_minute.configure(justify="center")

        # AM/PM Combobox
        checkin_ampm = ttk.Combobox(DataframeLeft, values=["AM", "PM"], width=5, font=("times new roman", 12, "bold"),
                                    state="readonly")
        checkin_ampm.current(0)
        checkin_ampm.grid(row=1, column=6, sticky=E, padx=0)
        checkin_ampm.configure(justify="center")

        # =================================== Check-out Time ==============================

        # Check-out Time Label
        lbl_checkout_time = Label(DataframeLeft, text="Check-out Time: ", font=("times new roman", 16, "bold"), padx=25,
                                  pady=0)
        lbl_checkout_time.grid(row=3, column=5, sticky=W)

        # Hour Combobox
        checkout_hour = ttk.Combobox(DataframeLeft, values=[f"{i:02}" for i in range(1, 13)], width=5,
                                     font=("times new roman", 12, "bold"), state="readonly")
        checkout_hour.current(0)
        checkout_hour.grid(row=3, column=6, sticky=W, padx=0)
        checkout_hour.configure(justify="center")

        # Minute Combobox
        checkout_minute = ttk.Combobox(DataframeLeft, values=[f"{i:02}" for i in range(0, 60, 5)], width=5,
                                       font=("times new roman", 12, "bold"), state="readonly")
        checkout_minute.current(0)
        checkout_minute.grid(row=3, column=6, sticky=E, padx=100)
        checkout_minute.configure(justify="center")

        # AM/PM Combobox
        checkout_ampm = ttk.Combobox(DataframeLeft, values=["AM", "PM"], width=5, font=("times new roman", 12, "bold"),
                                     state="readonly")
        checkout_ampm.current(0)
        checkout_ampm.grid(row=3, column=6, sticky=E, padx=0)
        checkout_ampm.configure(justify="center")

        checkin_time = f"{checkin_hour.get()}:{checkin_minute.get()} {checkin_ampm.get()}"
        checkout_time = f"{checkout_hour.get()}:{checkout_minute.get()} {checkout_ampm.get()}"

        print("Check-in Time:", checkin_time)
        print("Check-out Time:", checkout_time)


        # ================================ BOOK Button ================================
        def confirm_booking():
            name = textName.get()
            mobile = textmob.get()
            address = textadd.get()
            id_proof = textid.get()
            price = textprice.get()
            nationality = comnatTablet.get()
            gender = comgenTablet.get()
            bed = combedTablet.get()
            room_type = comRTTablet.get()
            room_no = comidTablet.get()
            checkin = checkin_date.get()
            checkout = checkout_date.get()
            checkin_time = f"{checkin_hour.get()}:{checkin_minute.get()} {checkin_ampm.get()}"
            checkout_time = f"{checkout_hour.get()}:{checkout_minute.get()} {checkout_ampm.get()}"

            # === VALIDATION: Check kung may empty fields ===
            if not all([
                name, mobile, address, id_proof, price, nationality, gender, bed,
                room_type, room_no, checkin, checkout,
                checkin_hour.get(), checkin_minute.get(), checkin_ampm.get(),
                checkout_hour.get(), checkout_minute.get(), checkout_ampm.get()
            ]):
                messagebox.showwarning("Incomplete", "Please fill in all required fields before booking.")
                return  # Stop the booking process

            # === Confirm Booking Dialog ===
            result = messagebox.askyesno("Confirm Booking", "Are you sure you want to confirm?")
            if result:
                # Save to booking history
                self.booking_history.append({
                    "Name": name,
                    "Mobile": mobile,
                    "Address": address,
                    "ID Proof": id_proof,
                    "Price": price,
                    "Nationality": nationality,
                    "Gender": gender,
                    "Bed": bed,
                    "Room Type": room_type,
                    "Room No": room_no,
                    "Check-in Date": checkin,
                    "Check-out Date": checkout,
                    "Check-in Time": checkin_time,
                    "Check-out Time": checkout_time
                })

                messagebox.showinfo("Confirmed", "Booking has been confirmed!")

        book_btn = Button(DataframeLeft, text="BOOK", font=("times new roman", 16, "bold"),
                          bg="green", fg="white", width=15, height=2,
                          command=confirm_booking)
        book_btn.grid(row=4, column=6, pady=0, padx=0, sticky=E)


    def go_back_to_main(self):
        self.root.destroy()             # Close the current checkout window
        self.return_to_main()           # Call the main menu function








