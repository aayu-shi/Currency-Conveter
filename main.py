from tkinter import *
from forex_python.converter import CurrencyRates
from tkinter import messagebox


class Application(object):

    def __init__(self, master):

        self.variable2 = None
        self.variable1 = None
        self.master = master
        currency_code_list = ["INR", "USD", "EUR", "CNY", "CAD", "CNY", "DKK"]

        # frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=450, bg='#ded3e8', padx=50, pady=20)
        self.bottom.pack(fill=BOTH)

        # top frame design
        self.top_image = PhotoImage(file='icons/exchange.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=200, y=40)

        # heading
        self.heading = Label(self.top, text='My Currency Converter', font='times 22 bold', bg='white', fg='black')
        self.heading.place(x=290, y=55)

        # grid
        self.label_amount = Label(self.bottom, text='Amount', font='arial 15 bold', fg='black', width=18)
        self.label_amount.grid(row=0, column=0, pady=20)
        self.entry_amount = Entry(self.bottom, width=30, bd=4)
        self.entry_amount.grid(row=0, column=1, padx=50, pady=20)

        self.label_from = Label(self.bottom, text='From Curr', font='arial 15 bold', fg='black', width=18)
        self.label_from.grid(row=1, column=0, pady=20)
        self.curr1 = StringVar()
        self.drop = OptionMenu(self.bottom, self.curr1, *currency_code_list)
        self.drop["width"] = 13
        self.drop.grid(row=1, column=1, padx=50, pady=20)

        self.label_to = Label(self.bottom, text='To Curr', font='arial 15 bold', fg='black', width=18)
        self.label_to.grid(row=2, column=0, pady=20)
        self.curr2 = StringVar()
        self.drop = OptionMenu(self.bottom, self.curr2, *currency_code_list)
        self.drop["width"] = 13
        self.drop.grid(row=2, column=1, padx=50, pady=20)

        button = Button(self.bottom, text="Convert", width=15, font='Sans 12 bold', bg='#faf7a2',
                        command=self.converter)
        button.grid(row=3, column=1, pady=20)

        self.label_converted = Label(self.bottom, text='Converted Amount', font='arial 15 bold', fg='black', width=18)
        self.label_converted.grid(row=4, column=0, pady=20)
        self.converted_amount = Entry(self.bottom, width=30, bd=4)
        self.converted_amount.grid(row=4, column=1, padx=50, pady=20)

        button = Button(self.bottom, text="Clear All", width=15, font='Sans 12 bold', bg='#faf7a2',
                        command=self.clear_all)
        button.grid(row=5, column=1, pady=20)

    # real time currency conversion function
    def converter(self):
        c = CurrencyRates()
        to_cur = self.curr2.get()
        from_cur = self.curr1.get()
        if self.entry_amount.get() == "":
            messagebox.showerror("Error", "Amount not entered", icon='warning')
        elif from_cur == "currency" or to_cur == "currency":
            messagebox.showerror("Error", "Please select currency", icon='warning')
        else:
            new_amt = c.convert(from_cur, to_cur, float(self.entry_amount.get()))
            self.converted_amount.insert(0, str(new_amt))

    # clear entries
    def clear_all(self):
        self.entry_amount.delete(0, END)
        self.converted_amount.delete(0, END)


def main():
    root = Tk()
    app = Application(root)
    root.title("Currency Converter")
    root.geometry("800x600+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
