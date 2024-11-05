import 'package:flutter/material.dart';




import 'Red.dart';
import 'Blue.dart';

class Router {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case '/':
        return MaterialPageRoute(builder: (_) => Blue());
      case '/red':
        return MaterialPageRoute(builder: (_) => Red());
      case '/blue':
        return MaterialPageRoute(builder: (_) => Blue());
      default:
        return MaterialPageRoute(
            builder: (_) => Scaffold(
                  body: Center(
                      child: Text('No route defined for ${settings.name}')),
                ));
    }
  }
}


void main() => runApp(
      MaterialApp(
            home: Blue(),
            onGenerateRoute: Router.generateRoute,
          ));
