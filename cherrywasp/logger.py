import os


class CherryLogger:
    """ Creates log files and logs results.

    Inputs: file_name_prefix(str)

    Returns: file written to disk"""
    def __init__(self):
        self.file_name_prefix = ""
        self.headers = "bssid,essid"
        self.file_path = os.path.join(os.getcwd(), "/logs")

    def file_setup(self, file_prefix):
        self.file_name_prefix = file_prefix
        if os.path.exists(self.file_path) is False:
            os.mkdir(os.path.join(os.getcwd(), "/logs"))
        self.write_headers()

    def write_headers(self):
        packet_types = ["beacon", "probe_request"]
        for packet_type in packet_types:
            file_name = self.file_name_prefix + "_" + packet_type + ".csv"
            with open(file_name, 'w') as f:
                f.write(self.headers)

    def write_to_file(self, packet_type, bssid, essid):
        file_name = self.file_name_prefix + "_" + packet_type + ".csv"
        full_path = os.path.join(self.file_path, file_name)
        with open(full_path, "a") as r:
            r.write("{0},{1}\n".format(bssid, essid))
