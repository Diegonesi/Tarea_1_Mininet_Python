from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link, TCIntf
from mininet.log import setLogLevel

class MiTopologia(Topo):
    def build(self):
        # Agrega hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        # Agrega switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        
        # Conecta hosts a sus respectivos switches
        self.addLink(h1, s1)
        self.addLink(h2, s4)
        
        # Conecta s1 a s2
        self.addLink(s1, s2, intf=TCIntf, bw=250, delay='150ms', loss=5)
        
        # Conecta s2 a s3 con configuración de enlace
        self.addLink(s2, s3, intf=TCIntf, bw=100, delay='70ms', loss=4)
        
        # Conecta s3 a s4 con configuración de enlace
        self.addLink(s3, s4, intf=TCIntf, bw=150, delay='200ms', loss=3)
        


topo = MiTopologia()
setLogLevel('info')
net = Mininet(topo=topo)
net.start()


CLI(net)
net.stop()

