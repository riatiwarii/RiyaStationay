document.addEventListener("DOMContentLoaded", function () {
    var productSelect = document.getElementById("product-select");
    var priceSpan = document.getElementById("price");
    var quantityInput = document.getElementById("quantity");
    var totalCostSpan = document.getElementById("totalCost");
    var cartList = document.getElementById("cart-items");
    var cartItems = [];

    // Function to update the cart display
    function updateCart() {
        cartList.innerHTML = "";
        cartItems.forEach(function (item, index) {
            var li = document.createElement("li");
            li.textContent = `${item.product_name} - $${item.price} x ${item.quantity}`;
            
            // Plus button
            var plusButton = document.createElement("button");
            plusButton.type = "button";
            plusButton.textContent = "+";
            plusButton.classList.add("plus-minus-button");
            plusButton.addEventListener("click", function () {
                // Increase the quantity when the plus button is clicked
                item.quantity++;
                // Update the cart display
                updateCart();
                // Update cart items in localStorage
                localStorage.setItem("cartItems", JSON.stringify(cartItems));
            });
            
            // Minus button
            var minusButton = document.createElement("button");
            minusButton.type = "button";
            minusButton.textContent = "-";
            minusButton.classList.add("plus-minus-button");
            minusButton.addEventListener("click", function () {
                // Decrease the quantity when the minus button is clicked
                if (item.quantity > 1) {
                    item.quantity--;
                } else {
                    // Remove the item from the cart if quantity reaches 0
                    cartItems.splice(index, 1);
                }
                // Update the cart display
                updateCart();
                // Update cart items in localStorage
                localStorage.setItem("cartItems", JSON.stringify(cartItems));
            });
            
            var removeForm = document.createElement("form");
            removeForm.method = "post";
            var csrfInput = document.createElement("input");
            csrfInput.type = "hidden";
            csrfInput.name = "csrfmiddlewaretoken";
            csrfInput.value = "{{ csrf_token }}";
            
            li.appendChild(plusButton);
            li.appendChild(minusButton);
            
            removeForm.appendChild(csrfInput);
            li.appendChild(removeForm);
            cartList.appendChild(li);
        });
        // Calculate and display the total cost
        var totalCost = cartItems.reduce(function (total, item) {
            return total + item.price * item.quantity;
        }, 0);
        totalCostSpan.textContent = totalCost.toFixed(2);
        // Update cart items in localStorage
        localStorage.setItem("cartItems", JSON.stringify(cartItems));
    }

    // Load cart items from localStorage when the page loads
    var storedCartItems = localStorage.getItem("cartItems");
    if (storedCartItems) {
        cartItems = JSON.parse(storedCartItems);
        updateCart();
    }

    // Update price when product selection changes
    productSelect.addEventListener("change", function () {
        var selectedProduct = productSelect.value;
        // You can set the price dynamically based on the selected product here
        // For this example, I'm hardcoding prices
        var prices = {
            "Notebook": 10.00,
            "Punching Machine": 20.00,
            "Stapler": 5.00,
        };
        priceSpan.textContent = prices[selectedProduct];
    });

    // Handle adding items to the cart asynchronously
    var addToCartButton = document.getElementById("add-to-cart-button");
    addToCartButton.addEventListener("click", function () {
        var selectedProduct = productSelect.value;
        var price = parseFloat(priceSpan.textContent);
        var quantity = parseInt(quantityInput.value);

        // Check if the item already exists in the cart
        var existingItemIndex = cartItems.findIndex(function (item) {
            return item.product_name === selectedProduct;
        });

        if (existingItemIndex !== -1) {
            // If the item exists, increase its quantity
            cartItems[existingItemIndex].quantity += quantity;
        } else {
            // If the item does not exist, add it to the cart
            cartItems.push({
                product_name: selectedProduct,
                price: price,
                quantity: quantity,
            });
        }

        // Update the cart display
        updateCart();
    });
});