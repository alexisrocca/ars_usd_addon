fetch('https://www.dolarsi.com/api/api.php?type=dolar').then(response => response.json()).then(data => dolar_price = data[0].casa.compra);

frappe.ui.form.on("Item", {
    refresh(frm) {
        
    }
})
