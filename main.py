try:
    from ping3 import ping, verbose_ping
except:
    print('ping3 not found')

ping.DEBUG = True
verbose_ping.DEBUG = True
ping.EXCEPTIONS = True
verbose_ping.EXCEPTIONS = True

class Lol_ping:

    NA = '104.160.131.3'
    EUW = '104.160.141.3'
    EUNE = '104.160.142.3'
    OCE = '104.160.156.1'
    LAN = '104.160.136.3'

    def test_servers(self):
        print('Testing servers')
        try:
            if ping(self.NA, timeout=1) is False or None:
                print('NA   🔴')
            else:
                print('NA   🟢')

            if ping(self.EUW, timeout=1) is False or None:
                print('EUW  🔴')
            else:
                print('EUW  🟢')

            if ping(self.EUNE, timeout=1) is False or None:
                print('EUNE 🔴')
            else:
                print('EUNE 🟢')

            if ping(self.OCE, timeout=1) is False or None:
                print('OCE  🔴')
            else:
                print('OCE  🟢')

            if ping(self.LAN, timeout=1) is False or None:
                print('LAN  🔴')
            else:
                print('LAN  🟢')
        except:
            print('Servers cannot be reachables, check the IPs')
        finally:
            print('Servers tested correctly\n')

    def region_selector(self):
        regions = ['NA', 'EUW', 'EUNE', 'OCE', 'LAN']
        region_selected = ''
        input_message = 'Choose a region:\n'

        for index, item in enumerate(regions):
            input_message += f'{index+1}) {item}\n'
        input_message += 'Selected region: '

        while region_selected.upper() not in regions:
            region_selected = input(input_message)

        print('Picked region --> ' + region_selected.upper())
        return region_selected.upper()

    def ping_servers(self, region):

        match region.upper():
            case 'NA':
                region = self.NA
                print('NA --> ' + region)
            case 'EUW':
                region = self.EUW
                print('EUW --> ' + region)
            case 'EUNE':
                region = self.EUNE
                print('EUNE --> ' + region)
            case 'OCE':
                region = self.OCE
                print('OCE --> ' + region)
            case 'LAN':
                region = self.LAN
                print('LAN --> ' + region)
            case _:
                print('No selected region')

        region_ping = verbose_ping(str(region))
        return print(region_ping)
        # print(ping(region))


if __name__ == "__main__":

    lolping = Lol_ping()

    # 1) Test servers
    # lolping.test_servers()

    # 2) Choose a region
    region = lolping.region_selector()

    # 3) Test selected server
    lolping.ping_servers(region)

'''
IP Provider --> https://www.reddit.com/r/leagueoflegends/comments/4efy17/comment/d20167p/

NA - 104.160.131.3

EUW - 104.160.141.3

EUNE - 104.160.142.3

OCE - 104.160.156.1

LAN - 104.160.136.3
'''
