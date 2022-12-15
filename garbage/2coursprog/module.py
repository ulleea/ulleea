def printing():
    print('меня вызвали')
    return 1,2
#
#
# # def dataa( s):
# #     dd = s[2][0:2]
# #     mm = s[2][2:4]
# #     yy = s[2][4:6]
# #     s = '20' + yy + '-' + mm + '-' + dd
# #     return s
# #
# #
# # def days_between( s, sprev):
# #     d1 = dataa(s)
# #     d2 = dataa(sprev)
# #     from datetime import datetime
# #     d1 = datetime.strptime(d1, "%Y-%m-%d")
# #     d2 = datetime.strptime(d2, "%Y-%m-%d")
# #     return abs((d2 - d1).days)
# # a=days_between([11,22,'010321'],[11,22,'300421'])
# # print(a)
#
# # g=dict()
# # g[1]=0
# # g[2]=3
# # for i in g.values():
# #     print(i)
# from datetime import date
# a=2
# if type(a)==int:
#     print('ya')
#
# def dataa( s):
#     dd = s[0:2]
#     mm = s[2:4]
#     yy = s[4:6]
#     yy=int('20'+yy)
#     dd=int(dd)
#     mm=int(mm)
#     s=date(yy,mm,dd)
#     return s
#
# def diff_dates(date1, date2):
#     return (date1-date2).days
#
# def main():
#     d1 = date(2013,1,1)
#     d2 = date(2013,1,1)
#     print(d1)
#     result1 = diff_dates(d2, d1)
#     print ('{} days between {} and {}'.format(result1, d1, d2))
#     print ("Happy programmer's day!")
# main()
# g=dict()
# g[1]=[[1,2],[3,4]]
# g[3]=[4,5]
# g[1][1].append(g[1][1][-1]+1)
# g[1][1].insert(0,g[1][1][-1]+1)
# print(g)
# print(g[1][1][-1])