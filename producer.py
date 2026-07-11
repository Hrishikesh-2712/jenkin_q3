from kafka import KafkaProducer
import json, time
import random
import datetime

producer = KafkaProducer(bootstrap_servers="localhost:9092",
                          value_serializer=lambda v: json.dumps(v).encode())


while True:
    sensor_id = random.randint(1,10)
    temperature = random.randint(20,40)
    timestamp = datetime.datetime.now()
    #producer.send("sensor-data", {"sensor_id": "s1", "temperature": 28.0})
    producer.send("sensor-data", {sensor_id: "s1",
                                  "temperature": temperature,
                                  "timestamp":f"{timestamp}"})
    # TODO: randomize sensor_id/temperature, add a real timestamp field
    time.sleep(1)
    
