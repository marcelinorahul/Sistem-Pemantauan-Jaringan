from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
import threading
import time
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Inisialisasi Flask-Migrate
migrate = Migrate(app, db)

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat konfigurasi dari file config.py dalam folder instance
app.config.from_pyfile('instance/config.py')

# Inisialisasi SQLAlchemy
db = SQLAlchemy(app)

# Inisialisasi Flask-Bootstrap
Bootstrap(app)

# Import modul
from modules import snmp_monitor, data_processor, alert_system, port_scanner
from modules.database import init_app

# Model database untuk perangkat
class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(50))
    cpu_usage = db.Column(db.Float)
    mem_usage = db.Column(db.Float)
    bandwidth = db.Column(db.Float)
    open_ports = db.Column(db.String)

# Inisialisasi database
init_app(app)

# Route untuk halaman utama
@app.route('/')
def index():
    devices = Device.query.all()
    return render_template('index.html', devices=devices)

# Route untuk detail perangkat
@app.route('/device/<int:device_id>')
def device_detail(device_id):
    device = Device.query.get_or_404(device_id)
    return render_template('device_detail.html', device=device)

# Fungsi untuk memantau jaringan
def monitor_network():
    while True:
        try:
            devices = Device.query.all()
            for device in devices:
                data = snmp_monitor.poll_device(device.ip_address)
                port_data = port_scanner.scan_ports(device.ip_address)
                data_processor.process_data(device, data, port_data)
                db.session.commit()
        except Exception as e:
            print(f"Error in monitoring: {e}")
        time.sleep(300)  # Interval 5 menit



# Menjalankan aplikasi Flask dan thread pemantauan jaringan
if __name__ == '__main__':
    threading.Thread(target=monitor_network, daemon=True).start()
    app.run(debug=True)
