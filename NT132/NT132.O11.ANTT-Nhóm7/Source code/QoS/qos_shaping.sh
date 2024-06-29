# file config 
sudo ovs-vsctl -- set port s1-eth3 \
qos=@newqos -- --id=@newqos \
create qos type=linux-htb other-config:max-rate=100000000 \
queues=1=@q1,2=@q2 \
-- --id=@q1 create queue other-config:min-rate=70000000 \
-- --id=@q2 create queue other-config:min-rate=30000000

#set port21 -> queue 1
sudo ovs-ofctl add-flow s1 tcp,tp_dst=21,actions=set_queue:1,normal

#set port 80 -> queue 2
sudo ovs-ofctl add-flow s1 tcp,tp_dst=80,actions=set_queue:2,normal
