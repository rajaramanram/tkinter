from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import re
import sqlite3
import pandas as pd
import random,sys
from tkinter.ttk import Separator
from tkinter import filedialog
import xlwings as xw
from datetime import *
from datetime import datetime
from tkinter import ttk
from PIL import Image,ImageTk

def getqanda2(a):
    tv_item=tv4.item(tv4.selection())
    item=tv4.selection()[0]
    var=tv4.item(item)['values'][0]
    var2=tv4.item(item)['values'][3]
    make_cursor.execute("SELECT * FROM test WHERE Userid=? AND Test=?",[(var),(var2)])
    rows3=make_cursor.fetchall()
    window_q2= Toplevel(window)
    window_q2.geometry("1200x500")
    window_q2.title("CANDIDATE Q&A")
    window_q2.config(background='green')
    tv_q=ttk.Treeview(window_q2,columns=(1,2,3,4,5),show="headings")
    tv_q.pack()
    tv_q.heading(1,text="ID")
    tv_q.heading(2,text="Username")
    tv_q.heading(3,text="Test")
    tv_q.heading(4,text="Question")
    tv_q.heading(5,text="Answer")
    
    for y in rows3:
        tv_q.insert('','end',values=y)
    
def getqanda(a):
    tv_item=tv2.item(tv2.selection())
    item=tv2.selection()[0]
    var=tv2.item(item)['values'][1]
    var2=tv2.item(item)['values'][2]
    make_cursor.execute("SELECT * FROM test WHERE Userid=? AND Test=?",[(var),(var2)])
    rows3=make_cursor.fetchall()
    window_q= Toplevel(window)
    window_q.geometry("1200x500")
    window_q.title("CANDIDATE Q&A")
    window_q.config(background='green')
    tv3=ttk.Treeview(window_q,columns=(1,2,3,4,5),show="headings")
    tv3.pack()
    tv3.heading(1,text="ID")
    tv3.heading(2,text="Username")
    tv3.heading(3,text="Test")
    tv3.heading(4,text="Question")
    tv3.heading(5,text="Answer")
    
    for y in rows3:
        tv3.insert('','end',values=y)
def answer():
    global currentQ,currentA,ans,score
    a_nswer = var.get()
    #print(a_nswer)
    if currentA == str(a_nswer):
        score+=10
    User_namedb=auser_name.get()
    
    make_cursor.execute("""INSERT INTO test(Userid,Username,Test,Question,Answer)
                                VALUES(?,?,?,?,?)""",(get_id3,User_namedb,v_test.get(),currentQ,a_nswer))
    create_database.commit()
def create_table():
    global create_database,make_cursor
    create_database=sqlite3.connect("address_book.db")
    create_database.execute("PRAGMA foreign_keys = ON")
    make_cursor=create_database.cursor()
    make_cursor.execute("""CREATE TABLE IF NOT EXISTS forms(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    UserName text,
                    Password text,
                    Email text,
                    Gender text,
                    DOB text,
                    Address text,
                    Language text,
                    Field text)""")
    make_cursor.execute("CREATE TABLE IF NOT EXISTS test(Userid INTEGER FOREGIN KEY REFERENCES forms(ID),Username TEXT,Test TEXT,Question TEXT,Answer TEXT)")
    make_cursor.execute("CREATE TABLE IF NOT EXISTS answer(ID INTEGER PRIMARY KEY AUTOINCREMENT,Userid INTEGER FOREGIN KEY REFERENCES forms(ID),Test TEXT,Number_of_Question TEXT,Score TEXT)")
    make_cursor.execute("CREATE TABLE IF NOT EXISTS attempt(Username TEXT,Test TEXT,Counter INTEGER)")
    make_cursor.execute("CREATE TABLE IF NOT EXISTS get_que (Exam TEXT,Amount_of_Que INTEGER)")
    create_database.commit()
