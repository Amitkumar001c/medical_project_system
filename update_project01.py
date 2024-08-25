import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS medical_system")

from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

    #=========================================================== Functinality Declration =================================================================
        
def submitfunc():
    if patient.get()=="" or nameoftablet.get()=="" or dose.get()=="" or nooftablets.get()=="" or lot.get()=="" or issuedate.get()=="" or Expdate.get()=="" or dailydose.get()=="" or sideEffect.get()=="" or DOB.get()=="" or Furtherinfo.get()=="" or BloodPressure.get()=="" or storage.get()=="" or Medication.get()=="" or PatientID.get()=="" or contact.get()=="" or Address.get()=="" or fathername.get()=="" or dr.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        conn=mysql.connector.connect(host="localhost" , username="root" , password="" , database="medical_system"  )
        my_cursor=conn.cursor() 
        sql=("INSERT INTO Medical (patient,nameoftablet,ref,dose,nooftablets,lot,issuedate,Expdate,dailydose,sideEffect,DOB,Furtherinfo,BloodPressure,storage,Medication,PatientID,contact,Address,fathername,dr) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val=(patient.get(),nameoftablet.get(),ref.get(),dose.get(),nooftablets.get(),lot.get(),issuedate.get(),Expdate.get(),dailydose.get(),sideEffect.get(),DOB.get(),Furtherinfo.get(),BloodPressure.get(),storage.get(),Medication.get(),PatientID.get(),contact.get(),Address.get(),fathername.get(),dr.get())

        my_cursor.execute(sql,val)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")

def iprectinoption():
    
    txtprescription.insert(END , "Patient Name :\t\t\t" + patient.get() + "\n")
    txtprescription.insert(END , "Nameoftablet :\t\t\t" + nameoftablet.get() + "\n")
    txtprescription.insert(END , "Refrence No :\t\t\t" + ref.get() + "\n")
    txtprescription.insert(END , "Dose :\t\t\t" + dose.get() + "\n")
    txtprescription.insert(END , "Number Of Tablets :\t\t\t" + nooftablets.get() + "\n")
    txtprescription.insert(END , "Lot :\t\t\t" + lot.get() + "\n")
    txtprescription.insert(END , "Issue Date :\t\t\t" + issuedate.get() + "\n")
    txtprescription.insert(END , "Expairy Date :\t\t\t" + Expdate.get() + "\n")
    txtprescription.insert(END , "Daily Dose :\t\t\t" + dailydose.get() + "\n")
    txtprescription.insert(END , "Side Effects :\t\t\t" + sideEffect.get() + "\n")
    txtprescription.insert(END , "DOB :\t\t\t" + DOB.get() + "\n")
    txtprescription.insert(END , "Further Information :\t\t\t" + Furtherinfo.get() + "\n")
    txtprescription.insert(END , "Blood Pressure :\t\t\t" + BloodPressure.get() + "\n")
    txtprescription.insert(END , "Storage Advice :\t\t\t" + storage.get() + "\n")
    txtprescription.insert(END , "Medication :\t\t\t" + Medication.get() + "\n")
    txtprescription.insert(END , "Patient ID :\t\t\t" + PatientID.get() + "\n")
    txtprescription.insert(END , "Contact NO :\t\t\t" + contact.get() + "\n")
    txtprescription.insert(END , "ADDRESS :\t\t\t" + Address.get() + "\n")
    txtprescription.insert(END , "Father Name :\t\t\t" + fathername.get() + "\n")
    txtprescription.insert(END , "Doctor :\t\t\t" + dr.get() + "\n")             
                                
#================================================================ CLEAR ===============================================================================
def Clear():
    patient.delete(0,'end')
    nameoftablet.delete(0,'end')
    ref.delete(0,'end')
    dose.delete(0,'end')
    nooftablets.delete(0,'end')
    lot.delete(0,'end')
    issuedate.delete(0,'end')
    Expdate.delete(0,'end')
    dailydose.delete(0,'end')
    sideEffect.delete(0,'end')
    DOB.delete(0,'end')
    Furtherinfo.delete(0,'end')
    BloodPressure.delete(0,'end')
    storage.delete(0,'end')
    Medication.delete(0,'end')
    PatientID.delete(0,'end')
    contact.delete(0,'end')
    Address.delete(0,'end')
    fathername.delete(0,'end')
    dr.delete(0,'end')




#=================================================================== SHOW ================================================================================
def Show():
    global show
    show = Toplevel(root)
    show.title("Contents of Table")
    show.geometry("1000x700")
    show.configure(background="floral white")

    h=Scrollbar(show, orient='horizontal')
    h.pack(side=BOTTOM,fill=X)
    v = Scrollbar(show)
    v.pack(side = RIGHT, fill = Y)

    #frame=Frame(show)
    #frame.place(x=0 , y=20 , width=1536 , height=800)
    t = Text(show, width = 15, height = 15, wrap = NONE,xscrollcommand = h.set,yscrollcommand = v.set)
    
    #Defining Headings
    e=Label(t,width=15,text='Patient - Name',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=0)
    e=Label(t,width=15,text='Names of Tablet',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=1)
    e=Label(t,width=15,text='Refreance No',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=2)
    e=Label(t,width=15,text='Dose',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=3)
    e=Label(t,width=15,text='No Of Tablets',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=4)
    e=Label(t,width=15,text='Lot',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=5)
    e=Label(t,width=15,text='Issue - Date',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=6)
    e=Label(t,width=15,text='Expiry Date',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=7)
    e=Label(t,width=15,text='Daily - Dose',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=8)
    e=Label(t,width=15,text='Side - Effects',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=9)
    e=Label(t,width=15,text='D.O.B',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=10)
    e=Label(t,width=15,text='Further - Info',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=11)
    e=Label(t,width=15,text='Blood Pressure',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=12)
    e=Label(t,width=15,text='Storage Advice',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=13)
    e=Label(t,width=15,text='Medication',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=14)
    e=Label(t,width=15,text='Patient - ID',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=15)
    e=Label(t,width=15,text='Contact No',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=16)
    e=Label(t,width=15,text='Patient Address ',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=17)
    e=Label(t,width=15,text='Father name',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=18)
    e=Label(t,width=15,text='Docter - name',borderwidth=5, relief='raised',bg='DeepSkyBlue4',fg="white",font=("Arial",10))
    e.grid(row=0,column=19)


    #Establishing Connection
    my_connect = mysql.connector.connect(
      host="localhost",
      user="root", 
      passwd="",
      database="medical_system"
    )

    my_conn = my_connect.cursor()
    #To Print Table
    my_conn.execute("SELECT * FROM medical")
    i=1
    for element in my_conn: 
        for j in range(len(element)):
            e = Label(t,width=14,padx=5, text=element[j],borderwidth=5,relief='ridge',bg='grey86',fg="black",font=("Arial",10) ) 
            e.grid(row=i, column=j) 

        i=i+1

    t.pack(side=TOP, fill=X)

    h.config(command=t.xview)
    v.config(command=t.yview)
    
    show.mainloop()

class medical():

    conn=mysql.connector.connect(host="localhost" , username="root" , password="" , database="medical_system"  )
    my_cursor=conn.cursor()
    my_cursor.execute(" CREATE TABLE IF NOT EXISTS Medical (patient VARCHAR(225),nameoftablet VARCHAR(225),ref VARCHAR(225),dose VARCHAR(225),nooftablets VARCHAR(225),lot VARCHAR(225),issuedate VARCHAR(225),Expdate VARCHAR(225),dailydose VARCHAR(225),sideEffect VARCHAR(225),DOB VARCHAR(225),Furtherinfo VARCHAR(225),BloodPressure VARCHAR(225),storage VARCHAR(225),Medication VARCHAR(225),PatientID VARCHAR(225),contact VARCHAR(225),Address VARCHAR(225),fathername VARCHAR(225),dr VARCHAR(225))")
    global root
    root = Tk()
    root.title("Medical Management System")
    root.geometry("1200x700")
    global patient
    global nameoftablet
    global ref
    global dose
    global nooftablets
    global lot
    global issuedate
    global Expdate
    global dailydose
    global sideEffect
    global DOB
    global Furtherinfo
    global BloodPressure
    global storage
    global Medication
    global PatientID
    global contact
    global Address
    global fathername
    global dr

    patient=StringVar()
    nameoftablet=StringVar()
    ref=StringVar()
    dose=StringVar()
    nooftablets=StringVar()
    lot=StringVar()
    issuedate=StringVar()
    Expdate=StringVar()
    dailydose=StringVar()
    sideEffect=StringVar()
    DOB=StringVar()
    Furtherinfo=StringVar()
    BloodPressure=StringVar()
    storage=StringVar()
    Medication=StringVar()
    PatientID=StringVar()
    contact=StringVar()
    Address=StringVar()
    fathername=StringVar()
    dr=StringVar()

    
    lbltitle=Label(root , bd=30 , relief= RIDGE , text=" + MEDICAL MANAGEMENT SYSTEM" ,fg="white" , bg="red" ,
                   font=("times new roman" , 50 , "bold"))            
 
    lbltitle.pack(side=TOP , fill=X)                                
    
     
    
    # DATAFRAME  
                        
                        
    Dataframe=Frame(root , bd=20 , padx=15 , relief=RIDGE)   
    Dataframe.place(x=0 , y=135 , width=1536 , height=455)
     
    Dataframeleft=LabelFrame(Dataframe , bd=10 , relief=RIDGE , padx=10 ,
                            font=("times new roman" , 12 , "bold" ) , text=" PATIENT INFORMATION" , fg = "red" )
    
    Dataframeleft.place(x=0 ,y=5 , width=900 , height=400)
    
    DataframeRight=LabelFrame(Dataframe , bd=13 , relief=RIDGE , padx=25 , pady=4 ,
                            font=("times new roman" , 10 , "bold" ) , text=" PRESCRIPTION", fg = "red" )
    
    DataframeRight.place(x=910 , y=5 , width=560 , height=400)
    
    #BUTTONS-FRAME
    
    Buttonframe=Frame(root , bd=20 , relief=RIDGE , bg="gray")   
    Buttonframe.place(x=0 , y=590 , width=1536 , height=120)
    
    
    #=============================== DATAFRAME LEFT ====================================
    
    lblpatient=Label(Dataframeleft , text = "Patient - Name :" , font=("Arial" , 10 , "bold" ) , padx =2 , pady =7 )
    lblpatient.grid(row=0 , column=0 , sticky = W)
    patient = Entry(Dataframeleft , font=("arial", 10 , "bold") ,textvariable=patient , width=45)
    patient.grid(row=0 , column=1)
    
    

    lblnameoftablets=Label(Dataframeleft , text = "Names of Tablet :" , font=("Arial" , 10 , "bold" ) , padx =2 , pady =7 )
    lblnameoftablets.grid(row=1 , column=0 , sticky = W)
    nameoftablet = ttk.Combobox(Dataframeleft , textvariable=nameoftablet ,font = ("arial" , 10 , "bold" ) , width =43)
    
    #-----------> [comnametablet] = is create ComboBox...................
    #-----------> [ttk (module)] = is help to tkinter to cteate a ComboBox ...........
    
    nameoftablet['values']=("Corona Vacacine" , "Zestril" , "Lipitor" , "Zocor" , "Synthorid" , "Ventolin" , "Ativan")
                           #----------------->passing a tupple
    nameoftablet.grid(row=1 , column=1 )
    
    
    
    lblref=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Refreance No :" , padx =2 , pady =7 )
    lblref.grid(row=2 , column=0 , sticky = W)
    ref = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=ref , width=45)
    ref.grid(row=2 , column=1)
    
    
    
    lbldose=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Dose :" , padx =2 , pady =7 )
    lbldose.grid(row=3 , column=0 , sticky = W)
    dose = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=dose , width=45)
    dose.grid(row=3 , column=1)
    
    
    
    lblnooftablets=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "No Of Tablets :" , padx =2 , pady =7 )
    lblnooftablets.grid(row=4 , column=0 , sticky = W)
    nooftablets = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=nooftablets , width=45)
    nooftablets.grid(row=4 , column=1)
    
    
    
    lbllot=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Lot :" , padx =2 , pady =7 )
    lbllot.grid(row=5 , column=0 , sticky = W)
    lot = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=lot , width=45)
    lot.grid(row=5 , column=1)
    
    
    
    lblissuedate=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Issue - Date :" , padx =2 , pady =7 )
    lblissuedate.grid(row=6 , column=0 , sticky = W)
    issuedate = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=issuedate , width=45)
    issuedate.grid(row=6 , column=1)
    
    
    
    lblExpDate=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Expiry Date :" , padx =2 , pady =7 )
    lblExpDate.grid(row=7 , column=0 , sticky = W)
    Expdate = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=Expdate , width=45)
    Expdate.grid(row=7 , column=1)
    
    
    
    lbldailydose=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Daily - Dose :" , padx =2 , pady =7 )
    lbldailydose.grid(row=8 , column=0 , sticky = W)
    dailydose = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=dailydose , width=45)
    dailydose.grid(row=8 , column=1)
    
    
    
    lblsideEffects=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Side - Effects :" , padx =2 , pady =7 )
    lblsideEffects.grid(row=9 , column=0 , sticky = W)
    sideEffect = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=sideEffect , width=45)
    sideEffect.grid(row=9 , column=1)
    
    
    
    lblDOB=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "D.O.B :" , padx =2 , pady =7 )
    lblDOB.grid(row=0 , column=2 , sticky = W)
    DOB = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=DOB , width=43)
    DOB.grid(row=0 , column=3)
    
    
    
    lblfurtherinfo=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Further - Info :" , padx =2 , pady =7 )
    lblfurtherinfo.grid(row=1 , column=2 , sticky = W)
    Furtherinfo = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=Furtherinfo , width=43)
    Furtherinfo.grid(row=1 , column=3)
    
    
    
    lblBloodPressure=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Blood Pressure :" , padx =2 , pady =7 )
    lblBloodPressure.grid(row=2 , column=2 , sticky = W)
    BloodPressure = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=BloodPressure , width=43)
    BloodPressure.grid(row=2 , column=3)
    
    
    
    lblstorage=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Storage Advice :" , padx =2 , pady =7 )
    lblstorage.grid(row=3 , column=2 , sticky = W)
    storage = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=storage , width=43)
    storage.grid(row=3 , column=3)
    
    
    
    lblMedication=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Madication :" , padx =2 , pady =7 )
    lblMedication.grid(row=4 , column=2 , sticky = W)
    Medication = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=Medication , width=43)
    Medication.grid(row=4 , column=3)
    
    
    
    
    lblpatientID=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Patient - ID :" , padx =2 , pady =7 )
    lblpatientID.grid(row=5 , column=2 , sticky = W)
    PatientID = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=PatientID , width=43)
    PatientID.grid(row=5 , column=3)
    
    
    
    lblcontact=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Contact No :" , padx =2 , pady =7 )
    lblcontact.grid(row=6 , column=2 , sticky = W)
    contact = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=contact , width=43)
    contact.grid(row=6 , column=3)
    
    
    
    lblAddress=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Patient Address :" , padx =2 , pady =7 )
    lblAddress.grid(row=7 , column=2 , sticky = W)
    Address = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=Address , width=43)
    Address.grid(row=7 , column=3)
    
    
    
    lblfathername=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Father name :" , padx =2 , pady =7 )
    lblfathername.grid(row=8 , column=2 , sticky = W)
    fathername = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=fathername , width=43)
    fathername.grid(row=8 , column=3)
    
    
    
    lbldr=Label(Dataframeleft , font=("Arial" , 10 , "bold" ) , text = "Docter - name :" , padx =2 , pady =7 )
    lbldr.grid(row=9 , column=2 , sticky = W)
    dr = Entry(Dataframeleft , font=("arial", 10 , "bold") , textvariable=dr , width=43)
    dr.grid(row=9 , column=3)
    
    
    #===================================================  DATAFRAME RIGHT  =========================================================
    global txtprescription
    txtprescription = Text(DataframeRight , font=("Arial" , 10 , "bold" ) , width=69 , height=20 , padx =2 , pady=6)
    txtprescription.grid(row=0 , column=0)
    
    
    #====================================================     BUTTONS   ===========================================================
    
    btnprecriptionData=Button(Buttonframe ,command=submitfunc , text = "SUBMIT - DATA" , bg ="green yellow" , fg="black" , font=("times of roman" , 10 , "bold" ) , width=36, height=4 , padx =6 , pady=3) 
    btnprecriptionData.grid(row=0 , column=0)



    
    btnDelete=Button(Buttonframe ,command=Clear, text = " CLEAR - ENTRY " , bg ="orange red" , fg="black" , font=("Arial" , 10 , "bold" ) , width=36 , height=4 , padx =5 , pady=3) 
    btnDelete.grid(row=0 , column=1)
    
    btnShow=Button(Buttonframe ,command=Show, text = " SHOW - DATA " , bg ="DeepSkyBlue2" , fg="black" , font=("Arial" , 10 , "bold" ) , width=36 , height=4 , padx =6 , pady=3) 
    btnShow.grid(row=0 , column=2)
    
    btnclear=Button(Buttonframe ,command=iprectinoption, text = " PRICRIPTION " , bg ="yellow" , fg="black" , font=("Arial" , 10 , "bold" ) , width=69 , height=4 , padx =7 , pady=3) 
    btnclear.grid(row=0 , column=(3))
    


    root.mainloop()
        
# Rest of your code ...

medical()
