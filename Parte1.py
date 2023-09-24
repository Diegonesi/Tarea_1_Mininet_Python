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
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        
        # Agrega switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        
        # Conecta hosts a s1
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        
        # Conecta s1 a s2
        self.addLink(s1, s2)
        
        # Conecta s2 a s3 con configuración de enlace
        self.addLink(s2, s3, intf=TCIntf, bw=5, delay='20ms', loss=10)
        
        # Conecta s3 a s4 con configuración de enlace
        self.addLink(s3, s4, intf=TCIntf, bw=15, delay='40ms', loss=2)
        
        # Conecta s3 a h3
        self.addLink(h3, s3)
        
        # Conecta s4 a h4
        self.addLink(h4, s4)

topo = MiTopologia()
setLogLevel('info')
net = Mininet(topo=topo)
net.start()


CLI(net)
net.stop()

