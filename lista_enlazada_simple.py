#lista_enlazada_simple.py


class Nodo(object):
	def __init__(self, data):
		self.data = data
		self.next = None


	def get_data(self):
		return self.data


	def get_next(self):
		return self.next


	def set_data(self, new_data):
		self.data = new_data



	def set_next(self, new_next):
		self.next = new_next


def create_root(data="root"):
	return Nodo(data)

def new_node(data):

	return Nodo(data)



#p = q
#q = Nodo("Brunett")
#p.next = q

#print(r.get_data())
#print(p.get_data())
#print(q.get_next())





def peek_all(r, flag = True):
	p = r
	while flag != False:
		print(p.get_data())
		p = p.next
		#print(q.get_data())
		if p.next == None:
			print(p.get_data())
			flag = False
	return "done" 

def menu():
	p = r
	opc = str(input("Seleccione una Opcion!!"))
	if r.next != None:
		if opc == "1":
			d = str(input("Escribe el dato para almacenar!!"))
			q = new_node(d)
			p.next = q
			#print(q.get_data())
			menu()
		elif opc == "2":
			print(peek_all(r))
	else:
		r.next = p

	return "Finish"
	
r = create_root()

menu()















