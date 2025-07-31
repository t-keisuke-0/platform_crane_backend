## ER 図

```mermaid
erDiagram
    users {
        int id PK "ユーザーID"
        string username UK "ユーザー名"
        string encrypted_password UK "暗号化済みパスワード SNS認証の場合はNULL想定"
        string email UK "メールアドレス SNS認証の場合はNULL想定"
        string icon_url "アイコン画像 URL"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    social_accounts {
        int id PK "ソーシャル認証アカウントID"
        int user_id FK,UK "users.id"
        enum provider_name UK "認証プロバイダー名"
        string provider_user_id "プロバイダー側のユーザー ID"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    prizes {
        int id PK "プライズ ID"
        string name UK "プライズ名"
        enum kinds UK "プライズ種類"
        string image_url "画像 URL"
        int manufacturer_id FK,UK "manufacturers.id"
        date release_date "発売日"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    manufacturers {
        int id PK "メーカー ID"
        string name UK "メーカー名"
        string website "公式サイトURL"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    stores {
        int id PK "店舗 ID"
        string name UK "店舗名"
        string location "住所, 設置場所"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    prize_arrivals {
        int id PK "入荷 ID"
        int prize_id FK,UK "prizes.id"
        int store_id FK,UK "stores.id"
        date arrival_date UK "入荷日"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    play_records {
        int id PK "プレイ記録 ID"
        int user_id FK "users テーブルの ID"
        int prize_id FK "prizes テーブルの ID"
        int store_id FK "stores テーブルの ID"
        int play_count "プレイ回数"
        int spent_amount "消費金額"
        bool is_got "獲得したかどうか"
        date play_date "プレイ日"
        text description "説明文"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    play_record_likes {
        int id PK "いいね ID"
        int play_record_id FK,UK "play_records.id"
        int user_id FK,UK "users.id"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }
    play_record_views {
        int id PK "既読 ID"
        int play_record_id FK,UK "play_records.id "
        int user_id FK,UK "users.id"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
    }

    users ||--o{ social_accounts : has
    users ||--o{ play_records : plays
    users ||--o{ play_record_likes : likes
    users ||--o{ play_record_views : views
    prizes ||--o{ prize_arrivals : arrives
    prizes ||--o{ play_records : played
    prizes ||--o{ manufacturers : made_by
    stores ||--o{ prize_arrivals : receives
    stores ||--o{ play_records : played_at
    play_records ||--o{ play_record_likes : has_likes
    play_records ||--o{ play_record_views : has_views

```

---

## テーブル定義詳細

### users（ユーザー情報）

| カラム名           | 意味                 | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ------------------ | -------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id                 | ユーザー ID          | 〇  |     | int      | 〇       | auto_increment    |        |
| username           | ユーザー名           |     |     | string   | 〇       |                   | 〇     |
| encrypted_password | 暗号化済みパスワード |     |     | string   |          |                   | 〇     |
| email              | メールアドレス       |     |     | string   |          |                   | 〇     |
| icon_url           | アイコン画像 URL     |     |     | string   |          |                   |        |
| created_at         | 作成日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at         | 更新日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### social_accounts（ソーシャル認証アカウント情報）

| カラム名         | 意味                            | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ---------------- | ------------------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id               | ソーシャル認証アカウント情報 ID | 〇  |     | int      | 〇       |                   |        |
| user_id          | users テーブルの ID             |     | 〇  | int      | 〇       |                   | 〇     |
| provider_name    | 認証プロバイダー名（enum 管理） |     |     | enum     | 〇       |                   | 〇     |
| provider_user_id | プロバイダー側のユーザー ID     |     |     | string   | 〇       |                   |        |
| created_at       | 作成日時                        |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at       | 更新日時                        |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### prizes（プライズ情報）

