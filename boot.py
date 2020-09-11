# This file is executed on every boot (including wake-boot from deepsleep)
# WIFI setup + WebREPL
import esp
esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WIFIname', '')	# put SSID here #
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
do_connect()
import webrepl
webrepl.start()
gc.collect()

## need to manual setup webrepl by using import webrepl_setup then follow the instruction ##
