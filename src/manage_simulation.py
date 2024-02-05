import os
import pyaedt
import time

import pandas as pd
import numpy as np

class SimulationManager:
    '''Class to manage simulation settings'''
    def __init__(self, hfss_connection):

        self.hfss = hfss_connection
        self.setup = None # this is the simulation object
        self.simulation_properties = None # simulation properties
        self.solution_data = None # solution data class
        self.plot = None # post processor class
        self.expressions = None # this will hold the setup report names
        self.design_properties = None

        self.pandas_frame = pd.DataFrame() # initialize panda data frame here

    def get_setups(self):
        return self.hfss.setups


    def initalize_simulation_setup(self):
        
        '''Gets setup object and initializes parameters for the simulation'''
        self.setup = self.hfss.setups[0] #gets first setup name (under analysis tab)
        self.setup.update() # call this to save changes to setup
        return

    def get_design_properties(self):
        design_properties = self.hfss.available_variations.nominal_w_values_dict
        return design_properties

    def get_s_parameters(self):
        """Retrieve S11 and S12 parameter magnitude for a specific frequency after simulation."""
        solution_data = self.setup.get_solution_data(expressions=['dB(S(From_Bottom:1,From_Top:1))','dB(S(From_Top:1,From_Top:1))','dB(S(From_Bottom:2,From_Top:2))','dB(S(From_Top:2,From_Top:2))'])
        print(solution_data.intrinsics)
        print("\n\n\n")
        print(solution_data.nominal_variation)
        print("\n\n\n")

        print(solution_data.primary_sweep_values)
        print("\n\n\n")



        # S21, S12, S11, S22
        # S21 AND S12 ~ Transmission of a signal ~ 0dB
        # S11 AND S22 ~ Reflection of a signal ~ -infinty
        s_params = {expression: solution_data.data_real(expression)[0] for index, expression in enumerate(solution_data.expressions)}
        return s_params
    

    def run_simulation(self):
        """Run the simulation."""
        self.hfss.analyze(num_cores=4, num_gpu=1)
        design_properties = self.get_design_properties()
        s_params = self.get_s_parameters()
        new_row_data = {**design_properties, **s_params}
        self.pandas_frame = self.pandas_frame._append(new_row_data, ignore_index=True)

    def stop_simulation(self, filename):
        """Save the pandas DataFrame to a CSV file."""
        self.pandas_frame.to_csv(filename, index=False)
        print(f"DataFrame saved to {filename}.")
