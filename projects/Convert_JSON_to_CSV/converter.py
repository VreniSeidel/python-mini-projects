import json
import getpass
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo


class Convert:
    def __init__(self):
        self.filetype = None
        self.filename = None
        self.username = getpass.getuser()


    def select_file(self):
        self.filetype = (("Json file", "*.json"), ("All file", "*.*"))
        self.filename = filedialog.askopenfilename(title="Open file", initialdir=f"/home/{self.username}", filetypes=self.filetype)
        self.__convert()


    def __convert(self):
        try:
            with open(f"{self.filename}", 'r') as f:
                data = json.loads(f.read())
                output = ','.join([*data[0]])
                
                for obj in data:
                    output += f"\n{obj['Name']}, {obj['age']}, {obj['birthyear']}"

                with open('output.csv', 'w') as f:
                    f.write(output)
            showinfo(title="Selected file", message="Converted")
            exit()
        except Exception as ex:
            showinfo(title="Error", message=f"{str(ex)}")
            exit()


def main():
    root = Tk()
    root.title("Convert JSON to CSV")
    root.resizable(False, False)
    root.geometry("180x100")

    convert = Convert()

    open_button = ttk.Button(root, text="Open a file", command=convert.select_file)
    open_button.pack(expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
