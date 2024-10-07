package main

import (
	"fmt"
	"log"
	"context"

	paho "github.com/eclipse/paho.mqtt.golang"
	influxdb "github.com/influxdata/influxdb-client-go/v2"
	"github.com/kelseyhightower/envconfig"
)

// I want to display a list of devices
// then the user can select a device
// after selecting the device he can choose a color or to shut down the device's LED

// this has to be done as a cli application

// List of colors
var COLORS = []string{
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "white",
}

// This tells the envconfig package what to read from the environment
type Config struct {
	MQTTBroker 			string `envconfig:"MQTT_BROKER" default:"tcp://localhost:1883"`
	MQTTTopic 			string `envconfig:"MQTT_TOPIC" default:"#"`
	InfluxDBHost 		string `envconfig:"INFLUXDB_HOST" default:"http://localhost:8086"`
	InfluxDBName 		string `envconfig:"INFLUXDB_NAME" default:"cm-project"`
	InfluxDBUser 		string `envconfig:"INFLUXDB_USER"`
	InfluxDBPassword 	string `envconfig:"INFLUXDB_PASSWORD"`
	InfluxMeasurement 	string `envconfig:"INFLUX_MEASUREMENT"`
	InfluxToken 		string `envconfig:"INFLUX_TOKEN"`
}

var influx_client influxdb.Client
var mqtt_client paho.Client
var config Config

func init() {
	// Read the configuration from the environment
	err := envconfig.Process("", &config)
	if err != nil {
		log.Fatal(err.Error())
	}

	fmt.Println("MQTT_BROKER:", config.MQTTBroker)
	fmt.Println("MQTT_TOPIC:", config.MQTTTopic)
	fmt.Println("INFLUXDB_HOST:", config.InfluxDBHost)
	fmt.Println("INFLUXDB_NAME:", config.InfluxDBName)
	fmt.Println("INFLUXDB_USER:", config.InfluxDBUser)

	// Create a new MQTT client
	opts := paho.NewClientOptions()
	opts.AddBroker(config.MQTTBroker)
	opts.SetClientID("board_controller")
	opts.SetCleanSession(true)

	// Connect to the MQTT broker
	mqtt_client = paho.NewClient(opts)
	if token := mqtt_client.Connect(); token.Wait() && token.Error() != nil {
		log.Fatal(token.Error())
	}

	// Connect to InfluxDB
	influx_client = influxdb.NewClient(config.InfluxDBHost, config.InfluxToken)
	_, err = influx_client.Health(context.Background())
	if err != nil {
		log.Fatal(err.Error())
	}

	if influx_client == nil {
		log.Fatal("InfluxDB client is nil")
	}
}

func main() {

	// Loop until the user wants to exit
	for {
		// get the list of devices
		devices, err := getDevices()
		if err != nil {
			log.Fatal(err)
		}

		// display the list of devices
		fmt.Println("Devices:")
		fmt.Println("0: All")
		for i, device := range devices {
			fmt.Printf("%d: %s\n", i+1, device)
		}

		// print the exit option
		fmt.Printf("%d: Exit\n", 9)

		// ask the user to select a device
		fmt.Print("Select an option: ")
		var device int
		fmt.Scanln(&device)

		// check if the user wants to exit
		if device == 9 {
			return
		}

		// ask the user to select a command
		fmt.Println("Commands:")
		fmt.Println("0: Turn off LED")
		for i, color := range COLORS {
			fmt.Printf("%d: Set color to %s\n", i+1, color)
		}
		fmt.Print("Select a command: ")
		var command int
		fmt.Scanln(&command)

		if device == 0 {
			err = sendCommand("all", command)
			if err != nil {
				log.Fatal(err)
			}
		} else {
			// send the command to the device
			err = sendCommand(devices[device-1], command)
			if err != nil {
				log.Fatal(err)
			}
		}

		fmt.Println("Command sent")
		fmt.Println()
	}
}

func getDevices() ([]string, error) {
	// get the list of devices from influxdb
	// import "influxdata/influxdb/v1"

	// v1.tagValues(
	// bucket: "cm-project",
	// tag: "device"
	// )

	// Create a query string
	query := fmt.Sprintf("import \"influxdata/influxdb/v1\"\nv1.tagValues(bucket: \"%s\", tag: \"device\")", config.InfluxDBName)

	// Query the database
	result, err := queryDB(influx_client, config.InfluxDBName, query)
	if err != nil {
		log.Fatal(err)
	}

	return result, nil
}

func sendCommand(device string, command int) error {
	// send an mqtt message to the gateway
	// example topic: cm-project/gateway/device02/led_status
	// example payload: 1

	// get the command name
	var commandName string
	if command == 0 {
		commandName = "status"
	} else {
		commandName = "color"
	}

	// create the topic
	topic := fmt.Sprintf("cm-project/controller/%s/%s", device, commandName)
	fmt.Println(topic)

	// create the payload
	var payload string
	if command == 0 {
		payload = "0"
	} else {
		payload = COLORS[command-1]
	}

	// publish the message
	token := mqtt_client.Publish(topic, 0, false, payload)
	token.Wait()
	if token.Error() != nil {
		return token.Error()
	}

	return nil
}

func queryDB(client influxdb.Client, org string, query string) ([]string, error) {
	// Create a new query
	queryAPI := client.QueryAPI(org)
	result, err := queryAPI.Query(context.Background(), query)
	if err != nil {
		return nil, err
	}

	// Iterate over query results
	var devices []string
	for result.Next() {
		// Process the row
		devices = append(devices, result.Record().Value().(string))
	}

	if result.Err() != nil {
		return nil, result.Err()
	}

	return devices, nil
}