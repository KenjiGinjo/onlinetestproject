# 关于 MYSQL

我使用的是 macOS，所以我使用的是 brew 来安装 mysql

```shell
brew install mysql
```

安装完成后，可以使用以下命令来启动和停止 mysql

```shell
brew services start mysql
brew services stop mysql
```

使用以下命令来登录 mysql

```shell
mysql -u root -p
CREATE DATABASE mydatabase;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON mydatabase.\* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

这样就可以创建一个数据库和一个用户了，接下来就可以使用这个用户来操作数据库了
在测试之前，请确保已经有了 mysql 的环境

# 关于后端 api

1. **初始化 Flask 应用 (`__init__.py`)**:用于初始化 Flask 应用和其他扩展，如 SQLAlchemy。

2. **配置文件 (`config.py`)**: 配置更加集中和可管理。

3. **模型 (`models/models.py`)**: 将所有 SQLAlchemy 模型移动到这里。

4. **路由 (`routes/user_routes.py`)**: 将所有相关的路由移动到这里。

5. **迁移目录 (`migrations/`)**: 如果使用 Flask-Migrate 管理数据库迁移，该目录将包含迁移脚本。

6. **单元测试 (`tests/`)**: 包含所有单元测试的文件夹。

7. **启动脚本 (`run.py`)**: 项目的入口点，用于运行 Flask 应用。

8. **依赖文件 (`requirements.txt`)**: 列出项目依赖的外部 Python 包。

9. **数据 seed (`seed.py`)**: 用于初始化数据库逻辑是增加 10 个用户，如果需要可以修改这个文件来增加更多的用户
