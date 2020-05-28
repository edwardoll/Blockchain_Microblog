package com.example.myview.config;

import org.hibernate.dialect.MySQL5Dialect;
import org.springframework.stereotype.Component;

//解决hibernate自动建表字符集为latin不能插入中文的问题。

@Component
@SuppressWarnings("deprecation")
public class MysqlConfig extends MySQL5Dialect {
    @Override
    public String getTableTypeString() {
        return "ENGINE=InnoDB DEFAULT CHARSET=utf8";
    }
}
