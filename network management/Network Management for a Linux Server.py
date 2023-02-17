# Challenge: Network Management for a Linux Server
# You have been asked to write a Python script to manage network settings on a Linux server. Your script should be able to:

# Configure a static IP address for the server
# Configure the server's hostname
# Configure the DNS settings for the server
# Test the network connectivity of the server
# The script should make use of the subprocess module in Python to run shell commands to configure the network settings on the Linux server.

# Questions to Consider
# How will you ensure that the IP address, hostname, and DNS settings entered are valid?
# How will you handle situations where the network settings are already configured?
# How will you test the network connectivity of the server in an efficient and reliable manner?
# How will you ensure the script can be run as an administrative user without being prompted for a password?

import subprocess

def configure_ip_address(ip_address, netmask, gateway):
    # Configure a static IP address for the server
    subprocess.run(["ip", "addr", "add", f"{ip_address}/{netmask}", "dev", "eth0"])
    subprocess.run(["ip", "route", "add", "default", "via", gateway])

def configure_hostname(hostname):
    # Configure the server's hostname
    with open("/etc/hostname", "w") as hostname_file:
        hostname_file.write(hostname)
    subprocess.run(["hostnamectl", "set-hostname", hostname])

def configure_dns(nameserver):
    # Configure the DNS settings for the server
    with open("/etc/resolv.conf", "w") as resolv_conf:
        resolv_conf.write(f"nameserver {nameserver}")

def test_network_connectivity():
    # Test the network connectivity of the server
    result = subprocess.run(["ping", "-c", "1", "google.com"], stdout=subprocess.PIPE)
    return result.returncode == 0

if __name__ == "__main__":
    # Example usage:
    ip_address = "192.168.1.100"
    netmask = "24"
    gateway = "192.168.1.1"
    hostname = "server1"
    nameserver = "8.8.8.8"

    configure_ip_address(ip_address, netmask, gateway)
    configure_hostname(hostname)
    configure_dns(nameserver)

    if test_network_connectivity():
        print("Server is connected to the network")
    else:
        print("Server is not connected to the network")
