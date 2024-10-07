import 'package:flutter/material.dart';
import 'profile.dart'; // Import the profile.dart file

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

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 4, // We have 4 tabs
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Shopping App'),
          backgroundColor: Colors.blueGrey, // cor de fundo
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
                  leading: Image.asset(product.imageUrl), // Product image
                  title: Text(product.name), // Product name
                  subtitle: Text('\$${product.price.toString()}'), // Product price
                  onTap: () {
                    // Navigate to product detail page
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ProductDetailScreen(product: product),
                      ),
                    );
                  },
                );
              },
            ),
            // Categories tab
            const Center(child: Text('Categories Placeholder')),
            // Cart tab
            const Center(child: Text('Cart is Empty')),
            // Profile tab with button to navigate to Profile screen
            Center(
              child: ElevatedButton(
                onPressed: () {
                  // Navigate to the Profile page
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

  const ProductDetailScreen({required this.product});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
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
                // Placeholder: Add to cart action
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
