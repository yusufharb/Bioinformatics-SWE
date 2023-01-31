from tkinter import *
import tkinter as tk
import os
from tkinter.filedialog import askopenfile 
import time
import subprocess


#command5 = 'sudo apt-get install ncbi-blast+'
#os.system(command5)

def openfile():
    file_path = askopenfile(mode='r', filetypes=[('fastq Files', '*fastq')])
    if file_path is not None:
        pass

def upload():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

def blast():
	new_blast = Tk()
	new_blast.geometry('400x500')
	new_blast.title('first page')
	new_blast['background'] = 'grey'
	f = open("D:\pythons\blast.sh", "r")
	command_blast = 'bash blast.sh'
	os.system(command_blast)


def msa():
	new_msa= Tk()
	new_msa.geometry('400x500')
	new_msa.title('first page')
	new_msa['background'] = 'grey'

def pairwise():
	new_pairwise = Tk()
	new_pairwise.geometry('400x500')
	new_pairwise.title('first page')
	new_pairwise['background'] = 'grey'

def build():
	new_build=Tk()
	new_build.geometry('400x500')
	new_build.title('first page')
	new_build['background'] = 'grey'

def fast():
	new_fast = Tk()
	new_fast.geometry('400x500')
	new_fast.title('first page')
	new_fast['background'] = 'grey'
	command = 'sed -n \'1~4s/^@/>/p;2~4p\' {}.fastq > output.fasta'
	#command1 = 'sed -n \'1~4s/^@/>/p;2~4p\' {}.fastq > OUTFILE.fasta'.format(file_path)
	os.system(command)

def report():
	new_report = Tk()
	new_report.geometry('400x500')
	new_report.title('first page')
	new_report['background'] = 'grey'







def next():
	new_next=Tk()
	new_next.geometry('400x500')
	new_next.title('first page')
	new_next['background'] = 'grey'
	label = Label(new_next,text="Chooce which you need",fg='#008080',font="time 15 bold",padx=90,pady=10)
	label.grid(row=0,column=0,columnspan=20)
	
	openfile_btn= Button(new_next,text='upload', font=('bold',15) ,fg='#158aff',bd=0, bg='#c3c3c3',command=openfile)
	openfile_btn.place(x=50,y=50)
	
	
	Blast_btn= Button(new_next,text='Blast', font=('bold',15) ,fg='#158aff',bd=0, bg='#c3c3c3',command=blast)
	Blast_btn.place(x=50,y=100)
	
	
	MSA_btn = tk.Button(new_next, text='MSA', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',command=msa)
	MSA_btn.place(x=50, y=150)

	pairwise_btn = tk.Button(new_next, text='Pairwise', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',command=pairwise)
	pairwise_btn.place(x=50, y=200)

	Build_btn = tk.Button(new_next, text='phylogenetic tree', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',command=build)
	Build_btn.place(x=50, y=250)

	fast_btn = tk.Button(new_next, text='fast-fastq and count', font=('bold', 15), fg='#158aff', bd=0,
						 bg='#c3c3c3',command=fast)
	fast_btn.place(x=50, y=300)

	report_btn = tk.Button(new_next, text='Report', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',command=report)
	report_btn.place(x=50, y=350)


#window
tkWindow = Tk()
tkWindow.geometry('300x250')
tkWindow.title('Login')

Label(tkWindow, text="LOGIN", fg='#008080').pack()

#username label and text entry box
Label(tkWindow,text="").pack()
Label(tkWindow,text="Username",font=('arial', 10),).place(x=20,y=40)
username_login = Entry(tkWindow,textvariable="Username")
username_login.pack()

#username label and text entry box
Label(tkWindow,text="").pack()
Label(tkWindow,text="Password",font=('arial', 10),).place(x=25,y=80)
password_login = Entry(tkWindow,textvariable="Password",show= '*')
password_login.pack()
#login button
Label(tkWindow, text="").pack()
Button(tkWindow, text="Login", width=10, height=1,font=('bold',15) ,fg='#158aff',bd=0, bg='#c3c3c3',command=next).pack()

tkWindow.mainloop()





tkWindow.mainloop()
