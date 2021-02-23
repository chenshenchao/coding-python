# 附录 A

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
