import tushare as ts
import util

import pandas
from sqlalchemy import create_engine
engine = create_engine(util.db_url)

# classified_industry = ts.get_industry_classified()
# pandas.io.sql.to_sql(classified_industry, "classified_industry", engine, schema='StockPick', if_exists='append')
#
# classified_concept = ts.get_concept_classified()
# pandas.io.sql.to_sql(classified_concept, "classified_concept", engine, schema='StockPick', if_exists='append')

# classified_area = ts.get_area_classified()
# pandas.io.sql.to_sql(classified_area, "classified_area", engine, schema='StockPick', if_exists='append')

# small and medium enterprise board
# SMEs board 中小板
# classified_mid_small_company = ts.get_sme_classified()
# pandas.io.sql.to_sql(classified_mid_small_company,
# "classified_mid_small_company", engine, schema='StockPick', if_exists='append')

# 创业板 growth enterprise market
# classified_gem = ts.get_gem_classified()
# pandas.io.sql.to_sql(classified_gem, "classified_gem", engine, schema='StockPick', if_exists='append')

# 风险警示板
# classified_st = ts.get_st_classified()
# pandas.io.sql.to_sql(classified_st, "classified_st", engine, schema='StockPick', if_exists='append')

# 沪深300成份及权重
# classified_hs300_weight = ts.get_hs300s()
# pandas.io.sql.to_sql(classified_hs300_weight, "classified_hs300_weight",
# engine, schema='StockPick', if_exists='append')

# 上证50成份股
# classified_sz50s = ts.get_sz50s()
# pandas.io.sql.to_sql(classified_sz50s, "classified_sz50s", engine, schema='StockPick', if_exists='append')

# 中证500成份股
# classified_zz500s = ts.get_zz500s()
# pandas.io.sql.to_sql(classified_zz500s, "classified_zz500s", engine, schema='StockPick', if_exists='append')

