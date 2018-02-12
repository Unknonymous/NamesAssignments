students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# above was copied directly from the learning platform per the assignment instructions

'''def names(arr):                             #set function
    for i in range (0, len(arr)):           #loop through list
        print arr[i]['first_name'] + " " + arr[i]['last_name']  #print full name string

names(students)'''

users = {          
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
#users dictionary was copied from platform per assignment instructions

def data(arr):                                                      #set the function
    for i in range (0, len(arr.keys())):                            #loop through the arrays keys
        print arr.keys()[i]                                         #print keys as section headers
        for h in range (0, len(arr[arr.keys()[i]])):                #loop through the listed dictionaries
            #print len(arr[arr.keys()[i]][h].keys())
            fname = ''                                              #set/reset printable full name variable
            for g in range (0, len(arr[arr.keys()[i]][h].keys())):  #loop through the nested dictionaries
                fname += " " + arr[arr.keys()[i]][h].values()[g]    #add values from nested dictionaries to fname variable
            #print fname
            lenname = len(fname)-2                                  #count length of fname, minus contatenated spaces
            #print lenname
            print h+1, "-", fname, "-", lenname                     #build and print the output string
    
        
data(users)