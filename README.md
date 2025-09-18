# LogAPI - System Maintenance Tool

## 概要
WealthAI Enterprise Systems用ログ管理・表示システム

## 主要機能
- **ログ表示**: システムログのWeb表示
- **ログ管理**: ログファイルの管理・検索
- **Portal統合**: 統合ポータルからアクセス可能

## 技術スタック
- **Backend**: Python FastAPI
- **Frontend**: HTML5 + Bootstrap
- **Port**: 8005

## アクセス情報
- **URL**: http://44.217.45.24/logs/
- **直接**: http://44.217.45.24:8005/
- **GitHub**: https://github.com/takehig/System-Maintenance

## 運用管理
```bash
# サービス管理
sudo systemctl start|stop|restart logapi
sudo systemctl status logapi

# ログ確認
sudo journalctl -u logapi -f
```

## 設置場所
- **EC2**: /home/ec2-user/LogAPI/
- **systemd**: /etc/systemd/system/logapi.service
- **Nginx**: /logs/ → http://127.0.0.1:8005/
