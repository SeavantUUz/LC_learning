# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/25'

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        r = []
        index = 0
        while num:
            t = num % 1000
            if t:
                if index == 1:
                    r.append('Thousand')
                elif index == 2:
                    r.append('Million')
                elif index == 3:
                    r.append('Billion')
                r.append(self.parse(num % 1000))
            index += 1
            num /= 1000
        return ' '.join(reversed(r))

    def parse(self, num):
        mapping = {
        1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
        11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',
        19:'Nineteen',
        20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred',
    }
        r = []
        h = num / 100
        c = num % 100
        if h:
            r.append('%s Hundred' % mapping[h])
        if c in mapping:
            r.append(mapping[c])
        else:
            a = c / 10
            if a:
                r.append(mapping[a*10])
            b = c % 10
            if b:
                r.append(mapping[b])
        return ' '.join(r)


if __name__ == '__main__':
    s = Solution()
    print s.numberToWords(1000200)
    print s.numberToWords(1234567)

