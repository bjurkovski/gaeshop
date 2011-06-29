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

	searchProduct: function() {
		q = encodeURI($("#searchBox").val());
		window.location.replace("/search?q="+q);
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
						if(json.success) {
							$("#productName").val("");
							$("#productPrice").val("0.00");
							$("#productDescription").val("");
							$("#productStock").val("0");
							alert("Produto inserido com sucesso!");
						}
						else
							alert("Erro ao inserir produto! Erro: " + json.message);
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
		var content = "Endereço de Entrega: <input type='text' id='shippingAddress'><br/>"

					+ "Forma de Pagamento:\
<select id='paymentMethod'>\
	<option value=\"card\">Cartão de Crédito</option>\
	<option value=\"billet\">Boleto Bancário</option>\
	<option value=\"paypal\">PayPal</option>\
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
							//alert("Compra efetuada com sucesso!");
							$("#popupDialog").dialog("option", "buttons", {
										"OK": function() { $(this).dialog("close"); window.location.reload(); }
							});
							$("#popupDialog").dialog("option", "modal", true);
							$("#popupDialog").dialog("option", "title", "Compra efetuada com sucesso!");
							var content = "";
							for(var i=0; i<json.receipt.length; i++) {
								content += json.receipt[i][1] + "x " + json.receipt[i][0] + "<br/>";
							}
							$("#popupDialog").html(content);
							$('#popupDialog').dialog('open');
						}
						else
							alert("Erro ao confirmar pedido. Erro: " + json.message);
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
						if(json.success) {
							$.ajax({url: "/get/cart_info",
									type: 'GET',
									dataType: 'json',
									success: function(info) {
										if(info.success)
											$("#cartSize").html(info.size);
							  		}
							});
						}
						else {
							$("#popupDialog").dialog("option", "buttons", {
										"OK": function() { $(this).dialog("close"); }
							});
							$("#popupDialog").dialog("option", "modal", true);
							$("#popupDialog").dialog("option", "title", "Erro");
							$("#popupDialog").html("Usuário deslogado. Faça login para efetuar esta operação.");
							$('#popupDialog').dialog('open');
						}

						instance.waitingResponse = false;
			  		}
			});
		}
	}
};

shop.init();
