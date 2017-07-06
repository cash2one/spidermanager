/**
 * Created by zjh on 2017/7/5.
 */

function formatTableName(value, row, index) {

    return '<a data-toggle="popover" data-placement="right" data-html="true" onclick="showTaleDetail(this)" value="' + row.spdTableName + '" style="cursor:pointer ">' + value + '</a>';
}

function showTaleDetail(e) {
    var popopersel = $(".popover-content");
    var tableId = $(e).attr('value');
    if (popopersel.has('#' + tableId).length == 0) {
        $("[data-toggle='popover']").popover('hide');
    }

    var tableDescId = $(e).attr('value') + '_desc';
    $(e).popover({
        html: 'true',
        content: '<button  type="button"  class="btn btn-sm btn-primary" onclick="$(this).parent().parent().hide()" style="float: right;margin-bottom: 5px;">关闭</button><div id="' + tableId + '" style="width:600px;height:450px;"><h4>表字段描述及样例数据</h4><div class="col-md-12"><table   id="' + tableDescId +
        '"><thead><tr><th  data-align="center" data-field="columnName">列名</th><th data-align="center" data-field="columnDesc">列描述</th><th data-align="left" data-field="sampleData">样例数据</th></tr></thead></table></div>'
    }).click(function () {
        $.getJSON("/tableDetail?tableName=" + tableId, function (data) {
            $("#" + tableDescId).bootstrapTable({
                data: data,
                striped:true,
                height: 400
            });
        });

    });
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
