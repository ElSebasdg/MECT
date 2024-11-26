package pt.ua.practice

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.text.BasicText
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken
import org.eclipse.paho.client.mqttv3.MqttCallback
import org.eclipse.paho.client.mqttv3.MqttClient
import org.eclipse.paho.client.mqttv3.MqttMessage
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence
import pt.ua.practice.ui.theme.PracticeTheme

class MainActivity : ComponentActivity() {
    private lateinit var mqttClient: MqttClient

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            PracticeTheme {
                var messages by remember { mutableStateOf(listOf<String>()) }
                val coroutineScope = rememberCoroutineScope()

                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    MqttScreen(
                        messages = messages,
                        modifier = Modifier.padding(innerPadding)
                    )

                    // Connect to MQTT broker on launch
                    LaunchedEffect(Unit) {
                        coroutineScope.launch(Dispatchers.IO) {
                            connectToMQTT { newMessage ->
                                messages = messages + newMessage
                            }
                        }
                    }
                }
            }
        }
    }

    private fun connectToMQTT(onMessageReceived: (String) -> Unit) {
        val brokerUrl = "tcp://test.mosquitto.org:1883"
        val clientId = "compose_client_${System.currentTimeMillis()}"

        try {
            mqttClient = MqttClient(brokerUrl, clientId, MemoryPersistence())
            mqttClient.setCallback(object : MqttCallback {
                override fun connectionLost(cause: Throwable?) {
                    runOnUiThread {
                        Toast.makeText(
                            this@MainActivity,
                            "Disconnected from broker",
                            Toast.LENGTH_SHORT
                        ).show()
                    }
                }

                override fun messageArrived(topic: String, message: MqttMessage) {
                    val receivedMessage = "Topic: $topic\nMessage: ${message.toString()}"
                    onMessageReceived(receivedMessage)
                }

                override fun deliveryComplete(token: IMqttDeliveryToken?) {
                    // No actions needed here for this example
                }
            })

            mqttClient.connect()
            mqttClient.subscribe("test/flutter/topic")

            runOnUiThread {
                Toast.makeText(this, "Connected to MQTT broker", Toast.LENGTH_SHORT).show()
            }
        } catch (e: Exception) {
            e.printStackTrace()
            runOnUiThread {
                Toast.makeText(this, "Failed to connect: ${e.message}", Toast.LENGTH_LONG).show()
            }
        }
    }

    override fun onDestroy() {
        if (::mqttClient.isInitialized && mqttClient.isConnected) {
            mqttClient.disconnect()
        }
        super.onDestroy()
    }
}

@Composable
fun MqttScreen(messages: List<String>, modifier: Modifier = Modifier) {
    LazyColumn(modifier = modifier) {
        items(messages.size) { index ->
            BasicText(text = messages[index])
        }
    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    PracticeTheme {
        MqttScreen(messages = listOf("Sample Message 1", "Sample Message 2"))
    }
}
