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
