$(function(){

    initTopSwiper();

    initSwiperMenu();

})

function initTopSwiper(){
    var mySwiper = new Swiper ('#topSwiper', {
    //direction: 'vertical', 垂直
    loop: true, //轮回

    // 如果需要分页器
    pagination: '.swiper-pagination',

    autoplay:2000,
  })

}

function initSwiperMenu(){
    var mySwiper = new Swiper ('#swiperMenu', {
        slidesPerView: 3,
  })
}