import os
import pyaedt

class MaterialManager:
    '''Class to manage material properties'''
    def __init__(self, hfss_connection):
        self.hfss = hfss_connection
        self.material_name = 'CustomMaterial'
        self.freq_range = "1Ghz-10GHz" # freq range should not differ much
        
    def create_or_update_material(self, material_properties):
        """Create a new material or update it if it already exists."""
        existing_material = self.material_exists(self.material_name)
        if existing_material:
            self.update_material(existing_material, material_properties)
        else:
            self.create_material(material_properties)

    def create_material(self, material_properties):
        """Create a new material with given properties."""
        material = self.hfss.materials.add_material(self.material_name)
        for prop, value in material_properties.items():
            setattr(material, prop, value)
        return material

    def material_exists(self, material_name):
        """Check if a material already exists in the project."""
        return self.hfss.materials.checkifmaterialexists(material_name)
        

    def update_material(self, material, material_properties):
        """Update an existing material's properties."""
        for prop, value in material_properties.items():
            setattr(material, prop, value)
    
    def get_results(self, result_type):
        """Extract and print simulation results."""
        results = self.hfss.post.get_report_data(expression=result_type)
        print(f"Results for {result_type}: {results}")
        return results
    

