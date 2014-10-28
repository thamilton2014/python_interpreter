__author__ = 'thamilton'


class Memory(object):
    mem = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
        'z': 0
    }

    # #
    # @param character - cannot be null
    # @return value stored at memory location for character
    # @throws ValueError if character is null
    # #
    def fetch(self, character):
        if character is None:
            ValueError("[Memory] null character argument")
        return Memory.mem.get(character)

    # #
    # @param index_val - cannot be null
    # @param param
    # @throws ValueError if input_val is null
    # #
    def store(self, index_val, param):
        if index_val is None:
            raise ValueError("[Memory] null index_val argument")
        if param is None:
            raise ValueError("[Memory] null param argument")
        Memory.mem[index_val] = param

    def display_memory(self):
        print(Memory.mem)
