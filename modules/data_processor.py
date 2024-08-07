from modules.alert_system import send_alert
from app import db, Device

def process_data(device, data, open_ports):
    device.cpu_usage = data.get('cpu', 0)
    device.mem_usage = data.get('memory', 0)
    device.bandwidth = data.get('bandwidth', 0)
    device.open_ports = ','.join(map(str, open_ports))

    if device.cpu_usage > 80:
        send_alert(device.ip_address, f"CPU usage high: {device.cpu_usage}%")
    if device.mem_usage > 80:
        send_alert(device.ip_address, f"Memory usage high: {device.mem_usage}%")
    if device.bandwidth > 1000:
        send_alert(device.ip_address, f"High bandwidth usage: {device.bandwidth} Mbps")
    if open_ports:
        send_alert(device.ip_address, f"Open ports detected: {', '.join(map(str, open_ports))}")
