import os
import pyaedt

class SimulationManager:
    '''Class to manage simulation settings'''
    def __init__(self, hfss_connection):

        self.hfss = hfss_connection
        self.setup = None # this is the simulation object
        self.simulation_properties = None # simulation properties
        self.solution_data = None

    def initalize_simulation_setup(self):
        
        '''Gets setup object and initializes parameters for the simulation'''
        self.setup = self.hfss.setups[0] # gets first setup name (under analysis tab)
        self.simulation_properties = self.setup.props # gets the simulation properties

        self.setup.update() # call this to save changes to setup

    def run_simulation(self):
        """Run the simulation."""
        self.solution_data = self.hfss.post
        self.hfss.analyze()
        # info = self.hfss.get_report_data()