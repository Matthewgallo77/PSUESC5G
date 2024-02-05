import signal
import threading
import atexit

from aedt_connection import HFSSConnection
from manage_material import MaterialManager
from manage_variables import VariableManager
from manage_simulation import SimulationManager


stop_event = threading.Event()

def listen_for_exit_request():
    input("Press <Enter> to stop the simulation...\n")
    stop_event.set()  # Set the event to signal that the user wants to stop the simulation
    print("Stopping simulation...")


def on_exit(simulation_manager, hfss_connection):
    print("Finalizing...")
    simulation_manager.stop_simulation('simulation_results.csv')
    hfss_connection.save_project()
    print("DataFrame saved and project saved. Program terminated safely.")


def main():
    global stop_requested
    hfss_connection = HFSSConnection().initialize_hfss() # intializes connection to desktop app
    simulation_manager = SimulationManager(hfss_connection)
    variable_manager = VariableManager(hfss_connection, stop_event)

    atexit.register(on_exit, simulation_manager, hfss_connection)

    exit_thread = threading.Thread(target=listen_for_exit_request)
    exit_thread.start()
    try:
        while not stop_event.is_set():
            variable_manager.modify_parameters_and_run_simulation(simulation_manager)
            
    finally:
        on_exit(simulation_manager, hfss_connection)


if __name__ == "__main__":
    main()