from ping3 import ping, verbose_ping

NA = '104.160.131.3'

testing = ping(NA, timeout=1)

if testing is False or None:
    print('NA   🔴')
else:
    print('NA   🟢')
    print(testing)