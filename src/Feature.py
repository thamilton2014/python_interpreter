__author__ = 'thamilton'


class Feature(object):
    # #
    # @param compound - cannot be null
    # @throws ValueError if compound is null
    # #
    def __init__(self, compound):
        if compound is None:
            raise ValueError("[Feature] null compound argument")
        self.compound = compound

    def execute(self):
        self.compound.execute()
