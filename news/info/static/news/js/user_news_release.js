function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {

    $(".release_form").submit(function (e) {
        e.preventDefault()

        // TODO 发布完毕之后需要选中我的发布新闻
        $(this).ajaxSubmit({
            // 因为新闻的正文内容是通过前端的富文本编辑器框架实现的（tinymce.min.js）
            // 所以需要使用前端框架读取新闻正文内容
            beforeSubmit: function (request) {
                // 在提交之前，对参数进行处理
                for(var i=0; i<request.length; i++) {
                    var item = request[i];
                    if (item["name"] == "content") {
                        item["value"] = tinyMCE.activeEditor.getContent()
                    }
                }
            },
            url: "/user/news_release",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    // 选中索引为6的左边菜单
                    window.parent.fnChangeMenu(6);
                    // 滚动到顶部
                    window.parent.scrollTo(0, 0);
                }else {
                    alert(resp.errmsg);
                }
            }
        });
    })
})