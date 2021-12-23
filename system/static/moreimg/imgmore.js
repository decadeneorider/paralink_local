$(function() {
	var flag = true; //防止用户快速多次点击
	init(); //初始化
	//点击切换图片
	$(".moveimg").click(function() {
		$(".moveimg").removeClass('active');
		$(this).addClass('active');
		var thisSrc = $(this).attr('src');
		$(".big-img img").attr('src', thisSrc);
	});
	//左右移动
	$(".small-img .left").on('click', function() {
		flag ? left() : "";
	});

	$(".small-img .right").on('click', function() {
		flag ? right() : "";
	});

	function left() {
		flag = false;
		//计算最后
		var imgPosition = $(".moveimg:last").offset().left + $(".moveimg:last").width();
		var boxPosition = $(".small-img").offset().left + $(".small-img").width();
		if(imgPosition >= boxPosition) {
			$('.small-img ul').animate({
				left: '-=105'
			}, 500, function() {
				flag = true;
			});
		} else {
			flag = true;
		}
	}

	function right() {
		flag = false;
		//计算第一个
		var imgPosition = $(".moveimg:first").offset().left;
		var boxPosition = $(".small-img").offset().left;
		if(imgPosition < boxPosition) {
			$('.small-img ul').animate({
				left: '+=105'
			}, 500, function() {
				flag = true;
			});
		} else {
			flag = true;
		}
	}

	function init() {
		var numImg = $('.moveimg').length;
		//重新定义ul 宽度
		$(".small-img ul").css('width', numImg * 105 + 'px');
		$($('.moveimg')[0]).addClass('active'); //第一个给默认选中
		$(".big-img img").attr('src', $($('.moveimg')[0]).attr('src'));
	}
});