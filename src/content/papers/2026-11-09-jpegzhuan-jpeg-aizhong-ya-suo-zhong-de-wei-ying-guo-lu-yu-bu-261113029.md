---
title: Artifact Filtering versus Artifact-Compensated Training in JPEG to JPEG AI
  Recompression
title_zh: JPEG转JPEG AI重压缩中的伪影过滤与伪影补偿训练对比
authors:
- Igor Podtsepko
- Yuriy Kim
- Karam Mahfod
- Evgeny Belyaev
- Kristian Kirs
- Jianping Lin
- Ilya Papiev
affiliations:
- ITMO University, Russia
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.13029'
url: https://arxiv.org/abs/2611.13029
pdf_url: https://arxiv.org/pdf/2611.13029
published: '2026-11-09'
collected: '2026-11-12'
category: Other
direction: 图像压缩 · JPEG AI重压缩优化
tags:
- Image Compression
- JPEG AI
- Artifact Removal
- Training Optimization
- Preprocessing
one_liner: 提出伪影补偿训练方案，在不增加推理耗时的前提下解决JPEG转JPEG AI的伪影残留问题
practical_value: '- 电商/内容平台存量JPEG商品图转JPEG AI格式降存储成本时，可复用伪影补偿训练思路，替代前置去伪影预过滤方案，避免推理耗时飙升

  - 针对带噪声/伪影的输入数据做模型训练时，可借鉴「补偿式训练」思路，无需额外前置处理模块即可兼顾效果与效率

  - 存量数据格式升级场景下，优先做训练侧优化而非推理侧加模块，可大幅降低工程落地的算力成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
海量存量JPEG图像转新一代JPEG AI格式存储时，直接用无压缩图像训练的JPEG AI模型会将JPEG压缩伪影识别为图像有效内容保留，严重降低输出画质；若在重压缩前新增神经网络去伪影预过滤模块，推理耗时会暴涨29倍，工程落地的算力成本不可接受。
### 方法关键点
提出伪影补偿训练范式，在JPEG AI模型训练阶段就引入带JPEG伪影的输入数据，将去伪影能力内置到压缩模型的权重中，无需在推理侧额外新增处理模块。
### 关键结果
实现去伪影+高效压缩能力融合，推理耗时无增加，压缩效果与「预过滤+重压缩」两阶段方案完全对齐。
