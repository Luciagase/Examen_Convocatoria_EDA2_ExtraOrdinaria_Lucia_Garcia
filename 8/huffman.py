class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def get_nodes(frequencies):
    return sorted([Node(symbol, frequency) for symbol, frequency in frequencies.items()], key=lambda x: x.frequency)

def huffman_tree(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        inner = Node(frequency=left.frequency + right.frequency)
        inner.left = left
        inner.right = right
        nodes.append(inner)
    return nodes[0]

def huffman_encoding(node, prefix='', code={}):
    if node is None:
        return
    if node.symbol is not None:
        code[node.symbol] = prefix
    huffman_encoding(node.left, prefix + '0', code)
    huffman_encoding(node.right, prefix + '1', code)
    return code

def compress(message, code):
    return ''.join([code[symbol] for symbol in message])

def decompress(compressed, node):
    message = ''
    current = node
    for bit in compressed:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.symbol is not None:
            message += current.symbol
            current = node
    return message

# Diccionario de frecuencias
frequencies = {"A":0.2, "F":0.17, "1":0.13, "3": 0.21, "0":0.05, "M": 0.09, "T": 0.15}
# Generación del árbol de Huffman
nodes = get_nodes(frequencies)
huff_tree = huffman_tree(nodes)
huff_code = huffman_encoding(huff_tree)

# Mensaje a comprimir
message = 'FAMT130'

# Compresión y descompresión
compressed = compress(message, huff_code)
decompressed = decompress(compressed, huff_tree)

print(f'Mensaje original: {message}')
print(f'Mensaje comprimido: {compressed}')
print(f'Mensaje descomprimido: {decompressed}')