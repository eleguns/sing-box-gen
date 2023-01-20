import os
from uuid import uuid4

class SingBoxGen :
    def __init__(self) -> None:
        pass
    def which_protocol(self):
        network = int(input('\n1) vmess\n2) vless\n\nEnter your protocol number:'))
        if network not in [1,2]:
            self.witch_protocol()
        if network == 1:
             self.vmess_protocols()
        if network == 2:
             self.vless_protocols()
    def vmess_protocols(self):
        config = int(input('\n1) vmess+ws\n2) vmess+ws+tls\n\nEnter your config number:'))
        if config not in [1,2]:
            self.vmess_protocols()
        if config == 1:
            self.vmess_ws()
        if config == 2:
            self.vmess_ws_tls()
    def vless_protocols(self):
        config = int(input('\n1) vless+ws\n2) vless+ws+tls\n\nEnter your config number:'))
        if config not in [1,2]:
            self.vless_protocols()
        if config == 1:
            self.vless_ws()
        if config == 2:
            self.vless_ws_tls()
    def get_port(self):
        port = int(input('Enter port number between 1-60000, default: 443'))
        if port not in range(1, 60001):
            return self.get_port()
        return port
    def get_dns_server(self):
        tag_list = ['google-dns', 'cloudflare-dns']
        address_list = ['8.8.8.8', '1.1.1.1']
        dns_server = int(input('\n1) google dns\n2) cloudflare dns\n\nEnter number of dns server you want'))
        if dns_server not in [1,2]:
            return self.get_dns_server()
        return tag_list[dns_server - 1], address_list[dns_server - 1]
    def ask_cert(self):
        auto_cert = input('do you have certificate or you want from script to create that (m: manual, a: automatic):')
        if auto_cert not in ['m', 'a']:
            return self.ask_cert()
    def vmess_ws_tls(self):
        port = self.get_port()
        uuid = uuid4()
        alterId = input('Enter number of alterId, default: 0')
        dns-tag, dns-address = self.get_dns_server()
        auto_cert = self.ask_cert()
        if auto_cert == 'm':
            cert_path = input('enter your cert path:')
            key_path  = input('enter your key path:')
        if auto_cert == 'a':
            sni = input('enter your url address for sni, like: www.google.com')
            if sni == '':
                sni = 'www.ray.uk'
        


def main():
    obj = SingBoxGen()
    obj.which_protocol()

if __name__ == '__main__':
    main()