from opcua import Server
import time

# 서버 인스턴스 생성
server = Server()

# 서버 URL 설정
server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

# 네임스페이스 추가
uri = "http://su_opcua_server.org"
idx = server.register_namespace(uri)

# 객체 생성
my_obj = server.nodes.objects.add_object(idx, "MyObject")

# 변수 추가
my_var = my_obj.add_variable(idx, "MyVariable", 0)

# 변수 쓰기 가능
my_var.set_writable()

# 서버 시작
server.start()
print("OPC UA Server started at {}".format(server.endpoint))

try:
    while True:
        # 변수 값 변경
        my_var.set_value(my_var.get_value() + 1)
        time.sleep(1)
finally:
    server.stop()
    print("Server stopped")
