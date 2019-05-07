import tushare as ts
import util

pro = ts.pro_api('19a3fbaab79440cfa9e78d3bb37958f7599f0d3c6cbd409e50a079dd')

con = util.conn
cursor = con.cursor()
profit_data_2019_1 = util.get_data_by_table_query(cursor, 'profit_data_2019_1', 'roe > 10')

for share_profit in profit_data_2019_1:
    print(share_profit)


# df = pro.hsgt_top10(trade_date='20190430', market_type='3')
# df.to_excel('./20190430_top10_深股通.xlsx', sheet_name='Sheet1')

# df = pro.query('hsgt_top10', ts_code='000063.SZ', start_date='20190401', end_date='20190430')

# print(df)
# df.to_excel('./600201.SH_0401_0430.xlsx')


# df = pro.top_inst(trade_date='20190430')
# df.to_excel('./430_龙虎榜.xlsx')



# df = pro.dividend(ts_code='002727.SZ', fields='ts_code,div_proc,stk_div,record_date,ex_date')

# df_income = pro.income(ts_code='600000.SH', start_date='20180101', end_date='20180730', fields='ts_code,ann_date,f_ann_date,end_date,report_type,comp_type,basic_eps,diluted_eps')

# df = ts.get_stock_basics()
# df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')
# print(df)
# print(df_income)

"""
import pandas
from sqlalchemy import create_engine
engine = create_engine(db_url)
# First time insert to table will failed, need change code field to varchar(45) from text
pandas.io.sql.to_sql(df, 'stock_basic_index', engine, schema='StockPick', if_exists='append')
"""

"""
# Save DataFrame to Excel
"""

# df.to_excel('./20194030_stock_basics.xlsx')
