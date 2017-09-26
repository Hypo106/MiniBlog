第一次使用：
    初始化：(venv)  python manage.py db init
                   这个命令会在项目下创建 migrations 文件夹，所有迁移脚本都存放其中。

    创建第一个版本：(venv) $ python manage.py db migrate -m "initial migration"
                      检查migrations\versions，会新建一个版本.py，检查里面表格及字段

    运行升级 (venv) $ python manage.py db upgrade，
                     会把项目使用的数据库文件，更新为新的表格、字段，同时保留数据