import os
import pyaedt

class HFSSConnection:
    def __init__(self):
        self.project_name = self.find_aedt_file(os.getcwd())
        self.design_name = 'HFSSDesign1' #input("Enter design name: ")  # input design name
        self.specified_version = '2023.2'
        self.new_desktop_session = False
        self.student_version = True
        self.hfss = None
        self.modeler = None

        self.simulation_name = 'TestSim'

    @staticmethod
    def find_aedt_file(directory):
        """Find the first .aedt file in the given directory."""
        aedt_files = [f for f in os.listdir(directory) if f.endswith('.aedt')]
        if aedt_files:
            return os.path.splitext(aedt_files[0])[0]
        else:
            print('.aedt file not found in', directory)
            return None

    def initialize_hfss(self):
        
        self.hfss = pyaedt.Hfss(specified_version=self.specified_version, projectname=self.project_name, designname=self.design_name, new_desktop_session=self.new_desktop_session, student_version=self.student_version)
        self.modeler = self.hfss.modeler
        return self.hfss # this will be global object to interact with application

    def save_project(self):
        self.hfss.save_project() # saves changes to project 

    def get_results(self, result_type):
        """Extract and print simulation results."""
        try:
            results = self.hfss.post.copy_report_data(expression=result_type)
            print(f"Results for {result_type}: {results}")
            return results
        except AttributeError:
            print(f"Error: Method to get results for {result_type} not found.")
            return None





