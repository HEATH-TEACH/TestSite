function addToCart(productId) {
    fetch('/add_to_cart', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => {
        if (response.ok) {
            alert('Product added to cart!');
        } else {
            alert('Failed to add product.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        console.log('An error occurred.');
    });
}
