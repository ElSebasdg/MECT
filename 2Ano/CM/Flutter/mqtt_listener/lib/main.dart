import 'dart:convert';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:mqtt_client/mqtt_client.dart';
import 'package:mqtt_client/mqtt_server_client.dart';
import 'package:fl_chart/fl_chart.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Light Sensor Readings',
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
  List<FlSpot> luxReadings = [];
  int xAxisCounter = 0;
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
    print('Failed to subscribe to $topic');
  }

  void _pong() {
    print('Ping response client received');
  }

  void _onMessage(List<MqttReceivedMessage<MqttMessage>> event) {
    final MqttPublishMessage recMessage = event[0].payload as MqttPublishMessage;
    final String message =
    MqttPublishPayload.bytesToStringAsString(recMessage.payload.message);

    try {
      final decodedMessage = jsonDecode(message);
      if (decodedMessage['type'] == 'sensor_reading' && decodedMessage['id'] == 2) {
        final luxValue = decodedMessage['lux'] as double;

        setState(() {
          luxReadings.add(FlSpot(xAxisCounter.toDouble(), luxValue));
          xAxisCounter++;
        });
        print('Added lux value to chart: $luxValue');
      } else {
        print('Message received but does not match expected format.');
      }
    } catch (e) {
      print('Error parsing message: $e');
    }
  }

  void _clearMessages() {
    setState(() {
      luxReadings.clear();
      xAxisCounter = 0;
    });
    print('Cleared all messages');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Light Sensor Readings'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.cleaning_services, color: Colors.white),
            onPressed: _clearMessages,
            tooltip: 'Clear Data',
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Expanded(
              child: LineChart(
                LineChartData(
                  minY: 0,
                  titlesData: FlTitlesData(
                    leftTitles: AxisTitles(
                      sideTitles: SideTitles(showTitles: true, reservedSize: 40),
                    ),
                    bottomTitles: AxisTitles(
                      sideTitles: SideTitles(showTitles: false),
                    ),
                  ),
                  gridData: FlGridData(show: true),
                  borderData: FlBorderData(
                    show: true,
                    border: Border.all(color: Colors.black, width: 1),
                  ),
                  lineBarsData: [
                    LineChartBarData(
                      spots: luxReadings,
                      isCurved: true,
                      color: Colors.indigo,
                      barWidth: 3,
                      belowBarData:
                      BarAreaData(show: true, color: Colors.indigo.withOpacity(0.3)),
                      dotData: FlDotData(show: false),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
            Text(
              luxReadings.isNotEmpty
                  ? 'Latest Lux Reading: ${luxReadings.last.y.toStringAsFixed(2)}'
                  : 'Awaiting Data...',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    client.disconnect();
    super.dispose();
  }
}