| カラム名        | 意味                        | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| --------------- | --------------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id              | プライズ ID                 | 〇  |     | int      | 〇       | auto_increment    |        |
| name            | プライズ名                  |     |     | string   | 〇       |                   | 〇     |
| kinds           | プライズ種類（enum 管理）   |     |     | enum     | 〇       |                   | 〇     |
| image_url       | 画像 URL                    |     |     | string   |          |                   |        |
| manufacturer_id | manufacturers テーブルの ID |     | 〇  | int      | 〇       |                   | 〇     |
| release_date    | 発売日                      |     |     | date     |          |                   |        |
| created_at      | 作成日時                    |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at      | 更新日時                    |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### manufacturers（メーカー情報）

| カラム名   | 意味           | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ---------- | -------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id         | メーカー ID    | 〇  |     | int      | 〇       | auto_increment    |        |
| name       | メーカー名     |     |     | string   | 〇       |                   | 〇     |
| website    | 公式サイト URL |     |     | string   |          |                   |        |
| created_at | 作成日時       |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at | 更新日時       |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### stores（店舗情報）

| カラム名   | 意味           | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ---------- | -------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id         | 店舗 ID        | 〇  |     | int      | 〇       | auto_increment    |        |
| name       | 店舗名         |     |     | string   | 〇       |                   | 〇     |
| location   | 住所・設置場所 |     |     | string   |          |                   |        |
| created_at | 作成日時       |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at | 更新日時       |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### prize_arrivals（プライズ入荷情報）

| カラム名     | 意味                 | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ------------ | -------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id           | 入荷 ID              | 〇  |     | int      | 〇       |                   |        |
| prize_id     | prizes テーブルの ID |     | 〇  | int      | 〇       |                   | 〇     |
| store_id     | stores テーブルの ID |     | 〇  | int      | 〇       |                   | 〇     |
| arrival_date | 入荷日               |     |     | date     |          |                   | 〇     |
| created_at   | 作成日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at   | 更新日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### play_records（プレイ記録）

| カラム名     | 意味                 | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| ------------ | -------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id           | プレイ記録 ID        | 〇  |     | int      | 〇       | auto_increment    |        |
| user_id      | users テーブルの ID  |     | 〇  | int      | 〇       |                   |        |
| prize_id     | prizes テーブルの ID |     | 〇  | int      | 〇       |                   |        |
| store_id     | stores テーブルの ID |     | 〇  | int      | 〇       |                   |        |
| play_count   | プレイ回数           |     |     | int      | 〇       | 1                 |        |
| spent_amount | 消費金額（円）       |     |     | int      | 〇       | 0                 |        |
| is_got       | 獲得したかどうか     |     |     | bool     | 〇       | false             |        |
| play_date    | プレイ日             |     |     | date     | 〇       |                   |        |
| description  | 説明文               |     |     | text     |          |                   |        |
| created_at   | 作成日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at   | 更新日時             |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### play_record_likes（プレイ記録いいね）

| カラム名       | 意味                | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| -------------- | ------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id             | いいね ID           | 〇  |     | int      | 〇       | auto_increment    |        |
| play_record_id | プレイ記録 ID       |     | 〇  | int      | 〇       |                   | 〇     |
| user_id        | users テーブルの ID |     | 〇  | int      | 〇       |                   | 〇     |
| created_at     | 作成日時            |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at     | 更新日時            |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |

### play_record_views（プレイ記録既読）

| カラム名       | 意味                | PK  | FK  | データ型 | NOT NULL | DEFAULT           | UNIQUE |
| -------------- | ------------------- | --- | --- | -------- | -------- | ----------------- | ------ |
| id             | 既読 ID             | 〇  |     | int      | 〇       | auto_increment    |        |
| play_record_id | プレイ記録 ID       |     | 〇  | int      | 〇       |                   | 〇     |
| user_id        | users テーブルの ID |     | 〇  | int      | 〇       |                   | 〇     |
| created_at     | 作成日時            |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
| updated_at     | 更新日時            |     |     | datetime | 〇       | CURRENT_TIMESTAMP |        |
