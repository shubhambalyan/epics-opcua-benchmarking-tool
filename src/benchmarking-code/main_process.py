import pandas as pd
import time
import epics
import random
import os
from epics import caget, caput, cainfo, PV
import multiprocessing
from threading import Thread

class BenchmarkingTask:
    def __init__(self, no_of_pvs, time_interval, folder_label):
        self.no_of_pvs = no_of_pvs
        self.time_interval = time_interval/1000 # Convert milliseconds to seconds for the sleep()
        self.folder_label = folder_label

    # Function to display PV values
    def display_PV_values(self, pvlist):
        for pv in pvlist:
            print("PV Name: {}; PV Value: {}".format(pv, caget(pv)))
    
    # Create the process variables PV list
    def create_pvs_list(self):
        ao_pv_list = []
        ai_pv_list = []
        ao_pv_name = "process_data_read{}:temperature"
        ai_pv_name = "process_data_read{}:temperature_rb"
        for i in range(self.no_of_pvs):
            ao_pv_list.append(ao_pv_name.format(i+1))
            ai_pv_list.append(ai_pv_name.format(i+1))
        
        return ao_pv_list, ai_pv_list
        
    def create_directory(self):
        folder_name = '{}_{}_PVS_{}_ms'.format(self.folder_label, self.no_of_pvs, self.time_interval*1000)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        return folder_name
    
    # Function to read and write to PVs at regular time interval
    def read_and_write_PVs(self, pv_name, n, folder_name):
        d = []
        pv1 = PV(pv_name)
        for i in range(20): 
            try:
                pv1.put(i+n)
                time.sleep(self.time_interval) 
                timestmp = pv1.timestamp
                ms = round(timestmp*1000)
                val = pv1.get()
                d.append((pv_name, i+n, val, ms)) 
            except TypeError as e:
                continue
        
        df = pd.DataFrame(d, columns=('PV Name', 'Value Written', 'Value Read', 'Time'))
        df['Delta'] = (df['Time']-df['Time'].shift()).fillna(0)
        csv_name = '{}_delta.csv'.format(pv_name)
        file_name = folder_name + '/' + csv_name
        df.to_csv(file_name, encoding='utf-8', index=False)
    
    def start_task(self):
        ao_pvlist, ai_pvlist = self.create_pvs_list()
        
        # Display some initial values
        print("PVs Initial Values --> ")
        self.display_PV_values(random.sample(ao_pvlist, 10))
        
        folder_name = self.create_directory()
        
        # Create n threads, one for each process variable
        jobs = []
        val = 0
        for i in range(self.no_of_pvs):
            # Declare new processes and pass arguments to it
            val = val + 2 
            jobs.append(Thread(target=self.read_and_write_PVs, args=(ao_pvlist[i], val, folder_name)))
        
        for job in jobs:
            job.start()
                    
        # Starting jobs in batches
        """count = 0
        for job in jobs:
            job.start()
            count = count + 1
            if count == 100:
                time.sleep(1)
                count = 0"""
    
        for job in jobs:
            job.join()
        
        print("PVs Final Values --> ")
        self.display_PV_values(random.sample(ao_pvlist, 10))
