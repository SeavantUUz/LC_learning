# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/10/18'


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = []
        num = 0
        for i in input:
            if i == '+' or i == '-' or i == '*':
                tokens.append(int(num))
                tokens.append(i)
                num = 0
            else:
                num = 10*num + int(i)
        tokens.append(num)
        return sorted(self.helper(tokens))


    def helper(self, tokens):
        if not tokens:
            return []
        if len(tokens) == 1:
            return tokens
        result = []
        for index, token in enumerate(tokens):
            if token == '+' or token == '-' or token == '*':
                left = self.helper(tokens[:index])
                right = self.helper(tokens[index+1:])
                if not left:
                    result.extend(right)
                elif not right:
                    result.extend(left)
                else:
                    for l_value in left:
                        for r_value in right:
                            if token == '+':
                                result.append(l_value+r_value)
                            elif token == '-':
                                result.append(l_value-r_value)
                            else:
                                result.append(l_value*r_value)

        return result


if __name__ == '__main__':
    s = Solution()
    # print s.diffWaysToCompute('2-1-1')
    print s.diffWaysToCompute('2*3-4*5')

