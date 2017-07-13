/**
 * Created by zjh on 2017/7/5.
 */

function formatTableName(value, row, index) {

    return '<a data-toggle="popover" data-placement="right" data-html="true" onclick="showTaleDetail(this)" value="' + row.spdTableName + '|'+row.dacpTableName+'" style="cursor:pointer ">' + value + '</a>';
}

function showTaleDetail(e) {
    var popopersel = $(".popover-content");
    var tableId = $(e).attr('value').split('|')[0];
    var dacpTableName = $(e).attr('value').split('|')[1];
    if (popopersel.has('#' + tableId).length == 0) {
        $("[data-toggle='popover']").popover('hide');
    }

    var tableDescId = tableId + '_desc';
    $(e).popover({
        html: 'true',
        content: '<button  type="button"  class="btn btn-sm btn-primary" onclick="$(this).parent().parent().hide()" style="float: right;margin-bottom: 5px;">关闭</button><div id="' + tableId + '" style="width:600px; height:450px;"><h4>表字段描述及样例数据</h4><h5>爬虫库模型名称：'+tableId+'</h5><h5>DACP模型名称：'+dacpTableName+'</h5><div class="col-md-12" style="height:430px;overflow: auto"><table id="' + tableDescId + '"></table></div>'
    }).click(function () {
        $.getJSON("/tableDetail?tableName=" + tableId, function (data) {
            var showData = formatDetailData(data);
            $("#" + tableDescId).bootstrapTable({
                data: showData,
                striped: true,
                //  width:100,
                //height: '400',//高度固定后，表头出现对不齐的情况
                columns: [{
                    field: 'columnDesc',
                    title: '列描述',
                    align: 'center',
                    width: '40%'
                }, {
                    field: 'columnName',
                    title: '列名',
                    align: 'center',
                    width: '30%'
                }, {
                    field: 'sampleData',
                    title: '样例数据',
                    align: 'center',
                    width: '30%'
                },],
                resizable: true
            });
            $('#' + tableDescId + ' th:eq(2) div:eq(0) button').remove();
            $('#' + tableDescId + ' th:eq(2) div:eq(0)').append('<button id="change"  class="glyphicon glyphicon-refresh" style="float: right;"></button>');
            $('#change').bind('click',function () {
                var changeData = formatDetailData(data);
                $("#" + tableDescId).bootstrapTable('load', changeData);
            })
        });

    });
}


/**
 * 将后台传递过来的数据组装成展示格式
 * @param data
 */
function formatDetailData(data) {
    var tableDesc = data.tableDesc;
    var sampleDataArray = data.sampleData;
    var dataIndex = Math.round(Math.random() * 9);
    var sampleData = sampleDataArray[dataIndex];
    for (var i = 0; i < tableDesc.length; i++) {
        var column = tableDesc[i];
        column.sampleData = sampleData[column.columnName];
    }
    ;
    return tableDesc;
}
/*function close() {
 alert(1);
 $("[data-toggle='popover']").popover('hide');
 }*/

/*$('body').click(function (event) {
 var target = $(event.target);
 var popoperTri = $(target).attr('data-toggle');// 判断自己当前点击的内容
 if ('popover' != popoperTri) {
 $("[data-toggle='popover']").popover('hide');     // 当点击body的非弹出框相关的内容的时候，关闭所有popover
 };
 });*/
//a标签每次都要点击两次才触发popoer，没找到原因，先代码触发模拟一次点击事件
setTimeout(function () {
    $("[data-toggle='popover']").trigger('click');
}, 1000)
