from tkinter import *
import tkinter as tk

def blast():
	new_blast = Tk()
	new_blast.geometry('400x500')
	new_blast.title('first page')
	new_blast['background'] = 'grey'

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

def report():
	new_report = Tk()
	new_report.geometry('400x500')
	new_report.title('first page')
	new_report['background'] = 'grey'






















def new_next():
  new_next=Tk()
  new_next.geometry('300x500')
  new_next.title('first page')
  new_next['background'] = 'grey'
  def t_menu():
    def coll_t_menu():
        t_menu_fm.destroy()
        to_btn.config(text='☰')
        to_btn.config(command=t_menu)



    t_menu_fm= tk.Frame(new_next,bg='#158aff')
    Blast_btn = Button(t_menu_fm, text='Blast', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=blast)
    Blast_btn.place(x=20, y=20)
    MSA_btn = tk.Button(t_menu_fm, text='MSA', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=msa)
    MSA_btn.place(x=20, y=80)

    pairwise_btn = tk.Button(t_menu_fm, text='Pairwise', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                             command=pairwise)
    pairwise_btn.place(x=20, y=140)

    Build_btn = tk.Button(t_menu_fm, text='phylogenetic tree', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3',
                          command=build)
    Build_btn.place(x=20, y=220)

    fast_btn = tk.Button(t_menu_fm, text='fast-fastq and count', font=('bold', 15), fg='#158aff', bd=0,
                         bg='#c3c3c3', command=fast)
    fast_btn.place(x=20, y=300)

    report_btn = tk.Button(t_menu_fm, text='Report', font=('bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', command=report)
    report_btn.place(x=20, y=380)

    window_height = new_next.winfo_height()

    t_menu_fm.place(x=0,y=50,height=window_height,width=230)
    to_btn.config(text='X')
    to_btn.config(command=coll_t_menu)


  head_frame=tk.Frame(new_next,bg='#158aff',highlightbackground='white',highlightthickness=1)
  head_frame.pack(side=tk.TOP,fill=tk.X)
  head_frame.pack_propagate(False)
  head_frame.configure(height=50)
  to_btn =tk.Button(head_frame,text='☰', bg='#158aff', fg='white',
                       font=('Bold', 20), bd=0,activebackground='#158aff', activeforeground='white',command=t_menu)
  to_btn.pack(side=tk.LEFT)
  lb=tk.Label(head_frame,text='choose',bg='#158aff',fg='white',font=('Bold',20))



tkWindow = Tk()
tkWindow.geometry('500x500')
tkWindow.title('Login System')
tkWindow.resizable(False,False)
tkWindow.config(background='#D5DBDB')
#TITLE
title = Label(tkWindow, text='Login System',font=('courier',15),bg='black',fg='white')
title.pack(fill=X)
#frame
fr1=Frame(tkWindow,width='300',height='350',bg='whitesmoke')
fr1.pack(pady=30)
#image
photo = PhotoImage(file="C:\\Users\\Rana nasser\\Downloads\\encrypted.png")
panel = Label(tkWindow,image= photo)
panel.place(x=200,y=60)
#label
lb1= Label(fr1,text='USERNAME:',font=('courier',15),bg='whitesmoke')
lb1.place(x=10,y=140)
lb2= Label(fr1,text='PASSWORD:',font=('courier',15),bg='whitesmoke')
lb2.place(x=10,y=180)
#entry
en1 =Entry(fr1)
en1.place(x=134,y=145)
en2 =Entry(fr1,show= '*')
en2.place(x=134,y=185)
#button
bt1=Button(fr1,text='Login',font=('courier,15'),bg='#76D7C4',width='11',command=new_next)

bt1.place(x=15,y=260)





tkWindow.mainloop()