create_table()
def update_window():
    global user_update_name,check1,check2,check3
    global user_password
    global user_retype_password
    global user_email
    global v_gender
    global gender_get
    global entry_mode
    global user_address
    global user_language
    global v_language
    global v_check1
    global v_check2
    global v_check3,window_u
    window9.withdraw()
    window_u=Toplevel(window)
    window_u.geometry("600x600")
    window_u.title("UPDATE PROFILE WINDOW")
    window_u.config(background='light green')
    v_name =StringVar()
    v_password=StringVar()
    v_retype =StringVar()
    v_email=StringVar()
    v_gender=IntVar()
    v_dob=StringVar()
    v_address=StringVar()
    v_language=StringVar()
    v_check1=IntVar()
    v_check2 =IntVar()
    v_check3=IntVar()
    make_cursor.execute("SELECT * FROM 'forms' WHERE Username=?",[(auser_name.get())])
    get_field3=make_cursor.fetchall()
    create_database.commit()
    title_label = Label(window_u,text="UPDATE PROFILE",width =30,font=("Helvetica", 14, "bold italic"),background='light green')
    title_label.place(x=120,y=70)
    lb_fullname = Label(window_u,text="FullName",width =20,font=("arial",10,"bold"),background='light green')
    lb_fullname.place(x=45,y=130)
    user_update_name = Entry(window_u,textvariable = v_name,width=30)
    user_update_name.place(x=240,y=130)
    name_validate_call = window_u.register(name_validate)
    user_update_name.config(validate="key",validatecommand=(name_validate_call,'%P'))

    lb_password = Label(window_u,text="Password",width =20,font=("arial",10,"bold"),background='light green')
    lb_password.place(x=45,y=170)
    user_password = Entry(window_u,show ='*',textvariable = v_password,width=30)
    user_password.place(x=240,y=170)
    password_validate_call = window_u.register(password_validate)
    user_password.config(validate="focusout",validatecommand=(password_validate_call,'%P'))                 

    lb_retype_password = Label(window_u,text="Confirm Password",width =20,font=("arial",10,"bold"),background='light green')
    lb_retype_password.place(x=70,y=210)
    user_retype_password = Entry(window_u,show='*',textvariable = v_retype,width=30)
    user_retype_password.place(x=240,y=210)
    retype_validate_call = window_u.register(retype_validate)
    user_retype_password.config(validate="focusout",validatecommand=(retype_validate_call,'%P'))

    lb_email = Label(window_u,text="Email ID",width =20,font=("arial",10,"bold"),background='light green')
    lb_email.place(x=45,y=250)
    user_email = Entry(window_u,textvariable = v_email,width=30)
    user_email.place(x=240,y=250)
    email_validate_call = window_u.register(email_validate)
    user_email.config(validate="focusout",validatecommand=(email_validate_call,'%P'))

    lb_gender = Label(window_u,text="Gender",width =20,font=("arial",10,"bold"),background='light green')
    lb_gender.place(x=42,y=280)
    Radiobutton(window_u,text="Male",padx =5,variable=v_gender,value=1,background='light green').place(x=230,y=280)
    Radiobutton(window_u,text="Female",padx =20,variable=v_gender,value=2,background='light green').place(x=290,y=280)
    #gender_get=v_gender.get()
    lb_dob = Label(window_u,text="DOB MM/DD/YYYY",width =20,font=("arial",10,"bold"),background='light green')
    lb_dob.place(x=70,y=310)
    entry_mode=DateEntry(window_u,width=30,date_pattern='MM/dd/yyyy')
    entry_mode.place(x=240,y=310)


    lb_address = Label(window_u,text="Address",width =20,font=("arial",10,"bold"),background='light green')
    lb_address.place(x=45,y=340)
    user_address = Text(window_u,width=30,height=4)
    user_address.place(x=240,y=340)

    lb_language = Label(window_u,text="Language",width =20,font=("arial",10,"bold"),background='light green')
    lb_language.place(x=50,y=420)
    language_list=['Tamil','Urudu','Hindi','Telugu','Bengali','kannada','Malayalam']
    user_language = OptionMenu(window_u,v_language,*language_list)
    user_language.config(width=30,bg='light blue')
    v_language.set('Select Language')
    user_language.place(x=240,y=420)

    course_label = Label(window_u,text="Select Field",width =20,font=("arial",10,"bold"),background='light green')
    course_label.place(x=50,y=450)
    check1=Checkbutton(window_u,text='Python', onvalue = 1, offvalue = 0,variable=v_check1,background='light green')
    check1.place(x=240,y=450)
    check2=Checkbutton(window_u,text='Java',onvalue = 1, offvalue = 0,variable=v_check2,background='light green')
    check2.place(x=340,y=450)
    check3=Checkbutton(window_u,text='Javascript' ,onvalue = 1, offvalue = 0,variable=v_check3,background='light green')
    check3.place(x=440,y=450)
    entries = [child for child in window_u.winfo_children() if isinstance(child, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))
    for record3 in get_field3:
        user_update_name.insert(0,record3[1])
        user_password.insert(0,record3[2])
        user_retype_password.insert(0,record3[2])
        user_email.insert(0,record3[3])
        #user_dob.insert(0,record3[4])
        user_address.insert("1.0",record3[6])
        #user_address.insert(0,record3[6])
        #user_name.insert(0,record3[7])
    register_button = Button(window_u,text = "CLICK TO UPDATE",command=lambda:[update_profile(),window_u.withdraw(),main_window()],bg='red',fg='white').place(x=440,y=490)
    delete_button=register_button = Button(window_u,text = "CLEAR FIELDS",command=delete_fields,bg='red',fg='white').place(x=190,y=490)
    previous_button = Button(window_u,text = "< BACK",command=lambda:[window_u.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=490)
    window_u.mainloop()
def result_window():
    global tv4
    window_m=Toplevel(window)
    window_m.geometry("700x600")
    window_m.config(bg="blue")
    window_m.title("RESUT-WINDOW")
    make_cursor.execute("SELECT Test,Number_of_Question,Score FROM answer WHERE Userid=?",[get_id3])
    rows3=make_cursor.fetchall()
    tv4=ttk.Treeview(window_m,columns=(1,2,3,),show="headings",height="3")
    tv4.pack(pady=10,padx=10)
    #tv4.heading(1,text="Username")
    tv4.heading(1,text="Test")
    tv4.heading(2,text="Number of Question")
    tv4.heading(3,text="Score")
    for y in rows3:
        tv4.insert('','end',values=y)
    logout_button = Button(window_m,text = "LOG-OUT",width=30,command=lambda:[window_m.withdraw(),main_window()],bg='red',fg='white')
    logout_button.place(x=400,y=450)
    previous5_button = Button(window_m,text = "< BACK",command=lambda:[window_m.withdraw(),test_select()],bg='orange',fg='white').place(x=40,y=450)
    window_m.mainloop()
def test_select():
    global window9,get_table,test_name,v_test,user_test,get_id3
    window4.withdraw()
    window9=Toplevel(window)
    window9.geometry("700x600")
    window9.config(bg='PeachPuff')
    window9.title("TEST WINDOW")
    lab_auser = Label(window9,text="WELCOME"+'  '+auser_name.get(),width =60,font=("arial",14,"bold"),bg='red')
    #lab_auser.grid(row=10,column=0,columnspan=2,pady=10,padx=0)
    lab_auser.place(x=0,y=60)
    make_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    get_table=make_cursor.fetchall()
    #print(get_table)
    create_database.commit()
    #create_database4.close()
    if len(get_table)==0:
        no_test = Label(window9,text="NO TEST UPLOADED",width =50,font=("arial",14,"bold"),bg='Green')
        no_test.place(x=40,y=250)
    else:
        make_cursor.execute("SELECT ID FROM forms WHERE UserName=? AND Password=?",[(auser_name.get()),(auser_password.get())])
        get_id=make_cursor.fetchone()
        get_id3=0
        for i in get_id:
            get_id3+=i
        make_cursor.execute("SELECT Field FROM 'forms' WHERE ID=?",[get_id3])
        get_field=make_cursor.fetchone()
        get_field3=""
        for i in get_field:
            get_field3+=i
        get_field2=get_field3.split(",")
        print(get_field2)
        create_database.commit()
        v_test=StringVar()
        select_button2=Label(window9,text="Select Test",width=20,bg='PeachPuff',font=("Helvetica", 13, "bold italic"))
        select_button2.place(x=50,y=170)
        test_name=[]
        make_cursor.execute("SELECT EXISTS(SELECT * FROM answer WHERE Userid=?)",[get_id3])
        get_result=make_cursor.fetchone()
        for i in get_result:
            pass
        if i==1:
             show_button = Button(window9,width=10,text = "TEST RESULT",command=lambda:[window9.withdraw(),result_window()],bg='green',fg='white')
             show_button.place(x=540,y=450)
        for i in get_table:
            for y in i:
                test_name.append(y)
        print(test_name)
        for z in get_field2:
            if z in test_name:
                user_test = OptionMenu(window9,v_test,*get_field2)
                user_test.config(width=35,bg='light blue')
                v_test.set('Select Test')
                user_test.place(x=220,y=160)
                button_upload2=Button(window9,text="SUBMIT",width=15,command=lambda:[window9.withdraw(),quiz()],font=("Helvetica", 10, "bold italic"),bg='light blue')
                button_upload2.place(x=520,y=160)
            else:
                no_test = Label(window9,text="NO TEST UPLOADED",width =50,font=("arial",14,"bold"),bg='Green')
                no_test.place(x=40,y=350)
            break
            
    update_button = Button(window9,text = "UPDATE PROFILE",command=lambda:[window9.withdraw(),update_window()],bg='blue',fg='white').place(x=240,y=450)
    logout_button = Button(window9,text = "LOG-OUT",width=80,command=lambda:[window9.withdraw(),main_window()],bg='red',fg='white')
    logout_button.place(x=80,y=550)
    previous5_button = Button(window9,text = "< BACK",command=lambda:[window9.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=450)
    window9.mainloop()
    
def database_user():
    global questions,options,qn,currentA,que,ans,score,currentQ,queNo,get_amount
    make_cursor.execute("SELECT Amount_of_Que FROM get_que WHERE Exam=?",[v_test.get()])
    getQ=make_cursor.fetchone()
    get_amount=0
    for i in getQ:
        get_amount+=i
    print(get_amount)
    
    make_cursor.execute(f"SELECT * FROM {v_test.get()} order by RANDOM() LIMIT {get_amount}")
    questionQ=make_cursor.fetchall()
    questions={}
    que=[]
    ans=[]
    options=[]
    print_record=[]
    for i in questionQ:
        print_record+=i
        questions[print_record[1]]=print_record[6]
        que.append(print_record[1])
        ans.append(print_record[6])
        options.append([print_record[2],print_record[3],print_record[4],print_record[5]])
        print_record=[]
    create_database.commit()
    #create_database2.close()
    qn=1
    score=0
    
    
    
def upload_submit():
    global active_sheet_name
    wb = xw.Book(file_search)
    active_sheet_name = wb.sheets.active.name
    #print(active_sheet_name)
    get_excel=pd.read_excel(file_search,sheet_name=active_sheet_name)
    get_excel.head()
    make_cursor.execute(f"""CREATE TABLE IF NOT EXISTS {active_sheet_name}(
                        serialno INTEGER,
                        Question TEXT,
                        Option1 TEXT,
                        Option2 TEXT,
                        Option3 TEXT,
                        Option4 TEXT,
                        Answer TEXT)""")
    for i in range(0,len(get_excel)):
        serial_no=get_excel.iloc[i,0]
        Q_uestion=get_excel.iloc[i,1]
        O_ption1=get_excel.iloc[i,2]
        O_ption2=get_excel.iloc[i,3]
        O_ption3=get_excel.iloc[i,4]
        O_ption4=get_excel.iloc[i,5]
        A_nswer=get_excel.iloc[i,6]
        get_query=make_cursor.execute(f"""INSERT INTO {active_sheet_name} (serialno,Question,Option1,Option2,Option3,Option4,Answer)
                               VALUES(?,?,?,?,?,?,?)""",(serial_no,Q_uestion,O_ption1,O_ption2,O_ption3,O_ption4,A_nswer))
    make_cursor.execute(f"SELECT * , oid FROM {active_sheet_name}")
    records2=make_cursor.fetchall()
    print_record2 = ''
    for record2 in records2:
        print_record2 +=str(record2)+"\n"
   
    make_cursor.execute("INSERT INTO get_que(Exam,Amount_of_Que)VALUES(?,?)",(active_sheet_name,allocate_question.get()))
    create_database.commit()
    upload_entry=Label(window8,text="File Uploaded",width=60,font=("Helvetica", 10, "bold italic"),bg='red')
    upload_entry.place(x=100,y=330)

   
def _next():
    global currentQ,queNo,qn,i,currentA,score
    currentA=''
    currentQ =''
    queNo=None
    i=0
   
    if len(que)>0:
        currentQ = random.choice(que)
        currentA = questions[currentQ]
        q = Label(window5,text='Que. '+str(qn),font=('arial',10)).place(x=20,y=80)
        qn+=1
        queNo = que.index(currentQ) 
        queLabel.config(text=currentQ,fg='green',height=6)
        option1.config(text=options[queNo][0],bg='sky blue',value=options[queNo][0],bd=1,command=answer)
        option2.config(text=options[queNo][1],bg='sky blue',value=options[queNo][1],bd=1,command=answer)
        option3.config(text=options[queNo][2],bg='sky blue',value=options[queNo][2],bd=1,command=answer)
        option4.config(text=options[queNo][3],bg='sky blue',value=options[queNo][3],bd=1,command=answer)
        que.remove(currentQ)
        ans.remove(currentA)
        options.remove(options[queNo])
    elif len(que)==0:
        messagebox.showinfo("Test Over",message='Your Score in Test: '+str(score))
        User_namedb=auser_name.get()
        score_db=str(score)
        make_cursor.execute("SELECT Email FROM 'forms' WHERE Username=? AND Password=?",[(auser_name.get()),(auser_password.get())])
        get_email=make_cursor.fetchone()
        get_email3=""
        for i in get_email:
            get_email3+=str(i)
        #get_email2=get_field3.split(",")
        make_cursor.execute("SELECT ID FROM forms WHERE UserName=? AND Password=?",[(auser_name.get()),(auser_password.get())])
        get_id=make_cursor.fetchone()
        get_id3=0
        for i in get_id:
            get_id3+=i
        
        make_cursor.execute("INSERT INTO answer(Userid,Test,Number_of_Question,Score)VALUES(?,?,?,?)",(get_id3,v_test.get(),get_amount,score_db))
        create_database.commit()
        window5.withdraw()
        window9.withdraw()
        test_select()
def deleterecord():
    make_cursor.execute("DELETE from 'forms' WHERE oid= "+entry_delete.get())
    create_database.commit()
def test_counter():
    global window5,queLabel,var,option1,option2,option3,option4,submit
    #print(v_test.get())
    var=StringVar()
    window4.withdraw()
    window5=Toplevel(window)
    window5.geometry("700x600")
    window5.config(bg='PeachPuff')
    window5.title("TEST WINDOW")
    #lab_auser = Label(window5,text="WELCOME"+' '+auser_name.get(),width =50,font=("arial",14,"bold"),bg='red')
    #lab_auser.place(x=0,y=70)
    appName = Label(window5,text=v_test.get()+' '+"QUIZ TEST",font=('impact',20,'italic'),justify=CENTER,bg='goldenrod2',fg='white')
    appName.pack(side=TOP,fill=BOTH)    
    queLabel = Label(window5,text='',justify=LEFT,font=25)
    queLabel.pack(side=TOP,fill=BOTH)
    if v_test.get()=="Python":
        image=Image.open("Python.jpeg")
        photo=ImageTk.PhotoImage(image)
        label=Label(window5,image=photo)
        label.place(x=0,y=250)
    elif v_test.get()=="Java":
        image=Image.open("th.jpeg")
        photo=ImageTk.PhotoImage(image)
        label=Label(window5,image=photo)
        label.place(x=0,y=250)
    elif v_test.get()=="Javascript":
        image=Image.open("Javascript.jpeg")
        photo=ImageTk.PhotoImage(image)
        label=Label(window5,image=photo)
        label.place(x=0,y=250)
    else:
        pass
    
    s = Separator(window5).place(x=0,y=195)
    option1=Radiobutton(window5,text='',font=20,width=20,relief=FLAT,indicator=0,value=1,variable = var)
    option1.place(x=150,y=250)
    option2=Radiobutton(window5,text='',font=20,width=20,relief=FLAT,indicator=0,value=2,variable = var,bd=0)
    option2.place(x=400,y=250)
    option3=Radiobutton(window5,text='',font=20,width=20,relief=FLAT,indicator=0,value=3,variable = var,bd=0)
    option3.place(x=150,y=300)
    option4=Radiobutton(window5,text='',font=20,width=20,relief=FLAT,indicator=0,value=4,variable = var,bd=0)
    option4.place(x=400,y=300)
    database_user()
    submit = Button(window5,text='NEXT',bg='blue',fg='white',width=20,font=('impact',10),command=_next)
    submit.place(x=470,y=450)
    label_note = Label(window5,text="NOTE:Press NEXT to STAT QUIZ and NEXT QUESTION",font=("arial",10,"bold"),bg='red')
    label_note.place(x=10,y=550)
    previous5_button = Button(window5,text = "< BACK",command=lambda:[window5.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=450)
    window5.mainloop()
def quiz(): 
    make_cursor.execute("SELECT *FROM attempt WHERE Username=? AND Test=?",[(auser_name.get()),(v_test.get())])
    correct_attempt = make_cursor.fetchall()
    if correct_attempt:
        make_cursor.execute("SELECT Counter FROM attempt WHERE Username=? AND Test=?",[(auser_name.get()),(v_test.get())])
        records_counter=make_cursor.fetchone()
        #print(records_counter)
        print_counter = 0
        for record in records_counter:
            print_counter+=record   
        print(print_counter)
        if print_counter==3:
            messagebox.showinfo("Information","you attend the maximum attempts in given Test")
            window9.destroy()
            create_database.commit()
            
        else:
            print_counter+=1
            make_cursor.execute("UPDATE attempt SET Counter=? WHERE Username=? AND Test=?",(print_counter,auser_name.get(),v_test.get()))
            test_counter()
            create_database.commit()
            
    else:
        make_cursor.execute("INSERT INTO attempt(Username,Test,Counter)VALUES(?,?,?)",(auser_name.get(),v_test.get(),1))
        test_counter()
        create_database.commit()
    create_database.commit()
    #create_database_attempt.close()
def find_user():
    global window5
    if auser_name.get() == "":
        messagebox.showinfo("Information","Enter Name")
    elif auser_password.get()== "":
        messagebox.showinfo("Information","Enter Password")
    else:   
        
        make_cursor.execute("SELECT *FROM 'forms' WHERE Username=? AND Password=?",[(auser_name.get()),(auser_password.get())])
        correct = make_cursor.fetchall()
        if correct:
            test_select()
            
        else:
            data_form()
            #messagebox.showwarning("Warning","your are not a user")
        create_database.commit()
    
def already_user():
    global auser_name
    global auser_password,window4
    window.withdraw()
    window4=Toplevel(window)
    window4.geometry("300x300")
    window4.config(bg='Moccasin')
    window4.title("LOGIN WINDOW")
    auser_name =StringVar()
    auser_password=StringVar()
    title_auser = Label(window4,text="LOGIN PAGE",width =30,font=("arial",14,"bold"),bg='Moccasin')
    title_auser.place(x=0,y=70)

    label_aname = Label(window4,text="FullName",width =20,font=("arial",10,"bold"),bg='Moccasin')
    label_aname.place(x=10,y=130)
    auser_name = Entry(window4,textvariable = auser_name)
    auser_name.place(x=140,y=130)
    auser_validate_call = window4.register(name_validate)
    auser_name.config(validate="key",validatecommand=(auser_validate_call,'%P'))
    auser_name.bind('<Return>', lambda e: auser_password.focus_set())

    label_apassword = Label(window4,text="Password",width =20,font=("arial",10,"bold"),bg='Moccasin')
    label_apassword.place(x=10,y=170)
    auser_password = Entry(window4,show ='*',textvariable = auser_password)
    auser_password.place(x=140,y=170)
    alogin_button = Button(window4,text = "LOGIN",command=find_user,bg='blue',fg='white').place(x=250,y=210)
    previous4_button = Button(window4,text = "< BACK",command=lambda:[window4.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=210)
    window4.mainloop()
def showrecord():
    global tv2,tv4
    window = Toplevel(window3)
    window.geometry("1200x500")
    window.title("RECORD WINDOW")
    window.config(background='orange')
    '''make_cursor.execute("select * from forms")
    get_columns= [member[0] for member in make_cursor.description]
    #print(get_columns)
    rows=make_cursor.fetchall()
    
    tv=ttk.Treeview(window,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="3")
    tv.pack()
    #for i in range(1,len(get_columns)+1):
    #   tv.heading(i,text=get_columns[i-1])
    tv.column(1,width=100)
    tv.column(3,width=100)
    tv.column(5,width=100)
    tv.column(6,width=100)
    tv.heading(1,text="ID")
    tv.heading(2,text="Username")
    tv.heading(3,text="Password")
    tv.heading(4,text="Email")
    tv.heading(5,text="Gender")
    tv.heading(6,text="DOB")
    tv.heading(7,text="Address")
    tv.heading(8,text="Language")
    tv.heading(9,text="Field")
    for y in rows:
        tv.insert('','end',values=y)
    make_cursor.execute("select * from answer")
    rows2=make_cursor.fetchall()
    tv2=ttk.Treeview(window,columns=(1,2,3,4,5),show="headings",height="3")
    tv2.pack(pady=10,padx=10)
    #for i in range(1,len(get_columns)+1):
    #   tv.heading(i,text=get_columns[i-1])
    tv2.heading(1,text="ID")
    tv2.heading(2,text="Userid")
    tv2.heading(3,text="Test")
    tv2.heading(4,text="Number of Question")
    tv2.heading(5,text="Score")
    tv2.bind('<ButtonRelease-1>',getqanda)
    for y in rows2:
        tv2.insert('','end',values=y)'''
    make_cursor.execute("SELECT forms.ID,UserName,Email,Test,Number_of_Question,Score FROM forms,answer WHERE forms.ID=answer.Userid")
    rows3=make_cursor.fetchall()
    tv4=ttk.Treeview(window,columns=(1,2,3,4,5,6),show="headings",height="3")
    tv4.pack(pady=10,padx=10)
    tv4.heading(1,text="ID")
    tv4.heading(2,text="Username")
    tv4.heading(3,text="Emailid")
    tv4.heading(4,text="Test")
    tv4.heading(5,text="Number of Question")
    tv4.heading(6,text="Score")
    tv4.bind('<ButtonRelease-1>',getqanda2)
    for y in rows3:
        tv4.insert('','end',values=y)
def previous_admin():
    window8.withdraw()
    data_form()
def select_file():
    v_question=IntVar()
    global file_search,allocate_question
    file_search=filedialog.askopenfilename(parent=window8,initialdir="/",title="select files",filetypes=(("Excel Files", "*.xlsx"), ("all files", "*.*")))    
    #print(file_search)
    file_label=Label(window8,text=str(file_search),width =30,font=("Helvetica", 14, "bold italic"),background='blue')
    file_label.place(x=50,y=60)
    question_no = Label(window8,text="Question Allocate",width =20,font=("arial",10,"bold"),background='light green')
    question_no.place(x=45,y=130)
    allocate_question = Entry(window8,textvariable = v_question,width=30)
    allocate_question.place(x=240,y=130)
    
def upload_test():
    global window8,select_variable,button_var,button_upload
    button_var=StringVar()
    select_variable=StringVar()
    window3.withdraw()
    window8=Toplevel(window)
    window8.geometry("700x500")
    window8.config(bg='Green')
    window8.title("UPLOAD BOX")
    select_button=Button(window8,text="Select File",width=10,command=select_file,font=("Helvetica", 10, "bold italic"),bg='yellow')
    select_button.place(x=430,y=60)
    button_upload=Button(window8,text="SUBMIT",width=15,command=upload_submit,font=("Helvetica", 10, "bold italic"),bg='light blue')
    button_upload.place(x=520,y=60)
    previous_button = Button(window8,text='< BACK',bg='blue',width=25,font=('impact',12),command=previous_admin)
    previous_button.place(x=430,y=420)
    logout_button = Button(window8,text = "LOGOUT",command=lambda:[window8.withdraw(),main_window()],bg='red',fg='white').place(x=40,y=420)
    window8.mainloop()
def show_result2():
    make_cursor.execute("select * from answer")
    rows2=make_cursor.fetchall()
    window_r = Toplevel(window3)
    window_r.geometry("900x500")
    window_r.title("RESULT WINDOW")
    window_r.config(background='blue')
    tv2=ttk.Treeview(window_r,columns=(1,2,3,4),show="headings",height="2")
    tv2.pack()
    '''for i in range(1,len(get_columns)+1):
        tv.heading(i,text=get_columns[i-1])'''
    tv2.heading(1,text="Username")
    tv2.heading(2,text="Email")
    tv2.heading(3,text="Test")
    tv2.heading(4,text="Score")
    for y in rows2:
        tv2.insert('','end',values=y)

    
def data_form():
    global window3
    global entry_delete
    window4.withdraw()
    window3=Toplevel(window)
    window3.geometry("600x600")
    window3.config(bg='PeachPuff')
    window3.title("CANDIDATES DATA")
    button_record = Button(window3,text="SHOW RECORDS",command=showrecord,bg='blue',fg='white')
    button_record.grid(row=2,column=0,columnspan=2,pady=10,padx=10,ipadx=240)
    id_label=Label(window3,text="Delete ID",font=("arial",10,"bold"),bg='PeachPuff')
    id_label.grid(row=4,column=0)
    entry_delete=Entry(window3,width=20)
    entry_delete.grid(row=4,column=1)
    delete_record = Button(window3,text="DELETE RECORDS",command=deleterecord,bg='red',fg='white')
    delete_record.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=240)
    upload_record = Button(window3,text="UPLOAD TEST",command=upload_test,bg='orange',fg='white')
    upload_record.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=250)
    show_result = Button(window3,text="SHOW TEST RESULT",command=show_result2,bg='green',fg='white')
    show_result.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=240)
    previous3_button = Button(window3,text = "< BACK",command=lambda:[window3.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=550)
    window3.mainloop()

 
def admin():
    global admin_name
    global admin_password,window2
    window.withdraw()
    window2=Toplevel(window)
    window2.geometry("300x300")
    window2.config(bg='Moccasin')
    window2.title("ADMIN WINDOW")
    a_name =StringVar()
    a_password=StringVar()
    title_admin = Label(window2,text="ADMIN PAGE",width =30,font=("arial",14,"bold"),bg='Moccasin')
    title_admin.place(x=0,y=70)

    label_fullname = Label(window2,text="FullName",width =20,font=("arial",10,"bold"),bg='Moccasin')
    label_fullname.place(x=10,y=130)
    admin_name = Entry(window2,textvariable = a_name)
    admin_name.place(x=140,y=130)
    admin_validate_call = window2.register(name_validate)
    admin_name.config(validate="key",validatecommand=(admin_validate_call,'%P'))
    admin_name.bind('<Return>', lambda e: admin_password.focus_set())

    label_password = Label(window2,text="Password",width =20,font=("arial",10,"bold"),bg='Moccasin')
    label_password.place(x=10,y=170)
    admin_password = Entry(window2,show ='*',textvariable = a_password)
    admin_password.place(x=140,y=170)
    login_button = Button(window2,text = "LOGIN",command=validate_admin,bg='blue',fg='white').place(x=260,y=210)
    previous2_button = Button(window2,text = "< BACK",command=lambda:[window2.withdraw(),main_window()],bg='orange',fg='white').place(x=40,y=210)
    window2.mainloop()
def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()
def name_validate(name):
    name_regex=re.compile(r'[@!#$%^&*()_<>?}{~:/\0-9]')
    if (name_regex.search(name) == None):
        return True
    else:
        messagebox.showinfo("Information","Don't use numbers and special charecters in Username")
        return False
        
def password_validate(user_password):
    password_regex = re.compile('^(?=.*[!$?@#%^&*])(?=.*[a-z])(?=.*[0-9]).{8}$')
    if (password_regex.search(user_password)!=None):
        return True
    else:
        messagebox.showinfo("Information","YourPassword must contain atleast one number,one specialcharcter,length with 8 ")
        return False
def retype_validate(retype_password):
    if retype_password== user_password.get():
        return True
    else:
        messagebox.showinfo("Information","Type same password in re_type password")
        return False
    
def email_validate(user_email):
    if re.match("[^@]+@[^@]+\.[^@]+",user_email):
        return True
    else:
        messagebox.showinfo("Information","Enter valid Email id")
        return False
def dob_validate(user_dob):
    if re.match(r"^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$",user_dob):
        return True
    else:
        messagebox.showinfo("Information","Enter DOB in Correct Format")
        return False
def get_gender():
    global gender,gender_get,get_course
    global course_label
    gender_get=v_gender.get()
    get_course=[]
    if gender_get == 1:
        gender = "Male"
    else:
        gender ="Female"
    course_get = v_check1.get()
    course2_get = v_check2.get()
    course3_get = v_check3.get()
    if course_get == 1:
        course_get="Python"
        get_course.append(course_get)

    if course2_get == 1:
        course2_get="Java"
        get_course.append(course2_get)   
    if course3_get == 1:
        course3_get="Javascript"
        get_course.append(course3_get)
    else:
        course3_get =''
    #course_label= course_get+','+ course2_get+','+ course3_get
    total=",".join(get_course)
        
    course_label=str(total)
def validate_form():
    get_today = date.today()
    get_today3=get_today.strftime("%Y")
    time_in_datetime = datetime.strptime(entry_mode.get(), "%m/%d/%Y").date()
    get_dob=time_in_datetime.strftime("%Y")
    get_age=int(get_today3)-int(get_dob)
    make_cursor.execute("SELECT *FROM 'forms' WHERE Username=? AND Password=?",[(user_name.get()),(user_password.get())])
    correct_p = make_cursor.fetchall()
    make_cursor.execute("SELECT Email From 'forms' WHERE Email=?",[(user_email.get())])
    correct_e = make_cursor.fetchall()
    if user_name.get() == "":
        messagebox.showinfo("Information","Enter Name")
    elif user_password.get()== "":
        messagebox.showinfo("Information","Enter Password")
    elif user_retype_password.get() == "":
        messagebox.showinfo("Information","Enter Confirm Password")
    elif user_email.get() == "":
        messagebox.showinfo("Information","Enter Email ID")
    elif correct_p:
        messagebox.showinfo("Information","Enter Different Password,Given Password Already Entered")
    elif correct_e:
        messagebox.showinfo("Information","Enter Different Email,Given Email Already Entered")
        
    elif v_gender.get == 0:
        messagebox.showinfo("Information","Enter Gender")
    elif get_age>60:
        messagebox.showinfo("Information","Minimum Age To register should be 60")
        window6.withdraw()
        main_window()
    elif len(user_address.get("1.0",'end-1c'))==0:
        messagebox.showinfo("Information","Enter address")
        
    
    elif v_check1.get()== 0 and v_check2.get()==0 and v_check3.get()==0:
        messagebox.showinfo("Information","Enter Course Fields")
        
    
    else:
        #print(user_language.get())
        print(v_language.get())
        get_gender()
        answer_question=messagebox.askyesno(title='Information', message="Are Those Inputs Correct ? "
                            '\n' 'Username: %s \n Password: %s \n Email ID: %s \n Gender:%s\n DOB: %s \n Address: %s \n Language: %s \n Field:%s'%
                            (user_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),user_address.get("1.0",'end-1c'),
                            v_language.get(),course_label))
        if answer_question:
            get_gender()
            '''make_cursor.execute("INSERT INTO forms VALUES(:username, :password, :email, :gender, :dob, :address, :language, :field)",
                                {
                                    'UserName':user_name.get(),
                                    'Password':user_password.get(),
                                    'Email':user_email.get(),
                                    'Gender':gender,
                                    'DOB':entry_mode.get(),
                                    'Address':user_address.get("1.0",'end-1c'),
                                    'Language':v_language.get(),
                                    'Field' : course_label
                                })
            make_cursor.execute("""INSERT INTO 'forms'(Username,Password,Email,Gender,DOB,Address,Language,Field)
                        VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"""
                        %(user_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),
                          user_address.get("1.0",'end-1c'),v_language.get(), course_label))'''
            make_cursor.execute("""INSERT INTO 'forms' (Username,Password,Email,Gender,DOB,Address,Language,Field)
                        VALUES(?,?,?,?,?,?,?,?)""",(user_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),
                          user_address.get("1.0",'end-1c'),v_language.get(), course_label))
            create_database.commit()
            
            window6.withdraw()
            already_user()
