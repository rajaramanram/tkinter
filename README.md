# tkinter
INTRODUCTION:
	The main aim of this project is to create registration form for the candidate, admin page and user login page with database connection.
	PYTHON -- Python is a high-level, interpreted and general-purpose dynamic programming language.
	GUI -TKINTER -- Tkinter is the standard GUI library for python. python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface  to the Tk GUI toolkit.
	SQLITE3 -- Sqlite is a lighter version of SQL. It is standalone DBMS. Used for Embedded type of software, IOT-Internet of Things and storing small data .
first gui window:
	This Login box have three login methods:
			1) ADMIN LOGIN.
			2)USER LOGIN.
			3)REGISTRATION FOR NEW CANDIDATE.
REGISTER  HERE BUTTON:
	After this button clicked by the user ,a pop up window will show to register the information about the user.
    	Entry widget -- This widget  is used to enter the input in the box.
   	Label widget-- This widget shows the  information text.
	Call back Function-- To validate user input call back function is used. In username "validate=key" is used to validate no number enter in user name. In other widgets "validate = focusout" is to validate after the input is finished by the user.
Radio Button-- To select the gender of the user radio button is used to select one option.
	Date picker-- It is the imported module used to select date easy for the user.
	Option Menu-- To drop down the list of language and select languages tkinter optionmenu is used here.
	Checkbutton-- To select multiple interested course by the user checkbutton widget is used.
	Get values-- To get the values of these widget variabelname.get() is used.
REgex:
	Regular Expression plays an important role in validation of user. input.
re.compile(pattern)--search pattern can be converted into a pattern object. If want  to use a complex regular expression multiple times, it is a good idea to use its compiled version, more efficient.
		re.search()-- This function searches the patterns first occurrence in the given string("entire string")
		re.match()-- This function searches the given pattern from the given string at the beginning only.
CLICK TO SUBMIT:
	After user fill the form ,user press the click button to submit.A message  is show the data which is entered by the user to check after click "yes", The data in form is stored in sqlite
ADMIN LOGIN:
	In admin login, admin have to enter username and password to enter the admin page. If user clicks the admin window will show in display.
  show Records:
	After click this button by the admin,  all candidates records will show in the same Candidates data box.
delete records:
	Delete record is based on which rowid entered in Delete ID entry widget. After delete id is entered by the admin the certain record is delete from the database.
upload test:
	This button is used to upload certain file or test to the candidate user via data base.
select files:
	Select file button will display in "UPLOAD BOX" to select file to upload to the already-user candidates.
After test finished by the candidates, the username ,question and answer selected by the user is stored in separate Database "Test Over" message  will appear in the screen.
