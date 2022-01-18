import sys
import tkinter as tk
from tkinter import messagebox
from creation import bin_dict_maker

lst = [] * 10  # declaring variables and stuff
storage_radio = list()
font = 'Times New Roman'



class Creation(tk.Frame):

    # noinspection SpellCheckingInspection
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # initializing the class
        self.master = master

        self.master.title('Creation ~ by Noctis')
        self.frame_test()

    def frame_test(self):
        info_frame = tk.Frame(self)  # the four frames that i've used
        file_frame = tk.Frame(self)
        data_frame = tk.Frame(self)
        button_frame = tk.Frame(self)

        info_frame.grid(row=0, sticky='W' + 'E' + 'N' + 'S')  # grid manager for the frames
        file_frame.grid(row=1, sticky='W' + 'E' + 'N' + 'S')
        data_frame.grid(row=2, sticky='W' + 'E' + 'N' + 'S')
        button_frame.grid(row=12, sticky='W' + 'E' + 'N' + 'S')

        text = '''Welcome everyone
        This program is made by Noctis.
         This creates binary files with data stored in dictionaries'''

        info_text = tk.Label(info_frame, text=text, font=(font, 20))  # info frame
        info_text.grid(row=0, sticky='W' + 'E' + 'N' + 'S', pady=(5, 20), padx=(10, 50))

        tk.Label(file_frame, text='File Name:', font=(font, 10)).grid(row=1, padx=(50, 0),
                                                                      pady=(30, 60))
        filename = tk.Entry(file_frame)  # file name entry
        filename.grid(row=1, column=1, columnspan=5, pady=(30, 60))
        tk.Label(file_frame, text='.dat file', font=(font, 10)).grid(row=1, column=6,
                                                                     padx=(5, 50), pady=(30, 60))
        tk.Label(file_frame, text='Number of Dictionaries:', font=(font, 10)).grid(row=1, column=7,
                                                                                   padx=(5, 5), pady=(30, 60))
        size = tk.Entry(file_frame)  # number of dics in file
        size.grid(row=1, column=8, padx=(10, 10), pady=(30, 60))

        key_entry = list()
        opt_entry = list()
        for j in range(10):  # loop for the ten entries in data_frame
            global lst, storage_radio

            tk.Label(data_frame, text=f'Enter key {j + 1}',
                     font=(font, 10)).grid(row=2 + j, padx=(50, 0))

            key_entry.append(tk.Entry(data_frame))  # entry for keys
            key_entry[j].grid(row=2 + j, column=1, padx=(10, 10))

            check_radio = tk.IntVar()
            storage_radio.append(check_radio)
            # radio button for types
            radio_int = tk.Radiobutton(data_frame, text='Integer', variable=check_radio, value=1)
            radio_int.deselect()
            radio_int.grid(row=2 + j, column=2)

            radio_str = tk.Radiobutton(data_frame, text='String', variable=check_radio, value=2)
            radio_str.deselect()
            radio_str.grid(row=2 + j, column=3)

            tk.Label(data_frame, text='Enter optional data',
                     font=(font, 10)).grid(row=2 + j, column=4, padx=(30, 20))

            opt_entry.append(tk.Entry(data_frame))  # optional entries
            opt_entry[j].grid(row=2 + j, column=5, padx=(20, 50))
        # note to self, loop finished
        ok_button = tk.Button(button_frame, text='Accept',
                              command=lambda: done(key_entry, opt_entry, filename, size), relief='ridge')
        ok_button.pack(side='right', padx=(10, 5), pady=(20, 5))  # ok button

        no_button = tk.Button(button_frame, text='Cancel', command=cancel, relief='ridge')
        no_button.pack(side='right', padx=(30, 5), pady=(20, 5))  # cancel button


# using pack here coz ive no clue how to grid it properly

def cancel():
    if tk.messagebox.askokcancel(title='Cancelling', message='Do you wish to close '
                                                             'the program?', default='cancel'):
        root.destroy()
        # cancel func for button


def done(data, opt_data, file, size):  # the func for ok button
    keys = [ele.get() for ele in data]
    str_int_lst = [h.get() for h in storage_radio]
    opt = [v.get() for v in opt_data]

    try:
        stuff = bin_dict_maker(keys, str_int_lst, opt, file.get(), int(size.get()))

        message = f'''The given data has been successfully stored into {file.get()}.dat
        the data stored is:
        {stuff}
        '''
        tk.messagebox.showinfo(title='Task completed successfully', message=message)

    except Exception as error:
        tk.messagebox.showerror(title='ERROR!!', message=f'Please recheck your data and try again\n {error}')


if __name__ == '__main__':
    root = tk.Tk()

    if (sys.platform.startswith('win')):
        root.iconbitmap('..\\assets\\creation_gui_icon.ico')
    else:
        logo = tk.PhotoImage(file='../assets/creation_gui_icon.gif')
        root.call('wm', 'iconphoto', root._w, logo)

    program = Creation(root)
    program.grid()
    program.mainloop()
