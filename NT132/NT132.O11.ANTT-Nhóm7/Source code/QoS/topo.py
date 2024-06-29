from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from time import sleep


class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."
        # Add hosts
        KT_PC_A  = self.addHost( 'KT_PC_A', ip='192.168.4.10/24')
        KT_PC_B  = self.addHost( 'KT_PC_B', ip='192.168.4.11/24')
     
       	KD_PC_A  = self.addHost( 'KD_PC_A', ip='192.168.4.13/24')
       	KD_PC_B  = self.addHost( 'KD_PC_B', ip='192.168.4.14/24')        
        
        #Add Switch
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        
        # Add links
        self.addLink( KT_PC_A, s1 )
        self.addLink( KT_PC_B, s1 )
     
        self.addLink( KD_PC_A, s2 )
        self.addLink( KD_PC_B, s2 )
        
        self.addLink( s1, s2 )
        
topos = { 'mytopo': ( lambda: MyTopo() ) } 
