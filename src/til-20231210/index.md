---
title: Discord Botの簡易サンプル
date: 2023-12-10
lastmod: 2023-12-10
---

## 概要

Discord の Bot 作成のための簡易サンプルです。

## 実行方法

## Tips

### Discord Bot の作成

下記の手順で Discord Bot を作成する。

- Discord developer site にアクセスする。
- Applications から"New Application"を選択する。
- Name を設定する。
- "Sections" -> "Bot"から"Authorization Flow"の"Public bot"を OFF にする。
- Server に bot を追加するために、下記の URL の CLIENT_ID を書き換えてアクセスする。
  - <https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=0&scope=bot%20applications.commands>
  - permission は 0 にしているので適切な権限を付与する。
- メッセージにアクセスするため、"Bot"から"Message Content Intents"を有効にする。
