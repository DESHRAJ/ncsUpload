# ncsUpload
A django application that put the csv content to the MySql Database automatically. No need to manually enter the details into db. 

This web applicaiton is live at https://ncsupload.herokuapp.com/

Guidelines to use this django Application:
1. Created for the MCQ module used by the Nibble Computer Society.
2. If you want to use this application for your own purpose, then see the ncsUpload/views.py file to change the content according to yourself.
3. If you have any queries or you want to contact me, then feel free to ping me at deshrajdry@gmail.com.

How to Use:

1. Create an excel file. 
2. In the first column, enter the question one by one. 
3. In the second, third, fourth and fifth column, enter the choices accordingly. 
4. In the fifth question of every column, enter the correct answer. 
5. Save the file in .csv format.( Here python reads the .csv format and not .xls format)
6. Upload the file on this applicaiton and click "Generate Query".
7. You will get the result successfully. 

Example of storing data in the Excel sheet:

What is the core of Linux Operating System?	| Shell	| Kernel	| Command	| Terminal	| b
