class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class QueueIterator:
    def __init__(self, head):
        self._current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.get_current() is None:
            raise StopIteration
        data = self.get_current().get_data()
        self.set_current(self.get_current().get_next())
        return data

    def get_current(self):
        return self._current

    def set_current(self, new_node):
        self._current = new_node


class Queues:
    def __init__(self, limit=1000):
        self._head = None
        self._tail = None
        self._limit = limit
        self._size = 0

    def __repr__(self):
        representation = '['
        current = self.get_head()
        if current is None:
            representation += ']'
        else:
            while current.get_next() is not None:
                representation += f'{current.get_data()}, '
                current = current.get_next()
            representation += f'{current.get_data()}]'
        return representation

    def __iter__(self):
        return QueueIterator(self.get_head())

    def get_head(self):
        return self._head

    def set_head(self, new_node):
        self._head = new_node

    def get_tail(self):
        return self._tail

    def set_tail(self, new_node):
        self._tail = new_node

    def get_limit(self):
        return self._limit

    def is_allowed(self):
        return self.get_size() < self.get_limit()

    def get_size(self):
        return self._size

    def increase_size(self):
        self._size += 1

    def decrease_size(self):
        self._size -= 1

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_allowed():
            if self.get_head() is None:
                self.set_head(new_node)
                self.set_tail(new_node)
            else:
                self.get_tail().set_next(new_node)
                self.set_tail(new_node)
            self.increase_size()
        else:
            print('Limit reached')
        return self

    def dequeue(self):
        if self.get_head() is None:
            print('Queue is Empty')
            return None
        else:
            node = self.get_head()
            self.set_head(self.get_head().get_next())
            self.decrease_size()
            return node.get_data()


    def peek(self):
        if self.get_head() is None:
            print('Queue is Empty')
            return self
        else:
            return self.get_head().get_data()
