#! /home/shubham/opcua_test/ioc/opcuaIoc

dbLoadDatabase("/home/shubham/opcua_test/ioc/opcuaIoc.dbd")
opcuaIoc_registerRecordDeviceDriver(pdbbase)
opcuaCreateSession OPC1 opc.tcp://127.0.0.1:4840/freeopcua/server
opcuaCreateSubscription SUB1 OPC1 20

dbLoadRecords("/home/shubham/benchmarking/code/db.db")
epicsEnvSet(EPICS_IOC_LOG_INET, 192.168.26.140)
epicsEnvSet(EPICS_IOC_LOG_FILE_NAME, "/home/shubham/epics_logs/epics.log")
iocLogInit()
iocInit()
