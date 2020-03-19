class GapBuffer:                                                                                                                                   
    def __init__(self, capacity=4588):
        self.buf = [0] * capacity
        self.capacity = capacity
        # initially, the gap is entire buffer wide
        self.gap_start = 0
        self.gap_end = capacity - 1

    def append(self, c):
        # TODO abhi - extend self.buf when appending 
        # beyond self.capacity
        self.buf[self.gap_start] = c
        self.gap_start += 1

    # this will never be called for append operations
    def insert_at(self, i: int, c): 
        # shift all the chars from i onwards to the end of the buf
        # so that a gap is created in between
        num_chars_to_shift = self.gap_start - i
        GapBuffer.__copy(self.buf, 
               i,
               self.buf, 
               self.gap_end - num_chars_to_shift + 1, 
               num_chars_to_shift)
        self.gap_start -= num_chars_to_shift
        self.gap_end -= num_chars_to_shift

        self.buf[self.gap_start] = c
        self.gap_start += 1

    # copy count number of elements of buf1 starting at i
    # to buf2 starting at j
    def __copy(buf1, i, buf2, j, count):
        for _ in range(count):
            buf2[j] = buf1[i]
            j += 1
            i += 1

    def delete(self):
        pass

    def __repr__(self):
        str = ''.join(self.buf[0:self.gap_start]) + \
              ''.join(self.buf[self.gap_end + 1:])
        return str

gb = GapBuffer()
gb.append('a')
gb.append('h')
gb.append('i')
gb.insert_at(1, 'b')
assert(str(gb) == "abhi")
