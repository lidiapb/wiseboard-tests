import dbus
from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop

def signal_handler(*args, **kwargs):
    for i, arg in enumerate(args):
        print("arg:%d        %s" % (i, str(arg)))
    print('kwargs:')
    print(kwargs)
    print('---end----')

DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()
#register your signal callback
bus.add_signal_receiver(signal_handler,
                        bus_name='org.bluez')

loop = GLib.MainLoop()
print("Listening...")
loop.run()