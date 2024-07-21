import customtkinter
import webbrowser

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Login System", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.frame, text="login", command=self.login)
        self.button.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember Me")
        self.checkbox.pack(pady=12, padx=10)

        self.label_result = customtkinter.CTkLabel(master=self.frame, text="", font=("Roboto", 16))
        self.label_result.pack(pady=12, padx=10)

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        
        if username == "xj3j" and password == "123456":
            self.frame.destroy()
            self.panel()
        else:
            self.label_result.configure(text="Invalid credentials!", text_color="red")

    def panel(self):
        panel_frame = customtkinter.CTkFrame(master=self, corner_radius=10, fg_color="#2a2d2e")
        panel_frame.pack(pady=15, padx=15, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=panel_frame, text="Welcome to the panel!", font=("Roboto", 24), text_color="white")
        label.pack(pady=12, padx=10)

        label = customtkinter.CTkLabel(master=panel_frame, text="Username: xj3j", font=("Roboto", 24), text_color="white")
        label.pack(pady=12, padx=10)

        button_frame = customtkinter.CTkFrame(master=panel_frame, corner_radius=10, fg_color="#2a2d2e")
        button_frame.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=button_frame, text="Lock", command=self.lock_cheat, width=100)
        button.pack(side="left", pady=12, padx=10)

        button = customtkinter.CTkButton(master=button_frame, text="Hitbox", command=self.hitbox_cheat, width=100)
        button.pack(side="left", pady=12, padx=10)

        fov_frame = customtkinter.CTkFrame(master=button_frame)
        fov_frame.pack(side="left", pady=12, padx=10)

        button = customtkinter.CTkButton(master=fov_frame, text="FOV Changer", command=lambda: self.fov_changer_cheat(self.fov_entry.get()), width=100)
        button.pack(side="left", pady=12, padx=10)

        self.fov_entry = customtkinter.CTkEntry(master=fov_frame, placeholder_text="New FOV value", width=100)
        self.fov_entry.pack(side="left", pady=12, padx=10)

        button = customtkinter.CTkButton(master=panel_frame, text="Logout", command=self.logout, width=100)
        button.pack(pady=12, padx=10)

        button = customtkinter.CTkButton(master=panel_frame, text="Join Discord", command=self.open_google, width=100)
        button.pack(pady=12, padx=10)

    def logout(self):
        self.destroy()

    def open_google(self):
        webbrowser.open("https://discord.gg/N2VuEP4U")

    def lock_cheat(self):
        print("Lock cheat activated!")

    def hitbox_cheat(self):
        print("Hitbox cheat activated!")

    def fov_changer_cheat(self, fov_value):
        try:
            fov_value = int(fov_value)
            print(f"FOV changed to {fov_value}!")
        except ValueError:
            print("Invalid FOV value! Please enter a number.")

if __name__ == "__main__":
    app = App()
    app.mainloop()