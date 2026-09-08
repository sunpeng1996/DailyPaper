---
title: Multi-scale Image Representation Compression
title_zh: 多尺度图像表示压缩（MIRC）
authors:
- Tianhao Peng
- Ho Man Kwan
- Fan Zhang
- Shan Liu
- David Bull
affiliations:
- Visual Information Lab, University of Bristol, UK
- Tencent Media Lab, Palo Alto, USA
arxiv_id: '2609.04274'
url: https://arxiv.org/abs/2609.04274
pdf_url: https://arxiv.org/pdf/2609.04274
published: '2026-09-02'
collected: '2026-09-08'
category: Other
direction: 图像编码 · 神经网络过拟合压缩
tags:
- Learned Image Compression
- Implicit Neural Representation
- Neural Codec
- Multi-scale Representation
- Overfitted Compression
one_liner: 提出端到端优化的多尺度过拟合图像编码MIRC，较VVC降10.5%BD-rate且解码复杂度可灵活配置
practical_value: '- 电商商品图/广告素材压缩场景可复用多尺度参数共享+端到端率失真优化框架，在画质无损前提下降低存储与CDN带宽成本

  - 客户端图片加载场景可根据设备性能选择1.2~2.9kMAC/像素的配置档位，平衡解码速度与显示画质

  - 商家私域固定静态素材批量压缩场景可参考过拟合压缩思路，针对特定素材训练获得更高压缩率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有过拟合图像编码（如Cool-chic）存在两大短板：未实现端到端率失真优化，训练时权重保持全精度，量化参数需在训练后单独选择；单尺度生成逻辑忽略跨尺度冗余，压缩效率天花板较低。

### 方法关键点
MIRC过拟合图像编码复用NVRC神经视频编码的端到端流水线，对隐变量、生成网络、熵模型所有编码组件在统一率失真目标下同步量化和熵编码；新增多尺度表示+跨阶段参数共享机制，仅增加极小幅传输开销即可提升编码效率。

### 关键结果
在CLIC2020专业验证集上，相比VVC（VTM22.0）实现10.5% BD-rate降低；提供1.2~2.9kMAC/像素的多档配置，可根据部署目标灵活选择解码算力预算。
