"""

*** Programa de Registro de Iglesias del Románico Sardo ***

Este programa sirve como el primer paso en un proceso más largo en el que aplico
el Python y el ArcPy a un proyecto de interés personal. La idea es a partir del csv 
que genera este programa, generar una capa de puntos en ArcGIS Pro mediante el ArcPy, 
lo que será la etapa que a continuación. 

Aunque yo haya elegido este ejemplo orientado hacia a la gestión del patrimonio,
los conceptos y el esqueleto general se pueden aplicar a otros casos, como la
planificación urbana, la gestión ambiental, y muchos más. 

Últimamente se habla de la intersección entre las humanidades y la tecnología,
y considero que éste podría ser un ejemplo de como estos dos mundos se cruzan.


"""

import pandas as pd
import os

COLUMNS = [
    "ID",
    "Nombre",
    "Latitude",
    "Longitude",
    "Municipio",
    "Provincia",
    "Año_Contrucción",
    "Siglo",
    "Estado",
    "Condición",
    "Notas",
]

FILENAME = "iglesias.csv"

def main():
    print("\n=== Registro de Iglesias del Románico Sardo ===")
    print("\nCampos:", ", ".join(COLUMNS))
    print("\nUtiliza grados decimales para la latitud y la longitud (WGS84).")
    print("\nPulsa Enter para dejar campo en blanco.\n")

    data = []

    if os.path.exists(FILENAME):
        try:
            df = pd.read_csv(FILENAME)
            data = df.to_dict(orient="records")
            print(f"Se han cargado {len(data)} registros previos.")
        except Exception as e:
            print("Error cargando el archivo previo:", e)
    

    while True:
        print("\nElegir una opción:")
        print("1) Añadir iglesia")
        print("2) Consultar datos")
        print("3) Guardar")
        print("4) Eliminar datos")
        print("5) Salir")

        choice = input("> ").strip()

        if choice == "1":
            row = {}
            print("\nDatos de iglesia:")
            for col in COLUMNS:
                row[col] = input(f"  {col}: ").strip()
            data.append(row)
            print("Iglesia Añadida.")

        elif choice == "2":
            if not data:
                print("\nAún no hay datos.")
            else:
                df = pd.DataFrame(data, columns=COLUMNS)
                print("\nDatos guardados en ruta", os.path.abspath(FILENAME))
                print(df.to_string(index=False))

        elif choice == "3":
            if not data:
                print("\nNo hay nada para guardar.")
                continue

            df = pd.DataFrame(data, columns=COLUMNS)

            try:
                df.to_csv(FILENAME, index=False)
                print(f"\nGuardado en: {os.path.abspath(FILENAME)}")
            except Exception as e:
                print("Error guardando archivo:", e)

    

        elif choice == "5":
            print("¡Adiós!")
            break
        
        
        elif choice == "4":
            if not data:
                print("\nNo hay datos para eliminar.")
                continue

            id_delete = input("El ID de la iglesia a eliminar: ").strip()

            for i, row in enumerate(data):
                if row["ID"] == id_delete:
                    confirm = input(
                        f"¿Eliminar '{row['Nombre']}'? (s/n): "
                    ).strip().lower()

                    if confirm == "s":
                        data.pop(i)
                        print("Registro eliminado.")
                    else:
                        print("Eliminación cancelada.")
                    break
            else:
                print("ID no encontrado.")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
