import tkinter as tk


class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        if event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-3, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(3, "units")


class DashboardPage(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        scroll = ScrollableFrame(self)
        scroll.pack(fill="both", expand=True)
        main = scroll.scrollable_frame

        # Navbar
        header = tk.Frame(main, bg="black", height=60, bd=20, relief="ridge")
        header.pack(fill="x", pady=10)
        tk.Label(header, text="HOTEL MANAGEMENT SYSTEM", fg="white", bg="black",
                 font=("times new roman", 25, "bold")).pack(side="left", padx=20)
        nav = tk.Frame(header, bg="black")
        nav.pack(side="right", padx=20)
        nav_buttons = [("HOME",), ("HISTORY",), ("MANAGE ROOM",), ("CUSTOMER REGISTRATION",), ('CHECK OUT',)]
        for label in nav_buttons:
            tk.Button(nav, text=label[0], font=("times new roman", 14, "bold"), bg="white", fg="black", padx=10).pack(
                side="left", padx=5)

        # Ridge Frame Below Navbar
        below_nav_frame = tk.Frame(main, bd=20, relief="ridge")
        below_nav_frame.pack(fill="x", padx=0, pady=(0, 20))

        # Banner
        tk.Label(main, text="Image placeholder", relief="solid", width=150, height=20).pack(pady=10)


        # Rooms Section
        tk.Label(main, text="Rooms", font=("times new roman", 14, "bold")).pack(pady=10)
        room_frame = tk.Frame(main)
        room_frame.pack(pady=10)
        for i in range(5):
            room = tk.Frame(room_frame, padx=10)
            room.pack(side="left")
            tk.Label(room, text=" ", width=20, height=10, relief="solid").pack()
            tk.Label(room, text=f"Room {i + 1}").pack()

        # Booking Table

        tk.Label(main, text="Booking", font=("times new roman", 14, "bold")).pack(pady=10)
        table = tk.Frame(main)
        table.pack()

        headers = ["Room No", "Check-in date", "Check-out date", "Customer name", "Availability"]
        for i, header_text in enumerate(headers):
            tk.Label(
                table, font=("Arial", 12, "bold"), text=header_text,
                borderwidth=1, relief="solid", width=28, height=2
            ).grid(row=0, column=i, sticky="nsew")  # Add sticky="nsew"

        statuses = ["Available", "Occupied", "Maintenance"]
        status_colors = {"Available": "green", "Occupied": "orange", "Maintenance": "red"}
        for row in range(20):
            for col in range(len(headers)):
                if col == 4:  # Availability column
                    status = statuses[row % len(statuses)]
                    tk.Label(
                        table, text=status, borderwidth=1, relief="solid", width=28, height=2,
                        fg=status_colors[status], font=("Arial", 12, "bold")
                    ).grid(row=row + 1, column=col, sticky="nsew")  # Add sticky="nsew"
                else:
                    tk.Label(
                        table, text=f"Data {row + 1}", borderwidth=1, relief="solid", width=28, height=2,
                        font=("Arial", 12)
                    ).grid(row=row + 1, column=col, sticky="nsew")  # Add sticky="nsew"

        # Make columns expand equally
        for i in range(len(headers)):
            table.grid_columnconfigure(i, weight=1)

        # Footer
        footer = tk.Frame(main, bg="#e0e0e0", height=40)
        footer.pack(fill="x", pady=20)
        tk.Label(footer, text="lagayan ng kuan", font=("Arial", 10)).pack(pady=10)


# --- Main App and Auth Pages ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kuan")
        self.geometry("1000x700")
        

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for Page in (FirstPage, LoginPage, SignupPage, DashboardPage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        self.frames[page].tkraise()


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Hotel Booking System", font=("times new roman", 24, "bold")).pack(pady=40)
        tk.Button(self, text="Login", width=20, font=("Arial", 18), bg="#36454F", fg="#FFFFFF",
                  command=lambda: controller.show_frame(LoginPage)).pack(pady=10)
        tk.Button(self, text="Signup", width=20, font=("Arial", 18),
                  command=lambda: controller.show_frame(SignupPage)).pack(pady=10)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        frame = tk.Frame(self)
        frame.pack(expand=True)
        tk.Label(frame, text="LOGIN", font=("Arial", 24, "bold")).pack(pady=10)
        tk.Label(frame, text="Username", font=("Arial", 18)).pack()
        self.username_entry = tk.Entry(frame, width=30, font=("Arial", 18))
        self.username_entry.pack(pady=5)
        tk.Label(frame, text="Password", font=("Arial", 18)).pack()
        self.password_entry = tk.Entry(frame, width=30, show='•', font=("Arial", 18))
        self.password_entry.pack(pady=5)
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Login", font=("Arial", 18), bg="#36454F", fg="#FFFFFF", width=10,
                  command=lambda: controller.show_frame(DashboardPage)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Sign up", font=("Arial", 18), width=10,
                  command=lambda: controller.show_frame(SignupPage)).pack(side="left", padx=5)


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        frame = tk.Frame(self)
        frame.pack(expand=True)
        tk.Label(frame, text="SIGN UP", font=("Arial", 24, "bold")).pack(pady=10)
        tk.Label(frame, text="Username", font=("Arial", 18)).pack()
        tk.Entry(frame, width=30, font=("Arial", 18)).pack(pady=5)
        tk.Label(frame, text="Email", font=("Arial", 18)).pack()
        tk.Entry(frame, width=30, font=("Arial", 18)).pack(pady=5)
        tk.Label(frame, text="Password", font=("Arial", 18)).pack()
        tk.Entry(frame, width=30, font=("Arial", 18)).pack(pady=5)
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Sign up", font=("Arial", 18), bg="#36454F", fg="#FFFFFF", width=10).pack(side="left",
                                                                                                            padx=5)
        tk.Button(btn_frame, text="Login", font=("Arial", 18), width=10,
                  command=lambda: controller.show_frame(LoginPage)).pack(side="left", padx=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()