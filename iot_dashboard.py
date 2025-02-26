import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

# Simulating sensor data
def get_sensor_data():
    temperature = round(random.uniform(20, 40), 2)  # Simulated temperature (°C)
    voltage = round(random.uniform(3.0, 5.0), 2)    # Simulated voltage (V)
    return temperature, voltage

# Data storage
time_values = []
temperature_values = []
voltage_values = []

# Create plot
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # Create second y-axis

def update_graph(i):
    current_time = time.strftime("%H:%M:%S")  # Get current time
    temperature, voltage = get_sensor_data()  # Get simulated sensor data

    # Append data
    time_values.append(current_time)
    temperature_values.append(temperature)
    voltage_values.append(voltage)

    # Limit data to last 20 entries
    if len(time_values) > 20:
        time_values.pop(0)
        temperature_values.pop(0)
        voltage_values.pop(0)

    ax1.clear()
    ax2.clear()

    # Plot Temperature
    ax1.plot(time_values, temperature_values, 'r-', label="Temperature (°C)")
    ax1.set_ylabel("Temperature (°C)", color='r')
    ax1.tick_params(axis='y', labelcolor='r')

    # Plot Voltage
    ax2.plot(time_values, voltage_values, 'b-', label="Voltage (V)")
    ax2.set_ylabel("Voltage (V)", color='b')
    ax2.tick_params(axis='y', labelcolor='b')

    # Titles and labels
    plt.xticks(rotation=45, ha='right')
    ax1.set_title("Real-Time IoT Dashboard")
    ax1.set_xlabel("Time (HH:MM:SS)")
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

# Animate the graph
ani = animation.FuncAnimation(fig, update_graph, interval=1000)

# Show plot
plt.show()
