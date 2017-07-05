# -*- coding: utf-8 -*-
import json

from flask import render_template

from spidermanager import app


@app.route("/item", methods=['GET'])
def item():
    itemJson = [
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video2",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video3",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video4",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video5",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video6",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video7",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video8",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video9",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video10",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video11",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video12",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video13",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video14",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }, {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video15",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        },
        {
            "tableId": "10000",
            "tableName": "豆瓣电影信息",
            "spdTableName": "douban_video16",
            "tableType": "视频",
            "dataSource": "豆瓣电影",
            "totalRecords": "60487",
            "lastUpdate": "2017/7/3 9:39:10"
        }
    ]
    return json.dumps(itemJson)


@app.route("/tableDetail", methods=['GET'])
def tableDetail():
    tableDetail = {
        "tableDesc": [
            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            },            {
                "columnName": "XXX",
                "columnDesc": "XXX"
            },
            {
                "columnName": "YYY",
                "columnDesc": "YYY"
            }
        ],
        "sampleData": {
            "XXX": "aaa", "YYY": "bbb"
        }
    }
    return json.dumps(tableDetail)
