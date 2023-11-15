#Para poder inicializar el programa debes instalar en cmd con pip el networkx, el pandas y el folium.
import os, folium as fl, webbrowser as wb, networkx as nx, pandas as pd, time
from pickle import TRUE
from folium.plugins import HeatMap as HM
#Empieza a contar el tiempo de ejecución
inicio = time.time()
##Hacer el mapa de calor de acuerdo a el acoso en las calles de Medellín.
def calorcito():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=';')
    lo,la = [eval(calle)[0] for calle in df["origin"]],[eval(coord)[1] for coord in df["origin"]]
    mapa_calor = fl.Map(location=[6.252, -75.57], zoom_start = 13)
    HM(list(zip(la, lo, df['harassmentRisk'])), min_opacity=0.1, radius=25, blur=25, max_zoom=1).add_to(mapa_calor)
    mapa_calor.save(os.path.join('SEEHEATMAPHARASSMENT.html')); wb.open_new_tab('SEEHEATMAPHARASSMENT.html')
    ##Timer para medir la ejecucíon del programa
    fin = time.time()
    print("Tiempo de ejecución:  " + str(fin-inicio)) 
##Cambios en el csv fastidiosito este con los NaN y eso.
def fastidiosocsv():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=';')
    df["lengthpowerharassmentRisk"] = df["length"]**df["harassmentRisk"]##Nueva columna con la distancia mas corta elevada al acoso.
    suma = df['harassmentRisk'].sum()
    contadorcito = 52658
    promedio = suma/contadorcito ##Promedio para los NaN
    df["harassmentRisk"] = df["harassmentRisk"].fillna(value = promedio) 
    df.to_csv("calles_de_medellin_con_acoso.csv",sep=';',index=False)
