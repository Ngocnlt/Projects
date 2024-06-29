sudo ifconfig PBA_S1 192.168.1.1/24 up
sudo ifconfig PBB_S1 192.168.2.1/24 up

sudo ovs-ofctl add-flow PBA_S1 arp,action=normal


sudo ovs-ofctl add-flow PBA_S1 ip,nw_dst=192.168.1.10,actions=mod_dl_dst=00:00:00:00:00:01,output:1

sudo ovs-ofctl add-flow PBA_S1 ip,nw_dst=192.168.2.0/24,actions=mod_dl_src=de:66:75:92:fb:3d,mod_dl_dst=26:a8:af:1a:6d:05,dec_ttl,output:2



sudo ovs-ofctl add-flow PBB_S1 arp,action=normal

sudo ovs-ofctl add-flow PBB_S1 ip,nw_dst=192.168.2.11,actions=mod_dl_dst=00:00:00:00:00:04,output:1

sudo ovs-ofctl add-flow PBB_S1 ip,nw_dst=192.168.1.0/24,actions=mod_dl_src=26:a8:af:1a:6d:05,mod_dl_dst=de:66:75:92:fb:3d,dec_ttl,output:2

sudo ovs-appctl ofproto/trace KT_PC_A in_port=1,ip,nw_src=192.168.1.10,nw_dst=192.168.2.11,dl_src=00:00:00:00:00:01,nw_ttl=64