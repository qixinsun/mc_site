$(document).ready(function () {

	$("#select1 dd").click(function () {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectA").remove();
		} else {
			var copyThisA = $(this).clone();
			if ($("#selectA").length > 0) {
				$("#selectA a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisA.attr("id", "selectA"));
			}
		}
	});

	$("#select2 dd").click(function () {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectB").remove();
		} else {
			var copyThisB = $(this).clone();
			if ($("#selectB").length > 0) {
				$("#selectB a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisB.attr("id", "selectB"));
			}
		}
	});

	$("#select3 dd").click(function () {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectC").remove();
		} else {
			var copyThisC = $(this).clone();
			if ($("#selectC").length > 0) {
				$("#selectC a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisC.attr("id", "selectC"));
			}
		}
	});

	$("#select4 dd").click(function () {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectD").remove();
		} else {
			var copyThisD = $(this).clone();
			if ($("#selectD").length > 0) {
				$("#selectD a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisD.attr("id", "selectD"));
			}
		}
	});

	$("#select5 dd").click(function () {
		$(this).addClass("selected").siblings().removeClass("selected");
		if ($(this).hasClass("select-all")) {
			$("#selectE").remove();
		} else {
			var copyThisE = $(this).clone();
			if ($("#selectE").length > 0) {
				$("#selectE a").html($(this).text());
			} else {
				$(".select-result dl").append(copyThisE.attr("id", "selectE"));
			}
		}
	});


	// $("#selectA").live("click", function () {
	// 	$(this).remove();
	// 	$("#select1 .select-all").addClass("selected").siblings().removeClass("selected");
	// });

	// $("#selectB").live("click", function () {
	// 	$(this).remove();
	// 	$("#select2 .select-all").addClass("selected").siblings().removeClass("selected");
	// });

	// $("#selectC").live("click", function () {
	// 	$(this).remove();
	// 	$("#select3 .select-all").addClass("selected").siblings().removeClass("selected");
	// });

	// $("#selectD").live("click", function () {
	// 	$(this).remove();
	// 	$("#select4 .select-all").addClass("selected").siblings().removeClass("selected");
	// });

	// $("#selectE").live("click", function () {
	// 	$(this).remove();
	// 	$("#select5 .select-all").addClass("selected").siblings().removeClass("selected");
	// });

	$(".ssl").click(function(){
		var params='?kw='+$("#kw").val();
		if (params == '请输入...'){
			params = '';
		}
		show_cars(params);
	})

	$(".select dd").live("click", function () {
		if ($(".select-result dd").length > 1) {
			$(".select-no").hide();
		} else {
			$(".select-no").show();
		}
	});

	add_listen();
	show_cars('?a=');
});

function add_listen() {
	var objs = document.getElementsByTagName("dd");
	for (i = 0; i < objs.length; i++) {
		var obj = objs[i];
		obj.addEventListener('click', function () {
			var params = get_params_value();
			show_cars(params);
		});
	}
}

function listen_choices(){
	var choices = $(".select-result .selected")
	for(i=0; i<choices.length; i++){
		var obj = choices[i];
		obj.addEventListener('click', function () {
			var params = get_params_value();
			show_cars(params);
		});
	}
}

function get_params_value() {
	var a, b, c, d, e
	try {
		a = $("#selectA")[0].innerText;
	} catch (err) { a = '' }
	try {
		b = $("#selectB")[0].innerText;
	} catch (err) { b = '' }
	try {
		c = $("#selectC")[0].innerText;
	} catch (err) { c = '' }
	try {
		d = $("#selectD")[0].innerText;
	} catch (err) { d = '' }
	try {
		e = $("#selectE")[0].innerText;
	} catch (err) { e = '' }

	return '?a=' + a + '&b=' + b + '&c=' + c + '&d=' + d + '&e=' + e;
}

function show_cars(params) {
	var obj = $("#car-area");
	obj.empty();
	$.ajax({
		type: 'GET',
		url: '/car/get_filter_cars/' + params,
		success: function (res) {
			var data = res.data;
			for (i = 0; i < data.length; i++) {
				var item = data[i]
				car = '<div class="car">\
								<a href="/car/detail/'+ item.id +'"' + '>\
								<img src='+ item.pic + ' alt="" style="width: 250px; height: auto;">\
								</a>\
								<p>'+ item.name + '</p>\
								<p>'+ item.price + '万元</p>\
								</div>';
				obj.append(car);
			}
			count();
		}
	});
}	
