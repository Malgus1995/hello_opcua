from opcua import Client

# 클라이언트 인스턴스 생성
client = Client("opc.tcp://localhost:4840/freeopcua/server/")

try:
    # 서버에 연결
    client.connect()
    print("Client connected to OPC UA Server")

    # 객체 노드 가져오기
    my_object = client.get_node("ns=2;i=1")  # ns=2에서 객체를 가져옴

    # 객체의 자식 노드 확인
    children = my_object.get_children()
    print("Children of My Object:")
    my_variable = None  # 변수를 저장할 변수 초기화
    for child in children:
        print("Child Node:", child.get_browse_name().Name)
        print("Node ID:", child.nodeid)  # 노드 ID 출력
        
        # 변수 이름과 비교하여 my_variable을 찾기
        if child.get_browse_name().Name == "MyVariable":
            my_variable = child
            break

    if my_variable is None:
        print("Variable 'MyVariable' not found.")
    else:
        # 변수 값 읽기
        value = my_variable.get_value()
        print("Current value:", value)
finally:
    client.disconnect()
    print("Client disconnected")
