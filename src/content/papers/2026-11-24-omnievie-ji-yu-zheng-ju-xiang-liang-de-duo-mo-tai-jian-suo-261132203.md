---
title: 'OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval'
title_zh: OmniEVIE：基于证据向量的多模态检索嵌入模型
authors:
- Zifei Wang
- Wei Wen
- Qiang Ji
- Qian-Wen Zhang
- Ruizhi Qiao
- He Liu
- Xing Sun
- Qiang Lin
affiliations:
- Tencent IMA Product Center
- Tencent Youtu Lab
arxiv_id: '2611.32203'
url: https://arxiv.org/abs/2611.32203
pdf_url: https://arxiv.org/pdf/2611.32203
published: '2026-11-24'
collected: '2026-11-25'
category: Multimodal
direction: 多模态检索 · 多向量压缩索引
tags:
- MultimodalRetrieval
- MultiVectorEmbedding
- IndexCompression
- LateInteraction
- RetrievalOptimization
one_liner: 4.5B参数多模态多向量检索模型，通过压缩索引和分层检索大幅降低存储延迟并保持高精度
practical_value: '- 电商多模态商品召回可直接复用ST-HAC训练对齐压缩的方案，将商品图、详情页、短视频向量压缩至单条<10KB，百万级商品库存储仅需不到10GiB，同时避免训推偏差

  - 三阶段分层检索架构可直接落地大规模多模态召回场景，在百万级候选池下延迟低至50ms级，比全量多向量检索提速200倍以上，满足线上SLA要求

  - 对比学习训练可复用三级证据校验假阴性过滤、动态采样的技巧，减少错误负样本的梯度干扰，在细粒度商品匹配、Agent工具检索场景下可显著提准

  - 查询侧显著性门控+噪声floor的设计无需改动模型结构，仅用少量参数即可放大关键匹配token的贡献，适合多模态query理解和细粒度匹配场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态检索需覆盖图文、长文档、视频、Agent工具/内存等多场景，单向量表征丢失局部匹配证据，跨编码器重排需在线读取原始介质，全量多向量索引存储成本过高、检索延迟过长，无法落地百万级以上的线上召回池。
### 方法关键点
- 4.5B统一多模态多向量嵌入模型，支持文本、图像、视觉文档、视频、工具检索，输出最多128个维度64的int8压缩向量，单条记录仅9472字节
- 训练阶段前置ST-HAC时空层次聚类压缩逻辑，训推使用完全一致的向量表征，避免训推偏差
- 三阶段分层检索架构：S1用均值向量粗筛，S2用1-bit符号汉明距离中筛，S3用int8多向量+查询侧显著性门控、噪声floor精排，直接返回命中的页面区域/视频时段
- 三级证据校验过滤假阴性，动态采样根据基线与教师模型的差距调整采样权重，分阶段训练加参数分块合并兼顾多模态效果
### 关键结果
- MMEB-V3 190个任务得分60.06，超过9B参数的WeMM-Emb-9B基线0.73，压缩索引精度仅比未压缩全序列低0.62
- 百万级索引单线程查询延迟54.2ms，比4096维单向量精确检索快11.1倍，比全量int8 MaxSim快236倍
- 视频时序定位QVHighlights验证集上返回段与标注段相交率达94.3%
### 核心结论
多向量检索落地的核心是将索引压缩逻辑前置到训练阶段，通过分层检索架构在存储、延迟和精度之间找到最优trade-off
