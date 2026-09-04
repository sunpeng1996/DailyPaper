---
title: 'CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation'
title_zh: CORE：通过重排器蒸馏提升MLLM嵌入的组合推理能力
authors:
- Tingyu Song
- Mingxin Li
- Yanzhao Zhang
- Dingkun Long
- Chu Liu
- Pengjun Xie
- Yilun Zhao
- Shu Wu
affiliations:
- CASIA
- Alibaba Group
- University of Chinese Academy of Sciences
- Yale University
arxiv_id: '2609.04083'
url: https://arxiv.org/abs/2609.04083
pdf_url: https://arxiv.org/pdf/2609.04083
published: '2026-09-03'
collected: '2026-09-04'
category: Multimodal
direction: 多模态检索 · 重排器蒸馏嵌入优化
tags:
- MLLM
- Multimodal Retrieval
- Reranker Distillation
- Compositional Reasoning
- Embedding
- Rank KL
one_liner: 提出CORE框架，通过重排器蒸馏与五级合成数据提升多模态嵌入的组合推理能力
practical_value: '- 电商多模态检索场景（如用户组合条件搜商品），可复用五级匹配的梯度hard negative合成方法，生成属性错配、对象错配等分层负例，提升细粒度检索精度

  - 现有多模态嵌入模型优化可直接复用Rank-KL蒸馏方法，用已有的重排器软标签做listwise训练，收益优于对比学习和CoSENT，且不损失通用检索性能

  - 重排器微调针对组合推理任务需调大LoRA rank（建议512+），属性-对象绑定类细粒度任务需要更高的参数适配容量

  - 电商图文搜索多条件检索场景，可直接迁移该框架蒸馏逻辑，无需大规模标注就能提升组合查询的召回准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有MLLM-based多模态嵌入模型在组合推理任务上存在明显缺陷，无法区分相同概念不同属性-对象绑定的场景（如“白盘黑椅”和“黑盘白椅”），但同一MLLM作为交叉注意力重排器时却能正确判断这类差异，说明嵌入空间未能保留模型已有的组合推理能力。现有方法要么负例合成质量粗糙，要么对比学习损失将所有负例同等对待，无法传递梯度相似性信号。

### 方法关键点
- 五级匹配数据合成pipeline：定义从全匹配、部分存在、属性错误、对象错误到完全不匹配的5级组合相似度层级，自动生成分层候选集，经过MLLM双校验和人工验证，数据准确率达94%
- Rank-KL蒸馏损失：将重排器对五级候选的排序分数转换为概率分布，训练嵌入模型对齐该分布，替代传统对比学习损失，保留细粒度相似度结构
- 训练策略：嵌入模型用LoRA秩32微调，重排器用LoRA秩512微调，均保留原模型的通用检索能力

### 关键结果
在COLA、SUGARCREPE++、NEGBENCH三个组合推理基准测试：
1. CORE-RERANKER-8B总平均准确率达82.7%，比Jina-Reranker高10.7个百分点
2. CORE-EMBED-8B总平均得分0.666，为所有参评嵌入模型最高，比基线VL-EMB-8B提升5.7个点
3. 多条件检索基准MCMR上R@1从0.375提升到0.412，COCO、Flickr30K通用检索性能无损失

### 最值得记住的一句话
针对细粒度组合检索任务，listwise的重排器蒸馏损失对比对比学习和pairwise损失，能更有效利用梯度负例的监督信号，同时不损失通用检索性能。
