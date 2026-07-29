---
title: 'The Case Against Generation for Retrieval: Discriminative Language Models
  as Effective Retrievers'
title_zh: 放弃生成式检索：基于判别式大语言模型的高效检索器
authors:
- Zhe Xu
- Prachi Agrawal
- Kavosh Asadi
- Tianyi Chen
- Carl Hu
- Justin Johnson
- Wuwei Lan
- Mingfu Liang
- Xi Liu
- Tik On Lui
affiliations:
- Meta
arxiv_id: '2607.25346'
url: https://arxiv.org/abs/2607.25346
pdf_url: https://arxiv.org/pdf/2607.25346
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 推荐系统 · LLM原生双塔检索
tags:
- Two-Tower
- LLM4Rec
- Knowledge Distillation
- Cross-Encoder
- Retrieval
one_liner: 将LLM作为语义编码骨干优化双塔检索，性能追平SOTA生成式推荐且具备工业级落地效率
practical_value: '- 双塔架构优化可直接复用共享LLM编码器+EOS pooling设计，相比独立双塔参数量减半，且能保证用户/Item语义空间天然对齐，效果优于常规均值
  pooling

  - 蒸馏流程可照搬：用yes/no输出头+用户条件NTP损失优化交叉编码器教师，再做候选集分数分布蒸馏到双塔，能低成本提升双塔召回效果

  - 工程优化可直接落地FSQ数值特征压缩、Transformer层剪枝、FP8后量化这套方案，QPS累计提升超45%，几乎无效果损失，适配大流量电商场景

  - 冷启动/抗陈旧场景可参考LLM原生双塔方案，仅需少量训练数据即可追平传统DLRM效果，对低曝光尾item增益明显，且无需频繁重训'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式LLM推荐普遍存在自回归解码延迟高、推理成本大、生成结果易出现无效item ID等grounding问题，无法落地大规模工业检索场景；而传统双塔检索架构虽效率达标，但语义表征能力不足，难以充分挖掘用户行为和物品属性的语义信号。

### 方法关键点
- 交叉编码器教师优化：采用yes/no二分类输出头计算用户item相关性分数，新增用户上下文条件下的item文本next-token预测辅助损失，提升教师排序精度
- 双塔学生优化：用户/Item塔共享LLM编码器，采用EOS token pooling生成序列嵌入，语义空间对齐效果优于均值 pooling；新增仅作用于用户塔的Coconut风格隐式推理，不影响Item embedding离线预计算
- 跨数据集迁移+蒸馏：先在多数据集上预训练提升泛化性，再将交叉编码器在候选集上的排序分数分布通过KL散度蒸馏到双塔，对齐排序偏好

### 关键实验
- 公开数据集：在3个Amazon Reviews基准上对比SOTA生成式推荐OneRec-Think（8B参数），仅用0.6B参数的交叉编码器在12个测评指标中拿下10个最优，R@10最高提升64.3%；双塔学生在所有数据集的R@10指标上均超过OneRec-Think，最高提升35.3%
- 内部生产实验：仅用0.5%的训练数据即可追平高度优化的DLRM双塔基线，尾item（低曝光）NE提升5.5%，头用户（高活跃）NE提升2.3%；冻结模型3天无性能衰减，而传统DLRM性能下降4.3%

### 核心结论
无需盲目跟风生成式检索，经过LLM语义增强和蒸馏优化的传统双塔架构，仍是当前工业级大规模检索最具性价比的落地方案
