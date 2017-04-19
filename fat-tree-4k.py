#!/usr/bin/python

from mininet.net import Mininet
from mininet.term import makeTerm
from mininet.node import RemoteController
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import json
from bottle import route, run, request

net = "net_object"


def myFatTree():
    global net
    net = Mininet(topo=None,
                  link=TCLink,
                  build=False,
                  ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='172.20.5.41',
                           protocol='tcp',
                           port=6633)

    info('*** Add switches\n')
    info('*** switches protocols')
    openFlowVersions = []
    openFlowVersions.append('OpenFlow13')
    protoList = ",".join(openFlowVersions)
    switchParms = {}
    switchParms['protocols'] = protoList

    # CORE
    cs1 = net.addSwitch('cs1', cls=OVSKernelSwitch, **switchParms)
    cs2 = net.addSwitch('cs2', cls=OVSKernelSwitch, **switchParms)
    cs3 = net.addSwitch('cs3', cls=OVSKernelSwitch, **switchParms)
    cs4 = net.addSwitch('cs4', cls=OVSKernelSwitch, **switchParms)

    # AGRE
    as11 = net.addSwitch('as11', cls=OVSKernelSwitch, **switchParms)
    as22 = net.addSwitch('as22', cls=OVSKernelSwitch, **switchParms)
    as33 = net.addSwitch('as33', cls=OVSKernelSwitch, **switchParms)
    as44 = net.addSwitch('as44', cls=OVSKernelSwitch, **switchParms)
    as55 = net.addSwitch('as55', cls=OVSKernelSwitch, **switchParms)
    as66 = net.addSwitch('as66', cls=OVSKernelSwitch, **switchParms)
    as77 = net.addSwitch('as77', cls=OVSKernelSwitch, **switchParms)
    as88 = net.addSwitch('as88', cls=OVSKernelSwitch, **switchParms)

    # EDGE
    es111 = net.addSwitch('es111', cls=OVSKernelSwitch, **switchParms)
    es222 = net.addSwitch('es222', cls=OVSKernelSwitch, **switchParms)
    es333 = net.addSwitch('es333', cls=OVSKernelSwitch, **switchParms)
    es444 = net.addSwitch('es444', cls=OVSKernelSwitch, **switchParms)
    es555 = net.addSwitch('es555', cls=OVSKernelSwitch, **switchParms)
    es666 = net.addSwitch('es666', cls=OVSKernelSwitch, **switchParms)
    es777 = net.addSwitch('es777', cls=OVSKernelSwitch, **switchParms)
    es888 = net.addSwitch('es888', cls=OVSKernelSwitch, **switchParms)

    info('*** Add hosts\n')
    # POD 1
    pod1h1 = net.addHost('pod1h1', cls=Host, ip='10.0.0.1', mac='B6:29:CE:E1:DB:11', defaultRoute=None)
    pod1h2 = net.addHost('pod1h2', cls=Host, ip='10.0.0.2', mac='B6:29:CE:E1:DB:12', defaultRoute=None)

    pod1h3 = net.addHost('pod1h3', cls=Host, ip='10.0.0.3', mac='92:88:E9:9C:0D:13', defaultRoute=None)
    pod1h4 = net.addHost('pod1h4', cls=Host, ip='10.0.0.4', mac='92:88:E9:9C:0D:14', defaultRoute=None)

    # POD 2
    pod2h1 = net.addHost('pod2h1', cls=Host, ip='10.0.0.5', mac='92:88:E9:9C:0D:21', defaultRoute=None)
    pod2h2 = net.addHost('pod2h2', cls=Host, ip='10.0.0.6', mac='92:88:E9:9C:0D:22', defaultRoute=None)

    pod2h3 = net.addHost('pod2h3', cls=Host, ip='10.0.0.7', mac='92:88:E9:9C:0D:23', defaultRoute=None)
    pod2h4 = net.addHost('pod2h4', cls=Host, ip='10.0.0.8', mac='92:88:E9:9C:0D:24', defaultRoute=None)

    # POD 3
    pod3h1 = net.addHost('pod3h1', cls=Host, ip='10.0.0.9', mac='92:88:E9:9C:0D:31', defaultRoute=None)
    pod3h2 = net.addHost('pod3h2', cls=Host, ip='10.0.0.10', mac='92:88:E9:9C:0D:32', defaultRoute=None)

    pod3h3 = net.addHost('pod3h3', cls=Host, ip='10.0.0.11', mac='92:88:E9:9C:0D:33', defaultRoute=None)
    pod3h4 = net.addHost('pod3h4', cls=Host, ip='10.0.0.12', mac='92:88:E9:9C:0D:34', defaultRoute=None)

    # POD 4
    pod4h1 = net.addHost('pod4h1', cls=Host, ip='10.0.0.13', mac='92:88:E9:9C:0D:41', defaultRoute=None)
    pod4h2 = net.addHost('pod4h2', cls=Host, ip='10.0.0.14', mac='92:88:E9:9C:0D:42', defaultRoute=None)

    pod4h3 = net.addHost('pod4h3', cls=Host, ip='10.0.0.15', mac='92:88:E9:9C:0D:43', defaultRoute=None)
    pod4h4 = net.addHost('pod4h4', cls=Host, ip='10.0.0.16', mac='92:88:E9:9C:0D:44', defaultRoute=None)

    info('*** Add links\n')
    # CORE
    net.addLink(cs1, as11, bw=10)
    net.addLink(cs1, as33, bw=10)
    net.addLink(cs1, as55, bw=10)
    net.addLink(cs1, as77, bw=10)

    net.addLink(cs2, as11, bw=10)
    net.addLink(cs2, as33, bw=10)
    net.addLink(cs2, as55, bw=10)
    net.addLink(cs2, as77, bw=10)

    net.addLink(cs3, as22, bw=10)
    net.addLink(cs3, as44, bw=10)
    net.addLink(cs3, as66, bw=10)
    net.addLink(cs3, as77, bw=10)

    net.addLink(cs4, as22, bw=10)
    net.addLink(cs4, as44, bw=10)
    net.addLink(cs4, as66, bw=10)
    net.addLink(cs4, as88, bw=10)

    # AGGREGATION
    net.addLink(as11, es111, bw=10)
    net.addLink(as11, es222, bw=10)
    net.addLink(as22, es111, bw=10)
    net.addLink(as22, es222, bw=10)

    net.addLink(as33, es333, bw=10)
    net.addLink(as33, es444, bw=10)
    net.addLink(as44, es333, bw=10)
    net.addLink(as44, es444, bw=10)

    net.addLink(as55, es555, bw=10)
    net.addLink(as55, es666, bw=10)
    net.addLink(as66, es555, bw=10)
    net.addLink(as66, es666, bw=10)

    net.addLink(as77, es777, bw=10)
    net.addLink(as77, es888, bw=10)
    net.addLink(as88, es777, bw=10)
    net.addLink(as88, es888, bw=10)

    # EDGE
    net.addLink(es111, pod1h1, bw=20)
    net.addLink(es111, pod1h2, bw=20)
    net.addLink(es222, pod1h3, bw=20)
    net.addLink(es222, pod1h4, bw=20)

    net.addLink(es333, pod2h1, bw=20)
    net.addLink(es333, pod2h2, bw=20)
    net.addLink(es444, pod2h3, bw=20)
    net.addLink(es444, pod2h4, bw=20)

    net.addLink(es555, pod3h1, bw=20)
    net.addLink(es555, pod3h2, bw=20)
    net.addLink(es666, pod3h3, bw=20)
    net.addLink(es666, pod3h4, bw=20)

    net.addLink(es777, pod4h1, bw=20)
    net.addLink(es777, pod4h2, bw=20)
    net.addLink(es888, pod4h3, bw=20)
    net.addLink(es888, pod4h4, bw=20)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    # CORE
    net.get('cs1').start([c0])
    net.get('cs2').start([c0])
    net.get('cs3').start([c0])
    net.get('cs4').start([c0])

    # AGGREGATION
    net.get('as11').start([c0])
    net.get('as22').start([c0])
    net.get('as33').start([c0])
    net.get('as44').start([c0])
    net.get('as55').start([c0])
    net.get('as66').start([c0])
    net.get('as77').start([c0])
    net.get('as88').start([c0])

    # EDGE
    net.get('es111').start([c0])
    net.get('es222').start([c0])
    net.get('es333').start([c0])
    net.get('es444').start([c0])
    net.get('es555').start([c0])
    net.get('es666').start([c0])
    net.get('es777').start([c0])
    net.get('es888').start([c0])

    info('*** Post configure switches and hosts\n')
    run(host='172.20.5.41', port=8090)
    CLI(net)
    net.stop()

