package pt.ua.practice

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.tooling.preview.Preview
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.eclipse.paho.android.service.MqttAndroidClient
import org.eclipse.paho.client.mqttv3.*
import pt.ua.practice.ui.theme.PracticeTheme

class MainActivity : ComponentActivity() {

    private lateinit var mqttClient: MqttAndroidClient
    private val serverUri = "tcp://test.mosquitto.org:1883"
    private val topic = "test/compose/topic"
    private var isMQTTConnected = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        mqttClient = MqttAndroidClient(applicationContext, serverUri, "compose_client")

        setContent {
            PracticeTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    MQTTApp(
                        modifier = Modifier.padding(innerPadding),
                        mqttClient = mqttClient,
                        topic = topic,
                        isMQTTConnected = { isMQTTConnected }
                    )
                }
            }
        }

        connectToMQTTBroker()
    }

    private fun connectToMQTTBroker() {
        val options = MqttConnectOptions().apply {
            isCleanSession = true
        }

        mqttClient.setCallback(object : MqttCallback {
            override fun connectionLost(cause: Throwable?) {
                isMQTTConnected = false
                Log.d("MQTT", "Connection lost: ${cause?.message}")
            }

            override fun messageArrived(topic: String?, message: MqttMessage?) {
                Log.d("MQTT", "Message received: ${message.toString()} on topic: $topic")
            }

            override fun deliveryComplete(token: IMqttDeliveryToken?) {
                Log.d("MQTT", "Message delivery complete")
            }
        })

        try {
            mqttClient.connect(options, null, object : IMqttActionListener {
                override fun onSuccess(asyncActionToken: IMqttToken?) {
                    isMQTTConnected = true
                    Log.d("MQTT", "Connected to broker")
                }

                override fun onFailure(asyncActionToken: IMqttToken?, exception: Throwable?) {
                    isMQTTConnected = false
                    Log.e("MQTT", "Failed to connect: ${exception?.message}")
                }
            })
        } catch (e: MqttException) {
            e.printStackTrace()
        }
    }

    override fun onDestroy() {
        mqttClient.disconnect()
        super.onDestroy()
    }
}

@Composable
fun MQTTApp(
    modifier: Modifier = Modifier,
    mqttClient: MqttAndroidClient,
    topic: String,
    isMQTTConnected: () -> Boolean
) {
    var receivedMessage by remember { mutableStateOf("") }
    val coroutineScope = rememberCoroutineScope()

    Column(modifier = modifier.padding(16.dp)) {
        Text(text = "MQTT Jetpack Compose", style = MaterialTheme.typography.titleLarge)
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = {
            coroutineScope.launch {
                if (isMQTTConnected()) {
                    publishMessage(mqttClient, topic, "Hello from Jetpack Compose!")
                } else {
                    Log.e("MQTT", "Client is not connected, cannot publish message")
                }
            }
        }) {
            Text(text = "Send MQTT Message")
        }
        Spacer(modifier = Modifier.height(16.dp))
        Text(text = "Received Message: $receivedMessage")
    }

    DisposableEffect(Unit) {
        mqttClient.setCallback(object : MqttCallback {
            override fun connectionLost(cause: Throwable?) {
                Log.d("MQTT", "Connection lost")
            }

            override fun messageArrived(topic: String?, message: MqttMessage?) {
                receivedMessage = message.toString()
            }

            override fun deliveryComplete(token: IMqttDeliveryToken?) {
                Log.d("MQTT", "Message delivery complete")
            }
        })
        onDispose { }
    }
}

suspend fun publishMessage(mqttClient: MqttAndroidClient, topic: String, payload: String) {
    withContext(Dispatchers.IO) {
        try {
            val message = MqttMessage(payload.toByteArray())
            message.qos = 1
            mqttClient.publish(topic, message)
        } catch (e: MqttException) {
            Log.e("MQTT", "Error publishing message: ${e.message}")
        }
    }
}

@Preview(showBackground = true)
@Composable
fun MQTTAppPreview() {
    PracticeTheme {
        MQTTApp(
            mqttClient = MqttAndroidClient(null, "", ""),
            topic = "test",
            isMQTTConnected = { false }
        )
    }
}
