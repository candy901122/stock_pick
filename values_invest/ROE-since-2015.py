import tushare as ts
import util

import pandas
from sqlalchemy import create_engine
engine = create_engine(util.db_url)

# profit_data_2014_1 = ts.get_profit_data(2014, 1)
# profit_data_2014_2 = ts.get_profit_data(2014, 2)
# profit_data_2014_3 = ts.get_profit_data(2014, 3)
# profit_data_2014_4 = ts.get_profit_data(2014, 4)
#
# profit_data_2015_1 = ts.get_profit_data(2015, 1)
# profit_data_2015_2 = ts.get_profit_data(2015, 2)
# profit_data_2015_3 = ts.get_profit_data(2015, 3)
# profit_data_2015_4 = ts.get_profit_data(2015, 4)
#
# profit_data_2016_1 = ts.get_profit_data(2016, 1)
# profit_data_2016_2 = ts.get_profit_data(2016, 2)
# profit_data_2016_3 = ts.get_profit_data(2016, 3)
# profit_data_2016_4 = ts.get_profit_data(2016, 4)
#
# profit_data_2017_1 = ts.get_profit_data(2017, 1)
# profit_data_2017_2 = ts.get_profit_data(2017, 2)
# profit_data_2017_3 = ts.get_profit_data(2017, 3)
# profit_data_2017_4 = ts.get_profit_data(2017, 4)
#
# profit_data_2018_1 = ts.get_profit_data(2018, 1)
# profit_data_2018_2 = ts.get_profit_data(2018, 2)
# profit_data_2018_3 = ts.get_profit_data(2018, 3)
# profit_data_2018_4 = ts.get_profit_data(2018, 4)

# profit_data_2019_1 = ts.get_profit_data(2019, 1)

# First time insert to table will failed, need change code field to varchar(45) from text
# pandas.io.sql.to_sql(profit_data_2019_1, 'profit_data_2019_1', engine, schema='StockPick', if_exists='append')

# pandas.io.sql.to_sql(profit_data_2018_1, 'profit_data_2018_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2018_1, 'profit_data_2018_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2018_1, 'profit_data_2018_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2018_1, 'profit_data_2018_4', engine, schema='StockPick', if_exists='append')
#
# pandas.io.sql.to_sql(profit_data_2017_1, 'profit_data_2017_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2017_1, 'profit_data_2017_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2017_1, 'profit_data_2017_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2017_1, 'profit_data_2017_4', engine, schema='StockPick', if_exists='append')
#
# pandas.io.sql.to_sql(profit_data_2016_1, 'profit_data_2016_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2016_1, 'profit_data_2016_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2016_1, 'profit_data_2016_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2016_1, 'profit_data_2016_4', engine, schema='StockPick', if_exists='append')
#
# pandas.io.sql.to_sql(profit_data_2015_1, 'profit_data_2015_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2015_1, 'profit_data_2015_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2015_1, 'profit_data_2015_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(profit_data_2015_1, 'profit_data_2015_4', engine, schema='StockPick', if_exists='append')

# Get report data
# report_data_2019_1 = ts.get_report_data(2019, 1)
# report_data_2018_1 = ts.get_report_data(2018, 4)
# report_data_2018_2 = ts.get_report_data(2018, 3)
# report_data_2018_3 = ts.get_report_data(2018, 2)
# report_data_2018_4 = ts.get_report_data(2018, 1)
#
# pandas.io.sql.to_sql(report_data_2018_1, 'report_data_2018_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_data_2018_2, 'report_data_2018_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_data_2018_3, 'report_data_2018_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_data_2018_4, 'report_data_2018_4', engine, schema='StockPick', if_exists='append')

# Growth data
# growth_data_2019_1 = ts.get_growth_data(2019, 1)
# pandas.io.sql.to_sql(growth_data_2019_1, 'growth_data_2019_1', engine, schema='StockPick', if_exists='append')

# report_growth_2018_1 = ts.get_growth_data(2018, 4)
# report_growth_2018_2 = ts.get_growth_data(2018, 3)
# report_growth_2018_3 = ts.get_growth_data(2018, 2)
# report_growth_2018_4 = ts.get_growth_data(2018, 1)
#
# pandas.io.sql.to_sql(report_growth_2018_1, 'report_growth_2018_1', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_growth_2018_2, 'report_growth_2018_2', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_growth_2018_3, 'report_growth_2018_3', engine, schema='StockPick', if_exists='append')
# pandas.io.sql.to_sql(report_growth_2018_4, 'report_growth_2018_4', engine, schema='StockPick', if_exists='append')
