import tkinter as tk
import tkinter.ttk as ttk
import random
import time
import os
from PIL import Image, ImageTk

# Functions
def validate(input):
    if input.isdigit() or input == "":
        return True
    return False

def generate(gender, agemin, agemax):
    gen_list = ["Male", "Female", "Both", "Random"]
    if not gender in gen_list or agemin == "" or agemax == "":
        err = tk.Label(root, text="Error: Invalid Input", fg="red")
        err.place(x=10, y=70)
        err.after(1000, lambda: err.destroy())
    else:
        if gender == "Random":
            gender = random.choice(["Male", "Female", "Both"])
        
        age = random.randint(int(agemin), int(agemax))

        born_y = int(time.localtime().tm_year) - age
        born_m = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        if born_m in ["January", "March", "May", "July", "August", "October", "December"]:
            born_d = random.randint(1, 31)
        elif born_m in ["April", "June", "September", "November"]:
            born_d = random.randint(1, 30)
        elif born_m in ["February"]:
            if born_y % 4 == 0:
                born_d = random.randint(1, 29)
            else:
                born_d = random.randint(1, 28)
        
        born_date = str(born_d) + "/" + born_m + "/" + str(born_y)

        if gender == "Male":
            name = random.choice(man_names)
        elif gender == "Female":
            name = random.choice(girl_names)
        elif gender == "Both":
            temp = random.choice(["M", "F"])
            if temp == "M":
                name = random.choice(man_names)
            elif temp == "F":
                name = random.choice(girl_names)
        
        born_c = random.choice(countries)

        N = tk.Label(root, text=name, fg="blue")
        G = tk.Label(root, text=gender, fg="blue")
        A = tk.Label(root, text=age, fg="blue")
        B = tk.Label(root, text=born_date, fg="blue")
        C = tk.Label(root, text=born_c, fg="blue")

        N.place(x=10, y=70)
        G.place(x=10, y=90)
        A.place(x=10, y=110)
        B.place(x=10, y=130)
        C.place(x=10, y=150)

        def clear():
            N.destroy()
            G.destroy()
            A.destroy()
            B.destroy()
            C.destroy()
            clearbt.destroy()

        clearbt = tk.Button(root, text="Clear", command=clear)
        clearbt.place(x=500, y=100)

def about():
    aboutd = tk.Tk()
    aboutd.title("About")
    aboutd.geometry("500x200")
    aboutlab = tk.Label(aboutd, text="About", fg="blue", font=("Arial", 24, "bold"))
    aboutlab.pack(side=tk.TOP)
    aboutdes = tk.Label(aboutd, text="Created by EinKaffeBitte on GitHub, available on \nhttps://github.com/EinKaffeeBitte/NewLife. Made with Python 3.11.0 and Tkinter \n, packed with PyInstaller and \nAUto-Py-To-Exe.", fg="blue")
    aboutdes.place(x=30, y=60)

    aboutd.mainloop()

def credits():
    creditsd = tk.Tk()
    creditsd.title("Credits")
    creditsd.geometry("600x200")
    creditslab = tk.Label(creditsd, text="Credits", fg="blue", font=("Arial", 24, "bold"))
    creditslab.pack(side=tk.TOP)
    creditsdes = tk.Label(creditsd, text="Icon license: 'Germinating radish' by \nDennis Brown is licensed \nunder CC BY-SA 3.0. To view a copy of this license, visit \nhttps://creativecommons.org/licenses/by-sa/3.0/?ref=openverse.", fg="blue")
    creditsdes.place(x=30, y=60)
    btn = tk.Button(creditsd, text="Go to icon page", command=lambda: os.startfile("https://creativecommons.org/licenses/by-sa/3.0/?ref=openverse"))
    btn.place(x=30, y=150)

    creditsd.mainloop()


# Tk Window
root = tk.Tk()
root.title("New Life Generator")
root.geometry("600x300")
root.resizable(False, False)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About", command=about)
about_menu.add_command(label="Github", command=lambda: os.startfile("https://github.com/EinKaffeeBitte/NewLife"))
about_menu.add_command(label="Credits", command=credits)

icon = Image.open("./_internal/icon.png")
icon = ImageTk.PhotoImage(icon)

root.iconphoto(False, icon)

# Tk Elements
gender_label = tk.Label(root, text="Gender:")
gender_label.place(x=10, y=10)

gender_selector = ttk.Combobox(root, values=["Male", "Female", "Both", "Random"])
gender_selector.place(x=10, y=40)

agemin_label = tk.Label(root, text="Minimum Age:")
agemin_label.place(x=200, y=10)

age_min = tk.Entry(root, validate="key", validatecommand=(root.register(validate), "%P"))
age_min.place(x=200, y=40)

agemax_label = tk.Label(root, text="Maximum Age:")
agemax_label.place(x=390, y=10)

age_max = tk.Entry(root, validate="key", validatecommand=(root.register(validate), "%P"))
age_max.place(x=390, y=40)

generate_btn = tk.Button(root, text="Generate", command=lambda: generate(gender_selector.get(), age_min.get(), age_max.get()))
generate_btn.place(x=500, y=70)

# Database
man_names = ["Albert", "Bob", "Charlie", "David", "Eric", "Fred", "George", "Greg", "James", "John", "Kevin", "Liam", "Michael", "Nathan", "Oliver", "Patrick", "Robert", "Samuel", "Sebastian", "Simon", "Thomas", "Tom", "William"]
girl_names = ["Anne", "Alice", "Beth", "Carrie", "Diana", "Eileen", "Fiona", "Grace", "Hannah", "Ivy", "Janet", "Katie", "Lily", "Mia", "Nina", "Olivia", "Piper", "Quinn", "Ruby", "Sara", "Tara", "Ursula", "Victoria", "Wendy", "Xena", "Yvonne", "Zara"]
countries = ["USA", "England", "Japan", "China", "Russia", "Germany", "France", "Italy", "Spain", "Sweden", "Norway", "Netherlands", "Egipt", "South Africa", "South Korea", "North Korea", "Brazil", "Argentina", "Chile", "Colombia", "Uruguay", "Portugal", "Spain", "Canada", "India", "Mexico", "Iceland", "Greenland"]

root.mainloop()