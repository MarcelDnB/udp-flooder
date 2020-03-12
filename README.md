# udp-flooder
Flood your router users :)

# Usage
Run the command on a cmd in the right place:
`python flooder.py`

# Parameters
- **IP:** Victim ip, it must be private network ip obv.
- **PORT:** If you want to specify a concrete port, if you just want flood use random ports like 55555.
- **PACKETS PER THREAD:** Number of packets sent from each one of the threads, need this for threading
- **THREADS:** Number of threads that will work independently
- **LOOP OF LOOPS:** Loops until the program reach the **sleep**
- **SLEEP TIME:** Sleep between loops, to make it more uncomfortable :)
