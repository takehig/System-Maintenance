# LogAPI Service

システムログ監視サービス - Port 8005

## 機能

- 各サービスのsystemdログをリアルタイム表示
- ログ内容のクリップボードコピー機能
- 独立したWebインターフェース

## サービス一覧

- AIChat (Port 8002)
- CRM MCP (Port 8004) 
- ProductMaster MCP (Port 8003)
- Database Management (Port 8006)

## エンドポイント

- `GET /` - LogAPIメイン画面
- `GET /api/logs/{service}` - 指定サービスのログ取得
- `GET /health` - ヘルスチェック

## 起動方法

```bash
cd LogAPI
python -m pip install -r requirements.txt
python main.py
```

## systemd設定

```ini
[Unit]
Description=LogAPI Service
After=network.target

[Service]
Type=simple
User=ec2-user
WorkingDirectory=/home/ec2-user/LogAPI
ExecStart=/usr/bin/python3 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
