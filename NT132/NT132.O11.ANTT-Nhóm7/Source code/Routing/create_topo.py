from mininet.topo import Topo



class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."
        # Add hosts
        KT_PC_A = self.addHost( 'KT_PC_A', ip='192.168.1.10/24', mac='00:00:00:00:00:01',defaultRoute='via 192.168.1.1')
        
        KD_PC_B = self.addHost( 'KD_PC_B', ip='192.168.2.11/24', mac='00:00:00:00:00:02',defaultRoute='via 192.168.2.1')
        
        
        #Add Switch
        PBA_S1 = self.addSwitch('PBA_S1')
        PBB_S1 = self.addSwitch('PBB_S1')
        
        # Add links
        self.addLink( KT_PC_A, PBA_S1 )
     
        self.addLink( KD_PC_B, PBB_S1 )
        
        self.addLink( PBA_S1, PBB_S1 )
       
topos = { 'mytopo': ( lambda: MyTopo() ) } 
