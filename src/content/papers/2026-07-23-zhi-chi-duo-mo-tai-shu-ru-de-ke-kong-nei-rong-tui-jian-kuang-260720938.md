---
title: Controllable and Content-Based Recommendations
title_zh: 支持多模态输入的可控内容推荐框架CCBR
authors:
- Fırat Öncel
- Jihoon Jeong
- Emiliano Penaloza
- Mirco Ravanelli
- Laurent Charlin
- Cem Subakan
affiliations:
- Concordia University
- Université de Montréal
- Laval University
- HEC Montréal
- Mila – Quebec AI Institute
arxiv_id: '2607.20938'
url: https://arxiv.org/abs/2607.20938
pdf_url: https://arxiv.org/pdf/2607.20938
published: '2026-07-23'
collected: '2026-07-24'
category: GenRec
direction: 生成式推荐 · 可控用户文本干预
tags:
- Controllable Recommendation
- Collaborative Filtering
- Multimodal LLM
- Text Bottleneck
- User Profiling
one_liner: 通过文本瓶颈层对接多模态内容与传统CF模型，实现精度可比的可编辑可控推荐
practical_value: '- 可复用文本瓶颈层架构，无需重训现有CF主干，即可快速上线可控推荐功能，支持电商场景用户通过文本指令（如“要棉质通勤外套”）直接干预推荐结果，降低功能迭代成本

  - 多模态item的离线摘要缓存方案可直接落地，针对电商商品图、短视频提前用MLLM生成标准化内容描述，屏蔽ID信息避免预训练知识泄漏，同时大幅降低在线推理耗时

  - 文本表征与CF隐向量的两步对齐方法可迁移，先用类目标签监督文本编码器，再用InfoNCE损失对齐CF表征，在可控性提升的同时保证推荐精度损失控制在5%以内，平衡用户体验与业务指标

  - 冷启动场景适配方案可复用，新用户无交互历史时，直接基于用户上传的多模态内容（如参考款商品图、喜欢的音乐片段）生成用户画像完成推荐，缓解冷启动推荐效果差的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统协同过滤（CF）推荐依赖黑盒隐向量表征，用户无法针对临时偏好干预推荐结果，尤其电商、内容场景下用户的即时需求（如临时想买红色连衣裙、排除恐怖类电影）难以被满足；现有可控推荐方法仅支持文本元数据输入，无法利用商品图、音视频等多模态内容信号，且难以在可控性提升的同时保持推荐精度。
### 方法关键点
- 离线预处理：用多模态LLM将每个item的多模态内容（图片、音频、视频）转换为文本描述，屏蔽item ID、名称等先验信息，仅保留纯内容语义，结果全局缓存复用
- 用户画像生成：将用户历史交互item的文本描述输入指令微调LLM，聚合生成自然语言用户偏好画像，支持用户直接编辑文本、或上传新的多模态内容更新画像
- 表征对齐与推荐：用带类目标签监督的BGE-M3编码用户文本画像，通过InfoNCE损失对齐文本表征与CF模型的用户隐向量，复用CF解码器完成推荐，支持对接EASE、Multi-VAE等7种主流CF backbone
### 关键实验
在H&M（服饰图片）、MovieLens-20M（电影预告片）、Million Song Dataset（音乐音频）三个跨模态数据集测试：相比基线TEARS，VAE backbone下NDCG@100最高提升2.5个百分点；可控干预效果上，移除目标属性后对应类目召回率最高下降4pct，添加目标属性后对应类目召回率最高上升5.2pct，整体推荐精度仅比原生CF模型低5%以内。
### 核心结论
通过文本瓶颈层实现语义可解释性与传统CF模型性能的平衡，是现阶段落地可控推荐性价比最高的路径
