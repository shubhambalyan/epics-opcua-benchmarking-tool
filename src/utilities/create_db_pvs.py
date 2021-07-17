# Function to create n process variable records with a specific queue size
def create_pv_records(n, q):
    ao_record = """record(ao,{})
{{
field(DTYP, "OPCUA")
field(ADEL, "-1")
field(MDEL, "-1")
field(OUT, "@OPC1 ns=2;s={} monitor=n")
}}"""
    
    ai_record = """record(ai,{})
{{
field(DTYP, "OPCUA")
field(ADEL, "-1")
field(MDEL, "-1")
field(TSE, "-2")
field(SCAN, "I/O Intr")
field(INP, "@SUB1 ns=2;s={} timestamp=source qsize={}")
}}"""
    
    ao_pv_name = "process_data_read{}:temperature"
    ai_pv_name = "process_data_read{}:temperature_rb"
    
    namespace_label = "Process_Data_read{}.Temperature"
    
    with open("db.db", "a") as myfile:
        for i in range(n):
            data = ao_record.format(ao_pv_name.format(i+1), namespace_label.format(i+1))
            data = data + '\n' + ai_record.format(ai_pv_name.format(i+1), namespace_label.format(i+1), q) + '\n'
            myfile.write(data)
    
    print("db.db file with {} PVS and {} qsize created.".format(n, q))

if __name__ == '__main__':
    number_of_pvs = 2000
    queue_size = 51
    create_pv_records(number_of_pvs, queue_size)
