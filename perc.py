#importing sys, time, random and prettytable modules
import sys
import random
from time import time
from prettytable import PrettyTable as pt, SINGLE_BORDER, ALL

#defining functions
def table_rule():
    "The function to set table rules for tb1 and tb2"
    tb1.header = False
    tb1.hrules = ALL
    tb1.set_style(SINGLE_BORDER)

    tb2.header = False
    tb2.set_style(SINGLE_BORDER)
    tb2.border = False
    tb2.left_padding_width = 3
    tb2.right_padding_width = 2

def table_rule_txt():
            "This function sets the table rules to make it printable on txt file"
            tb1.vertical_char = ' '
            tb1.horizontal_char = ' '
            tb1.junction_char = ' '
            tb1.border = False
            tb1.preserve_internal_border = True
            tb1.max_width = 5
            tb1.padding_width = 3
            tb2.vertical_char = ' '
            tb2.horizontal_char = ' '
            tb2.junction_char = ' '
            tb2.border = False
            tb2.preserve_internal_border = True
            tb2.max_width = 2
            tb2.right_padding_width = 3
 
#declaring variables
lst = [] #to seperate user input
lst3 = [] #to input random inputs to display in grids
listt = [] #to add OK and NO
ans = [] #to append the inputs in each column
tb1 = pt()
tb2 = pt()

i = " __ "
rand = 0
rand2 = 0
row1 = 0
col = 0
tot = 0
gen = 1
fo = 0
ht = 0
n = 0
m = 0
p = 1

#declaring arguments in sys
if len(sys.argv) > 1:
    first = sys.argv[1]

else:
    first = "5x5"
    
if 4 <= len(first):
    print ("Invalid Grid Size")

elif len(first) <= 2:
    print ("Incomplete Grid Size")
        
else:
    for letter in first:
        lst.append(letter) #seperating the values to recognize no. of rows and columns

    if lst[1] == "x":
        #declaring rows and columns   
        row1 = int(lst[0])
        col = int(lst[2])
        tot = row1*col

        if  3 <= row1 <= 9:     #setting minimum and maximum number of rows and columns
            if 3 <= col <= 9:
                while gen <= tot:
                    rand = random.randrange(500)
                    rand2 = random.randrange(10,99)
        
                    if rand%2 == 0:  #generates random number and checks if it even
                      lst3.append (rand2)   #if even, two digit number is appended to list
                      gen += 1
                    else:
                      lst3.append (" __ ")  #if odd, blank is appended to list
                      gen += 1
                random.shuffle(lst3)

                #seperates one list into many as per the number of rows while adding rows to a table
                sublist = len(lst3) // row1
                s1, s2 = lst3[:sublist], lst3[sublist:]
                tb1.add_row(s1)

                while col <= len(s2):
                    sublist = len(lst3) // row1
                    s3, s2 = s2[:sublist], s2[sublist:]
                    tb1.add_row(s3)

                table_rule() #setting table rules
                print (tb1)

                #percolation process done by changing each number of column and rows
                while p < tot:
                  for row in tb1:
                    ans.append(tb1.rows[n][m])
                    n+=1
                    if row1 <= n:
                        if i in ans:
                            listt.append("NO")
                        else:
                            listt.append("OK")
                        ans.clear()
                        n=0
                        m += 1
                  if col <= m:
                    break
            
                tb2.add_row(listt)
                print(tb2)

                #getting html string and saving file as html to display on a web page
                tb1.add_row(listt)
                ht0 = tb1.get_html_string(attributes={"class":"table"}, format=True)

                s = str(round(time() * 1000))  #using time to create new files every time code is run
                with open("Web - " + s + ".html","a") as ht:
                    ht.write(str(ht0))
                ht.close

                #modifying prettytable rules to print into txt file
                table_rule_txt()
                tb1.del_row(row1)
                
                with open("Table - " + s + ".txt","a") as fo:
                    fo.write(str(tb1))
                    fo.write("\n")
                    fo.write(str(tb2))
                fo.close

            else:
                print ("Invalid Number of Columns")
        else:
            print ("Invalid Number of Rows")
    else:
        print("Invalid Syntax")
