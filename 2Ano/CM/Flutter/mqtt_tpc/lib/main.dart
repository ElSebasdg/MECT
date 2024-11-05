import 'dart:async';
import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Simulated Light Sensor',
      theme: ThemeData(
        fontFamily: 'SansSerif',
        primarySwatch: Colors.indigo,
        scaffoldBackgroundColor: Colors.white,
        appBarTheme: AppBarTheme(
          backgroundColor: Colors.indigo[600],
          elevation: 0,
          titleTextStyle: TextStyle(
            color: Colors.white,
            fontSize: 22,
            fontWeight: FontWeight.bold,
          ),
        ),
        textTheme: TextTheme(
          bodyMedium: TextStyle(fontSize: 18, color: Colors.grey[800]),
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(16),
            ),
            padding: EdgeInsets.symmetric(horizontal: 24, vertical: 14),
            textStyle: TextStyle(fontSize: 18),
          ),
        ),
      ),
      home: MQTTExample(),
    );
  }
}

class MQTTExample extends StatefulWidget {
  @override
  _MQTTExampleState createState() => _MQTTExampleState();
}

class _MQTTExampleState extends State<MQTTExample> {
  final client = MqttServerClient('test.mosquitto.org', '');
  List<String> messages = [];
  Timer? _timer;
  final _random = Random();

  @override
  void initState() {
    super.initState();
    _connectMQTT();
  }

  Future<void> _connectMQTT() async {
    client.logging(on: true);
    client.onConnected = _onConnected;
    client.onDisconnected = _onDisconnected;
    client.onSubscribed = _onSubscribed;
    client.onUnsubscribed = _onUnsubscribed;
    client.onSubscribeFail = _onSubscribeFail;
    client.pongCallback = _pong;

    final connMessage = MqttConnectMessage()
        .withClientIdentifier('flutter_client_${_random.nextInt(10000)}')
        .startClean()
        .withWillQos(MqttQos.atLeastOnce);
    client.connectionMessage = connMessage;

    try {
      await client.connect();
      client.updates!.listen(_onMessage);
    } catch (e) {
      print('Error: $e');
      client.disconnect();
    }
  }

  void _onConnected() {
    print('Connected to MQTT broker!');
    client.subscribe('test/flutter/topic', MqttQos.atLeastOnce);
  }

  void _onDisconnected() {
    print('Disconnected from MQTT broker');
  }

  void _onSubscribed(String topic) {
    print('Subscribed to $topic');
  }

  void _onSubscribeFail(String topic) {
    print('Failed to subscribe $topic');
  }

  void _onUnsubscribed(String? topic) {
    print('Unsubscribed from $topic');
  }

  void _pong() {
    print('Ping response client received');
  }

  void _onMessage(List<MqttReceivedMessage<MqttMessage>> event) {
    final MqttPublishMessage recMessage = event[0].payload as MqttPublishMessage;
    final String message =
    MqttPublishPayload.bytesToStringAsString(recMessage.payload.message);

    setState(() {
      messages.add(message);
    });

    print('Received message: $message from topic: ${event[0].topic}>');
  }

  double _getRandomLux(double baseLux, double variation) {
    // Retorna um valor de lux aleatório em torno do valor base
    return baseLux + (_random.nextDouble() * variation * 2) - variation;
  }

  void _publishLuxValue(double luxValue, int id) {
    final messageJson = jsonEncode({
      'type': 'sensor_reading',
      'id': id,
      'lux': luxValue,
    });

    final builder = MqttClientPayloadBuilder();
    builder.addString(messageJson);
    client.publishMessage('test/flutter/topic', MqttQos.atLeastOnce, builder.payload!);
  }

  void _simulateDay() {
    _stopTimer();
    _timer = Timer.periodic(Duration(seconds: 2), (timer) {
      double luxValue = _getRandomLux(750, 50); // Variação de ±50 ao redor de 750
      _publishLuxValue(luxValue, 2);
    });
  }

  void _simulateNight() {
    _stopTimer();
    _timer = Timer.periodic(Duration(seconds: 2), (timer) {
      double luxValue = _getRandomLux(0.5, 0.1); // Variação de ±0.1 ao redor de 0.5
      _publishLuxValue(luxValue, 2);
    });
  }

  void _stopTimer() {
    _timer?.cancel();
    _timer = null;
    print('Stopped sending messages');
  }

  void _clearMessages() {
    setState(() {
      messages.clear();
    });
    print('Cleared all messages');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Simulated Light Sensor'),
        centerTitle: true,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const SizedBox(height: 20),
              ElevatedButton.icon(
                onPressed: _simulateDay,
                icon: const Icon(Icons.wb_sunny_outlined, color: Colors.orangeAccent),
                label: const Text('Simulate Day'), // (750 lux ± 50)
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.indigo[100],
                  foregroundColor: Colors.indigo[900],
                ),
              ),
              const SizedBox(height: 16),
              ElevatedButton.icon(
                onPressed: _simulateNight,
                icon: const Icon(Icons.nightlight_round_outlined, color: Colors.indigo),
                label: const Text('Simulate Night'), // (0.5 lux ± 0.1)
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.indigo[100],
                  foregroundColor: Colors.indigo[900],
                ),
              ),
              const SizedBox(height: 16),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton.icon(
                    onPressed: _stopTimer,
                    icon: const Icon(Icons.stop_circle_outlined, color: Colors.redAccent),
                    label: const Text('Stop'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.red[100],
                      foregroundColor: Colors.red[900],
                    ),
                  ),
                  const SizedBox(width: 10),
                  ElevatedButton.icon(
                    onPressed: _clearMessages,
                    icon: const Icon(Icons.cleaning_services, color: Colors.blueAccent),
                    label: const Text('Clean'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue[100],
                      foregroundColor: Colors.blue[900],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 30),
              Expanded(
                child: Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.indigo[50],
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: ListView.builder(
                    itemCount: messages.length,
                    itemBuilder: (context, index) {
                      return ListTile(
                        leading: Icon(Icons.message, color: Colors.indigo[400]),
                        title: Text(
                          messages[index],
                          style: TextStyle(color: Colors.indigo[900]),
                        ),
                      );
                    },
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _stopTimer();
    client.disconnect();
    super.dispose();
  }
}