def update_profile():
    get_gender()
    #create_database7 = sqlite3.connect("address_book.db")
    #make_cursor7 = create_database7.cursor()
    #user_name_update=auser_name.get()
    '''make_cursor7.execute("""UPDATE 'forms' SET Username,Password,Email,Gender,DOB,Address,Language,Field
                ('%s','%s','%s','%s','%s','%s','%s','%s')WHERE Username=?""",[(auser_name.get())]%(user_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),
                user_address.get("1.0",'end-1c'),v_language.get(), course_label))'''
    #make_cursor7.execute(f"UPDATE forms SET Field={course_label} WHERE Username={user_name_update}")
    #make_cursor7.execute("UPDATE forms SET Field=? WHERE Username=?",(course_label,user_name_update))
    make_cursor.execute("""UPDATE 'forms' SET Username=?,Password=?,Email=?,Gender=?,DOB=?,Address=?,Language=?,Field=?
                WHERE Username=?""",(user_update_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),
                user_address.get("1.0",'end-1c'),v_language.get(), course_label,auser_name.get()))
    create_database.commit()
    #create_database7.close()
   
    #get_field3=make_cursor6.fectall()



def register_form():
    global user_name,check1,check2,check3
    global user_password
    global user_retype_password
    global user_email
    global v_gender
    global gender_get
    global entry_mode
    global user_address
    global user_language
    global v_language
    global v_check1
    global v_check2
    global v_check3,window6
    window6=Toplevel(window)
    window6.geometry("600x600")
    window6.title("Registration Form")
    window6.config(background='light green')
    v_name =StringVar()
    v_password=StringVar()
    v_retype =StringVar()
    v_email=StringVar()
    v_gender=IntVar()
    v_dob=StringVar()
    v_address=StringVar()
    v_language=StringVar()
    v_check1=IntVar()
    v_check2 =IntVar()
    v_check3=IntVar()

    #label widget implements a display box to place text
    title_label = Label(window6,text="Candidate Registration Form",width =30,font=("Helvetica", 14, "bold italic"),background='light green')
    title_label.place(x=120,y=70)

    lb_fullname = Label(window6,text="FullName",width =20,font=("arial",10,"bold"),background='light green')
    lb_fullname.place(x=45,y=130)
    user_name = Entry(window6,textvariable = v_name,width=30)
    user_name.place(x=240,y=130)
    #register callback function
    name_validate_call = window6.register(name_validate)
    #pass option value to callback function -validate(when to validate),validatecommand(what function),invalidcommand(optional)
    # %p is an %specifier this is used to pass input to callback function
    user_name.config(validate="key",validatecommand=(name_validate_call,'%P'))
    #user_name.bind('<Return>', lambda e: user_password.focus_set())

    lb_password = Label(window6,text="Password",width =20,font=("arial",10,"bold"),background='light green')
    lb_password.place(x=45,y=170)
    user_password = Entry(window6,show ='*',textvariable = v_password,width=30)
    user_password.place(x=240,y=170)
    password_validate_call = window6.register(password_validate)
    user_password.config(validate="focusout",validatecommand=(password_validate_call,'%P'))                 

    lb_retype_password = Label(window6,text="Confirm Password",width =20,font=("arial",10,"bold"),background='light green')
    lb_retype_password.place(x=70,y=210)
    user_retype_password = Entry(window6,show='*',textvariable = v_retype,width=30)
    user_retype_password.place(x=240,y=210)
    retype_validate_call = window6.register(retype_validate)
    user_retype_password.config(validate="focusout",validatecommand=(retype_validate_call,'%P'))

    lb_email = Label(window6,text="Email ID",width =20,font=("arial",10,"bold"),background='light green')
    lb_email.place(x=45,y=250)
    user_email = Entry(window6,textvariable = v_email,width=30)
    user_email.place(x=240,y=250)
    email_validate_call = window6.register(email_validate)
    user_email.config(validate="focusout",validatecommand=(email_validate_call,'%P'))

    lb_gender = Label(window6,text="Gender",width =20,font=("arial",10,"bold"),background='light green')
    lb_gender.place(x=42,y=280)
    Radiobutton(window6,text="Male",padx =5,variable=v_gender,value=1,background='light green').place(x=230,y=280)
    Radiobutton(window6,text="Female",padx =20,variable=v_gender,value=2,background='light green').place(x=290,y=280)
    #gender_get=v_gender.get()
    lb_dob = Label(window6,text="DOB YYYY/DD/MM",width =20,font=("arial",10,"bold"),background='light green')
    lb_dob.place(x=70,y=310)
    entry_mode=DateEntry(window6,width=30,date_pattern='MM/dd/yyyy')
    entry_mode.place(x=240,y=310)


    lb_address = Label(window6,text="Address",width =20,font=("arial",10,"bold"),background='light green')
    lb_address.place(x=45,y=340)
    user_address = Text(window6,width=30,height=4)
    user_address.place(x=240,y=340)

    lb_language = Label(window6,text="Language",width =20,font=("arial",10,"bold"),background='light green')
    lb_language.place(x=50,y=420)
    language_list=['Tamil','Urudu','Hindi','Telugu','Bengali','kannada','Malayalam']
    user_language = OptionMenu(window6,v_language,*language_list)
    user_language.config(width=30,bg='light blue')
    v_language.set('Select Language')
    user_language.place(x=240,y=420)

    course_label = Label(window6,text="Select Field",width =20,font=("arial",10,"bold"),background='light green')
    course_label.place(x=50,y=450)
    check1=Checkbutton(window6,text='Python', onvalue = 1, offvalue = 0,variable=v_check1,background='light green')
    check1.place(x=240,y=450)
    check2=Checkbutton(window6,text='Java',onvalue = 1, offvalue = 0,variable=v_check2,background='light green')
    check2.place(x=340,y=450)
    check3=Checkbutton(window6,text='Javascript' ,onvalue = 1, offvalue = 0,variable=v_check3,background='light green')
    check3.place(x=440,y=450)
    entries = [child for child in window6.winfo_children() if isinstance(child, Entry)]
    for idx, entry in enumerate(entries):
        entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))
    register_button = Button(window6,text = "CLICK TO SUBMIT",command=validate_form,bg='red',fg='white').place(x=440,y=490)
    delete_button=register_button = Button(window6,text = "CLEAR FIELDS",command=delete_fields,bg='red',fg='white').place(x=190,y=490)
    previous_button = Button(window6,text = "< BACK",command=lambda:[window6.destroy(),main_window()],bg='orange',fg='white').place(x=40,y=490)
    window6.mainloop()
def delete_fields():
    user_name.delete(0,END)
    user_password.delete(0,END)
    user_retype_password.delete(0,END)
    user_email.delete(0,END)
    entry_mode.delete(0,END)
    user_address.delete('1.0',END)
    #user_language.delete(0,END)
    
def main_window():
    #use Tk class for creating  main window
    global window,register_button,admin_button,user_button
    window = Tk()
    window.geometry("400x200")
    window.title("MAIN WINDOW")
    window.config(background='orange')
    title_label = Label(window,text="TEST YOUR SKILLS BY-TAKING QUIZ",width =40,font=("Helvetica", 12, "bold italic"),background='light green')
    title_label.place(x=0,y=30)
    register_button = Button(window,text = "REGISTER HERE",command=lambda:[window.withdraw(),register_form()],bg='red',fg='white').place(x=280,y=100)
    admin_button = Button(window,text = "LOGIN",width=30,command=already_user,bg='blue',fg='white').place(x=40,y=100)
    window.mainloop()
main_window()
