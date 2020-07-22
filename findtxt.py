import tkinter as tk

mw = tk.Tk()

def replace_func():
      screen_lb.config(text=anna.replace(find_en.get(),replace_en.get()))

def upper_func():
      screen_lb.config(text=anna.replace(find_en.get(), find_en.get().upper()))

def lower_func():
      screen_lb.config(text=anna.replace(find_en.get(), find_en.get().lower()))

def num_func():
      
      txt=find_en.get()
      hhhhh_bt.config(text = 'count:'+str(anna.count(txt)))




anna = """Elsa?
Do you want to build a snowman?
Come on, let's go and play!
I never see you anymore
Come out the door
It's like you've gone away
We used to be best buddies
And now we're not
I wish you would tell me why!
Do you want to build a snowman?
It doesn't have to be a snowman
Go away, Anna"""

screen_lb = tk.Label(mw, text=anna, font='sylfaen 12')
findtxt_lb = tk.Label(mw, text='Find What: ')
replacetxt_lb = tk.Label(mw, text='Replace With: ')

find_en = tk.Entry(mw, bd=2, width=20)
replace_en = tk.Entry(mw, bd=2, width=20)
replace_bt = tk.Button(mw, text='Replace', width=15, command=replace_func)
upper_bt = tk.Button(mw, text='Upper', width=15, command=upper_func)
lower_bt = tk.Button(mw, text='Lower', width=15, command=lower_func)
hhhhh_bt = tk.Button(mw, text='count:', width=15, command=num_func)

screen_lb.grid(row=0, columnspan=2)
findtxt_lb.grid(row=1, column=0, sticky='E')
find_en.grid(row=1, column=1)
replacetxt_lb.grid(row=2, column=0, sticky='E')
replace_en.grid(row=2, column=1)
replace_bt.grid(row=3, columnspan=2)
upper_bt.grid(row=4, columnspan=2)
lower_bt.grid(row=5, columnspan=2)
hhhhh_bt.grid(row=6, columnspan=2)


mw.mainloop()