# ------------------------API---------------------------------


@route('/dissertation/api/transmission')
def executeTransmission():
    transmissionFromIp = request.query.fromIp
    transmissionToIp = request.query.toIp
    # transmissionPort_src = request.query.port_src
    transmissionPort_dst = request.query.port_dst
    transmissionRate = request.query.rate
    transmissionTime = request.query.time
    transmissionType = request.query.type
    hostClient = None
    hostServer = None
    for host in net.hosts:
        if host.IP() == transmissionFromIp:
            hostClient = host
        elif host.IP() == transmissionToIp:
            hostServer = host
    if transmissionType == 'UDP':
        # iperf Client
        hostClient.popen('iperf -c ' + transmissionToIp + ' -p' + transmissionPort_dst +
                         ' -u -t ' + transmissionTime + ' -i 1 -b ' + transmissionRate + 'm')
        # iperf Server
        # hostServer.popen('echo "-----------------TEST---------------------" >> iperf_server_' + transmissionToIp)
        hostServer.popen('iperf -s -u -i 1 -p ' + transmissionPort_dst +
                         ' >> iperf_server_' + transmissionToIp + '_' + transmissionPort_dst, shell=True)

    info(transmissionType)
    return "ok"


@route('/dissertation/api/host/add/<hostName>/<deviceId>')
def addHostOnDevice(hostName, deviceId):
    info('*** Dynamically add a container at runtime\n')
    for switch in net.switches:
        if switch.dpid == deviceId[3:]:
            ip = net.getNextIp()
            host = net.addHost(hostName)
            net.addLink(host, switch, params1={"ip": ip})
            net.pingAll()
            return "Host added to switch: " + switch.dpid + " with ip: " + ip


