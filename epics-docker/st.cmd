#! /foo/epics/ioc/opcuaIoc

dbLoadDatabase("/foo/epics/ioc/opcuaIoc.dbd")
opcuaIoc_registerRecordDeviceDriver(pdbbase)
opcuaCreateSession OPC1 opc.tcp://127.0.0.1:4840/freeopcua/server
opcuaCreateSubscription SUB1 OPC1 100

dbLoadRecords("/foo/epics/ioc/db.db")
epicsEnvSet(EPICS_IOC_LOG_INET, 192.168.26.140)
iocLogInit()
iocInit()
