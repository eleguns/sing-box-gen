import os


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




def main():
    obj = SingBoxGen()
    obj.which_protocol()

if __name__ == '__main__':
    main()