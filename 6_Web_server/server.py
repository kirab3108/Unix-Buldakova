import socket
import logging
import os
from datetime import datetime

wd = "6_Web_server"

def log_print(st):
    logging.info(st)
    print(st)

STATUSES = {
        200: "Ok",
        404: "File not found",
        403: "Forbidden"
    }

def get_header(status_code, body, mime="text/html"):
  """Получает заголовок для ответа сервера"""
  return "\n".join(
      [
          f"HTTP/1.1 {status_code} {STATUSES[status_code]}",
          f"Content-Type: {mime}",
          f"Date: {datetime.now()}",
          f"Content-length: {len(body)}",
          "Connection: close"
          "Server: MyServer" "\n\n",
      ]
  )

def genRespBody(dat):
  d=dat.split()
  print( d)
  fn =d[1]
  status = 200
  file="" 
  if len(fn)>1:
    fn=fn[1:]
    print ("if")
    if fn in os.listdir(wd):
      print("qwer")
      file = fn
    else:
      print("jasdj")
      status = 404
      file = "404.html"
  else:
    file= "index.html"
  return file, status

  




sock = socket.socket()
try:
  sock.bind(('', 80))
except OSError:
  sock.bind(('', 8080))

while True:
  sock.listen(1000)
  conn, addr = sock.accept()
  log_print("Connected"+str(addr))


  try:
    data = conn.recv(8192).decode('utf-8')
  except OSError:
    data = None

  if data:
      #получение данных от клиента
      log_print('\nReceiving data from client:')
      log_print(data)
      if data.lower() == 'exit':
          log_print('here')
          break
      #отправка сообщений клиенту
      print("----")
      file, status =genRespBody(data)
      with open(wd+file, "r") as f:
        body=f.read()
        resp = get_header(status, body)+body
        print(resp)
      print("he134re")
      
      conn.send(resp.encode())
      conn.close()
      print("here")
