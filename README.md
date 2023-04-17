# Ping League of Legends servers with Python

---

## This tool can test if servers are up and check your ping to a desired server

---

### Servers

Courtesy of [Laslow21](https://www.reddit.com/r/leagueoflegends/comments/4efy17/comment/d20167p/)

- NA: 104.160.131.3
- EUW: 104.160.141.3
- EUNE: 104.160.142.3
- OCE: 104.160.156.1
- LAN: 104.160.136.3

### App structure

The app implements three methods:

- test_servers(): Make a ping with timeout=1 to the 5 servers. If server responds to the ping, the green ball appear(🟢), if not, red ball(🔴).

- region_selector():

- ping_servers():