@route('/dissertation/api/xterm/<ipAddress>')
def makeXTerm(ipAddress):
    for host in net.hosts:
        if host.IP() == ipAddress:
            makeTerm(host)


@route('/dissertation/api/pingall')
def pingall():
    net.pingAll()


@route('/dissertation/api/switch/add/<name>')
def addSwitch(name):
    switch = net.addSwitch(name)
    switch.start([net.get('c0')])
    return "Switch added! " + switch.dpid


@route('/cli/link/add/<switchId1>/<switchId2>')
def switchAddLink(switchId1, switchId2):
    switch1 = ''
    switch2 = ''
    for switch in net.switches:
        if switch.dpid == switchId1[3:]:
            switch1 = switch
        elif switch.dpid == switchId2[3:]:
            switch2 = switch
    if not switch1 or not switch2:
        info("Not devices where found")
    net.addLink(switch1, switch2)
    return "Link added!"


@route('/dissertation/api/link/rm/<deviceId1>/<deviceId2>')
def removeLink(deviceId1, deviceId2):
    device1 = ''
    device2 = ''
    for switch in net.switches:
        if switch.dpid == deviceId1[3:]:
            device1 = switch
        elif switch.dpid == deviceId2[3:]:
            device2 = switch
    if not device1 and device2:
        for host in net.hosts:
            if host.MAC() == deviceId1[:17].lower():
                device1 = host
    else:
        for host in net.hosts:
            info(host.MAC().lower() + "==" + deviceId2[:17] + "\n")
            if host.MAC() == deviceId2[:17].lower():
                device2 = host
    info("device1: " + str(device1) + " device2: " + str(device2) + "\n")
    net.removeLink(node1=device1, node2=device2)
    return "Link removed!"


@route('/dissertation/api/host/exec/<hostIpAddress>/<command>')
def cli(hostIpAddress, command='ls'):
    for host in net.hosts:
        if host.IP() == hostIpAddress:
            return net.get(host).cmd(command)


@route('/dissertation/api/host/mac/<hostIpAddress>')
def getMacFromIpAddress(hostIpAddress):
    for host in net.hosts:
        if host.IP() == hostIpAddress:
            return host.MAC()


@route('/dissertation/api/host/info/<host>')
def hostInfo(host='host1'):
    hostname = net.get(host).name
    hostMac = net.get(host).MAC()
    hostIp = net.get(host).IP()
    hostDict = {'hostname': hostname, 'hostmac': hostMac, 'hostip': hostIp}
    return json.dumps(hostDict, ensure_ascii=False)


if __name__ == '__main__':
    setLogLevel('info')
    myFatTree()

