import queue
class convolotional():
    def __init__(self):
        self.state = 00
    def encode(self, string):
        output = ''
        self.state = 00
        for i in string:
            if i == '0' and self.state == 00:
                output += '00'
            elif i == '1' and self.state == 00:
                output += '11'
                self.state = 10

            elif i == '0' and self.state == 10:
                output += '11'
                self.state = 1
            elif i == '1' and self.state == 10:
                output += '00'
                self.state = 11

            elif i == '0' and self.state == 1:
                output += '10'
                self.state = 00
            elif i == '1' and self.state == 1:
                output += '01'
                self.state = 10

            elif i == '0' and self.state == 11:
                output += '01'
                self.state = 1
            elif i == '1' and self.state == 11:
                output += '10'
                self.state = 11
        return output
    def drived_from(self, state):
        if state == 0:
            return [(0,'00', '0'),(1,'10', '0')]
        if state == 1:
            return [(3,'01', '0'),(2,'11', '0')]
        if state == 2:
            return [(0,'11','1'),(1,'01', '1')]
        if state == 3:
            return [(3,'10', '1'),(2,'00', '1')]
    def calc_diff(self, st1, st2):
        r = 0
        if st1[0] != st2[0]:
            r += 1
        if st1[1] != st2[1]:
            r += 1
        return r
    def decode(self, string):
        res = ['','','','']
        pre_res = ['','','','']
        matrix = [[0 for x in range(int(len(string)/2) + 1)] for y in range(4)]
        matrix[1][0] = 10000
        matrix[2][0] = 10000
        matrix[3][0] = 10000

        p = [string[i] + string[i+1] for i in range(0,int(len(string)),2)]
        for i in range(1, len(p) + 1):
            for j in range(4):
                status = self.drived_from(j)
                l = self.calc_diff(p[i - 1], status[0][1]) + matrix[status[0][0]][i-1]
                r = self.calc_diff(p[i - 1], status[1][1]) + matrix[status[1][0]][i-1]
                if l < r:
                    matrix[j][i] = l
                    res[j] = pre_res[status[0][0]] + str(status[0][2])
                else:
                    matrix[j][i] = r
                    res[j] = pre_res[status[1][0]] + str(status[1][2])
            for j in range(4):
                pre_res[j] = res[j]
        # for x in range(4):
        #     print(matrix[x])
        indx = 0
        for i in range(4):
            # print(res[i] , matrix[i][-1])
            if matrix[i][-1] < matrix[indx][-1]:
                indx = i
        return res[indx]


def text_bin(text,encoding="utf-8",errors = "surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding,errors),"big"))[2:]
    return bits.zfill(8*((len(bits)+7)//8))

def textf(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

#s = convolotional()
#k = input('input stream: ')
#m = text_bin(k)
#print('encoded stream:' + s.encode(m))
#print('decoded stream:' + s.decode(s.encode(m)))
#print(textf(m))