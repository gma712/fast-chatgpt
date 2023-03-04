# fast-chatgpt: ChatGPTを叩くFastAPI

## Usage

### `.env`の作成

```txt:.env
OPENAI_ORGANIZATION=org-xxxxxxxxxxx
OPENAI_API_KEY=xxxxxxxxxxxxxxxxx

```

### Poetryセットアップ→FastAPIサーバー立ち上げ

```bash
poetry install
poetry shell
uvicorn main:app --reload
```

### request.httpの内容を書き換えてPOST

```http
POST http://127.0.0.1:8000/chat HTTP/1.1
content-type: application/json

{
    "model": "gpt-3.5-turbo",
    "messages": [{
        "role": "user",
        "content": "これから私は何を糧に生きていけばよいのでしょうか？"
    }]
}
```

VS Codeの拡張機能 REST Client(https://marketplace.visualstudio.com/items?itemName=humao.rest-client)を入れておくと、エディタからSend Requestできる。
