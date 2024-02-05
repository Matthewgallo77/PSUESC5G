import os
import numpy as np
import pyaedt


class VariableManager:
    '''Class to manage geometry (solids and sheets)'''
    def __init__(self, hfss_connection, stop_event):
        self.hfss = hfss_connection
        # self.modeler = self.hfss.modeler
        self.variable_manager = self.hfss.variable_manager
        self.variables = self.variable_manager.variables
        self.stop_event = stop_event

        self.solids = {}
        self.sheets = {}

    def modify_parameters_and_run_simulation(self, simulation_manager):
            # Define the range and increment for each variable
            inscribe_r_range = np.arange(0.5, 1.05, 0.05)
            sub_h_range = np.arange(0.25, 1.55, 0.05)
            metal_h_range = np.arange(0.25, 1.05, 0.05)

            # Loop through each combination of parameters
            for inscribe_r in inscribe_r_range:
                self.variable_manager['inscribe_r'] = f"{inscribe_r}mm"
                for sub_h in sub_h_range:
                    self.variable_manager['sub_h'] = f"{sub_h}mm"
                    element_r_max = inscribe_r  # Element_r cannot be larger than inscribe_r
                    element_r_range = np.arange(0.25, element_r_max + 0.05, 0.05)
                    for element_r in element_r_range:
                        self.variable_manager['Element_r'] = f"{element_r}mm"
                        for metal_h in metal_h_range:
                            self.variable_manager['metal_h'] = f"{metal_h}mm"
                            simulation_manager.initalize_simulation_setup()
                            simulation_manager.run_simulation()

                            if self.stop_event.is_set():  # Check if the stop event is set
                                print("Simulation stopped by user.")
                                return
                                      

                    

    

    
   

    # def create_geometry(self, geometry_type, parameters, name, material):
    #     """Create a geometry object."""
    #     if geometry_type == 'box':
    #         return self.hfss.modeler.create_box(position=parameters['position'],
    #                                             dimensions_list=parameters['dimension'],
    #                                             name=name, matname=material)
    #     else:
    #         print(f"Geometry type '{geometry_type}' not recognized.")
    #         return None
        
    # def modify_solid_geometry(self, solid_name):
    #     """Modify an existing geometry object."""
    #     if solid_name in self.solids:
    #         object = self.solids[solid_name] # Primite.Object3d
        
      
    #     else:
    #         print(f"Solid with name '{solid_name}' not found in the solids dictionary.")





    # def get_geometries(self):
    #     """List solids and sheets in the model and store them in dictionaries."""
    #     # fetch solid and sheets objects
    #     solid_objects = self.modeler.solid_objects
    #     sheet_objects = self.modeler.sheet_objects
    #     for solid in solid_objects:
    #         self.solids[solid.name] = solid

    #     for sheet in sheet_objects:
    #         self.sheets[sheet.name] = sheet


    
    # def get_objects(self):
    #     return self.modeler.get_objects()
    


