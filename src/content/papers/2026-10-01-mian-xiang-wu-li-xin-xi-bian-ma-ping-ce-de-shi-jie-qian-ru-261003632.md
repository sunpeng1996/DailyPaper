---
title: World Embedding Benchmark
title_zh: 面向物理信息编码评测的世界嵌入基准数据集
authors:
- Yiqi Liu
- Ruifeng Yuan
- Yang Wang
- Long Li
- Fengyu Cai
- Hou Pong Chan
- Jialin Yu
- Hao Zhang
- Chenghua Lin
- Chenghao Xiao
affiliations:
- World-Embedding Team
- World-Representation-Lab
arxiv_id: '2610.03632'
url: https://arxiv.org/abs/2610.03632
pdf_url: https://arxiv.org/pdf/2610.03632
published: '2026-10-01'
collected: '2026-10-05'
category: Eval
direction: 多模态嵌入评测 · 物理表示编码
tags:
- Benchmark
- Video Embedding
- Physical Representation
- Multimodal Retrieval
- RAG
one_liner: 构建含80类共8000个物理仿真案例的评测基准，验证物理嵌入可提升生成视频保真度
practical_value: '- 垂域多模态Embedding评测可参考「跨模态对齐+定量属性可恢复性」双维度设计任务，避免仅看检索精度忽略属性准确性

  - 垂域RAG场景可加入领域特定对比训练提升跨模态检索效果，需注意平衡对齐收益与定量属性预测的精度损失

  - 电商商品短视频/3D展示等生成类业务可引入物理表示作为RAG参考，提升生成内容的物理合理性与真实感'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
世界模型、视频生成领域物理保真度关注度持续提升，但视频表示对物理信息的编码逻辑缺乏统一评测标准，现有评估多侧重视觉真实性，忽略物理规律符合性。
### 方法关键点
构建覆盖流体力学、固体力学、动力学、光学电磁学4大领域、80类共8000个可控仿真案例的基准，每个案例配对渲染视频与仿真物理标注，支持文本-视频检索、物理属性回归、视频-描述配对分类三类任务，明确区分跨模态物理对齐能力与定量物理信息可恢复性两个评测维度。
### 关键结果数字
预训练多模态嵌入模型检索表现较差，类内配对分类准确率接近随机水平；仅用轻量探针即可从冻结视频嵌入中恢复有效物理信息；加入物理领域视频-文本对做持续对比训练后，检索与配对分类效果提升，但物理属性回归表现下降，存在明确trade-off；将物理嵌入检索的参考视频用于MiniMax-H3的RAG生成，可显著提升生成视频物理保真度，检索性能越强增益越大
