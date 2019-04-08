class Node:
    def __init__(self):
        self.metas = []
        self.children = []


def main():
    with open("input.txt") as f:
        for line in f:
            data, chain = load_chain(line.split(" "))

    print(calculate_meta(chain, 0))


def calculate_meta(chain, total):
    children_amount = len(chain.children)
    for meta in chain.metas:
        if meta <= children_amount:
            total = calculate_meta(chain.children[meta-1], total)
    if children_amount == 0:
        for meta in chain.metas:
            total += int(meta)
    return total


def load_chain(data):
    chain = Node()
    child_amount, meta_data_amount, data = int(data[0]), int(data[1]), data[2:]
    for i in range(0, child_amount):
        data, child_chain = load_chain(data)
        chain.children.append(child_chain)
    for j in range(0, meta_data_amount):
        temp_meta = data[0]
        chain.metas.append(int(temp_meta))
        data.remove(temp_meta)
    return data, chain


if __name__ == '__main__':
    main()

