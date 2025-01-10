import esphome.codegen as cg
import esphome.config_validation as cv

# from esphome.components import uart
from esphome.const import CONF_ID

# DEPENDENCIES = ["uart"]

batteryMonitor_ns = cg.esphome_ns.namespace("batteryMonitor")
batteryMonComponent = batteryMonitor_ns.class_("MAX17048Sensor ", cg.Component)  # , uart.UARTDevice)

CONFIG_SCHEMA = (
    cv.Schema({cv.GenerateID(): cv.declare_id(batteryMonComponent)}).extend(cv.COMPONENT_SCHEMA)
    # .extend(uart.UART_DEVICE_SCHEMA)
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    # yield uart.register_uart_device(var, config)
