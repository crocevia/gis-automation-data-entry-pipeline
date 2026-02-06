"""

*** ArcGIS Pro script para crear capa de puntos a partir de un CSV y añadir a un mapa ***

Este Script Arcpy debe ser ejecutado dentro de la consola de Python de ArcGIS Pro

"""
import arcpy
import os

def create_iglesias_points():
    arcpy.env.overwriteOutput = True  

    # Ruta a la del proyecto actual
    aprx = arcpy.mp.ArcGISProject("CURRENT")
    gdb_path = aprx.defaultGeodatabase
    arcpy.env.workspace = gdb_path
    arcpy.env.scratchWorkspace = gdb_path

    # CSV dentro de la carpeta del proyecto
    project_folder = aprx.homeFolder
    iglesias_csv = os.path.join(project_folder, "iglesias.csv")

    if not arcpy.Exists(iglesias_csv):
        raise FileNotFoundError(f"CSV file not found: {iglesias_csv}")

    # capa en geodatabase
    output_fc = os.path.join(gdb_path, "iglesias_points")

    # Convertir tabla XY a puntos
    spatial_ref = arcpy.SpatialReference(4326)  # WGS 1984
    arcpy.management.XYTableToPoint(
        in_table=iglesias_csv,
        out_feature_class=output_fc,
        x_field="Longitude",
        y_field="Latitude",
        coordinate_system=spatial_ref
    )

    # Añadir capa al mapa
    current_map = aprx.activeMap
    print(f"Capa de puntos '{output_fc}' creada y añadida al mapa.")

if __name__ == "__main__":
    create_iglesias_points()
