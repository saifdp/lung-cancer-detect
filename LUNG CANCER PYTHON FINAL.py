
import tkinter as tk
import tkinter.messagebox
import pandas as p
from tkinter import *

import mysql.connector

import mysql.connector as mysql

#from tkinter import filedialog as fd 
import tkinter.filedialog
from tkinter import ttk

from datetime import date 
import datetime
import os

from dateutil import relativedelta

from PIL import ImageTk,Image  

import pandas as p
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from array import *
from pandas import DataFrame
import matplotlib.pyplot as plt

class NewWin():
    
   def __init__(self):
       self.win = tk.Tk()

       self.win.geometry("863x505+300+100");
       self.win.title(" Lung Cancer Prediction System ")
       self.win.configure(bg="#912388")
       self.canvas = tk.Canvas(self.win, width = 863, height = 505)  
       self.canvas.place(x=0,y=0);


       self.img3 = ImageTk.PhotoImage(Image.open("l2.png"))  
       l22 = tk.Label(self.win, image=self.img3,width=863,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l22.place(x=00,y=0)


       self.img2 = ImageTk.PhotoImage(Image.open("l2.png"))  
       l11 = tk.Label(self.win, image=self.img2,width=863,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l11.place(x=0,y=0)

#       self.l1 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
 #      self.l1.place(x=0,y=00)

#       self.img3 = ImageTk.PhotoImage(Image.open("can3.jpg"))  
#       l33 = tk.Label(self.win, image=self.img3,width=450,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l33.place(x=0,y=150)

       self.b2 = tk.Button(self.win,text=" Select Data Set File  ",width=25,bg="#092193",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.callback)
       self.b2.place(x=310,y=190)
       
  #     self.l12 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
   #    self.l12.place(x=0,y=430)
       
       self.win.mainloop()

   def callback(self):
       self.name=tkinter.filedialog.askopenfilename()
       #name=fd.askopenfilename() 
       print(self.name)
       self.t1 = tk.Label(self.win,text="",width=35,relief="raised",bg="#092193",fg="white",font=("cambria",12,"bold"))
       self.t1.place(x=290,y=260)
       self.t1.configure(text=self.name)

       self.b1 = tk.Button(self.win,text=" Read Data Values  ",width=25,bg="red",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.loading)
       self.b1.place(x=310,y=320)

#       fname=self.name
 #      print("File Name="+fname)
  #     if(fname==""):       
   #        tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Please Enter File Name....");
    #   else:
     #      tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
      #     self.loading()
#             

   def loading(self):
       
       fname=self.name
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" Lung Cancer Prediction System"," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
#       self.win.destroy()
 #      app=Test()
 
   def dataload(self):
       tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Data Loading Functio is Called...");
       fname=self.name
       data=p.read_csv(fname)
#       print(data);
       data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
#       print(data[['employee_name','ssn','dept','salary','doj','no_of_project_assigned','completed']]);
       n=data.shape
       print(" Total Record=")
       max=n[0]
       print(max)
       
  #     for i in range(max):
#           print(i)
 #          print("\t Record")
    
       rec=data.iloc[3];
       print(rec)
       print(rec[0])
       
       #[['employee name','gender','age','location']]);
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 
       #mdb=mysql.connector.connect(user="root",password="mj",database="crop",host="localhost",charset='utf8')
       #cursor=mdb.cursor()
       cursor.execute("delete from cancerdataset");
       mdb.commit()
#       sql="insert into emp values('jjj','222','Tester','12000','2015-2-2','40','25')";
 #      cursor.execute(sql);
 #      sql="select * from emp"



       for i in range(max):
           rec=data.iloc[i]
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           f6=str(rec[5])
           f7=str(rec[6])
           f8=str(rec[7])
           f9=str(rec[8])
           f10=str(rec[9])
           f11=str(rec[10])
           f12=str(rec[11])
           f13=str(rec[12])
           f14=str(rec[13])
           f15=str(rec[14])
           
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15);
           sql="insert into cancerdataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15));
           mdb.commit()
     
       print(" All Data Transfered And Stored in Data Base....");    
       tkinter.messagebox.showinfo(" Cancer Prediction System "," All Cancer Patients Data Transfered And Stored in Data Base....");
       self.win.destroy()
       app=Load();
       
     #  rows=cursor.fetchall()
      # total=cursor.rowcount
      # print("\n Total Data Records=\t"+str(total));


 
 
class Load():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" Lung Cancer Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from cancerdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Patients Data Set Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#092193",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('15', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="	Alcohol Use")
       self.tv.heading("#5",text="	Dust Allergy	")
       self.tv.heading("#6",text="Passive Smoker")
       self.tv.heading("#7",text="	Chest Pain")
       self.tv.heading("#8",text="	Coughing of Blood")
       self.tv.heading("#9",text="	Fatigue")
       self.tv.heading("#10",text=" Weight Loss") 
       self.tv.heading("#11",text="Shortness of Breath")
       self.tv.heading("#12",text="Swallowing Difficulty")
       self.tv.heading("#13",text="Clubbing of Finger Nails")
       self.tv.heading("#14",text="Frequent Cold")
       self.tv.heading("#15",text="Dry Cough")

	
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse Data Set ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)

       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=Analysis();

