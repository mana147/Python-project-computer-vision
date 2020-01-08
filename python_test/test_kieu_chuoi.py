strA = "0123456789"
strB = strA[5:len(strA)]
strC = '1:{p1} , 2:{p2}'.format(p1=123, p2="hieu")
strD = 'pham trung %s sad %s' % ('hieu', '123')
strE = 'hoc lap trinh '

str_out = strE.startswith('n',0,3)

print(str_out)

# ------------------------------------
