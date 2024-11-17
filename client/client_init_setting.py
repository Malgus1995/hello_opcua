from opcua import Client

opcua_server_tcp_str = "opc.tcp://localhost:4840/freeopcua/server/"

class Opc_client:

    def __init__(self,opcua_server_tcp_str):
        self.opcua_tcp_str = opcua_server_tcp_str
        self.client = Client(self.opcua_tcp_str)
        print("Client connected to OPC UA Server")

    def getRootObject(self):
        rootobject = self.client.get_node("ns=2;i=1")
        return rootobject
    
    def findNodeByName(self,node_name):
        rootobject = self.getRootObject()
        children = rootobject.get_children()
        for child in children:     
            # 변수 이름과 비교하여 my_variable을 찾기
            if child.get_browse_name().Name == node_name:
                res_node = child
                return res_node
            
    def disconnect(self):
        self.client.disconnect()
        print("Client disconnected")


            
        






        