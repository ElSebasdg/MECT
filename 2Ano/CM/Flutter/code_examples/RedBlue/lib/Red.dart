import 'package:flutter/material.dart';

class Red extends StatefulWidget {
  @override
  State<Red> createState() {
    return _RedWidget();
  }
}

class _RedWidget extends State<Red> {
  
  Widget build(BuildContext context) {
   

    return Scaffold(
      appBar: AppBar(
        title: Text('Red'),
      ),
      body: SizedBox.expand(
        child: Container(
          color: Colors.red,
          child: Column(children: [
            Text('Red')
          ]
        ),
        )
      )
    );
  }
}
