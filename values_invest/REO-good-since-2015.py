# Here ROE good, means roe > 10, but this file is not used, as execute sql in workbench is much better and easier.

import util

roe_good = 'roe > 10'

con = util.conn
cursor = con.cursor()
profit_data_2019_1 = util.get_data_field_by_table_query(cursor, 'profit_data_2019_1', 'code', roe_good)

profit_data_2018_1 = util.get_data_field_by_table_query(cursor, 'profit_data_2018_1', 'code', roe_good)
profit_data_2018_2 = util.get_data_field_by_table_query(cursor, 'profit_data_2018_2', 'code', roe_good)
profit_data_2018_3 = util.get_data_field_by_table_query(cursor, 'profit_data_2018_3', 'code', roe_good)
profit_data_2018_4 = util.get_data_field_by_table_query(cursor, 'profit_data_2018_4', 'code', roe_good)

profit_data_2017_1 = util.get_data_field_by_table_query(cursor, 'profit_data_2017_1', 'code', roe_good)
profit_data_2017_2 = util.get_data_field_by_table_query(cursor, 'profit_data_2017_2', 'code', roe_good)
profit_data_2017_3 = util.get_data_field_by_table_query(cursor, 'profit_data_2017_3', 'code', roe_good)
profit_data_2017_4 = util.get_data_field_by_table_query(cursor, 'profit_data_2017_4', 'code', roe_good)


for share_profit in profit_data_2019_1:
    print(share_profit)

