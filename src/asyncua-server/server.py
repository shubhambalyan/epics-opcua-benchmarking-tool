import logging
import asyncio
import sys
sys.path.insert(0, "..")

from asyncua import ua, Server
from asyncua.common.methods import uamethod

async def main():
    _logger = logging.getLogger('asyncua')
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://127.0.0.1:4840/freeopcua/server/')

    # setup our own namespace, not really necessary but should as spec
    uri = 'http://examples.freeopcua.github.io'
    idx = await server.register_namespace(uri)
    
    object_namespace = 'ns=2;s=Process_Data_read{}.Temperature'
    variable_namespace = 'ns=2;s=Process_Data_read{}.Temperature.{}'
    obj_description = 'Process Data Read {}'
    variable_description = 'Var {}'
    
    no_of_pvs = 100 # Number of process variables in the system
    val = 0.0
    
    for i in range(no_of_pvs):
        val = val + 1
        obj1 = await server.nodes.objects.add_object(object_namespace.format(i+1), obj_description.format(i+1))
        var1 = await obj1.add_variable(variable_namespace.format(i+1, i+1), variable_description.format(i+1), val)
        await var1.set_writable()

    #-------------------------------EXAMPLE FROM ASYNCUA STARTS-----------------------------
    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    myobj = await server.nodes.objects.add_object(idx, 'MyObject')
    myvar = await myobj.add_variable(idx, 'MyVariable', 6.7)
    # Set MyVariable to be writable by clients
    await myvar.set_writable()
    #await server.nodes.objects.add_method(ua.NodeId('ServerMethod', 2), ua.QualifiedName('ServerMethod', 2), func, [ua.VariantType.Int64], [ua.VariantType.Int64])
    _logger.info('Starting server!')
    async with server:
        while True:
            await asyncio.sleep(1)
            new_val = await myvar.get_value() + 0.1
            #_logger.info('Set value of %s to %.1f', myvar, new_val)
            await myvar.write_value(new_val)
    #-------------------------------EXAMPLE FROM ASYNCUA ENDS-------------------------------


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    asyncio.run(main(), debug=True)
