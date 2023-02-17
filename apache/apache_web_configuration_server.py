# Challenge: Apache Web Server Configuration
# You have been asked to write a Python script to manage the configuration of an Apache web server. Your script should be able to:

# Create a new virtual host for a website
# Delete an existing virtual host
# Modify the configuration settings for an existing virtual host
# Restart the Apache web server to apply changes

import os

APACHE_CONF_DIR = "/etc/apache2/sites-available"
APACHE_BIN_DIR = "/usr/sbin/apache2ctl"

if not os.path.exists(APACHE_BIN_DIR):
    raise Exception("Apache web server is not installed on this system")

def create_virtual_host(hostname, document_root):
    # Create a new virtual host for a website
    conf_file = os.path.join(APACHE_CONF_DIR, hostname)
    with open(conf_file, "w") as f:
        f.write(f"""<VirtualHost *:80>
    ServerName {hostname}
    DocumentRoot {document_root}

    <Directory {document_root}>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
""")

def delete_virtual_host(hostname):
    # Delete an existing virtual host
    conf_file = os.path.join(APACHE_CONF_DIR, hostname)
    os.remove(conf_file)

def modify_virtual_host(hostname, key, value):
    # Modify the configuration settings for an existing virtual host
    conf_file = os.path.join(APACHE_CONF_DIR, hostname)
    with open(conf_file, "r") as f:
        lines = f.readlines()
    with open(conf_file, "w") as f:
        for line in lines:
            if line.startswith(key):
                line = f"{key} {value}\n"
            f.write(line)

def restart_apache_server():
    # Restart the Apache web server to apply changes
    subprocess.run([APACHE_BIN_DIR, "restart"])

if __name__ == "__main__":
    # Example usage:
    hostname = "example.com"
    document_root = "/var/www/example.com"

    create_virtual_host(hostname, document_root)
    restart_apache_server()

    # Test that the virtual host was created successfully
    # (This will raise an exception if the virtual host was not created correctly)
    response = requests.get(f"http://{hostname}")
    response.raise_for_status()
