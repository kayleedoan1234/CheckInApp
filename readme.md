# Final project (Ngoc Doan)

For the Check In application, customers are able to enter their name, 
phone number, and select the services they want. After checking in, 
they will receive a quote indicating the total cost, and then return to 
the main page. The exit option is designed for the manager.


# Install required libraries
Ensure that you are in the main directory and run the following:
_This must be done before you can run the application if you are not using the included venv._

[//]: # (```shell)

[//]: # ($ pip install -r requirement.txt)

[//]: # (```)
or
``` shell
$ pip install PILLOW
$ pip install pytest
```
## To run the program
Click the green triangle run icon in the top-right corner of the Pycharm windows.
or
```shell
$ python3 project_gui.py
```

## Functionality
### Add on transaction
A new transaction will be added to the Transaction Class 
instance list file and recorded in the transactions.csv file when users 
click on the Check In button

When printing out the Transaction instance list it 
has the following information:
Transaction:1-Name:Emma, Phone number:423432443, Total: $35.00
Transaction:2-Name:Kaylin, Phone number:4343268843, Total: $40.00

### Return 
When customer click the Return button, they will go back to the Main GUI page.

### Check In
When the customer checks in. All of the transactions information
will be stored in the transactions.csv file.

### Exit
The application will exit when the Exit button is clicked.

## Data Files
### transactions.csv
The file contains the transaction data in the following format:

| Transaction number | Name   | Phone Number | Time                     | Services       | Total |
|--------------------|--------|--------------|--------------------------|----------------|-------|
| 1                  | Emma   | 4234324443   | Tue Aug 10 10:42:24 2021 | Gel Manicure   | 35.00 |
| 2                  | Kaylin | 4343268843   | Tue Aug 10 10:58:24 2021 | Dipping Powder | 40.00 |


## Class
### Transaction Class
### Variables

Each Accounts instance has the following instance variables:
1. transaction_number: public, integer data type
2. name: private, string 
3. phone_number: private, string
4. cost: public, float
5. name getter
6. name setter
7. phone_number getter
8. phone_number setter


#### Methods
The Transaction has the following methods:
* The dunder__init__ method
* The dunder__str__ method
* The log_transactions(self) instance method


## Auto Testing
Run the following command to test the test.py file. There are
3 test cases
```shell
$ pytest -v test.py

```


