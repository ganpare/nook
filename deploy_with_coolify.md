# Coolifyを使用したセルフデプロイ手順

この手順書では、Coolifyを使用してGitHubリポジトリからNookプロジェクトをセルフデプロイする方法を説明します。

## 前提条件

- Coolifyがインストールされていること
- GitHubリポジトリへのアクセス権があること
- DockerおよびDocker Composeがインストールされていること

## 手順

### 1. Coolifyで新しいアプリケーションを作成

1. Coolifyのダッシュボードにログインします。
2. 「New Application」をクリックします。
3. 「Git Repository」を選択します。
4. 以下の情報を入力します：
   - **Repository URL**: `https://github.com/<your-username>/nook`
   - **Branch**: `main`（またはデプロイしたいブランチ）
   - **Build Preset**: `Docker Compose`

### 2. 環境変数の設定

1. Coolifyの「Environment Variables」セクションで以下の環境変数を追加します：
   - `OPENWEATHERMAP_API_KEY`: OpenWeatherMapのAPIキー
   - `GROK_API_KEY`: Grok APIのキー
   - `REDDIT_CLIENT_ID`: Reddit APIのクライアントID
   - `REDDIT_CLIENT_SECRET`: Reddit APIのクライアントシークレット
   - `REDDIT_USER_AGENT`: Reddit APIのユーザーエージェント

### 3. Docker Composeファイルの指定

1. 「Docker Compose File」セクションで以下を指定します：
   - **File Path**: `docker-compose.yaml`

### 4. デプロイの実行

1. 「Deploy」ボタンをクリックしてデプロイを開始します。
2. デプロイが完了すると、以下のURLでアプリケーションにアクセスできます：
   - フロントエンド: `http://<your-coolify-domain>:5173`
   - バックエンド: `http://<your-coolify-domain>:8000`

## トラブルシューティング

- デプロイが失敗した場合は、Coolifyのログを確認してください。
- 環境変数が正しく設定されていることを確認してください。
- Dockerイメージのビルドエラーが発生した場合は、`Dockerfile`や`docker-compose.yaml`を再確認してください。

以上で、Coolifyを使用したセルフデプロイの手順は完了です。