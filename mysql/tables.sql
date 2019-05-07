CREATE TABLE `20194030_stock_basics` (
  `code` varchar(45) COLLATE latin1_general_ci NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `industry` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '细分行业',
  `area` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '地区',
  `pe` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '市盈率',
  `outstanding` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '流通股本',
  `totals` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '总股本(万)',
  `totalAssets` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '总资产(万)',
  `liquidAssets` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '流动资产',
  `fixedAssets` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '固定资产',
  `reserved` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '公积金',
  `reservedPerShare` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '每股公积金',
  `eps` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '每股收益',
  `bvps` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '每股净资',
  `pb` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '市净率',
  `timeToMarket` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '上市日期',
  `undp` varchar(45) COLLATE latin1_general_ci DEFAULT NULL,
  `perundp` varchar(45) COLLATE latin1_general_ci DEFAULT NULL,
  `rev` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT 'revenue 营业收入',
  `profit` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '利润',
  `gpr` varchar(45) COLLATE latin1_general_ci DEFAULT NULL,
  `npr` varchar(45) COLLATE latin1_general_ci DEFAULT NULL,
  `holders` varchar(45) COLLATE latin1_general_ci DEFAULT NULL COMMENT '股东人数'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci