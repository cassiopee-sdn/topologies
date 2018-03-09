"""
Typical topology for 2 group switches
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def HierarchyTopology():

    net = Mininet( topo=None, build=False)

    info("***Create nodes***\n")
    h1 = net.addHost( 'h1', mac='01:00:00:00:01:00', ip='192.168.0.1/24' )
    h2 = net.addHost( 'h2', mac='01:00:00:00:02:00', ip='192.168.0.2/24' )

    info("***Create switches***\n")
    s0 = net.addSwitch( 's0', listenPort=6634, mac='00:00:00:00:00:01' )
    s1 = net.addSwitch( 's1', listenPort=6634, mac='00:00:00:00:00:02' )
    s2 = net.addSwitch( 's2', listenPort=6634, mac='00:00:00:00:00:03' )
    s3 = net.addSwitch( 's3', listenPort=6634, mac='00:00:00:00:00:04' )
    s4 = net.addSwitch( 's4', listenPort=6634, mac='00:00:00:00:00:05' )
    s5 = net.addSwitch( 's5', listenPort=6634, mac='00:00:00:00:00:06' )

    info("***Creating links***\n")
    net.addLink( h1,s0 )
    net.addLink( s0,s1 )
    net.addLink( s0,s2 )
    net.addLink( s1,s3 )
    net.addLink( s1,s4 )
    net.addLink( s2,s3 )
    net.addLink( s2,s4 )
    net.addLink( s3,s5 )
    net.addLink( s4,s5 )
    net.addLink( s5,h2 )

    info("***Add Controllers***")
    odl1 = net.addController( 'c1', controller=RemoteController, ip='192.168.103.142', port=6633)
    odl2 = net.addController( 'c2', controller=RemoteController, ip='192.168.103.143', port=6633)

    net.build()

    info("***Connect each switch to a different controller***")
    s0.start( [odl1] )
    s1.start( [odl1] )
    s2.start( [odl1] )
    s3.start( [odl2] )
    s4.start( [odl2] )
    s5.start( [odl2] )

    s1.cmdPrint('ovs-vsctl show')

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    HierarchyTopology()

