from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import re


#use Tk class for creating  main window
window = Tk()

def name_validate(user_name):
    name_regex=re.compile(r'[@!#$%^&*()_<>?}{~:/\0-9]')
    if (name_regex.search(user_name) == None):
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
global gender
global course_get
global course2_get
global course3_get
def validate_form():
    if user_name.get() == "":
        messagebox.showinfo("Information","Enter Name")
    elif user_password.get()== "":
        messagebox.showinfo("Information","Enter Password")
    elif user_retype_password.get() == "":
        messagebox.showinfo("Information","Enter Confirm Password")
    elif user_email.get() == "":
        messagebox.showinfo("Information","Enter Email ID")
    elif v_gender.get() == 0:
        messagebox.showinfo("Information","Enter Gender")
    else:
               messagebox.askyesno(title='Information', message="Are Those Inputs Correct ? "
                            '\n' 'Username: %s \n Password: %s \n Email ID: %s \n Gender:%s\n DOB: %s \n Address: %s \n Language: %s \n Field:%s'%
                            (user_name.get(),user_password.get(),user_email.get(),gender,entry_mode.get(),user_address.get("1.0",'end-1c'),
                            v_language.get(),course_label))
def separate_box():
    separate_window = Toplevel(window)
    separate_window.geometry('600x600')
    name_label =Label(window,text="Username = "+ user_name.get(),width =20,font=("bold",10))
    name_label.place(x=45,y=60)
    password_label =Label(window,text="Password = "+ user_password.get(),width =20,font=("bold",10))
    password_label.place(x=45,y=100)
    email_label =Label(window,text="Email ID = "+ user_email.get(),font=("bold",10))
    email_label.place(x=65,y=140)
    gender_get=v_gender.get()
    if gender_get == 1:
        gender = "Male"
    else:
        gender ="Female"
    dob_label =Label(window,text="Gender = "+ gender,width =20,font=("bold",10))
    dob_label.place(x=35,y=180)
    address_label =Label(window,text="Address = "+user_address.get("1.0",'end-1c'),font=("bold",10))
    address_label.place(x=45,y=220)
    language_label =Label(window,text="Language = "+ v_language.get(),width =20,font=("bold",10))
    language_label.place(x=45,y=280)
    course_get = v_check1.get()
    course2_get = v_check2.get()
    course3_get = v_check3.get()
    if course_get == 1:
        course_get="Python"
    else:
        course_get =''

    if course2_get == 1:
        course2_get="Java"
    else:
        course2_get =''    
    if course3_get == 1:
        course3_get="Javascript"
    else:
        course3_get =''   
        
    course_label =Label(window,text="Selected Field = "+ course_get+' '+ course2_get+' '+ course3_get,font=("bold",10))
    course_label.place(x=45,y=320)
    separate_window.mainloop()

window.geometry("600x600")
window.title("Registration Form")
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
title_label = Label(window,text="Candidate Registration Form",width =30,font=("bold",12))
title_label.place(x=120,y=70)

lb_fullname = Label(window,text="FullName",width =20,font=("bold",10))
lb_fullname.place(x=45,y=130)
user_name = Entry(window,textvariable = v_name)
user_name.place(x=240,y=130)
#register callback function
name_validate_call = window.register(name_validate)
#pass option value to callback function -validate(when to validate),validatecommand(what function),invalidcommand(optional)
# %p is an %specifier this is used to pass input to callback function
user_name.config(validate="key",validatecommand=(name_validate_call,'%P'))
#user_name.bind('<Return>', lambda e: user_password.focus_set())

lb_password = Label(window,text="Password",width =20,font=("bold",10))
lb_password.place(x=45,y=170)
user_password = Entry(window,show ='*',textvariable = v_password)
user_password.place(x=240,y=170)
password_validate_call = window.register(password_validate)
user_password.config(validate="focusout",validatecommand=(password_validate_call,'%P'))                 

lb_retype_password = Label(window,text="Confirm Password",width =20,font=("bold",10))
lb_retype_password.place(x=70,y=210)
user_retype_password = Entry(window,show='*',textvariable = v_retype)
user_retype_password.place(x=240,y=210)
retype_validate_call = window.register(retype_validate)
user_retype_password.config(validate="focusout",validatecommand=(retype_validate_call,'%P'))

lb_email = Label(window,text="Email ID",width =20,font=("bold",10))
lb_email.place(x=45,y=250)
user_email = Entry(window,textvariable = v_email)
user_email.place(x=240,y=250)
email_validate_call = window.register(email_validate)
user_email.config(validate="focusout",validatecommand=(email_validate_call,'%P'))

lb_gender = Label(window,text="Gender",width =20,font=("bold",10))
lb_gender.place(x=42,y=280)
Radiobutton(window,text="Male",padx =5,variable=v_gender,value=1).place(x=230,y=280)
Radiobutton(window,text="Female",padx =20,variable=v_gender,value=2).place(x=290,y=280)



def grab_dob():
    separate_window = Toplevel(window)
    dob_calendar = Calendar(separate_window,selectmode='day',year=2019,month=6,day=14)
    dob_calendar.pack()
    button_select=Button(separate_window,text='Save')
    button_select.pack()
def show_dob():
    separate_window2=Toplevel(window)
    entry_mode=DateEntry(separate_window2,width=20)
    entry_mode.pack()
    #lb_dob.config(dob_calendar.get_date())
lb_dob = Label(window,text="DOB MM/DD/YYYY",width =20,font=("bold",10))
lb_dob.place(x=80,y=310)
entry_mode=DateEntry(window,width=20)
entry_mode.place(x=240,y=310)


lb_address = Label(window,text="Address",width =20,font=("bold",10))
lb_address.place(x=45,y=340)
user_address = Text(window,width=20,height=4)
user_address.place(x=240,y=340)

lb_language = Label(window,text="Language",width =20,font=("bold",10))
lb_language.place(x=50,y=420)
language_list=['Tamil','Urudu','Hindi','Telugu','Bengali','kannada','Malayalam']
user_language = OptionMenu(window,v_language,*language_list)
user_language.config(width=20)
v_language.set('Select Language')
user_language.place(x=240,y=420)

course_label = Label(window,text="Select Field",width =20,font=("bold",10))
course_label.place(x=50,y=450)
check1=Checkbutton(window,text='Python', onvalue = 1, offvalue = 0,variable=v_check1)
check1.place(x=240,y=450)
check2=Checkbutton(window,text='Java',onvalue = 1, offvalue = 0,variable=v_check2)
check2.place(x=340,y=450)
check3=Checkbutton(window,text='Javascript' ,onvalue = 1, offvalue = 0,variable=v_check3)
check3.place(x=440,y=450)
gender_get=v_gender.get()
if gender_get == 1:
    gender = "Male"
else:
    gender ="Female"
course_get = v_check1.get()
course2_get = v_check2.get()
course3_get = v_check3.get()
if course_get == 1:
    course_get="Python"
else:
    course_get =''

if course2_get == 1:
    course2_get="Java"
else:
    course2_get =''    
if course3_get == 1:
    course3_get="Javascript"
else:
    course3_get =''
course_label= course_get+ course2_get+ course3_get

def go_to_next_entry(event, entry_list, this_index):
    next_index = (this_index + 1) % len(entry_list)
    entry_list[next_index].focus_set()

entries = [child for child in window.winfo_children() if isinstance(child, Entry)]
for idx, entry in enumerate(entries):
    entry.bind('<Return>', lambda e, idx=idx: go_to_next_entry(e, entries, idx))


register_button = Button(window,text = "CLICK TO SUBMIT",command=validate_form).place(x=440,y=490)
window.mainloop()

