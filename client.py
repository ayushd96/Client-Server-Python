'''
author : ayush
created on : 17/05/2020
'''
import socket
import json
clientSocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # defining the socket.

class Client:
    clientSocket.connect(('localhost', 9999)) # Connecting the socket with the port and host defined.
    # The menu() method is the sole method in this class, displaying all the options to the client.
    def menu():
        while True:
            print('Python DB Menu:')
            print(
                "1. Find customer \n2. Add customer \n3. Delete customer \n4. Update customer age \n5. Update customer address \n6. Update customer phone \n7. Print report \n8. Exit")

            try:
                choice = input("Enter from Menu: ").strip()
                if not (choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "7" or choice == "8"):
                    print("Please Enter Correct Choice")
            except ValueError as e:
                print(e)
            #clientSocket.send(str.encode(choice))
            if(choice == "1"):
                try:
                    name = input("Enter Name of Customer: ").strip()
                    if (name.isspace() or name == ""):
                        raise ValueError("Please Enter Name.")
                    else:
                        request = (choice + "," + name)
                        clientSocket.send(str.encode(request))
                except ValueError as e:
                    print(e)
                    continue

                ack = clientSocket.recv(65535)
                ack = ack.decode("utf-8")
                #print(ack)
                if(ack == "1"):
                    message = clientSocket.recv(65535)
                    message = message.decode("utf-8")
                    message = eval(message)
                    print("Age : " ,message[0])
                    print("Address : " ,message[1])
                    print("Phone Number : " ,message[2])
                    #print("--------------", message,"---------------")
                if(ack == "0"):
                    message = clientSocket.recv(65535)
                    message = message.decode("utf-8")
                    print("--------------", message, "---------------")


            if (choice == "2"):
                try:
                    name = input("Enter Name of Customer: ").strip()
                    if(name.isspace() or name == ""):
                        raise ValueError("Please Enter Name.")
                except ValueError as e:
                    print(e)
                    continue

                def isInteger(n):  #This method checks the user-input if it is Integer value or not.
                    try:
                        float(n)
                    except ValueError:
                        return False
                    else:
                        return float(n).is_integer()

                try:
                    age = input("Enter the Age of the Customer: ").strip()
                    if (age.isspace() or isInteger(age) or age == ""):
                        request = (choice + "," + name + "," + age)
                        #print(request)
                    else:
                        raise ValueError("Please Enter the Age in Integers.")
                except ValueError as e:
                    print(e)
                    continue

                adress = input("Please Enter Address of Customer: ").strip()
                phno = input("Please Enter Phone Number of Customer: ").strip()
                request = (choice + "," + name + "," + str(age) + "," + adress + "," + phno)
                #print(request)
                clientSocket.send(str.encode(request))

                message = clientSocket.recv(65535)
                message = message.decode("utf-8")
                print("------------", message, "----------------")


            if (choice == "3"):
                try:
                    name = input("Enter the Name of Customer to be Deleted: ").strip()
                    if (name.isspace() or name == ""):
                        raise ValueError("Please Enter Name")
                except ValueError as e:
                    print(e)
                    continue

                request = (choice + "," + name)
                clientSocket.send(str.encode(request))
                
                message = clientSocket.recv(65535)
                message = message.decode("utf-8")
                print("---------------",message,"-----------------")

            if (choice == "4"):
                try:
                    name = input("Enter Name of Customer to Update the Age: ").strip()
                    if (name.isspace() or name == ""):
                        raise ValueError("Please Enter Name")
                except ValueError as e:
                    print(e)
                    continue

                def isInteger(n):
                    try:
                        float(n)
                    except ValueError:
                        return False
                    else:
                        return float(n).is_integer()

                try:
                    age = input("Enter the Age of the Customer: ").strip()
                    if (age.isspace() or isInteger(age) or age == ""):
                        request = (choice + "," + name + "," + age)
               #         print(request)
                    else:
                        raise ValueError("Please Enter the Age in Integers.")
                except ValueError as e:
                    print(e)
                    continue

                clientSocket.send(str.encode(request))

                message = clientSocket.recv(65535)
                message = message.decode("utf-8")
                print("--------------", message, "-----------------")


            if (choice == "5"):
                try:
                    name = input("Enter the Name of Customer to Update the Address :")
                    if(name.isspace() or name == ""):
                        raise ValueError("Please Enter the Name.")
                except ValueError as e:
                    print(e)
                    continue

                adress = input("Enter the Address of the Customer : ").strip()
                request = (choice + "," + name + "," + adress)
                clientSocket.send(str.encode(request))

                message = clientSocket.recv(65535)
                message = message.decode("utf-8")
                print("---------------",message,"----------------")

            if (choice == "6"):
                try:
                    name = input("Enter the Name of Customer to Update the Phone Number :").strip()
                    if(name.isspace() or name == ""):
                        raise ValueError("Please Enter the Name.")
                except ValueError as e:
                    print(e)
                    continue
                phno = input("Enter the Phone Number: ").strip()
                request = (choice + "," + name + "," + phno)
                clientSocket.send(str.encode(request))

                message = clientSocket.recv(65535)
                message = message.decode("utf-8")
                print("-------------",message,"-------------------")


            if (choice == "7"):
                clientSocket.send(str.encode(choice))

                message = clientSocket.recv(65535)
                message = json.loads(message.decode("utf-8"))
                recvddata = message
                count = 0
                print("=======================REPORT GENERATED==============================")
                print('{:<15}{:<6}{:<40}{:<}'.format("Name","Age","Address","Phone Number"))
                for v in recvddata:
                    print('{:<15}{:<6}{:<40}{:<}'.format(v[0],v[1][0],v[1][1],v[1][2]))
                    count = count + 1
                print("Total Number of Records in Database : ",count)


            if (choice == "8"):
                clientSocket.send(str.encode(choice))
                message = "Good Bye"
                print(message)
                #clientSocket.close()
                exit(0)

    menu()


# References
# 1. https://www.geeksforgeeks.org/socket-programming-python/
# 2. https://docs.python.org/3/howto/sockets.html
# 3. https://realpython.com/python-sockets/
# 4. https://stackoverflow.com/questions/23876608/how-to-send-the-content-of-a-dictionary-properly-over-sockets-in-python3x
# 5. https://www.w3schools.com/python/python_json.asp