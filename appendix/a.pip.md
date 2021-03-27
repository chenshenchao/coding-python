# 附录A 自定义包开发与发布

当我们使用 Python 一段时间后，就会有一些常用的代码，便可以打包成一个包方便以后直接使用。如果是可以开源的代码，就把它发布到 pypi.org 上为 Python 付出一点力量吧。

## 开发

```bash
# 安装到本地环境
pip install -e . -i https://pypi.python.org/pypi

# 指定源更新
pip install --upgrade <packagename> -i https://pypi.python.org/pypi
```

## 发布

```bash
# 安装发布工具
pip install twine wheel
```

```bash
# 打包
python setup.py sdist bdist_wheel

# 上传
twine upload dist/*
```
