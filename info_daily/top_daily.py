import tushare as ts
import util

import pandas
from sqlalchemy import create_engine
engine = create_engine(util.db_url)

# 每日龙虎榜列表
# top_daily = ts.top_list('2019-05-06')
# pandas.io.sql.to_sql(top_daily, "top_daily_20190506", engine, schema='StockPick', if_exists='append')

# 个股上榜统计
# individual = ts.cap_tops(days=10)
# pandas.io.sql.to_sql(individual, "individual_20190507_10", engine, schema='StockPick', if_exists='append')

# 营业部上榜统计
broker_tops = ts.broker_tops(days=10)
pandas.io.sql.to_sql(broker_tops, "broker_tops_20190507_10", engine, schema='StockPick', if_exists='append')

# 机构席位追踪
# institution_tops = ts.inst_tops()
# pandas.io.sql.to_sql(broker_tops, "broker_tops_20190507_10", engine, schema='StockPick', if_exists='append')

