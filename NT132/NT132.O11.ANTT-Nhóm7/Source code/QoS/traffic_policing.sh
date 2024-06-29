#show metering features supported by ovs
sudo ovs-ofctl -O OpenFlow15 meter-features s1

#add a meter in switch S1 and limit the rate to 300Mbps
sudo ovs-ofctl -O OpenFlow15 add-meter s1 meter=1,kbps,band=type=drop,rate=300000

#install a manual flow in switch S1(port21)
sudo ovs-ofctl -O OpenFlow15 add-flow s1 tcp,tp_dst=21,actions=meter:1,output:3

#install a manual flow in switch S1(port80)
sudo ovs-ofctl -O OpenFlow15 add-flow s1 tcp,tp_dst=80,actions=meter:1,output:3
