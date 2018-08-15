class CherryClient:
    """ Cherry Client
        An object that represents a wireless client seen in that environment.

        1. Type defines it as a client.
        2. BSSID is the MAC address of the client seen.
        3. requested_essid is all of the ESSIDs that the client has requested.

        add_new_essid adds a new ESSID or network name to the list for the particular client.
    """
    def __init__(self, bssid):
        self.type = "client"
        self.bssid = bssid
        self.requested_essid = set()

    def add_new_requested_essid(self, new_essid):
        self.requested_essid.add(new_essid)
