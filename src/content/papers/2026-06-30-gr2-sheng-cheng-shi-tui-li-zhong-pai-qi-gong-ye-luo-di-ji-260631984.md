---
title: GR2 Technical Report
title_zh: GR2 生成式推理重排器工业落地技术报告
authors:
- Yufei Li
- Zaiwei Zhang
- Mingfu Liang
- Kavosh Asadi
- Jay Xu
- Jimmy Kim
- Chongyang Bai
- Jieyi Zhang
- Hongye Xie
- Prachi Agrawal
affiliations:
- Meta AI
arxiv_id: '2606.31984'
url: https://arxiv.org/abs/2606.31984
pdf_url: https://arxiv.org/pdf/2606.31984
published: '2026-06-30'
collected: '2026-07-01'
category: RecSys
direction: 生成式推荐 · LLM重排工业落地
tags:
- LLM4Rec
- Re-ranking
- Semantic ID
- Reinforcement Learning
- Distillation
one_liner: Meta提出工业级LLM生成式推理重排框架，重排指标大幅提升且适配落地成本约束
practical_value: '- 语义ID落地方案可直接复用：采用RQ-VAE生成≥99%唯一性的Semantic ID，将亿级工业item映射到LLM词表，无需扩增词表即可让模型感知item语义，解决原生ID不在词表的痛点

  - 小模型训练优先用OPD替代SFT：工业规模下SFT易出现分布崩塌，On-Policy Distillation可让1.7B小模型恢复32B大教师82%的效果，仅占5%的参数量，大幅提升投产ROI

  - RL重排防奖励hacking可复用条件奖励设计：仅当输出不是输入原有顺序、或输入顺序本身最优时才发放排序奖励，避免模型直接照搬上游排序骗奖励

  - 在线推理优化方案可直接复用：通过二次RL将CoT推理内隐到模型权重，无需显式生成推理链，结合80%输入压缩率的上下文压缩、KV缓存、模型剪枝，可实现15倍以上的推理吞吐量提升，满足在线低延迟要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐多阶段漏斗中，重排阶段最直接影响用户最终体验，但现有LLM推荐方案大多聚焦召回、粗排，重排场景探索严重不足；同时三大落地痛点阻碍规模化应用：LLM多以零样本/SFT部署，未激活RL可验证奖励解锁的推理能力；工业亿级item的非语义ID不在LLM原生词表，无法直接用于推理；大模型推理成本高、SFT在工业规模易崩塌、存在奖励hacking问题，难以落地。

### 方法关键点
- 基于RQ-VAE生成≥99%唯一性的Semantic ID，将ID与自然语言混合中训练，让LLM识别item语义，无需扩增词表
- 用大模型教师生成重排推理轨迹，采用OPD替代SFT迁移能力，避免工业规模下SFT分布崩塌
- 基于DAPO算法做RL优化，奖励由格式校验、AUC/NDCG排序指标、可选LLM-as-judge组成，增加条件门控防奖励hacking
- 落地侧做三重优化：上下文压缩减少80%输入token，二次RL将CoT内隐到模型权重，结合KV缓存、模型剪枝压缩推理成本

### 关键实验
基于Meta内部7万条用户会话训练，测试集99%候选item、100%用户ID未见过，对比实时刷新的传统point-wise重排基线，GR2实现+18.7% R@1、+7.1% R@3、+9.6% N@3提升，效果连续9天无衰减，适配工业级流量规模。

**最值得记住的一句话**：LLM重排的核心收益来自世界知识与推理能力而非数据拟合，小模型通过蒸馏+RL可在远低于大模型的成本下拿到大部分收益
