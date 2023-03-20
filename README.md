# Smart_Retail_Management_System
This project is a Smart Retail Management System software which can be used by retail shops for billing, inventory management, and report generation.

This software mainly focuses on basic operations in retail
shop such as employee login, creating invoice, searching
for specific products, adding/deleting/modifying records
and generating reports.




OPERATING INSTRUCTIONS

On running the Python program,the user will be directed to the Smart Retail Management System, and the user will be asked to enter the employee code and password.

If a valid employee code and password are entered, then the user is taken to the program’s main menu. If the user enters wrong credentials (employee code or password), then access is denied.


There are 7 options in the main menu, as follows:
1.	Create a new invoice
2.	View product details
3.	Add a new product
4.	Update product details
5.	Delete product details
6.	View reports
7.	Exit program

By typing the number corresponding to the desired option (between 1 and 7) , the user will be able to perform the desired action. 


1. Create a new invoice
For creating a new invoice, the user will be asked to enter the following details:
  1.	Product Code
  2.	Quantity
After entering the above details, the program will obtain the deatails from the “Product” table and add the details to the “Transaction” table and “Master_Transaction” table. 
Then the program will prompt if the user wants to add  more items. If the user types “y”, then the process repeats, and the user can keep adding more products. Else, if the user type “n”, then the invoice will be created, and the system will display the following details:
•	Serial Number
•	Product Code
•	Product Name
•	Product MRP
•	Product Quantity
•	Total Amount for each product (Quantity x MRP)
•	Total Number of Products
•	Total Quantity of Products
•	Total Amount

2. Search a product
For searching a product, the user will be asked to enter the product code. Once the user enters the product code, the system will search the “Product” table, and display the following details on the screen:
•	Product Code
•	Product Name
•	Product MRP
•	Product Company
•	Available product units (inventory)

3. Add a new product
For adding a new product, the user will be asked to enter the following details, which are then added to the “Product” table
Product Code
•	Product Name
•	Product MRP
•	Product Company
•	Product units
•	Re-order Level (ROL)

4. Update product details
For updating the product details, the program will ask the user to enter the product code (of the product whose details are to be updated). After the product code is entered, the user can modify any of the following details, which are then modified in the “Product” table:
•	Product Code
•	Product Name
•	Product MRP
•	Product Company
•	Product units
•	Re-order Level (ROL)

5. Delete product details
For deleting any product, the program will ask the user to enter the product code (of the product which is to be delated). Once the product code is entered, the program will delete that particular record from the “Product” table.

6. View reports
When the user chooses this option, the program will compare the available quanity of each product against the Re-Order Level (ROL) in the “Product” table. 

If the If the available quantity for a product is more than the ROL, it will display “The inventory level of <Product Name> is OK”.  If the available quantity is less than or equal to the ROL, then it will display “You need to place order for <Product Name>”.

The program will also display the details of all transactions (billing) done on that day, from the “Master_Transaction” table.


7. Exit program
When the user chooses this option, the program will end the loop and exit.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
