import sys
sys.path.insert(0, "../..")


from asyncua.sync import Client

if __name__ == "__main__":

    with Client("opc.tcp://localhost:4840/freeopcua/server/") as client:
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", client.nodes.root.get_children())

        # Now getting a variable node using its browse path
        myvar = client.nodes.root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        obj = client.nodes.root.get_child(["0:Objects", "2:MyObject"])
        print("myvar is: ", myvar)
        print("myobj is: ", obj)
