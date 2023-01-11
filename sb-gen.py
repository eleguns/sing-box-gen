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
        configs_list = ['vmess+ws', 'vmess+ws+tls']
        text = '\n'
        for v, i in enumerate(os.listdir('/etc/sb-gen/data/vmess')):
            text += f'{i}){v}'
        text += '\nEnter the number of your own config:'
        configs = int(input(text))
        if configs not in [1, 2]:
            self.vmess_protocols()
        self.run_protocol(configs_list)
    def vless_protocols(self):
        configs_list = ['vless+ws', 'vless+ws+tls']
        text = '\n'
        for v, i in enumerate(os.listdir('/etc/sb-gen/data/vless')):
            text += f'{i}){v}'
        text += '\nEnter the number of your own config:'
        configs = int(input(text))
        if configs not in [1, 2]:
            self.vless_protocols()
        self.run_protocol(configs_list)
    def run_protocol(self, config: str):
        if 'tls' in config :
            self.run_with_tls(config.replace('+tls', ''))
        else :
            self.run_without_tls(config)




def main():
    obj = SingBoxGen()
    obj.which_protocol()

if __name__ == '__main__':
    main()