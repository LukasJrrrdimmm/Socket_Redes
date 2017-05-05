# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os as o
import string as st
# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8082 # porta do servidor
comando = b'GET'
#file = 'link/index.html'
# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# mantem o socket ativo mesmo apos a conexao ser encerrada (faz o reuso do endereco do servidor)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ("Serving HTTP on port %s ..." % PORT)
#print (comando ==b'GET')
while True:
	# aguarda por novas conexoes
	client_connection, client_address = listen_socket.accept()
	# o metodo .recv recebe os dados enviados por um cliente atraves do socket
	request = client_connection.recv(1024)
	print(str(request.split()))
	arquivo = request.split()[1]
	print(arquivo)
	file1 = ('/home/lukas/Downloads/Redes1/Redes1/link' + str(arquivo))
	print(file1)
	print(arquivo == b'/')
	print(o.path.isfile(file1))
	#print(o.path.exists(file))
	if (request.split()[0] == comando):
		if(arquivo == b'/favicon.ico'):
	   		file1 = '/home/lukas/Downloads/Redes1/Redes1/link/index.html';
			http_response = b'HTTP/1.1 200 OK\n'
			http_response = http_response + b'Content-Type: text/html\n'
			print(file1)
			f = open(file1)
			c = f.read()
			http_response= http_response + bytes(c)			
			#for line in c:

			#	http_response = http_response + bytes(line)
			print(str(http_response))
			# servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
			client_connection.send(str(http_response))
			#client_connection.send("\r\n")
		if(arquivo == b'/'):
	   		file1 = '/home/lukas/Downloads/Redes1/Redes1/link/index.html';
			http_response = b'HTTP/1.1 200 OK\n'
			http_response = http_response + b'\r\n'
			print(file1)
			f = open(file1)
			c = f.read()		
			for line in c:
				http_response = http_response + bytes(line)
			print(str(http_response))
			# servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
			client_connection.send(str(http_response))
			#client_connection.send("\r\n")
		else:
			if (o.path.isfile(file1) is True):
					http_response = b'HTTP/1.1 200 OK\n'
					http_response = http_response + '\r\n'
					print(file1)
					f = open(file1)
					c = f.read()
					for line in c:
						http_response = http_response + bytes(line)
					print(str(http_response))
					# servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
					client_connection.send(http_response)
					#client_connection.send("\r\n")
						# encerra a conexao
			else:
				http_response = b"""HTTP/1.1 404 Not Found \r\n\r\n
				<html>
					<head>
					<title>
						Page Not Found
					</title>
					<meta charset='utf-8'>
					</head>
					<body>
					<h1>
						404 Not Found
					</h1>
					</body>
				</html>
				\r\n
			"""
			 # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
			client_connection.send(http_response)
			#arq_html.write(http_response)
			# encerra a conexao

	else:
		#c, (client_host, client_port) = socket.accept()

		http_response = b"""HTTP/1.1 400 Bad Request \r\n\r\n
		<html>
		    <head>
			<title>
			    Error
			</title>
			<meta charset='utf-8'>
		    </head>
		    <body>
			<h1>
			    400 Bad Request
			</h1>
			<h2>
			    Page not found
			</h2>
		    </body>
		</html>
		\r\n
		"""

		# servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
		client_connection.send(http_response)
		# encerra a conexao
	client_connection.close()
