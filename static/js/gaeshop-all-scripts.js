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
		json = new Object;
		json.name = $("#productName").val();
		json.price = $("#productPrice").val();
		json.description = $("#productDescription").val();
		json.stock = $("#productStock").val();

		var JSONstring = $.toJSON(json);

		if(!this.waitingResponse) {
			this.waitingResponse = true;
			var instance = this;
			$.ajax({url: "/register/product",
					type: 'POST',
					data: {json: JSONstring},
					dataType: 'json',
					success: function(json) {
						if(json.success)
							alert("Produto inserido com sucesso!");
						else
							alert("Erro ao inserir produto!");
						instance.waitingResponse = false;
			  		}
			});
		}
	},

	addToCart: function(product) {
		json = new Object;
		json.key = product;
		json.quantity = $("#quantity_"+product).val();

		var JSONstring = $.toJSON(json);

		if(!this.waitingResponse) {
			this.waitingResponse = true;
			var instance = this;
			$.ajax({url: "/register/product",
					type: 'POST',
					data: {json: JSONstring},
					dataType: 'json',
					success: function(json) {
						instance.waitingResponse = false;
			  		}
			});
		}
	}
};

shop.init();