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
      title: 'MQTT Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
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
        .withClientIdentifier('flutter_client')
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MQTT Example'),
      ),
      body: Center(
        child: ListView.builder(
          itemCount: messages.length,
          itemBuilder: (context, index) {
            return ListTile(
              title: Text(messages[index]),
            );
          },
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
