
# AWS Tools

このリポジトリには、AWS環境の管理を簡素化するための便利なスクリプトが格納されています。各スクリプトは特定のタスクを自動化し、AWSリソースの管理を効率化します。

## 目次

- [スクリプト一覧](#スクリプト一覧)
- [前提条件](#前提条件)
- [セットアップ](#セットアップ)
- [スクリプトの使用方法](#スクリプトの使用方法)
- [ライセンス](#ライセンス)

## スクリプト一覧

- **delete_vpcs.py**: 指定したVPC内のすべてのリソースを削除し、VPC自体を削除します。
- **delete_s3_buckets.py**: バケット一覧を表示し、選択したバケットを削除します。

## 前提条件

- Python 3.6以上
- pip (Pythonパッケージ管理システム)
- AWS CLI (適切に設定された認証情報)

## セットアップ

1. リポジトリをクローンします。

    \`\`\`bash
    git clone https://github.com/yourusername/aws-tools.git
    cd aws-tools
    \`\`\`

2. 必要なPythonパッケージをインストールします。

    \`\`\`bash
    pip install boto3
    \`\`\`

3. AWS CLIを設定します。

    \`\`\`bash
    aws configure
    \`\`\`

## スクリプトの使用方法

### delete_vpcs.py

指定したVPC内のすべてのリソースを削除し、VPC自体を削除します。

\`\`\`bash
python delete_vpcs.py <vpc-id>
\`\`\`

例：

\`\`\`bash
python delete_vpcs.py vpc-0a1b2c3d4e5f6g7h
\`\`\`

### delete_s3_buckets.py

バケット一覧を表示し、選択したバケットを削除します。

\`\`\`bash
python delete_s3_buckets.py
\`\`\`

実行後に表示されるS3バケット一覧から、削除したいバケットの番号をカンマ区切りで入力してください。例えば、`1,3,5` のように入力すると、選択されたバケットとその中のすべてのコンテンツが削除されます。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
