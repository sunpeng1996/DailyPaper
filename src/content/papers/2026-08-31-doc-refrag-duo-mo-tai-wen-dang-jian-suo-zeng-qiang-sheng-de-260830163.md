---
title: 'Doc-REFRAG: Rethinking Multimodal Document Retrieval-Augmented Generation'
title_zh: Doc-REFRAG：多模态文档检索增强生成的优化框架
authors:
- Ruofan Hu
- Shengyang Xu
- Minjie Hong
- Xiaoda Yang
- Sashuai Zhou
- Ke Lei
- Tao Jin
- Zhou Zhao
affiliations:
- Zhejiang University
arxiv_id: '2608.30163'
url: https://arxiv.org/abs/2608.30163
pdf_url: https://arxiv.org/pdf/2608.30163
published: '2026-08-31'
collected: '2026-09-01'
category: RAG
direction: 多模态文档RAG · 视觉Token优化
tags:
- Multimodal-RAG
- Visual-Token-Compression
- Reinforcement-Learning
- Dataset
- Efficiency
- Document-VQA
one_liner: 提出带RL选择器的压缩-扩展多模态RAG框架与配套数据集，实现精度效率双优
practical_value: '- 多模态RAG落地时可复用「全局粗压缩+Query引导RL选择器动态扩关键块」架构，替代全量输入或静态剪枝，降低视觉Token开销30%+，适配电商商品图、营销素材的检索问答场景

  - 构建RAG训练集可借鉴「正例+硬负例交错构造」方法，模拟真实检索噪声，可提升模型在召回结果混杂的生产环境鲁棒性3-4个百分点

  - 多模态重排场景可复用其轻量选择器逻辑，无需单独部署重排模型，端到端延迟比传统检索-重排Pipeline降低60%，适合电商导购Agent的多模态Query响应'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态RAG大多适配单图/闭域文档，在真实多图、跨文档、混杂冗余/负例的开放RAG场景下精度下降明显；同时全量处理所有检索到的视觉Token会产生大量冗余计算，推理延迟过高，无法支撑交互式场景落地。
### 方法关键点
- 发布343K规模的DocLongRAG数据集，单问题平均关联37.4张图，混入大量硬负例模拟真实检索噪声，覆盖PDF/幻灯片/海报等多格式文档
- 采用「压缩-扩展」核心策略：先将单图视觉Token切分为不重叠块，通过2层MLP投影为粗粒度embedding，大幅降低初始输入序列长度
- 轻量RL选择器以问答准确率为奖励信号，仅动态扩展与Query语义相关的块为高分辨率Token，兼顾推理效率与语义完整性
- 三阶段训练范式：单图重建保证块语义保真→多图持续预训练适配混合Token序列→RL微调选择器
### 关键结果
在6个文档VQA基准上对比11个SOTA基线，平均准确率达57.5%，较最优基线提升6.6个百分点；处理20张检索图的端到端延迟仅6.1s，比传统检索-重排Pipeline降低60%；多模态重排场景下Recall@10超现有专用重排器，延迟降低47%以上。
### 核心洞察
多模态RAG的视觉Token优化不能仅依赖视觉显著性，必须与Query语义绑定，动态选择的精度效率收益远高于静态剪枝/压缩
