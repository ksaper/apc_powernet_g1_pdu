from apc.pm_pdu_handler import PmPduHandler
from cloudshell.power.pdu.power_resource_driver_interface import PowerResourceDriverInterface
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.context import AutoLoadDetails, InitCommandContext, ResourceCommandContext
from log_helper import LogHelper


class ApcPowernetG1PduDriver (ResourceDriverInterface, PowerResourceDriverInterface):
    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def get_inventory(self, context):
        handler = PmPduHandler(context)

        return handler.get_inventory()

    def PowerCycle(self, context, ports, delay):
        try:
            float(delay)
        except ValueError:
            raise Exception('Delay must be a numeric value')

        handler = PmPduHandler(context)
        return handler.power_cycle(ports, float(delay))

    def PowerOff(self, context, ports):
        handler = PmPduHandler(context)

        return handler.power_off(ports)

    def PowerOn(self, context, ports):
        handler = PmPduHandler(context)

        return handler.power_on(ports)
