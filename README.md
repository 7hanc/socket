# Client/Server 建立Socket 連線

# Goal
1. Client 發送 UI 輸入的字串給 Server 。
2. Server 回應 Client 收到的字數及Server端的時間。

# 簡易操作(適用於python3)
執行server.py與client.py    
當client端輸入"bye"時，結束

# Flow
In server:
* Step1: socket(): create socket
* Step2: bind():   bind socket
* Step3: listen(): maximum number of client which can be accepted
* Step4: accept(): wait for client's request
* Step5: send(), recv(): communicate with client
* Step6: close():  close connection

In client:
* Step1: socket(): create socket
* Step2: connect(): TCP connect 
* Step3: send(), recv(): communicate with server
* Step4: close(): close connection

<img src="https://i.imgur.com/z49ZnBu.png" width=30% height=30%>

# Output
Client: 
<img src="https://i.imgur.com/s7xxObH.png" width=30% height=30%>  Server: <img src="https://i.imgur.com/CskZEaX.png" width=30% height=30%>

# Notice
1. socket間以byte形式傳送數據

# Reference
https://realpython.com/python-sockets/   
https://www.journaldev.com/15906/python-socket-programming-server-client
