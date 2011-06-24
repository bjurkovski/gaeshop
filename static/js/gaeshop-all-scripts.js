var shop = {
	init: function() {
		$(document).ready(function () {
			$(".button").button();
			$('.quantitySpinner').numeric({emptyValue: false, minValue: 0, increment: 1});;
			$('.priceSpinner').numeric({emptyValue: false,
										minValue: 0,
										increment: 0.1,
										showCurrency: true,
										currencySymbol: 'R$',
										format: { format: '0.00', decimalChar: '.', thousandsChar: ',' }
			});
		});
	},

	registerProduct: function() {
		var instance = this;
		$.ajax({url: "/register/product",
				type: 'POST',
				data: {name: $("#productName").val(), price: $("#productPrice").val(), description: $("#productDescription").val()},
				dataType: 'json',
				success: function(json) {
					instance.attr = true;
		  		}
		});
	},
};

shop.init();
