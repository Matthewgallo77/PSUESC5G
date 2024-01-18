import os
import pyaedt
import numpy as np
import time

class SimulationManager:
    '''Class to manage simulation settings'''
    def __init__(self, hfss_connection):

        self.hfss = hfss_connection
        self.setup = None # this is the simulation object
        self.simulation_properties = None # simulation properties
        self.solution_data = None # solution data class
        self.plot = None # post processor class
        self.expressions = None # this will hold the setup report names

    def initalize_simulation_setup(self):
        
        '''Gets setup object and initializes parameters for the simulation'''
        self.setup = self.hfss.setups[0] #gets first setup name (under analysis tab)
        self.simulation_properties = self.setup.props # gets the simulation properties
        self.setup.update() # call this to save changes to setup


    def get_s_parameters(self):
        """Retrieve S11 and S12 parameter data for a specific frequency after simulation."""

        variations = self.hfss.available_variations.nominal_w_values_dict
        # For a single frequency point, update the variations dictionary accordingly
        s11 = self.setup.get_solution_data(expressions=['mag(S(FloquetPort1:1,FloquetPort1:1))','mag(S(FloquetPort2:1,FloquetPort2:1))'])
        s11.export_data_to_csv('test1.csv')

        # s11_data = self.hfss.post.get_solution_data(
        #     "S(1,1)",
        #     self.hfss.nominal_sweep,
        #     variations=variations
        # )



        # '''magnitude of s11 (reflective) and s12 transmissive '''
        # s11_mag = s11_data.data_magnitude("S(1,1)") 


    def run_simulation(self):
        """Run the simulation."""
        self.get_s_parameters()    