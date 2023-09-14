
'''
i = 1
while i <= 5:
    print('a' * i)
    i+=1
print ('done')

'''
'''
secret_number = 6
count = 0
while count < 3:
     count += 1
     number= int(input('Guess: '))
     if number == secret_number:
        print ('you are right!!!') 
        break
else:
    print ('you failed!!!')
'''

car_start = False
key_word = ""
while True:        
        key_word = input('>  ').lower()
        if key_word == "start":
           
           if car_start:
            print('the car is already started')                      
           else:
            print('car started... ready to go!')
            car_start = True  

        elif key_word == "stop":
             if not car_start:
                print('the car is already stopped!!!')                              
             else:
                 print('the car stopped!!!')
                 car_start = False                             
        
        elif key_word == 'help':
            print ("""
star - to start the car 
stop - to stop the car 
quit - to exit
            """)
        elif key_word == "quit":
            print("the race finished")
            break
        else:
            print ("i don't understand that " )






