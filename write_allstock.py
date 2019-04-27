import MySQLdb
import tushare as ts

# 将所有的股票 基本信息 写入到名为allstock的表中，这个文件只需要执行一次

# 通过tushare库获取所有的A股列表
"""
    获取沪深上市公司基本情况
Parameters
date:日期YYYY-MM-DD，默认为上一个交易日，目前只能提供2016-08-09之后的历史数据

Return
--------
DataFrame

Column:
        0 name
        1 industry
        2 area
        3 pe
        4 outstanding
        5 totals
        6 totalAssets
        7 liquidAssets
        8 fixedAssets
        9 reserved
        10 reservedPerShare
        11 esp
        12 bvps
        13 pb
        14 timeToMarket
        15 undp
        16 perundp
        17 rev
        18 profit
        19 gpr
        20 npr
        21 holders

"""

stock_info = ts.get_stock_basics()

conn = MySQLdb.connect(user='root', password='root', database='StockPick')
cursor = conn.cursor()

codes = stock_info.index
names = stock_info.name

# 22 columns, +code, 23 column
columns = stock_info.columns.values.tolist()
total_stock_count = len(stock_info)

# 通过for循环遍历所有股票，然后拆分获取到需要的列，将数据写入到数据库中
a = 0
for i in range(0, total_stock_count):
    cursor.execute(
        'insert into allstock (code,name,industry,area,pe,outstanding,totals,totalAssets,liquidAssets, fixedAssets,reserved,reservedPerShare, esp, bvps, pb, timeToMarket,undp, perundp, rev, profit, gpr, npr, holders) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (stock_info.index[i], stock_info.name[i], stock_info.industry[i], stock_info.area[i], stock_info.pe[i],
         stock_info.outstanding[i], stock_info.totals[i], stock_info.totalAssets[i], stock_info.liquidAssets[i],
         stock_info.fixedAssets[i], stock_info.reserved[i], stock_info.reservedPerShare[i], stock_info.esp[i],
         stock_info.bvps[i], stock_info.pb[i], stock_info.timeToMarket[i], stock_info.undp[i], stock_info.perundp[i],
         stock_info.rev[i], stock_info.profit[i], stock_info.gpr[i], stock_info.npr[i], stock_info.holders[i]))
    a += 1
    print('第%d支股票' % i)

# 统计所有A股数量
print('共获取到%d支股票' % a)

conn.commit()
cursor.close()
conn.close()