class Analysis():
   def __init__(self):

       self.ana = tk.Tk()
       self.ana.geometry("800x470+300+100");
       self.ana.title(" Lung Cancer Disease Prediction System ")
       self.ana.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.ana, width = 800, height = 470)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("l3.png"))  
       l1 = tk.Label(self.ana, image=self.img1,width=800,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

#       l2 = tk.Label(self.ana,text=" Cancer Patient Data Analysis for Disease Prediction  ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
#       l2.place(x=200,y=30)

       
       b1 = tk.Button(self.ana,text=" Extract Featured Attribute  ",width=30,bg="#092193",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.featureextraction)
       b1.place(x=250,y=180)
       
#       b2 = tk.Button(self.ana,text=" Classification ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.classify)
#       b2.place(x=220,y=180)

#       b3 = tk.Button(self.ana,text=" Prediction Of Crop ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.prediction)
 #      b3.place(x=150,y=180)

       b4 = tk.Button(self.ana, text=" Exit ",width=30,bg="#092193",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=250,y=290)

       self.ana.mainloop()

   def featureextraction(self):
       tkinter.messagebox.showinfo(" Lung Cancer Prediction System"," Extraction of Required Data from Oveall Data Set Information...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       cursor.execute("delete from cancerdataset1");

       sql="select * from cancerdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           
           f1=str(row[0])
           f2=int(row[1])
           f3=int(row[2])
           f4=int(row[3])
           f5=int(row[4])
           f6=int(row[5])
           f7=int(row[6])
           f8=int(row[7])
           f9=int(row[8])
           f10=int(row[9])
           f11=int(row[10])
           f12=int(row[11])
           f13=int(row[12])
           f14=int(row[13])
           f15=int(row[14])
           
           if(f3==1):
               gender="Male";
           else:
               gender="Female";
           
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15);
           sql="insert into cancerdataset1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,gender,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15));
           mdb.commit()
  
       self.ana.destroy()
       app=Load1()
       
 #  def classify(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
   #    self.ana.destroy()
  #     app=Classification()

   def prediction(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Load()

   def exit(self):
       self.ana.destroy()


class Load1():
   def __init__(self):
       self.load1 = tk.Tk()
       self.load1.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load1.configure(bg="#985676")
       self.load1.title(" Lung Cancer Predicction System ")


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select age,gender,alcohol,smoker,coughblood,wloss,breath,swaldiff,drycough from cancerdataset1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Extracted Featured Attributes Details Of Lung Cancer Patients ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=250,y=20)

       self.tv=ttk.Treeview(self.load1,column=(1,2,3,4,5,6,7,8,9),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="green",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('9', minwidth=50, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="Gender")
       self.tv.heading("#3",text="	Alcoholic")
       self.tv.heading("#4",text="Smoking")
       self.tv.heading("#5",text="	Blood Cough")
       self.tv.heading("#6",text="Loss Of Weight") 
       self.tv.heading("#7",text="Breath Problem")
       self.tv.heading("#8",text="Swallowing Difficulty")
       self.tv.heading("#9",text="Dry Cough")
 
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Predict Cancer Patients  ",width=40,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.loading)
       b1.place(x=450,y=14)

       self.load1.mainloop()
 
   def loading(self):
       self.load1.destroy()
       app=Prediction()



class Prediction():
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("401x110+400+200");
       self.prediction.title(" Lung Cancer Disease Prediction System ")
#       self.prediction.configure(bg="#232342")

       self.canvas = tk.Canvas(self.prediction, width = 400, height = 110)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("l4.png"))  
#       l1 = tk.Label(self.prediction, image=self.img1,width=400,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
#       l1.place(x=0,y=00)

#       l2 = tk.Label(self.prediction,text=" Prediction of Disease   ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=30,y=30)

       
       b1 = tk.Button(self.prediction,image=self.img1,width=400,bg="cyan",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.croppred)
       b1.place(x=0,y=0)
       

#       b4 = tk.Button(self.prediction, text=" Exit ",width=35,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=150,y=200)

       self.prediction.mainloop()

   def croppred(self):
       tkinter.messagebox.showinfo(" Lung Cancer Disease Prediction"," Disease Prediction Begins...")
       tkinter.messagebox.showinfo(" Lung Cancer Disease Prediction "," Prediction of Lung Cancer Disease ...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       cursor1 = mdb.cursor()
       
       cursor.execute("delete from cancerdisease");

       sql="select pid,age,gender,alcohol,smoker,coughblood,wloss,breath,swaldiff,drycough from cancerdataset1";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           pid=str(row[0])
           age=int(row[1])
           gen=str(row[2])
           alcohol=int(row[3])
           smoker=int(row[4])
           blood=int(row[5]) 
           wloss=int(row[6]) 
           breath=int(row[7])
           swaldiff=int(row[8])
           drycough=int(row[9])
           
           if(alcohol<3):
               alcohol1="Normal";
           elif(alcohol>3 and alcohol<6):
               alcohol1="Medium"
           else:
               alcohol1="High"
           
           if(smoker<3):
               smoker1="Normal";
           elif(smoker>3 and smoker<6):
               smoker1="Medium"
           else:
               smoker1="High"

           if(blood==0):
               blood1="Normal";
           elif(blood>1 and blood<3):
               blood1="Medium"
           else:
               blood1="High"

           if(wloss<3):
               wloss1="Normal";
           elif(wloss>3 and wloss<6):
               wloss1="Medium"
           else:
               wloss1="High"

           if(breath<2):
               breath1="Normal";
           elif(breath>2 and breath<5):
               breath1="Medium"
           else:
               breath1="High"

           if(swaldiff<3):
               swaldiff1="Normal";
           elif(swaldiff>3 and swaldiff<6):
               swaldiff1="Medium"
           else:
               swaldiff1="High"

           if(drycough<3):
               drycough1="Normal";
           elif(drycough>3 and drycough<6):
               drycough1="Medium"
           else:
               drycough1="High"

           if((breath1=="Medium") and (smoker1=="High") and (age>20) and (wloss1=="Medium") and (blood1=="Normal")):
               disease=" Cancer is At 1nd Stage "
           elif((blood1=="Medium") and (breath1=="Medium") and (wloss1=="Normal" or wloss1=="Medium")):
               disease=" Cancer is At 2nd Stage "
           elif((blood1=="Medium" or blood1=="High") and (breath1=="Medium" or breath1=="High") and (wloss1=="High" or wloss1=="High")):
               disease=" Cancer is At 3rd Stage "
           elif((blood1=="Medium" or blood1=="High") and (breath1=="Medium" or breath1=="High" or breath1=="Normal") and (wloss1=="High" or wloss1=="High" or wloss=="Normal")):
               disease=" Cancer is At 3rd Stage "
           elif((breath1=="Medium") and (smoker1=="Meidum" or smoker1=="High") and (age>30) and (wloss1=="Normal" or wloss1=="Medium") and (blood1=="Normal") and (drycough=="Normal")):
               disease=" Cancer is At Beigning Stage "
           elif((breath1=="Normal") and (smoker1=="Normal") and (age>20) and (wloss1=="Normal" or wloss1=="Medium" or wloss1=="High") and (blood1=="Normal") and (drycough1=="Normal" or drycough1=="Medium")):
               disease=" Cancer is Not At Present State "
           else:
               #((blood==0) and (breath<2) and (smoker<5) and (age>10 or age<60) and (wloss<3)):
               disease=" No Cancer "

           print(pid,"===",disease); 
           sql1="insert into cancerdisease values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor1.execute(sql1,(pid,age,gen,alcohol1,smoker1,blood1,wloss1,breath1,swaldiff1,drycough1,disease));
           mdb.commit()
     
       tkinter.messagebox.showinfo(" Lung Cancer Disease Prediction ","Lung Cancer Disease Prediction of a Patient Completed ....");
       self.prediction.destroy()
       app=Load2()
       
   def exit(self):
       self.prediction.destroy()
       app=Analysis()

class Load2():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" Lung Cancer Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from cancerdisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease Predicted Result Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#213473",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('11', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Pid")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="	Alcoholic")
       self.tv.heading("#5",text="Smoking")
       self.tv.heading("#6",text="	Blood Cough")
       self.tv.heading("#7",text="Loss Of Weight") 
       self.tv.heading("#8",text="Breath Problem")
       self.tv.heading("#9",text="Swallowing Difficulty")
       self.tv.heading("#10",text="Dry Cough")
       self.tv.heading("#11",text="Result")
 
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse The Result ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)
 
       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Cancer Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=Classification();


class Classification():
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("813x410+300+100");
       self.classify.title(" Lung Cancer Disease Prediction System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 813, height = 411)  
       self.canvas.place(x=0,y=0);

       self.img2 = ImageTk.PhotoImage(Image.open("l5.png"))  
       l2 = tk.Label(self.classify, image=self.img2,width=813,relief="groove",fg="#323223",font=("cambria",14,"bold"))
       l2.place(x=0,y=00)

#       self.img1 = ImageTk.PhotoImage(Image.open("air1.jpg"))  
 #      l1 = tk.Label(self.classify, image=self.img1,width=500,relief="groove",fg="#323223",font=("cambria",14,"bold"))
  #     l1.place(x=500,y=00)

#       l2 = tk.Label(self.classify,text=" Cancer Disease Prediction Data Analyse On Different Criteria  ",width=60,height=2,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=100,y=30)

 
       b1 = tk.Button(self.classify,text=" Cancer Disease Class  ",width=30,height=1,bg="white",fg="red",relief="groove",font=("cambria",15,"bold"),command=self.diseaseclass)
       b1.place(x=50,y=120)
       
       b2 = tk.Button(self.classify,text=" Age ",width=30,height=1,bg="white",fg="red",relief="groove",font=("cambria",15,"bold"),command=self.day)
       b2.place(x=50,y=210)

       b3 = tk.Button(self.classify,text=" Exit ",width=30,height=1,bg="white",fg="darkblue",relief="groove",font=("cambria",15,"bold"),command=self.exit)
       b3.place(x=50,y=300)

#       b4 = tk.Button(self.classify, text=" Overall Analysis Of Air Polllution ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=120,y=390)
       

       self.classify.mainloop()

   def diseaseclass(self):
       tkinter.messagebox.showinfo(" Lung Cancer Disease Data Analysis "," Lung Cancer Disease Patient Data Analysis On Disease Class ...")
       self.classify.destroy()
       app=DiseaseClass()
       
   def day(self):
       tkinter.messagebox.showinfo(" Lung Cancer Disease Data Analysis "," Lung Cancer Disease Patient Data Analysis On Age Group ...")
       self.classify.destroy()
       app=Day()

   def exit(self):
#       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classficaation of Data Based On Location...")
       self.classify.destroy()
      
#   def exit(self):
 #      self.classify.destroy()
  #      app=Analysis()


class Day():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Lung Cancer Disease  Data Analysis Based on Age Group  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select pid,age,res from cancerdisease";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('3', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Patient ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Result")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Classify Age Group ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=260,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=30,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Lung Cancer Disease Data Data Analysis "," Lung Cancer Disease Data Processingn on Age Group Processing classification Begins ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from temp");

       sql="select pid,age,res from cancerdisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           id=str(rec[0])
           age=int(rec[1])
           res=str(rec[2])
           
           if(age>10 and age<20):
               ageclass="Age(10-20) Class"
           elif(age>20 and age<30):
               ageclass="Age(20-30) Class"
           elif(age>30 and age<40):
               ageclass="Age(30-40) Class"
           elif(age>40 and age<50):
               ageclass="Age(40-50) Class"
           elif(age>50 and age<60):
               ageclass="Age(50-60) Class"
           else:
               ageclass="Age(>60) Class"
        
           sql="insert into temp values(%s,%s)"
           cursor.execute(sql,(ageclass,res));
           mdb.commit()
           
       self.load.destroy()
       app=Age1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

       
       
class Age1():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title("Lung  Cancer Disease  Data Analysis Based on Age Group  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select age,count(*) from temp group by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="5")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="No OF Patients")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Lung Cancer Disease Data Analysis "," Lung Cancer Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,res,count(*) from temp group by age,res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def selected(self,a):
       print(" Item Clicke");
       self.data=self.tv.item(self.tv.selection())
       print(self.data)
       item=self.tv.selection()[0]
       print(item)
       self.age=str(self.tv.item(item)['values'][0])
       print(self.age)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,res,count(*) from temp where age='"+self.age+"' group by age,res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
 

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallAgeGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Age Group Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease Data Analysis Based On Age Group Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=10)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=12, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas3.place(x=650,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(13,9), dpi=70)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=Classification()


       self.load.mainloop()       
       


class DiseaseClass():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Lung Cancer Disease Data Analysis Based on Disease Class  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select res,count(*) from cancerdisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease Data Analysis Based on Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Disease Class")
       self.tv.heading("#2",text=" Total Patient ")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Lung Cancer Disease Data Analysis "," Lung Cancer Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select res,count(*) from cancerdisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           res=str(row[0])
           cnt=int(row[1])
           sc=res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallLocGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallLocGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Disease Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Lung Cancer Disease Data Analysis Based On Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="lung",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas3.place(x=700,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(8,6), dpi=100)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=Classification()





class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("800x464+300+100");
       self.root.title(" Lung Cancer Prediction System ")
       self.root.configure(bg="green")
       self.canvas = tk.Canvas(self.root, width = 800, height = 464)  
       self.canvas.place(x=0,y=0);


       self.img1 = ImageTk.PhotoImage(Image.open("l1.png"))  
#       l1 = tk.Label(self.root, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l1.place(x=0,y=00)



       b1 = tk.Button(self.root,image=self.img1,width=800,height=464,bg="green",fg="white",relief="raised",font=("cambria",14,"bold"),command=self.createNewWindow)
       b1.place(x=0,y=0) 
       
       #b2 = tk.Button(self.root, text=" Exit ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
      # b2.place(x=50,y=200)

       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=NewWin()
       

   def exit(self):
       self.root.destroy()

app=Test()
