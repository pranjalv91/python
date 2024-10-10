#Define a dictionary
#Dictionary are defined by curly brackets {}
server1={
    "env":"dev",
    "servertype":"aws linux2",
    "ram":8096,
    "cpu":4,
    "active":True
}

server2={
    "env":"prd",
    "servertype":"aws linux2",
    "ram":10240,
    "cpu":8,
    "active":False
}

#Print value based on the key using get function
print(server1.get("env"))

#Create a list of servers to hold multiple dictionaries
#Wrong way of declaring a list: list_of_servers = list(server1,server2)
servers=[server1,server2]

#Print values if server is active
for server in servers:
    for key,value in server.items():
        if key=="active" and value==True:
            print(server.values())