
# AWS Tools

このリポジトリには、AWS環境の管理を簡素化するための便利なスクリプトが格納されています。各スクリプトは特定のタスクを自動化し、AWSリソースの管理を効率化します。

## 目次

- [スクリプト一覧](#スクリプト一覧)
- [前提条件](#前提条件)
- [セットアップ](#セットアップ)
- [スクリプトの使用方法](#スクリプトの使用方法)
- [ライセンス](#ライセンス)

## スクリプト一覧

- **attach_tag_to_ebs.sh**: EBSボリュームにタグを付与します。
- **delete-s3-bucket.py**: バケット一覧を表示し、選択したバケットを削除します。
- **delete-vpcs.py**: 指定したVPC内のすべてのリソースを削除し、VPC自体を削除します。
- **install-and-update-cli-v2.sh**: AWS CLI v2のインストールと更新を行います。

## 前提条件

- Python 3.6以上
- pip (Pythonパッケージ管理システム)
- AWS CLI (適切に設定された認証情報)

## セットアップ

1. リポジトリをクローンします。

    \`\`\`bash
    git clone https://github.com/ryoupr/aws-tools.git
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

### attach_tag_to_ebs.sh

EBSボリュームにタグを付与します。

\`\`\`bash
sh attach_tag_to_ebs.sh <volume-id> <tag-key> <tag-value>
\`\`\`

例：

\`\`\`bash
sh attach_tag_to_ebs.sh vol-0a1b2c3d4e5f6g7h Environment Production
\`\`\`

### delete-s3-bucket.py

バケット一覧を表示し、選択したバケットを削除します。

\`\`\`bash
python delete-s3-bucket.py
\`\`\`

実行後に表示されるS3バケット一覧から、削除したいバケットの番号をカンマ区切りで入力してください。例えば、`1,3,5` のように入力すると、選択されたバケットとその中のすべてのコンテンツが削除されます。

### delete-vpcs.py

指定したVPC内のすべてのリソースを削除し、VPC自体を削除します。

\`\`\`bash
python delete-vpcs.py <vpc-id>
\`\`\`

例：

\`\`\`bash
python delete-vpcs.py vpc-0a1b2c3d4e5f6g7h
\`\`\`

### install-and-update-cli-v2.sh

AWS CLI v2をインストールまたは更新します。

\`\`\`bash
sh install-and-update-cli-v2.sh
\`\`\`

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
