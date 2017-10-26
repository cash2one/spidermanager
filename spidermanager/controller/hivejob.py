# -*- coding: utf-8 -*-
import json

import cx_Oracle
import time
from flask import render_template, request, session, redirect, url_for

from spidermanager.setting import hive_db
from spidermanager import app

@app.route('/listhivejob',methods=['GET'])
def listhivejob():
    current_user = "admin"

    currentJobType = request.args.get('currentJobType')
    currentTableName = request.args.get('currentTableName')
    currentUserName = request.args.get('currentUserName')
    currentStatus = request.args.get('currentStatus')
    currentDate = request.args.get('currentDate')
    currentSort = request.args.get('currentSort')
    jobs=list()
    db_conn = cx_Oracle.connect(hive_db)
    cursor = db_conn.cursor()
    sql = "SELECT * FROM HIVE_JOB WHERE 1=1 "

    if current_user != "admin":
        sql += "AND USER_NAME = '"+current_user+"' "
    if currentJobType != "":
        sql += "AND JOB_TYPE = '" + str(currentJobType) + "' "
    if currentTableName != "":
        sql += "AND TABLE_NAME LIKE '%" + str(currentTableName) + "%' "
    if currentUserName != "":
        sql += "AND USER_NAME LIKE '%" + str(currentUserName) + "%' "
    if currentStatus != "":
        if currentStatus == "running":
            sql += "AND STATUS IN ('waiting','oracle2local','local2hive','abort') "
        else:
            sql += "AND STATUS = '" + str(currentStatus) + "' "
    if currentDate != "":
        sql += "AND TO_CHAR(JOB_TIME, 'YYYY-MM-DD') = '"+currentDate+"' "

    sql += " AND (STATUS != 'delete' OR ( STATUS = 'delete' AND (SYSDATE-JOB_TIME)<1 ) ) "
    sql += "ORDER BY "
    if currentSort != "":
        sql += str(currentSort)
    else:
        sql += "JOB_TIME DESC "

    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        job=dict()
        job['JOB_ID'] = row[0]
        job['JOB_TYPE'] = row[1]
        job['JOB_DETAIL'] = row[2]
        job['USER_NAME'] = row[3]
        job['TABLE_NAME'] = row[4]
        job['STATUS'] = row[5]
        if job['STATUS'] in ['waiting','oracle2local','local2hive']:
            # blue - waiting,oracle2local,local2hive
            job['COLOR'] = 'default'
            job['PROGRESS_ACTIVE'] = 'active'
            job['VIEW_ACTIVE'] = 'disabled = "disabled"'
            job['ABORT_ACTIVE'] = ''
            job['DELETE_ACTIVE'] = 'disabled = "disabled"'
        elif job['STATUS'] in ['done']:
            # green - done
            job['COLOR'] = 'success'
            job['PROGRESS_ACTIVE'] = ''
            job['VIEW_ACTIVE'] = ''
            job['ABORT_ACTIVE'] = 'disabled = "disabled"'
            job['DELETE_ACTIVE'] = ''
        elif job['STATUS'] in ['error']:
            # red - error
            job['COLOR'] = 'danger'
            job['PROGRESS_ACTIVE'] = ''
            job['VIEW_ACTIVE'] = 'disabled = "disabled"'
            job['ABORT_ACTIVE'] = 'disabled = "disabled"'
            job['DELETE_ACTIVE'] = ''
        elif job['STATUS'] in ['abort']:
            # yellow - abort (pending to delete)
            job['COLOR'] = 'warning'
            job['PROGRESS_ACTIVE'] = 'active'
            job['VIEW_ACTIVE'] = 'disabled = "disabled"'
            job['ABORT_ACTIVE'] = 'disabled = "disabled"'
            job['DELETE_ACTIVE'] = 'disabled = "disabled"'
        elif job['STATUS'] in ['delete']:
            # yellow - abort (pending to delete)
            job['COLOR'] = 'info'
            job['PROGRESS_ACTIVE'] = ''
            job['VIEW_ACTIVE'] = 'disabled = "disabled"'
            job['ABORT_ACTIVE'] = 'disabled = "disabled"'
            job['DELETE_ACTIVE'] = 'disabled = "disabled"'
        else:
            job['COLOR'] = 'warning'
            job['PROGRESS_ACTIVE'] = ''
            job['VIEW_ACTIVE'] = ''
            job['ABORT_ACTIVE'] = ''
            job['DELETE_ACTIVE'] = ''
        job['RATE'] = row[6]
        job['REMARK'] = row[7].decode('gbk')
        job['JOB_TIME'] = str(row[8])
        job['RECORD_COUNT'] = row[9]
        job['RECORD_SIZE'] = row[10]
        jobs.append(job)
    cursor.close()
    db_conn.commit()
    db_conn.close()

    return json.dumps(jobs, ensure_ascii=False)

