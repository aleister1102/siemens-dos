import snap7

active_list = ["91.123.183.172", "119.243.226.74", "183.77.153.19", "183.77.153.42"]

try:
    client = snap7.client.Client()
    client.connect("88.28.207.232", 0, 0, 102)
    connected = client.get_connected()
    print(connected)

    cpu_state = client.get_cpu_state()
    print(cpu_state)

    blocks = client.list_blocks()
    print(blocks)

    cpu_info = client.get_cpu_info()
    print(cpu_info)

    szl_list = client.read_szl_list()
    szl_list_hex = " ".join(format(x, "02x") for x in szl_list)
    print(szl_list_hex)

except Exception as e:
    print(e)
