

from aedt_connection import HFSSConnection
from manage_material import MaterialManager
from manage_geometry import GeometryManager
from manage_simulation import SimulationManager

def main():
    hfss_connection = HFSSConnection().initialize_hfss() # intializes connection to desktop app

    simulation_manager = SimulationManager(hfss_connection)
    simulation_manager.initalize_simulation_setup()
    simulation_manager.run_simulation()


    # geometry_manager = GeometryManager(hfss_connection)
    # geometry_manager.get_geometries()
    # geometry_manager.modify_solid_geometry('Ground')



    # meta_material = MaterialManager(hfss_connection) # pass in hfss connection for use
    
    # meta_material.create_or_update_material(material_properties = {"permittivity": 3.5, "conductivity": 450000, "permeability": 1.5})

    # hfss_connection.setup_simulation()
    # hfss_connection.run_simulation()
    # hfss_connection.get_results("S11")

    hfss_connection.save_project() # always save project

if __name__ == "__main__":
    main()