from main_process import BenchmarkingTask


if __name__ == "__main__":
    no_of_pvs = 2000 # Number of process variables in the system
    time_interval = 20 # Time interval between two calls to epics server in milliseconds
    folder_label = "physical_server" # 'physical_server' or 'docker' or 'VM'
    obj = BenchmarkingTask(no_of_pvs, time_interval, folder_label)
    try:
        obj.start_task()
    except KeyboardInterrupt:
        print('Exiting!')
