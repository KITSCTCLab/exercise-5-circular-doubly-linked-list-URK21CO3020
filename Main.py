class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        

    def add_at_head(self, data) -> bool:
        # Write code here
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def add_at_index(self, index, data) -> bool:
        # Write code here
        if index < 0 or index >= self.getLength():
            return False

        count = 0

        itr = self.head

        while itr is not None:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                itr.next.prev = node
                itr.next = node
            count += 1
            itr = itr.next
        return True

    def get(self, index) -> int:
        # Write code here
        

    def delete_at_index(self, index) -> bool:
        # Write code here

    def get_previous_next(self, index) -> list:
        # Write code here


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
Footer
© 2022 GitHub, Inc.
