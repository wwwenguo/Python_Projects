from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

# Mile input box
mile = Entry(width=8)
mile.insert(END, string='0')
mile.grid(row=0, column=1)

# Miles Unit
mile_unit = Label(text="Mile(s)")
mile_unit.grid(row=0, column=2)

# equal label
equal = Label(text="is equal to")
equal.grid(row=1, column=0)

# Km label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)


# Calculate Button
def calculate():
    miles = float(mile.get())
    kms = miles * 1.6
    # Calculated Km
    km = Label(text=str(kms))
    km.grid(row=1, column=1)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
