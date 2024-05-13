import networkx as nx
import matplotlib.pyplot as plt

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

