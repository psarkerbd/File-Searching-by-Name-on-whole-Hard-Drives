from tkinter import *;
import os;

def no():
    reply = 'Did not find';
    listbox.config(justify = 'center', fg = 'red')
    listbox.insert(END, reply);
    listbox.pack(side=LEFT, fill=BOTH, expand=1);

def action():
    directory = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\"];
    reply="";
    f = False;
    ufilename = FilenameEntry.get();
    filelist = [];
    
    for rootpath in directory:
        for root, dirnames, filenames in os.walk(rootpath):
            for name in filenames:
                if ufilename in name:
                    f = True;
                    total = root + '  ' + name;
                    filelist.append(total);
            
    listbox.delete(0, END);
    
    if (f == False):
        no();
    else:
        cnt = 0;
        listbox.delete(0, END);
        listbox.config(fg = 'green', yscrollcommand=scrollbar.set, justify = 'left')
        scrollbar.config(command=listbox.yview);
        for filename in filelist:
            cnt += 1;
            reply = str(cnt) + '. ' + filename
            listbox.insert(END, reply);
            listbox.pack(side=LEFT, fill=BOTH, expand=1);
            scrollbar.pack(side=RIGHT, fill=Y);
            
master = Tk();
master.title("File Searching by Python");
master.geometry('400x300')
TitleLabel = Label(master, text = 'File Searching by Python', font = 'bold 10 underline', fg='green')
TitleLabel.pack();
FilenameLabel = Label(master, text = "Enter File name", font = 'bold 10', fg='black');
FilenameLabel.pack(padx=6, pady=10, side=TOP);
FilenameEntry = Entry(master);
FilenameEntry.pack(padx=0, pady=0, side=TOP);

listbox = Listbox(master);

listbox.delete(0, END);

scrollbar = Scrollbar(master);

Searchbutton = Button(master, text = "Search", bg = 'black', fg='white', command = action)
Searchbutton.pack(padx=5, pady=10);

master.resizable(False, False);
master.mainloop();
