from opcua import Client
import time

# 클라이언트 인스턴스 생성
client = Client("opc.tcp://localhost:4840/freeopcua/server/")

try:
    # 서버에 연결
    client.connect()
    print("Client connected to OPC UA Server")

    # 변수 노드 가져오기
    my_var = client.get_node("ns=2;i=2")  # ns=2는 네임스페이스 인덱스, i=2는 아이디

    while True:
        # 변수 값 읽기
        value = my_var.get_value()
        print("Current value:", value)
        time.sleep(1)
finally:
    client.disconnect()
    print("Client disconnected")