class Solution(object):
    def convert(self, s, numRows):
        mat = [[]for i in range(numRows)]
        if numRows>1:
            for i,c in enumerate(s):
                if (i% (2*numRows-2)<(numRows)):
                    mat[(i% (2*numRows-2))].append(c)
                else:
                    mat[(2*numRows-2)-(i% (2*numRows-2))].append(c)
            return ''.join([''.join(mat[i]) for i in range(len(mat))])
        else:
            return s




















b= Solution()
s_tr = ""
conv_str = b.convert(s_tr,1)
print(conv_str) 