@app.route('/addhivejob', methods=['POST'])
def addhivejob():
    current_user = "admin"
    job_type = request.values.get('job_type')
    job_detail = request.values.get('job_detail')
    table_name = request.values.get('table_name')

    db_conn = cx_Oracle.connect(hive_db)

    job_id = 'JOB'+str(int(round(time.time() * 1000)))

    cursor = db_conn.cursor()
    sql = "INSERT INTO HIVE_JOB(" \
          "JOB_ID," \
          "JOB_TYPE," \
          "JOB_DETAIL," \
          "USER_NAME," \
          "TABLE_NAME," \
          "STATUS," \
          "RATE," \
          "REMARK," \
          "JOB_TIME," \
          "RECORD_COUNT," \
          "RECORD_SIZE) " \
          "VALUES(" \
          "'"+job_id+"'," \
          "'"+job_type+"'," \
          "'"+job_detail+"'," \
          "'"+current_user+"'," \
          "'"+table_name+"'," \
          "'waiting'," \
          "'10'," \
          "'等待'," \
          "SYSDATE," \
          "'0'," \
          "'0')"
    cursor.execute(sql)
    cursor.close()
    db_conn.commit()
    db_conn.close()
    result = dict()
    result['status']='ok'
    return json.dumps(result)

@app.route('/aborthivejob', methods=['POST'])
def aborthivejob():
    job_id = request.values.get('job_id')
    db_conn = cx_Oracle.connect(hive_db)
    cursor = db_conn.cursor()
    sql = "UPDATE HIVE_JOB SET " \
          "STATUS='abort' " \
          ",RATE='100' " \
          ",REMARK='主动放弃' " \
          ",JOB_TIME=SYSDATE " \
          "WHERE JOB_ID='"+job_id+"'"
    cursor.execute(sql)
    cursor.close()
    db_conn.commit()
    db_conn.close()
    result = dict()
    result['status']='ok'
    return json.dumps(result)


@app.route('/deletehivejob', methods=['POST'])
def deletehivejob():
    job_id = request.values.get('job_id')
    db_conn = cx_Oracle.connect(hive_db)
    cursor = db_conn.cursor()
    sql = "UPDATE HIVE_JOB SET " \
          "STATUS='abort' " \
          ",RATE='100' " \
          ",REMARK='正在清理' " \
          ",JOB_TIME=SYSDATE " \
          "WHERE JOB_ID='" + job_id + "'"
    cursor.execute(sql)
    cursor.close()
    db_conn.commit()
    db_conn.close()
    result = dict()
    result['status'] = 'ok'
    return json.dumps(result)


@app.route('/getresultexample')
def getresultexample():
    job_id = request.args.get('job_id')
    db_conn = cx_Oracle.connect(hive_db)
    cursor = db_conn.cursor()
    sql="SELECT RECORD_EXAMPLE FROM HIVE_JOB WHERE JOB_ID='"+job_id+"'"
    cursor.execute(sql)
    record = cursor.fetchone()
    try:
        result = str(record[0].read()).decode('gbk')
    except:
        result = ''
    cursor.close()
    db_conn.commit()
    db_conn.close()
    return result

@app.route('/hivejobdetail')
def hivejobdetail():

    if session.has_key('admin'):
        current_user = "admin"
        return render_template(
            "hivejobdetail.html",
            current_user=current_user
        )
    else:
        return redirect(url_for('login'))

