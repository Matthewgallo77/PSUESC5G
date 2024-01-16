
import os
import pyaedt

class GeometryManager:
    '''Class to manage geometry (solids and sheets)'''
    def __init__(self, hfss_connection):
        self.hfss = hfss_connection
        self.modeler = self.hfss.modeler

    def create_geometry(self, geometry_type, parameters, name, material):
        """Create a geometry object."""
        if geometry_type == 'box':
            return self.hfss.modeler.create_box(position=parameters['position'],
                                                dimensions_list=parameters['dimension'],
                                                name=name, matname=material)
        # Add other geometry types here (cylinder, sphere, etc.)
        else:
            print(f"Geometry type '{geometry_type}' not recognized.")
            return None
        
    def modify_geometry(self, object_name, new_parameters):
        """Modify an existing geometry object."""
        object = self.hfss.modeler[object_name]
        if object:
            for prop, value in new_parameters.items():
                object.set_property_value(prop, value)
        else:
            print(f"Object '{object_name}' not found.")

    def list_geometries(self):
        """List solids and sheets in the model."""
        solids = self.modeler.solid_names
        sheets = self.modeler.sheet_names
        return solids, sheets
