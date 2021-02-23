# 附录 A

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
