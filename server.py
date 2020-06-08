'''
author : ayush
created on : 18/05/2020
'''
import socket
import json

# The server class defining the connection and functionalities.
class Server:

    db = {}   # Dictionary to read contents of file.
    file = open("data.txt")
    for line in file:
        line = line.strip('\n')
        list = line.split('|')
        #print(list)
        if (list[0].isspace()):    # Skipping records with empty names.
            continue
        else:
            db[list[0].strip().upper()] = list[1:]
    #print(db)

    for key,val in db.items():
        val = db.get(key)
        #print(val)
        val[1] = val[1].strip()
        val[2] = val[2].strip()
        age = val[0].strip()

        # The following code checks if Age of customers is Integer, skip if not Integers.
        def isString(age):
            try:
                float(age)
                return True
            except ValueError:
                return False

        if (isString(age) == False):
            val[0] = ""
            #print(val[0])

        else:
            age = float(age)
            if(age.is_integer()):
                val[0] = int(age)
                #print(val[0])
            if not(age.is_integer()):
                val[0] = round(age)
                #print(val[0])

    #print(db)
    #print(len(db))

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 9999

    serverSocket.bind(('localhost', 9999))
    serverSocket.listen(5)

    print("Waiting for a connection...")
    clientSocket, address = serverSocket.accept()   #Connecting the sockets.
    print(f"Connnection from {address} has been established.")

    while True:
        request = clientSocket.recv(65535).decode('utf-8')
        #print(request)
        requestList = request.split(",")
        choice = requestList[0]
        #print(choice)
        #name = requestList[1]
        #print(name)

        if (choice == "1"):
            name = requestList[1]
            #print(name)
            if name in db.keys():
                ack = "1"
                clientSocket.send(str.encode(ack))
                data = str(db[name])
                clientSocket.send(str.encode(data))
            elif name not in db.keys():
                ack = "0"
                clientSocket.send(str.encode(ack))
                message = "Customer Not Found"
                clientSocket.send(str.encode(message))

        if (choice == "2"):
            name = requestList[1].strip()
            #print(name)
            age = requestList[2].strip()
            #age = int(age)
            #print(age)
            address = requestList[3].strip()
            #print(address)
            phno = requestList[4].strip()
            #print(phno)

            if name in db.keys():
                message = "Customer Exists"
                clientSocket.send(str.encode(message))
            if name not in db.keys():
                # print(name, age,address, phno)
                db.update({name: [age, address, phno]})
                message = "Customer Added Successfully"
                clientSocket.send(str.encode(message))
                # print(db)

        if (choice == "3"):
            name = requestList[1].strip()
            #print(name)

            if name not in db.keys():
                clientSocket.send(str.encode("Customer Not Found."))
            else:
                del db[name]
                clientSocket.send(str.encode("Customer Deleted Successfully."))
                # print(len(db))

        if (choice == "4"):
            name = requestList[1].strip()
            #print(name)
            age = requestList[2].strip()
            #age = int(age)
            #print(age)
            if name in db.keys():
                data = db.get(name)
                data[0] = age
                message = "Age Updated Successfully"
                clientSocket.send(str.encode(message))
            #   print(db)
            if name not in db.keys():
                message = "Customer Not Found"
                clientSocket.send(str.encode(message))

        if (choice == "5"):

            name = requestList[1].strip()
            #print(name)
            address = requestList[2].strip()
            #print(address)
            if name in db.keys():
                data = db.get(name)
                data[1] = address
                message = "Address Updated Successfully"
                clientSocket.send(str.encode(message))
            #   print(db)
            if name not in db.keys():
                message = "Customer Not Found"
                clientSocket.send(str.encode(message))

        if (choice == "6"):
            name = requestList[1].strip()
            #print(name)
            phno = requestList[2].strip()
            #print(phno)
            if name in db.keys():
                data = db.get(name)
                data[2] = phno
                message = "Phone Number Updated Successfully"
                clientSocket.send(str.encode(message))
            #   print(db)
            if name not in db.keys():
                message = "Customer Not Found"
                clientSocket.send(str.encode(message))
        
        if (choice == "7"):
            newdict = {}
            for key in (sorted(db.keys(), key = lambda s: s.casefold())):
                newdict[key] = db.get(key)
            #print(newdict)
            b = json.dumps(sorted(newdict.items())).encode("utf-8")
            clientSocket.sendall(b)

        if(choice == "8"):
            print("Client Disconnected..")
            clientSocket,address = serverSocket.accept()
            print(f'Connection from {address} has been established')


           # count = 0
            # f = open("report.txt", "w")
            # for key in sorted(db.keys()):
            #     f.write("%s : %s" % (key, db[key]))
            #     f.write('\n')
            #     count = count + 1
            # # print("%s : %s" % (key, db[key]))
            # f.write("Total Count of Records: ")
            # f.write(str(count))
            # f.close()

