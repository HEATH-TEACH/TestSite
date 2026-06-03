function getCart() {
    fetch('/get_cart')
        .then(response => response.json())
        .then(cart => {
            const table = document.createElement('table');

            const header = document.createElement('tr');
            ['Product', 'Quantity', 'Unit Price', 'Total Price'].forEach(text => {
                const th = document.createElement('th');
                th.textContent = text;
                header.appendChild(th);
            });
            table.appendChild(header);

            Object.values(cart).forEach(item => {
                const row = document.createElement('tr');
                const name = document.createElement('td');
                name.textContent = item.name;
                const quantity = document.createElement('td');
                quantity.textContent = item.quantity;
                const price_unit = document.createElement('td');
                price_unit.textContent = item.price;
                const total_price = document.createElement('td');
                total_price.textContent = (item.price * item.quantity).toFixed(2);

                row.appendChild(name);
                row.appendChild(quantity);
                row.appendChild(price_unit);
                row.appendChild(total_price);
                table.appendChild(row);
            });

            const cart_element = document.getElementById('p_cart');
            cart_element.innerHTML = '';
            cart_element.appendChild(table);
        })
        .catch(error => {
            console.error('Error fetching cart:', error);
        });
}

getCart()