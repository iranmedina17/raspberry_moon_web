#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_USER="$(id -un)"
SERVICE_FILE="/etc/systemd/system/moon-web.service"
PYTHON_BIN="$APP_DIR/.venv/bin/python"

if [ ! -f "$APP_DIR/app.py" ]; then
  echo "No encuentro app.py en $APP_DIR"
  exit 1
fi

if [ ! -x "$PYTHON_BIN" ]; then
  echo "No encuentro el entorno virtual en $APP_DIR/.venv"
  echo "Ejecuta primero:"
  echo "  python3 -m venv .venv"
  echo "  source .venv/bin/activate"
  echo "  pip install -r requirements.txt"
  exit 1
fi

echo "Creando servicio systemd para:"
echo "  Usuario: $APP_USER"
echo "  Carpeta: $APP_DIR"

sudo tee "$SERVICE_FILE" >/dev/null <<EOF
[Unit]
Description=Moon Phase Web Interface
After=network-online.target
Wants=network-online.target

[Service]
User=$APP_USER
WorkingDirectory=$APP_DIR
ExecStart=$PYTHON_BIN $APP_DIR/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now moon-web.service

echo
echo "Servicio instalado."
echo "Estado actual:"
sudo systemctl --no-pager status moon-web.service

