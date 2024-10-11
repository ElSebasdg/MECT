import 'package:flutter/material.dart';
import 'profile.dart'; // Import the profile.dart file

class Cart {
  final List<CartItem> _items = [];

  void addItem(Product product, int quantity) {
    final existingItem = _items.firstWhere(
          (item) => item.product.name == product.name,
      orElse: () => CartItem(product, 0),
    );

    if (existingItem.quantity == 0) {
      _items.add(CartItem(product, quantity));
    } else {
      existingItem.quantity += quantity;
    }
  }

  void removeItem(Product product) {
    _items.removeWhere((item) => item.product.name == product.name);
  }

  void decreaseQuantity(Product product) {
    final existingItem = _items.firstWhere(
          (item) => item.product.name == product.name,
      orElse: () => CartItem(product, 0),
    );

    if (existingItem.quantity > 1) {
      existingItem.quantity--;
    } else {
      removeItem(product);
    }
  }

  List<CartItem> get items => _items;

  double get totalPrice => _items.fold(0, (sum, item) => sum + (item.product.price * item.quantity));
}

class CartItem {
  final Product product;
  int quantity;

  CartItem(this.product, this.quantity);
}

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  // List of sample products
  final List<Product> products = [
    Product('Sapato di Nike', 20, 'assets/images/shoes.jpg'),
    Product('Tshirt Shrek', 119.99, 'assets/images/tshirt.jpg'),
    Product('Relogio Ben 10', 9999999.99, 'assets/images/watch.jpg'),
  ];

  final Cart cart = Cart();

  void addToCart(Product product, int quantity) {
    setState(() {
      cart.addItem(product, quantity);
    });
  }

  void removeFromCart(Product product) {
    setState(() {
      cart.removeItem(product);
    });
  }

  void decreaseQuantity(Product product) {
    setState(() {
      cart.decreaseQuantity(product);
    });
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4, // We have 4 tabs
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Shopping App'),
          backgroundColor: Colors.blueGrey,
          bottom: const TabBar(
            tabs: [
              Tab(icon: Icon(Icons.home), text: 'Home'),
              Tab(icon: Icon(Icons.category), text: 'Categories'),
              Tab(icon: Icon(Icons.shopping_cart), text: 'Cart'),
              Tab(icon: Icon(Icons.person), text: 'Profile'),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            // Home tab
            ListView.builder(
              itemCount: products.length,
              itemBuilder: (context, index) {
                final product = products[index];
                return ListTile(
                  leading: Image.asset(product.imageUrl),
                  title: Text(product.name),
                  subtitle: Text('\$${product.price.toString()}'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ProductDetailScreen(
                          product: product,
                          addToCart: addToCart,
                        ),
                      ),
                    );
                  },
                );
              },
            ),
            // Categories tab
            const Center(child: Text('Categories Placeholder')),
            // Cart tab
            CartScreen(
              cart: cart,
              removeFromCart: removeFromCart,
              decreaseQuantity: decreaseQuantity,
            ),
            // Profile tab with button to navigate to Profile screen
            Center(
              child: ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const Profile()),
                  );
                },
                child: const Text('Go to Profile Details'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class Product {
  final String name;
  final double price;
  final String imageUrl;

  Product(this.name, this.price, this.imageUrl);
}

class ProductDetailScreen extends StatelessWidget {
  final Product product;
  final Function(Product, int) addToCart;

  const ProductDetailScreen({required this.product, required this.addToCart});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueGrey,
        title: Text(product.name),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Image.asset(product.imageUrl),
            const SizedBox(height: 16),
            Text(product.name, style: const TextStyle(fontSize: 24)),
            const SizedBox(height: 8),
            Text('\$${product.price.toString()}',
                style: const TextStyle(fontSize: 20, color: Colors.green)),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                addToCart(product, 1);
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Added to cart')),
                );
              },
              child: const Text('Add to Cart'),
            ),
          ],
        ),
      ),
    );
  }
}

class CartScreen extends StatelessWidget {
  final Cart cart;
  final Function(Product) removeFromCart;
  final Function(Product) decreaseQuantity;

  const CartScreen({
    required this.cart,
    required this.removeFromCart,
    required this.decreaseQuantity,
  });

  @override
  Widget build(BuildContext context) {
    return cart.items.isEmpty
        ? const Center(child: Text('Cart is Empty'))
        : Column(
      children: [
        Expanded(
          child: ListView.builder(
            itemCount: cart.items.length,
            itemBuilder: (context, index) {
              final item = cart.items[index];
              return Dismissible(
                key: Key(item.product.name),
                direction: DismissDirection.endToStart,
                background: Container(
                  color: Colors.red,
                  alignment: Alignment.centerRight,
                  padding: const EdgeInsets.only(right: 20),
                  child: const Icon(Icons.delete, color: Colors.white),
                ),
                onDismissed: (direction) {
                  removeFromCart(item.product);
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text('${item.product.name} removed from cart')),
                  );
                },
                child: ListTile(
                  leading: Image.asset(item.product.imageUrl),
                  title: Text(item.product.name),
                  subtitle: Text('Quantity: ${item.quantity}'),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text('\$${(item.product.price * item.quantity).toStringAsFixed(2)}'),
                      IconButton(
                        icon: const Icon(Icons.remove),
                        onPressed: () {
                          decreaseQuantity(item.product);
                        },
                      ),
                    ],
                  ),
                ),
              );
            },
          ),
        ),
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(
            'Total: \$${cart.totalPrice.toStringAsFixed(2)}',
            style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
        ),
      ],
    );
  }
}