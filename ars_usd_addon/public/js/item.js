frappe.ui.form.on("Item", {
    refresh(frm) {
        
    }
})

frappe.tour['Item'] = [
	{
		fieldname: "price_ars",
		title: "Price ARS",
		description: __("Price ARS")
	},
	{
		fieldname: "price_usd",
		title: "Price USD",
		description: __("Price USD")
	}
];