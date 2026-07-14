---
title: Stream-aware Side Adaptation for Large Pre-trained Multimodal Embedding Models
  in Sequential Recommendation
title_zh: 面向序列推荐的预训练多模态嵌入模型流感知侧适配方法
authors:
- Junchen Fu
- Kaiwen Zheng
- Ioannis Arapakis
- Wenhao Deng
- Xin Xin
- Joemon M. Jose
- Xuri Ge
affiliations:
- University of Glasgow
- Telefónica Scientific Research
- Shandong University
arxiv_id: '2607.10909'
url: https://arxiv.org/abs/2607.10909
pdf_url: https://arxiv.org/pdf/2607.10909
published: '2026-07-12'
collected: '2026-07-14'
category: RecSys
direction: 序列推荐 · 预训练多模态模型侧适配
tags:
- Sequential Recommendation
- Multimodal Embedding
- Side Adapter
- Parameter Efficient Tuning
- Frozen Backbone
one_liner: 提出流感知侧适配框架Stresa，解决深层侧适配性能退化问题，释放预训练多模态嵌入模型在序列推荐的潜力
practical_value: '- 现有使用预训练多模态嵌入（如CLIP、Qwen3-VL）做物品表征的推荐业务，可直接替换原有侧适配模块为Stresa，无需改动下游序列模型和冻结主干的部署范式，适配所有层隐状态的同时避免性能下降

  - 两个核心trick可拆分复用：SHAF的身份保留路由设计解决深层特征遗忘问题，ReSA的流感知残差更新适配层间特征选择需求，可迁移到其他冻结大模型的参数高效微调场景

  - 保留冻结主干+离线缓存隐状态的工程范式，训练仅更新轻量侧分支，适配后物品embedding可离线批量刷新，完全兼容现有推荐系统的向量检索、召回链路，无额外在线推理开销'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大参数量预训练多模态嵌入模型（如Qwen3-VL Embedding）能生成跨模态统一语义表征，是多模态序列推荐的优质底座，但直接应用存在通用语义与推荐场景的领域偏移问题；端到端微调计算/存储成本过高，侧适配（冻结主干仅训练轻量侧分支）是工业友好的方案，但传统侧适配随适配层数加深性能显著退化，需通过层丢弃规避，浪费了深层隐状态的有效信息，核心源于残差加和无选择机制、渐进融合无法保留早期层表征两大问题。
### 方法关键点
- 提出Stresa流感知侧适配框架，完全兼容冻结主干+离线缓存隐状态的工业部署范式，无需改动下游序列推荐模型架构
- **SHAF流感知隐-适配器融合**：将特征拆分为多个子流，通过Sinkhorn归一化生成流路由矩阵，加入身份保留门控控制历史适配信息的跨流重组，既实现与当前层主干隐状态的精细融合，又避免早期层信息被深层特征覆盖
- **ReSA残差流适配器**：在瓶颈MLP前后及残差分支加入流感知混合操作，替换传统固定身份残差为可学习的流级残差映射，实现选择性残差更新，适配不同层的特征变换需求
### 关键实验
在MicroLens-50K、MicroLens-100K、Amazon Scientific三个公开数据集测试，以Qwen3-VL-2B/8B为冻结主干，对比Two-Stage、传统Side Adapter、IISAN、CROSSAN等SOTA基线：
- 相比传统Side Adapter，全层适配下HR@10最高提升4.3%，NDCG@10最高提升5.3%，且随适配层数增加性能稳定上升，无退化问题
- 相比最强基线CROSSAN，HR@10最高提升2%，NDCG@20最高提升3.7%，跨数据集、跨主干规模均稳定领先
- 仅增加15%左右训练计算开销，可训练参数比传统Side Adapter低50%
> 值得记住的一句话：冻结大模型侧适配的性能瓶颈不是深层隐状态无用，而是传统融合与残差设计无法稳定传递早期适配信息，流感知的身份保留设计可低成本解决这一问题
