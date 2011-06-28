var shop = {
	init: function() {
		$(document).ready(function () {
			$("button").button();
			$('.quantitySpinner').numeric({emptyValue: false, minValue: 0, increment: 1});;
			$('.priceSpinner').numeric({emptyValue: false,
										minValue: 0,
										increment: 0.1,
										showCurrency: true,
										currencySymbol: 'R$',
										format: { format: '0.00', decimalChar: '.', thousandsChar: ',' }
			});
			$("li.hasHiddenMenu").each(function () {
					$(this).hover(
						function () {
							$("ul.hiddenMenu", this).show();
						},
						function () {
							$("ul.hiddenMenu", this).hide();
						}
					);
			});
			$('#popupDialog').dialog({
				autoOpen: false,
				closeOnEscape: false,
				width: 600,
				zIndex: 3000
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

	registerOrder: function() {
		var instance = this;
		$("#popupDialog").dialog("option", "buttons", {
			"Confirmar": function() {
					instance.requestOrderRegistration();
					$(this).dialog("close");
			},
			"Cancelar": function() {
					$(this).dialog("close");
			}
		});
		$("#popupDialog").dialog("option", "modal", true);
		$("#popupDialog").dialog("option", "title", "Informações de Compra");
		var content = "Endereço de Entrega: \
<select id='shippingAddress'>\
	<option value=\"first option\">Option 1</option>\
	<option value=\"second option\">Option 2</option>\
	<option value=\"third option\">Option 3</option>\
</select>\
<br/>"
					+ "Forma de Pagamento: \
<select id='paymentMethod'>\
	<option value=\"first option\">Option 1</option>\
	<option value=\"second option\">Option 2</option>\
	<option value=\"third option\">Option 3</option>\
</select>\
<br/>";
		$("#popupDialog").html(content);
		$('#popupDialog').dialog('open');
	},

	requestOrderRegistration: function() {
		json = new Object;
		json.paymentMethod = $("#paymentMethod").val();
		json.shippingAddress = $("#shippingAddress").val();

		var JSONstring = $.toJSON(json);

		if(!this.waitingResponse) {
			this.waitingResponse = true;
			var instance = this;
			$.ajax({url: "/register/order",
					type: 'POST',
					data: {json: JSONstring},
					dataType: 'json',
					success: function(json) {
						if(json.success) {
							$("#cartSize").html("0");
							$(".cartItem").html("");
							alert("Compra efetuada com sucesso!");
						}
						else
							alert("Erro ao confirmar pedido.");
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
			$.ajax({url: "/register/cart_item",
					type: 'POST',
					data: {json: JSONstring},
					dataType: 'json',
					success: function(json) {
						$.ajax({url: "/get/cart_info",
								type: 'GET',
								dataType: 'json',
								success: function(info) {
									if(info.success)
										$("#cartSize").html(info.size);
						  		}
						});

						instance.waitingResponse = false;
			  		}
			});
		}
	}
};

shop.init();
