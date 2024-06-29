#Configuring QoS policing in switch s1
sudo ovs-vsctl set interface s1-eth1 ingress_policing_rate=50000
