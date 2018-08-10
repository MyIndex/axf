//页面加载完成以后，才执行的ｊｓ
$(function () {

    $('#alltypes').hide();
    $('#zhsort').hide();

    //点击全部类型的展示全部类型的ｄｉｖ
    $('#alltypespan').click(function(){

        $('#alltypes').show();

        //修改一下本身的样式图表
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');
    });

    //点击综合排序就展示综合排序的ｄｉｖ
    $('#zhsortspan').click(function(){
        $('#zhsort').show();
        $(this).removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');
    });

    //点击ｄｉｖ本身就隐藏
    $('#alltypes').click(function(){
        $(this).hide();
        $('#alltypespan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });

    //点击ｄｉｖ本身就隐藏
    $('#zhsort').click(function(){
        $(this).hide();
        $('#zhsortspan').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    });
    //添加点击事件
    $('.addShopping').click(function () {
        // alert($(this).attr('goodsid'));
        goodsid = $(this).attr('goodsid')
        //获取按钮上面的标签
        objects = $(this).prev()
        $.ajax({
            url:'/addshopcar/',
            type:'post',
            data:{'goodsid':goodsid},
            success:function (result) {
                if(result.code == '0009'){
                    window.location.href='/login/';
                }else {
                    objects.html(result.num)
                }

            }

        });
    });
    $('.subShopping').click(function () {
        // alert($(this).attr('goodsid'));
        goodsid = $(this).attr('goodsid')

        $.ajax({
            url:'/subshopcar/',
            type:'post',
            data:{'goodsid':goodsid},
            success:function (result) {
                if(result.code == '0009'){
                    window.location.href='/login/';
                }else{
                    gid = '#' + goodsid
                    $(gid).html(result.num)
                }

            }

        });
    });
});