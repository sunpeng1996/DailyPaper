---
title: 'SPAR: Enhancing Industrial-Scale Generative POI Recommendation via Real-World
  Spatial Perception'
title_zh: SPAR：基于真实空间感知增强工业级生成式POI推荐
authors:
- Fangye Wang
- Yunjin Gu
- Haowen Lin
- Yifang Yuan
- Song Yang
- Xiaojiang Zhou
- Pengjie Wang
affiliations:
- Alibaba Group AMAP
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2609.02062'
url: https://arxiv.org/abs/2609.02062
pdf_url: https://arxiv.org/pdf/2609.02062
published: '2026-09-02'
collected: '2026-09-03'
category: GenRec
direction: 生成式推荐 · 空间感知POI推荐
tags:
- Generative Recommendation
- POI Recommendation
- Semantic ID
- Spatial Perception
- LLM Fine-tuning
one_liner: 提出三阶段融合城市空间知识的生成式POI推荐框架，工业场景较SOTA平均提升38%
practical_value: '- 做本地生活/POI类生成式推荐时，可复用SI-SID设计：经纬度经正弦编码生成地理嵌入，与语义特征融合后做RQ-Kmeans，让Semantic
  ID自带空间拓扑属性，降低推荐POI与用户的距离偏差

  - 给LLM注入垂直领域结构化知识时，可参考MG-CPT三级语料构造思路：从实体属性、实体间关系、系统级交互三层构造预训练语料，小模型加领域CPT性能可超过大8倍的通用LLM

  - 行为SFT时怕领域预训练知识被冲刷，可复用TV-SFT任务向量锚定方案：将CPT知识提取为冻结任务向量，仅在空间向量上加LoRA微调适配，避免灾难性遗忘，该模块最高带来17%相对提升

  - 用户行为稀疏的冷启动场景下，可将场景原生结构化特征（如空间、时间）嵌入生成式推荐全链路，本实验冷启动下Recall@5相对提升近48%，大幅缩小冷启动性能gap'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式POI推荐仅将地理信息作为文本属性处理，缺乏显式的空间拓扑、可达性建模，推荐结果语义合理但往往距离用户实时位置过远、实际可达性差；且后续基于行为数据的SFT过程易导致预训练注入的空间知识发生灾难性遗忘，无法满足LBS场景的真实需求。

### 方法关键点
- **标识层SI-SID**：将POI经纬度做归一化后通过正弦编码器生成地理嵌入，与POI文本语义嵌入拼接、L2归一化后做RQ-Kmeans量化，生成同时具备语义与空间一致性的Semantic ID，空间邻近POI的ID前缀天然接近。
- **认知层MG-CPT**：构造三级共25个城市空间数据集（POI/路网基础属性、POI-POI/POI-路网关系、导航可达性），对基座LLM做持续预训练，让模型内化城市空间距离、方向、可达性等知识。
- **适配层TV-SFT**：将MG-CPT学到的空间知识提取为冻结的参数空间任务向量，行为SFT时仅微调基础模型全参数和空间向量上的LoRA，既避免空间知识被海量行为数据覆盖，又能适配推荐任务需求。

### 关键结果
在2个公开POI数据集+4个高德工业级城市数据集上测试，SPAR-8B较SOTA基线PLUM平均提升38.32%，0.6B小版本性能就超过所有8B基线；冷启动场景下Recall@5相对提升47%以上；推荐POI与用户的平均距离较基线降低27%以上。

### 核心结论
生成式POI推荐的核心是将用户行为兴趣空间锚定到真实城市物理空间，而非仅从行为数据反推地理属性。