fastidiosocsv()
##Interfaz: opciones, excepciones, ciclos y flujo del código en general.
def interfacita():
    df = pd.read_csv("calles_de_medellin_con_acoso.csv", sep=';')
    df.head() ##Ordenamiento de los datos con pandas. :D
    tipo3,tipo4,tipo2,djk_path3 = True,True,True,True
    color = ""
    color2 = ""
    continuar = True
    ##Ciclo para determinar cuantas veces quiere el usuario ejecutar el código.
    while continuar == True: 
        print("                        ||~~**MENU DE OPCIONES**~~||                  ")
        print("1. Buscar camino mas corto.")
        print("2. Buscar camino con menos acoso.")
        print("3. Buscar los dos caminos (el mas corto y el que tenga menos acoso).")
        print("4. Buscar un camino que tome en cuenta el acoso y la distancia (distancia elevada por acoso).")
        print("5. Ver el mapa de calor de acuerdo al acoso en Medellín (Finalizar programa.)")
        hi = True
        while hi  == True:
            tipo1 = int(input())
            ##Revisión de que la opcion digitada este en el menú de opciones.
            if tipo1 == 1:
                print("                    |~*¿QUÉ DESEA HACER?*~|                    ")
                print("1. Buscar el camino mas corto ingresando coordenadas.")
                print("2. Ver opciones predeterminadas de busqueda del camino mas corto.")
                tipo2 = 'length'
                color = 'black'
                hi = False
            elif tipo1 == 2:
                print("                    |~*¿QUÉ DESEA HACER?*~|                    ")
                print("1. Buscar el camino con menos acoso ingresando coordenadas.")
                print("2. Ver opciones predeterminadas de busqueda del camino con menos acoso.")
                tipo3 = 'harassmentRisk'
                color2 = 'red'
                hi = False
            elif tipo1 == 3:
                print("                    |~*¿QUÉ DESEA HACER?*~|                    ")
                print("1. Buscar los caminos ingresando coordenadas.")
                print("2. Ver opciones predeterminadas de busqueda de los caminos.")
                tipo2 = 'length'
                tipo3 = 'harassmentRisk'
                color = 'black'
                color2 = 'red'
                hi = False
            elif tipo1 == 4:
                print("                    |~*¿QUÉ DESEA HACER?*~|                    ")
                print("1. Buscar el camino ingresando coordenadas.")
                print("2. Ver opciones predeterminadas de busqueda del camino.")
                tipo4 = 'lengthpowerharassmentRisk'
                color = 'blue'
                hi = False
            elif tipo1 == 5: ##Finaliza ejecución del programa
                print("El mapa de calor es demoradito, en un momento se abrirá. :D")
                calorcito()
                hi = False
                break
            else:
                print("La opcion digitada no está entre las opciones.")
                print("->DIGITE NUEVAMENTE<-")
        bruh = True
        while bruh == True:
            opcion1 = int(input())
            ##Revisión de que la opcion digitada este en el menú de opciones.
            if opcion1 == 1:
                print("Digite las coordenadas de inicio: ")
                partida = input()
                print("Digíte las coordenadas de llegada: ")
                llegada = input()
                bruh = False
            elif opcion1 == 2:
                print("       ->LUGAR DE PARTIDA:   ")
                print("1. Universidad EAFIT.")
                print("2. Universidad Nacional.")
                print("3. Universidad de Antioquia.")
                print("4. Universidad Luis Amigo.")
                print("5. Universidad de Medellín.")
                print("6. Casa estudiante 1.")
                print("7. Casa estudiante 2.")
                hola = True
                while hola == True:
                    seleccion1 = int(input())
                    ##Revisión de que la opcion digitada este en el menú de opciones.
                    if seleccion1 in [1,2,3,4,5,6,7]:
                        hola = False
                    else:
                        print("La opcion digitada no está entre las opciones.")
                        print("->DIGITE NUEVAMENTE<-")
                print(" ")
                print("       ->LUGAR DE LLEGADA:   ")
                print("1. Universidad EAFIT.")
                print("2. Universidad Nacional.")
                print("3. Universidad de Antioquia.")
                print("4. Universidad Luis Amigo.")
                print("5. Universidad de Medellín.")
                print("6. Casa estudiante 1.")
                print("7. Casa estudiante 2.")
                hola2 = True
                while hola2 == True:
                    seleccion2 = int(input())
                    ##Revisión de que la opcion digitada este en el menú de opciones.
                    if seleccion2 in [1,2,3,4,5,6,7]:
                        hola2 = False
                    if seleccion2 not in [1,2,3,4,5,6,7]:
                        print("La opcion digitada no está entre las opciones.")
                        print("->DIGITE NUEVAMENTE<-")
                bruh = False
            else:
                print("La opcion digitada no está entre las opciones.")
                print("->DIGITE NUEVAMENTE<-")
            
            ##Definicion de coordenadas de lugar de partida y lugar de llegada según las opciones predeterminadas.
            if opcion1 == 2:
                ##Coordenadas de salida.
                if seleccion1 == 1:
                    partida = "(-75.5778046, 6.2029412)"
                elif seleccion1 == 2:
                    partida = "(-75.5762232, 6.266327)"
                elif seleccion1 == 3:
                    partida = "(-75.5694416, 6.2650137)"
                elif seleccion1 == 4:
                    partida = "(-75.5832559, 6.2601878)"
                elif seleccion1 == 5:
                    partida = "(-75.6101004, 6.2312125)"
                elif seleccion1 == 6:
                    partida = "(-75.6107506, 6.2444087)"
                else:
                    partida = "(-75.583682, 6.2892842)"
                ##Coordenadas de llegada.
                if seleccion2 == 1:
                    llegada = "(-75.5778046, 6.2029412)"
                elif seleccion2 == 2:
                    llegada = "(-75.5762232, 6.266327)"
                elif seleccion2 == 3:
                    llegada = "(-75.5694416, 6.2650137)"
                elif seleccion2 == 4:
                    llegada = "(-75.5832559, 6.2601878)"
                elif seleccion2 == 5:
                    llegada = "(-75.6101004, 6.2312125)"
                elif seleccion2 == 6:
                    llegada = "(-75.6107506, 6.2444087)"
                else:
                    llegada = "(-75.583682, 6.2892842)"
        ##Creación de los mapitas
        mapitacorto = nx.from_pandas_edgelist(df,'origin','destination',tipo2)
        mapitacoso = nx.from_pandas_edgelist(df,'origin','destination',tipo3)
        mapitaelevado = nx.from_pandas_edgelist(df,'origin','destination',tipo4)
        djk_path1 = nx.dijkstra_path(mapitacorto,partida,llegada,tipo2)
        ##Excepciones en caso de que haya NAN en el acoso
        try: djk_path2 = nx.dijkstra_path(mapitacoso,partida,llegada,tipo3)
        except:
            print("Se actualizó el archivo csv, por favor vuelva a digitar las opciones que busca.")
            fastidiosocsv()
            interfacita()
            return None
        try: djk_path3 = nx.dijkstra_path(mapitaelevado,partida,llegada,tipo4)
        except:
            print("Se actualizó el archivo csv, por favor vuelva a digitar las opciones que busca.")
            fastidiosocsv()
            interfacita()
        ##Manejo de Strings para cambiar de posición las coordenadas y que el Folium funcione.
        for i in range(len(djk_path1)):
            djk_path1[i] = eval(djk_path1[i])[::-1]
        for i in range(len(djk_path2)):
            djk_path2[i] = eval(djk_path2[i])[::-1]
        for i in range(len(djk_path3)):
            djk_path3[i] = eval(djk_path3[i])[::-1]
        ##Crear los html
        html1 = fl.Map(location = djk_path1[0],zoom_start = 13)
        html2 = fl.Map(location = djk_path2[0],zoom_start = 13)
        html3 = fl.Map(location = djk_path3[0],zoom_start = 13)
        ##Poner rayitas para indicar el camino en los mapitas
        rayita1 = fl.PolyLine(djk_path1,color = color,weight = 5).add_to(html1)
        rayita2 = fl.PolyLine(djk_path2,color = color2,weigth = 5).add_to(html2)
        rayita3 = fl.PolyLine(djk_path3,color = color, weigth = 5).add_to(html3)
        #Ver distancia en metros de los caminos dados.
        long = nx.dijkstra_path_length(mapitacorto,partida,llegada,tipo2)
        long2 = nx.dijkstra_path_length(mapitacoso,partida,llegada,tipo3)
        long2 = long2/len(djk_path2)
        long3 = nx.dijkstra_path_length(mapitaelevado,partida,llegada,tipo4)
        ##Guardar los html y abrirlos dependiendo de que pidió el usuario.
        if tipo1 == 1:
            print("La distancia a recorrer es de: "+str(int(long))+" metros")
            html1.save(os.path.join("SEEMAPSHORT.html"))
            wb.open_new_tab("SEEMAPSHORT.html")
        elif tipo1 == 2:
            print("El promedio de acoso en la distancia a recorrer es de: " + str(long2))
            html2.save(os.path.join("SEEMAPHARASSMENT.html"))
            wb.open_new_tab("SEEMAPHARASSMENT.html")
        elif tipo1 == 3:
            print("La distancia a recorrer en el camino mas corto es de: "+str(int(long))+" metros")
            print("El promedio de acoso en la distancia a recorrer es de: " + str(long2))   
            html1.save(os.path.join("SEEMAPSHORT.html"))
            html2.save(os.path.join("SEEMAPHARASSMENT.html"))
            wb.open_new_tab("SEEMAPSHORT.html")
            wb.open_new_tab("SEEMAPHARASSMENT.html")
        else:
            print("La distancia a recorrer en el camino mas corto elevado al acoso es de: "+str(int(long3))+" metros")
            html3.save(os.path.join("SEEMAPPOWERBOTH.html"))
            wb.open_new_tab("SEEMAPPOWERBOTH.html")
        ##Timer para medir la ejecucíon del programa
        fin = time.time()
        print("Tiempo de ejecución:  " + str(fin-inicio)) 
        ##Determinar si el usuario quiere seguir ejecutando o finalizar la ejecución.
        ##Tener en cuenta que si se decide seguir utilizando el programa sin finalizar la ejecución el tiempo del programa no será el real ya que se seguirá contando mientras se realizan todas las interacciones
        print("")
        print("¿Desea seleccionar una opcion nuevamente o cerrar el programa?")
        print("1. Iniciar de nuevo en el menú principal.")
        print("2. Salir del programa.")
        h = True
        while h == True:
            salir = int(input())
            if salir == 1:
                print("Empezamos de nuevo:")
                print(" ")
                h = False
            else:
                print("~*Fin de la ejecución*~")
                print("    Hasta luego :D")
                h = False
                continuar = False

##Se sabe pa' que es esto xd
interfacita()