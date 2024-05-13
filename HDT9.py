import networkx as nx
import matplotlib.pyplot as plt

def crear_grafo_desde_archivo(archivo):
    G = nx.Graph()
    with open(archivo, 'r') as file:
        for line in file:
            estacion_salida, estacion_destino, costo = line.strip().split(', ')
            costo = int(costo)
            G.add_edge(estacion_salida.strip('"'), estacion_destino.strip('"'), weight=costo)
            G.add_edge(estacion_destino.strip('"'), estacion_salida.strip('"'), weight=costo) # Agregar la ruta inversa
    return G

def mostrar_destinos_disponibles(G, estacion_salida):
    print("Destinos disponibles desde", estacion_salida, ":")
    for vecino in G.neighbors(estacion_salida):
        print(vecino)
        
def dijkstra(G, estacion_salida):
    shortest_paths = nx.single_source_dijkstra_path_length(G, estacion_salida)
    return shortest_paths

def mostrar_grafo(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='k', linewidths=1, font_size=5)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo de Rutas")
    plt.show()
        
    while True:
        print("\n---- Menú ----")
        print("1. Ver destinos desde una estación de salida.")
        print("2. Encontrar la ruta más barata a todos los destinos desde una estación de salida.")
        print("3. Ver el grafo de rutas.")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            estacion_salida = input("Ingrese la estación de salida: ")
            if estacion_salida in G.nodes:
                mostrar_destinos_disponibles(G, estacion_salida)
            else:
                print("La estación de salida no existe en el sistema.")
        
        elif opcion == '2':
            estacion_salida = input("Ingrese la estación de salida: ")
            if estacion_salida in G.nodes:
                shortest_paths = dijkstra(G, estacion_salida)
                print("Rutas más baratas desde", estacion_salida)
                for destino, costo in shortest_paths.items():
                    print(destino, ":", costo)
            else:
                print("La estación de salida no existe en el sistema.")
        
        elif opcion == '3':
            mostrar_grafo(G)

        elif opcion == '4':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

