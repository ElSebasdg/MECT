import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:math';
import 'package:crypto/crypto.dart';
import 'package:convert/convert.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SwitchBot Device List',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: DeviceListScreen(),
    );
  }
}

class DeviceListScreen extends StatefulWidget {
  @override
  _DeviceListScreenState createState() => _DeviceListScreenState();
}

class _DeviceListScreenState extends State<DeviceListScreen> {
  List<Map<String, dynamic>> devices = [];
  Map<String, dynamic>? deviceStatus;

  final String token = '85d4bc3e49c9b1065d268ba305ceef4887f985f496361cdd420c60537dca9fe67bf836a7977a0f8ee5503fba13a80f5f';
  final String secret = 'ce8f352762d010b0c47d2bdb5ddbd218';

  @override
  void initState() {
    super.initState();
    listDevices();
  }

  Future<void> listDevices() async {
    String nonce = _generateNonce();
    String timestamp = DateTime.now().millisecondsSinceEpoch.toString();
    String data = token + timestamp + nonce;
    String signature = _generateSignature(data, secret);

    final Uri url = Uri.parse('https://api.switch-bot.com/v1.1/devices');

    try {
      final response = await http.get(
        url,
        headers: {
          'Authorization': token,
          'sign': signature,
          'nonce': nonce,
          't': timestamp,
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);

        // Imprime a resposta JSON no console para debug
        print('Resposta JSON da API (listDevices): $data');

        setState(() {
          devices = List<Map<String, dynamic>>.from(data['body']['deviceList']);
        });
      } else {
        print('Erro ao obter a lista de dispositivos: ${response.statusCode}');
        print('Resposta: ${response.body}');
      }
    } catch (e) {
      print('Erro: $e');
    }
  }

  Future<void> getDeviceStatus(String deviceId) async {
    String nonce = _generateNonce();
    String timestamp = DateTime.now().millisecondsSinceEpoch.toString();
    String data = token + timestamp + nonce;
    String signature = _generateSignature(data, secret);

    final Uri url = Uri.parse('https://api.switch-bot.com/v1.1/devices/$deviceId/status');

    try {
      final response = await http.get(
        url,
        headers: {
          'Authorization': token,
          'sign': signature,
          'nonce': nonce,
          't': timestamp,
          'Content-Type': 'application/json',
        },
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);

        // Imprime a resposta JSON no console para debug
        print('Resposta JSON da API (getDeviceStatus): $data');

        setState(() {
          deviceStatus = data['body'];
        });

        showDialog(
          context: context,
          builder: (_) => AlertDialog(
            title: Text('Status do Dispositivo'),
            content: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("ID: ${deviceStatus?['deviceId'] ?? 'Desconhecido'}"),
                Text("Tipo: ${deviceStatus?['deviceType'] ?? 'Desconhecido'}"),
                Text("Hub ID: ${deviceStatus?['hubDeviceId'] ?? 'Desconhecido'}"),
                Text("Bateria: ${deviceStatus?['battery'] ?? 'N/A'}%"),
                Text("Versão: ${deviceStatus?['version'] ?? 'Desconhecido'}"),
                Text("Temperatura: ${deviceStatus?['temperature'] ?? 'N/A'} °C"),
                Text("Humidade: ${deviceStatus?['humidity'] ?? 'N/A'}%"),
              ],
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: Text('Fechar'),
              ),
            ],
          ),
        );
      } else {
        print('Erro ao obter o status do dispositivo: ${response.statusCode}');
        print('Resposta: ${response.body}');
      }
    } catch (e) {
      print('Erro: $e');
    }
  }

  String _generateNonce() {
    return Random().nextInt(1 << 32).toString();
  }

  String _generateSignature(String data, String secret) {
    final key = utf8.encode(secret);
    final bytes = utf8.encode(data);

    final hmacSha256 = Hmac(sha256, key); // HMAC-SHA256
    final digest = hmacSha256.convert(bytes);
    return base64Encode(digest.bytes);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Lista de Dispositivos SwitchBot'),
      ),
      body: devices.isEmpty
          ? Center(child: CircularProgressIndicator())
          : ListView.builder(
        itemCount: devices.length,
        itemBuilder: (context, index) {
          final device = devices[index];
          return ListTile(
            title: Text(device['deviceName'] ?? 'Dispositivo Desconhecido'),
            subtitle: Text('ID: ${device['deviceId']}'),
            onTap: () => getDeviceStatus(device['deviceId']),
          );
        },
      ),
    );
  }
}
