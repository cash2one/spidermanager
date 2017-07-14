# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, session

from spidermanager import app
from spidermanager.setting import SHOW_DATABASE_URI
import sqlalchemy.exc
from spidermanager.util.action_result import list2json, obj2json
from sqlalchemy import (create_engine, MetaData, Table, Column,
                        String, Float, LargeBinary)
import json

try:
    engine = create_engine(SHOW_DATABASE_URI, convert_unicode=True,pool_recycle=3600)
except sqlalchemy.exc.SQLAlchemyError,e:
    print e
@app.route("/item", methods=['GET','POST'])
def load_dict():
    dicts = []
    try:
        for res in engine.execute("select TBL_ID,MODEL_TBL_DESC,MODEL_TBL_SPD,MODEL_TBL_DACP,MODEL_TBL_TYPE,DATA_SOURCE,DECODE(STATUS,'A','待发布','P','已发布'),TOTAL_RECORDS,TO_CHAR(LAST_UPDATE, 'yyyy-MM-dd HH24:mm:ss') from dict_spd_data where STATUS in ('A','P')"):
            tmp_dict = {}
            tmp_dict['tableId'] = str(res[0])
            tmp_dict['tableName'] = str(res[1]).decode('gbk').encode('utf8')
            tmp_dict['spdTableName'] = str(res[2])
            tmp_dict['dacpTableName'] = str(res[3])
            tmp_dict['tableType'] = str(res[4]).decode('gbk').encode('utf8')
            tmp_dict['dataSource'] = str(res[5]).decode('gbk').encode('utf8')
            tmp_dict['status'] = str(res[6]).decode('gbk').encode('utf8')
            tmp_dict['totalRecords'] = str(res[7])
            tmp_dict['lastUpdate'] = str(res[8])
            dicts.append(tmp_dict)
    except sqlalchemy.exc.SQLAlchemyError,e:
        print e
    return json.dumps(dicts,ensure_ascii=False)

@app.route("/tableDetail", methods=['GET','POST'])
def table_detail():
    table_name = request.values.get('tableName')
    tableDetail = {}
    tableDesc = []
    col_name = []
    sampleData = []
    try:
        for res in engine.execute("SELECT b.column_name,b.comments\
                                     FROM user_tab_columns a, user_col_comments b\
                                    where a.table_name = upper('%s')\
                                      and a.table_name = b.table_name\
                                      and a.column_name = b.column_name\
                                    order by a.column_id"%table_name):
            tmp = {}
            tmp['columnName'] = res[0]
            if res[1] == None:
                tmp['columnDesc'] = ""
            else:
                tmp['columnDesc'] = res[1].decode('gbk').encode('utf8')
            col_name.append(res[0])
            tableDesc.append(tmp)
        sql = "select %s from %s where rownum<=10"%(",".join(col_name),table_name)
        for res in engine.execute(sql):
            tmp = {}
            for i in range(len(res)):
                if res[i] == None:
                    tmp[col_name[i]] = 'NULL'
                else:
                    tmp[col_name[i]] = res[i].decode('gbk').encode('utf8')
            sampleData.append(tmp)
        tableDetail['tableDesc'] = tableDesc
        tableDetail['sampleData'] = sampleData
    except sqlalchemy.exc.SQLAlchemyError,e:
        print e 
    return json.dumps(tableDetail,ensure_ascii=False)