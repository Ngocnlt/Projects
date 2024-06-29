#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    KTPCA = net.addHost('KT-PC-A', cls=Host, ip='192.168.1.10', defaultRoute=None)
    KDPCA = net.addHost('KD-PC-A', cls=Host, ip='192.168.2.10', defaultRoute=None)
    KTPCB = net.addHost('KT-PC-B', cls=Host, ip='192.168.1.11', defaultRoute=None)
    KDPCB = net.addHost('KD-PC-B', cls=Host, ip='192.168.2.11', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(KTPCA, s1)
    net.addLink(s1, KDPCA)
    net.addLink(KTPCB, s2)
    net.addLink(s2, KDPCB)
    net.addLink(s1, s2)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

