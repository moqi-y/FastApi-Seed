
```
app/：包含主应用程序文件。
main.py：初始化 FastAPI 应用程序。
dependencies.py：定义路由器使用的依赖项。
routers/：包含路由模块。crud/：包含 CRUD（创建、读取、更新、删除）操作模块。
schemas/：包含 Pydantic 模式模块。
models/：包含数据库模型模块。
external_services/：包含与外部服务交互的模块。
utils/：包含实用工具模块。tests/：包含测试模块。
```
### FastApi-Seed 项目目录结构说明
> - **app** - 应用的主目录，包含应用的核心代码和逻辑。
>  - **app/core** - 核心功能模块，可能包含应用的基础配置和核心逻辑。
>  - **app/crud** - CRUD（创建、读取、更新、删除）操作模块，包含与数据库交互的基本操作。
>  - **app/middleware** - 中间件目录，包含处理请求和响应的中间件逻辑。
>  - **app/models** - 数据模型目录，包含定义数据库模型的 Python 类。
>  - **app/routers** - 路由目录，包含定义应用的 API 路由和对应的处理函数。
>  - **app/schemas** - 模式目录，包含 Pydantic 模型，用于数据验证和序列化。
>  - **app/utils** - 工具函数目录，包含一些辅助函数和实用工具。
>  - **app/external_services** - 外部服务目录，包含与外部服务交互的代码。
>  - **static** - 静态文件目录，用于存放静态资源如 CSS、JavaScript 文件、图片等。
>- **.venv** - 虚拟环境目录，包含项目的依赖包。
>- **.env** - 环境变量文件，包含配置环境变量如数据库连接字符串等。
>- **FastApi-Seed.db** - 数据库文件，存储应用的数据。
>- **README.md** - 项目的自述文件，包含项目的基本信息和使用说明。
>- **requirements.txt** - 依赖文件，列出项目依赖的 Python 包及其版本。
>- **test_main.http** - HTTP 请求测试文件，包含用于测试 API 的 HTTP 请求样本。

## 安装依赖
**python版本：** 3.10.11
```bash
pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt
```
### 安装单个依赖包
```bash
pip install fastapi -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

其他国内源：
```
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

```
### JWT
使用以下命令，生成安全的随机密钥,然后，把生成的密钥复制到变量`JWT_SECRET_KEY`。
```bash
openssl rand -hex 32
```
