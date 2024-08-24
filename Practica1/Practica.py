
import os,time






class auto:
    # atributos
    placa = ""
    marca = 0
    modelo = 0
    descripcion = ""
    precio_unitario = 0.0


    # contructor
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
    
    # metodos

    def getplaca(self):
        return self.placa
    
    def getmarca(self):
        return self.marca
    
    def getmodelo(self):
        return self.modelo
    
    def getdescripcion(self):
        return self.descripcion
    
    def getprecio_unitario(self):
        return self.precio_unitario
    


    
    def setplaca(self, placa):
        self.placa = placa
    
    def setmarca(self, marca):
        self.marca = marca

    def setmodelo(self, modelo):
        self.modelo = modelo
    
    def setdescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def setprecio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario


class cliente:
    # atributos
    nombre = ""
    correo = ""
    nit = ""

    # contructor
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

    # metodos

    def getnombre(self):
        return self.nombre
    
    def getcorreo(self):
        return self.correo
    
    def getnit(self):
        return self.nit
    
    def setnombre(self, nombre):
        self.nombre = nombre

    def setcorreo(self, correo):
        self.correo = correo

    def setnit(self, nit):
        self.nit = nit


class compra:
    nombrec = ""
    correoc = ""
    nitc = ""
    autoc= []
    precioc = 0.0

    def __init__(self, nombrec, correoc, nitc, autoc, precioc):
        self.nombrec = nombrec
        self.correoc = correoc
        self.nitc = nitc
        self.autoc = autoc
        self.precioc = precioc

    def getnombrec(self):
        return self.nombrec
    
    def getcorreoc(self):
        return self.correoc
    
    def getnitc(self):
        return self.nitc

    def getautoc(self):
        return self.autoc
    
    def getprecioc(self):
        return self.precioc
    
    def setnombrec(self, nombrec):
        self.nombrec = nombrec

    def setcorreoc(self, correoc):
        self.correoc = correoc

    def setnitc(self, nitc):
        self.nitc = nitc
    
    def setautoc(self, autoc):
        self.autoc = autoc

    def setprecioc(self, precioc):
        self.precioc = precioc

    





def menu(opcion):
    print('')
    os.system('cls')
    
    print('')
    print("---------- Menu Principal ----------")
    print('1. Registrar auto')
    print('2. Registrar cliente')
    print('3. Realizar compra')
    print('4. Reporte de compras')
    print('5. Datos del estudiante')
    print('6. Salir')
    print('------------------------------------')

    opcion = int(input('Seleccione una opcion: '))

    




def main():
   
    os.system('cls')
    print("---------- Menu Principal ccc----------")
    print('1. Registrar auto')
    print('2. Registrar cliente')
    print('3. Realizar compra')
    print('4. Reporte de compras')
    print('5. Datos del estudiante')
    print('6. Salir')
    print('------------------------------------')

    opcion = int(input('Seleccione una opcion: '))

    print(type(opcion))

    lista_autos = []
    lista_clientes = []
    lista_compra = []
    lista_autos_compra = []
    while True:

        if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5 and opcion != 6 :
            os.system('cls')
            print('')
            print("---------- Menu Principal ----------")
            print('1. Registrar auto')
            print('2. Registrar cliente')
            print('3. Realizar compra')
            print('4. Reporte de compras')
            print('5. Datos del estudiante')
            print('6. Salir')
            print('------------------------------------')

            opcion = int(input('Seleccione una opcion: '))   
        
        
        else:

            

            # Switch statement
            if opcion == 1:
                print('REGISTRAR AUTO')


                placa_temp = input('Ingrese la placa: ')
                marca_temp = input('Ingrese la marca: ')
                modelo_temp = input('Ingrese el modelo: ')
                descripcion_temp = input('Ingrese la descripcion: ')
                precio_unitario_temp = input('Ingrese el precio unitario: ')

                
                auto1 = auto(placa_temp, marca_temp, modelo_temp, descripcion_temp, precio_unitario_temp)

                lista_autos.append(auto1)

                for i in range(len(lista_autos)):
                    print('')
                    print("Placa:", lista_autos[i].getplaca())
                    print("Marca:", lista_autos[i].getmarca())
                    print("Modelo:", lista_autos[i].getmodelo())
                    print("Descripcion:", lista_autos[i].getdescripcion())
                    print("Precio unitario:", lista_autos[i].getprecio_unitario())
                    print("")
                    
                print(len(lista_autos))    
                time.sleep(5)
                
                
            
                    
                
                
            elif opcion == 2:
                print('REGISTRAR CLIENTE')


                nombre_temp = input('Ingrese el nombre: ')
                correo_temp = input('Ingrese el correo: ')
                nit_temp = input('Ingrese el nit: ')

                cliente1 = cliente(nombre_temp, correo_temp, nit_temp)

                lista_clientes.append(cliente1)

                for i in range(len(lista_clientes)):
                    print('')
                    print("Nombre:", lista_clientes[i].getnombre())
                    print("Correo:", lista_clientes[i].getcorreo())
                    print("Nit:", lista_clientes[i].getnit())
                    print("")

                print(len(lista_clientes))
                time.sleep(5)


                
            elif opcion == 3:
                total = 0
                os.system('cls')
                print('REALIZAR COMPRA')
                nit = input('Ingrese el nit del cliente: ')

                for i in range(len(lista_clientes)):
                    if nit == lista_clientes[i].getnit():
                        print('Cliente encontrado')
                        
                    else:
                        print('Cliente no encontrado')
                        break
                
                while True:
                    print('')
                    print('---------Menu de Compra--------------------- ')
                    print('1. Agregar Auto')
                    print('2. Generar factura')

                    opcion_compra = int(input('Seleccione una opcion: '))

                    if opcion_compra == 1:
                        placa_temp = input('Ingrese la placa del auto: ')
                        for k in range(len(lista_autos)):
                            if placa_temp == lista_autos[k].getplaca():
                                lista_autos_compra.append(lista_autos[k].getmarca())
                                print('Auto agregado')
                                total = total + int(lista_autos[k].getprecio_unitario())
                                break
                               
                            else:
                                print('Auto no encontrado')
                                
                        
                    elif opcion_compra == 2:
                        print ('Generar factura')
                        print('---------------------------------------------')
                        compra1 = compra(lista_clientes[i].getnombre(), lista_clientes[i].getcorreo(), lista_clientes[i].getnit(), lista_autos_compra, total)
                        
                        print('Nombre del cliente:', compra1.getnombrec())
                        print('Correo del cliente:', compra1.getcorreoc())
                        print('Nit del cliente:', compra1.getnitc())
                        print('carros comprados')


                        #en el objeto de compra en la posicion 4 se encuentra la lista de autos comprados
                        #se recorre la lista de autos comprados y se imprime el nombre de cada auto
                        for w in range(len(lista_autos_compra)):
                            
                            print('auto : ', compra1.getautoc()[w])
                        
                        print('Total a pagar:', compra1.getprecioc())
                            

                      

                time.sleep(5)
            elif opcion == 4:
                os.system('cls')
                print('REPORTE DE COMPRAS')
                time.sleep(5)
            elif opcion == 5:
                os.system('cls')
                print('DATOS DEL ESTUDIANTE')

                print('Nombre: Carlos Heraldo Quiná Corona')
                print('Carnet: 202300645')
                
                time.sleep(5)
            elif opcion == 6:
                os.system('cls')
                print('SALIR')
                exit()
            else:
                os.system('cls')
                print('Opcion invalida')
                time.sleep(5)
            opcion = 0
            


main()




    

    
    
