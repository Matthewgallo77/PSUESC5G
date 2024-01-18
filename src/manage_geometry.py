   
import os
import pyaedt

class GeometryManager:
    '''Class to manage geometry (solids and sheets)'''
    def __init__(self, hfss_connection):
        self.hfss = hfss_connection
        self.modeler = self.hfss.modeler

        self.solids = {}
        self.sheets = {}

    def create_geometry(self, geometry_type, parameters, name, material):
        """Create a geometry object."""
        if geometry_type == 'box':
            return self.hfss.modeler.create_box(position=parameters['position'],
                                                dimensions_list=parameters['dimension'],
                                                name=name, matname=material)
        else:
            print(f"Geometry type '{geometry_type}' not recognized.")
            return None
        
    def modify_solid_geometry(self, solid_name):
        """Modify an existing geometry object."""
        if solid_name in self.solids:
            object = self.solids[solid_name]
              # if object:
        #     for prop, value in new_parameters.items():
        #         object.set_property_value(prop, value)
        # else:
        #     print(f"Object '{object_name}' not found.")
            # Perform operations on the object here
            # Example: object.move([10, 0, 0])
        else:
            print(f"Solid with name '{solid_name}' not found in the solids dictionary.")



    def get_geometries(self):
        """List solids and sheets in the model and store them in dictionaries."""
        # fetch solid and sheets objects
        solid_objects = self.modeler.solid_objects
        sheet_objects = self.modeler.sheet_objects
        for solid in solid_objects:
            self.solids[solid.name] = solid

        for sheet in sheet_objects:
            self.sheets[sheet.name] = sheet


    
    def get_objects(self):
        return self.modeler.get_objects()

