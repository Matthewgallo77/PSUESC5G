

from aedt_connection import HFSSConnection
from manage_material import MaterialManager
from manage_geometry import GeometryManager

def main():
    hfss_connection = HFSSConnection() # intializes connection to desktop app
    hfss_connection.initialize_hfss()

    meta_material = MaterialManager(hfss_connection) # pass in hfss connection for use
    meta_material.create_or_update_material(material_properties = {"permittivity": 3.5, "conductivity": 450000, "permeability": 1.5})

    geometry_manager = GeometryManager(hfss_connection)
    geometry_manager.create_geometry("box", {"position": [0, 0, 0], "dimension": [10, 10, 10]}, "MyBox", "CustomMaterial")

    # hfss_connection.setup_simulation()
    # hfss_connection.run_simulation()
    # hfss_connection.get_results("S11")

    hfss_connection.save_project() # always save project

if __name__ == "__main__":
    main()