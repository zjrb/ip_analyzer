from ip_address import ip_address

addresses = ip_address()


def clear():
    ip_address.clear()


def top100() -> list[int]:
    return ip_address.top100()


def requestHandled(ipAddress: str):
    ip_address.requestHandled(ip_address)
