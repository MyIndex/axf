$(function () {
    $('#cartboxall').change(function () {
        bl = $(this).prop('checked'); //获取当前复选框的状态
        // alert(bl);
        $('input[name="cartbox"]').prop('checked',bl); //配置复选框的状态
    });
    $('input[name="cartbox"]').change(function () {
        //如果全部勾选，全选框勾上，如果有一个没勾上，全选框取消
        bl = $('input[name="cartbox"]:checked').length == $('input[name="cartbox"]').length;
        $('#cartboxall').prop('checked',bl);
    });
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