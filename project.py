#!/usr/bin/python3
import tkinter
import os
import webbrowser
from pprint import pprint
import pymysql
from subprocess import PIPE,Popen

###################################### windows ###########
def win1():
	global w1
	w1=tkinter.Tk()
	w1.title("simulation tracker")
	return w1

def win2():
	global w2
	w2=tkinter.Tk()
	w2.title("show data")
	return w2

######################## insert db ####################
db=pymysql.connect(host="localhost",user="root",passwd="nani",db="naresh")
cur=db.cursor()
cur.execute("show tables")
def ins_db():
	for k,v in d['text'].items():
		pid=os.getpid()
		rule=v[0].get()
		vect=v[1].get()
		cmd=v[2].get()
		exp=v[3].get()
		act=v[4].get()
		log=v[5].get()
		cur.execute("insert into project values('%s','%s','%s','%s','%s','%s','%s')"%(pid,rule,vect,cmd,exp,act,log))
		db.commit()
		
################################# show db ###########################
def show():
	w2=win2();
	tkinter.Label(w2,text="pid",font=("helverpica",12)).grid(row=1,column=0)
	tkinter.Label(w2,text="Rule",font=("helverpica",12)).grid(row=1,column=1)
	tkinter.Label(w2,text="Vector",font=("helverpica",12)).grid(row=1,column=2)
	tkinter.Label(w2,text="Command",font=("helverpica",12)).grid(row=1,column=3)
	tkinter.Label(w2,text="Actual_output",font=("helverpica",12)).grid(row=1,column=4)
	tkinter.Label(w2,text="Excepted_output",font=("helverpica",12)).grid(row=1,column=5)
	tkinter.Label(w2,text="log_file",font=("helverpica",12)).grid(row=1,column=6)
	j=2;
	cur.execute("select * from project")
	for v in cur.fetchall():
		tkinter.Label(w2,text=v[0]).grid(row=j,column=0)
		tkinter.Label(w2,text=v[1]).grid(row=j,column=1)
		tkinter.Label(w2,text=v[2]).grid(row=j,column=2)
		tkinter.Label(w2,text=v[3]).grid(row=j,column=3)
		tkinter.Label(w2,text=v[4]).grid(row=j,column=4)
		tkinter.Label(w2,text=v[5].strip()).grid(row=j,column=5)
		
		def callback(event,arg):
			webbrowser.open_new(arg)
		lab9=tkinter.Label(w2,text=v[6],cursor="hand2",font=("helverpica",10))
		lab9.grid(row=j,column=6)
		lab9.bind("<Button-1>",lambda event,arg=lab9.cget("text"):callback(event,arg))
		j=j+1
		
########################### dictionarys ####################
d={}
d['check']={}
d['check_name']={}
d['text']={}
d['log']={}
i=4

############### create window #############
def win_create():
	l0=tkinter.Label(w,text="SIMULATION TRACKER",font=("helverpica",20))
	l0.grid(row=0,columnspan=10)
	l1=tkinter.Label(w,text="Ruleno",font=("helverpica",12))
	l1.grid(row=2,column=2)
	l2=tkinter.Label(w,text="Vector",font=("helverpica",12))
	l2.grid(row=2,column=3)
	l3=tkinter.Label(w,text="Command",font=("helverpica",12))
	l3.grid(row=2,column=4)
	l4=tkinter.Label(w,text="Expected_output",font=("helverpica",12))
	l4.grid(row=2,column=5)
	l5=tkinter.Label(w,text="Actuval_output",font=("helverpica",12))
	l5.grid(row=2,column=6)
	l6=tkinter.Label(w,text="Logfile",font=("helverpica",12))
	l6.grid(row=2,column=7)
	l7=tkinter.Label(w,text="Quit",font=("helverpica",12))
	l7.grid(row=2,column=8)

	b1=tkinter.Button(w,text="AddRow",command=add_row,font=("helverpica",12))
	b1.grid(row=1,column=2)
	b2=tkinter.Button(w,text="Inserttodb",command=ins_db,font=("helverpica",12))
	b2.grid(row=1,column=3)
	b3=tkinter.Button(w,text="Execute",command=exe,font=("helverpica",12))
	b3.grid(row=1,column=4)
	b4=tkinter.Button(w,text="Delete Row",command=del_row,font=("helverpica",12))
	b4.grid(row=1,column=5)
	b5=tkinter.Button(w,text="Show data",command=show,font=("helverpica",12))
	b5.grid(row=1,column=6)
	b6=tkinter.Button(w,text="import xml",font=("helverpica",12))
	b6.grid(row=1,column=7)
	b7=tkinter.Button(w,text="Quit",command=quit,font=("helverpica",12))
	b7.grid(row=1,column=8)

################# add_row ##############
def add_row():
	global i
	
	ck=tkinter.IntVar()
	c1=tkinter.Checkbutton(w,variable=ck)
	c1.grid(row=i,column=0)
	d['check'][i]=ck
	d['check_name'][i]=c1
	
	e1=tkinter.Entry(w,font=("helverpica",12))
	e1.grid(row=i,column=2)
	d['text'][i]=[]
	d['text'][i].append(e1)
	e2=tkinter.Entry(w,font=("helverpica",12))
	e2.grid(row=i,column=3)
	d['text'][i].append(e2)
	e3=tkinter.Entry(w,font=("helverpica",12))
	e3.grid(row=i,column=4)
	d['text'][i].append(e3)
	e4=tkinter.Entry(w,font=("helverpica",12))
	e4.grid(row=i,column=5)
	d['text'][i].append(e4)
	e5=tkinter.Entry(w,font=("helverpica",12))
	e5.grid(row=i,column=6)
	d['text'][i].append(e5)
	e6=tkinter.Entry(w,font=("helverpica",12))
	e6.grid(row=i,column=7)
	d['text'][i].append(e6)
	i+=1	
	pprint(d)
########################### delete ##################
def del_row():
	l=[]
	for k,v in d['check'].items():
		if v.get()==1:
			d['text'][k][0].destroy()
			d['text'][k][1].destroy()
			d['text'][k][2].destroy()
			d['text'][k][3].destroy()
			d['text'][k][4].destroy()
			d['text'][k][5].destroy()
			d['check_name'][k].destroy()
			l.append(k)
	for v in l:
		del d['text'][v]
		del d['check'][v]
		del d['check_name'][v]
	pprint(d)

############################ execute ###############
def exe():
	for k,v in d['text'].items():
		cmd1="./"+v[2].get()
		pro=Popen(args=cmd1,stdout=PIPE,shell=1,stderr=PIPE)
		v[4].delete(0,tkinter.END)
		v[4].insert(0,pro.stdout.read()+pro.stderr.read())
		v[5].insert(0,v[2].get()+".log")
		
############### window close #################
w=win1()
win_create()
w.mainloop()
