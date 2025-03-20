# Docker環境設定の違いと注意点

## 開発環境（dev）と本番環境（prod）の主な違い

### 開発環境 (docker-compose.dev.yaml)

1. **フロントエンド**
   - ホットリロードが有効
   - ソースコードをボリュームマウント
   - node_modulesは開発マシンのものを使用
   - Viteの開発サーバーを使用

2. **バックエンド**
   - デバッグモードが有効
   - ソースコードをボリュームマウント
   - Uvicornのリロードオプションが有効

### 本番環境 (docker-compose.yaml)

1. **フロントエンド**
   - ビルド済みの静的ファイルを使用
   - 本番用のNginxサーバーで配信
   - 最適化されたビルドを使用

2. **バックエンド**
   - 最適化モードで実行
   - ソースコードをコンテナにコピー
   - 本番用のUvicorn設定

## 注意点と既知の問題

### node_modulesの扱いに関する問題

**問題の現象**:
本番環境のビルド時に以下のようなエラーが発生する場合があります：
```
ERROR [frontend 5/6] COPY nook/frontend .                      2.1s
failed to solve: cannot replace to directory /var/lib/docker/overlay2/.../merged/app/node_modules/@eslint/js with file
```

**原因**:
- フロントエンドのビルド時に`node_modules`ディレクトリがコピーされようとする
- ホストマシンの`node_modules`とコンテナ内の`node_modules`で競合が発生

**解決策**:
1. `.dockerignore`に以下を追加して、`node_modules`をビルドコンテキストから除外
   ```
   **/node_modules
   ```

2. Dockerfileで適切な順序でインストールとコピーを行う
   ```dockerfile
   COPY package*.json ./
   RUN npm install
   COPY . .
   ```

### 開発環境での推奨される起動方法

1. 開発環境用のコマンド:
   ```bash
   docker-compose -f docker-compose.dev.yaml up --build
   ```

2. フロントエンド開発時の注意点:
   - ソースコードの変更は即時反映される
   - node_modulesの更新時は再ビルドが必要

### 本番環境での推奨される起動方法

1. 本番環境用のコマンド:
   ```bash
   docker-compose up --build
   ```

2. デプロイ時の注意点:
   - フロントエンドのビルドが必要
   - 環境変数の設定確認
   - ボリュームマウントの確認

## トラブルシューティング

1. **node_modulesの問題が発生した場合**:
   - コンテナとボリュームを完全に削除して再ビルド
   - .dockerignoreの設定を確認

2. **ホットリロードが機能しない場合**:
   - ボリュームマウントの設定を確認
   - 開発環境用のdocker-compose.dev.yamlを使用しているか確認

3. **環境変数の問題**:
   - .envファイルが正しい場所にあるか確認
   - 必要な環境変数がすべて設定されているか確認