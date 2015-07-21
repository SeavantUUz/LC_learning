# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/7/21'


def simplifyPath(path):
    simply_path = []
    word = ''
    for i in path:
        if i == '/':
            if word:
                if word == '..':
                    if simply_path:
                        simply_path.pop()
                elif word == '.':
                    pass
                else:
                    simply_path.append(word)
            word = ''
        else:
            word += i
    if word:
        if word == '..':
            if simply_path:
                simply_path.pop()
        elif word == '.':
            pass
        else:
            simply_path.append(word)
    return '/' + '/'.join(simply_path)


if __name__ == '__main__':
    print simplifyPath('/home/a//b')
    print simplifyPath('/a/./b/../../c/')
    print simplifyPath('/../')
    print simplifyPath('/..')
    print simplifyPath('/.')

