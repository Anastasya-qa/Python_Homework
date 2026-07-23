from address import Address


class Mailing:

    def __init__(self, to_address: Address, from_address: Address,
                 cost, track):
        self.toAddress = to_address
        self.fromAddress = from_address
        self.cost = cost
        self.track = track
