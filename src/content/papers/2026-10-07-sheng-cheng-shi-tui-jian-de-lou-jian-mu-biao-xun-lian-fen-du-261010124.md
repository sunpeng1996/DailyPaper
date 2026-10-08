---
title: 'Training with Missed Targets in Generative Recommendation: Separating Supervision
  from Probability Competition'
title_zh: 生成式推荐的漏检目标训练：分离监督信号与概率竞争
authors:
- Xuesi Wang
- Yangbin Shi
- Xiaolin Zheng
affiliations:
- Independent Researcher
- Zhejiang University
arxiv_id: '2610.10124'
url: https://arxiv.org/abs/2610.10124
pdf_url: https://arxiv.org/pdf/2610.10124
published: '2026-10-07'
collected: '2026-10-08'
category: GenRec
direction: 生成式推荐 · 重排训练优化
tags:
- Generative Recommendation
- Reranking
- Listwise Loss
- Semantic ID
- Training Strategy
one_liner: 提出三组匹配损失分离候选补全的监督与竞争效应，给出漏检目标训练的选型规则
practical_value: '- 生成式推荐重排器做漏检目标候选补全训练时，优先采用Cond损失：对召回候选、漏检目标两组样本分别做softmax归一化，避免仅训练时存在的漏检样本与推理时真实候选的概率竞争，可直接带来7.8%~22.2%的NDCG增益

  - 候选补全不要全局一刀切启用，需为每个生成器单独在验证集对比原生训练与带漏检目标训练的效果，仅当调整后增益的95%置信下界为正时才启用，可避免1.7%的指标损失

  - 多源召回融合训练场景可复用该分组归一化思路，对不同召回源的样本分别做损失归一化，消除跨源样本的不合理概率竞争，提升排序效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐通过生成Semantic ID召回候选，受解码逻辑限制仅能返回有限候选集，常漏检用户真实交互目标。行业常规候选补全方案会将漏检目标追加到重排器训练列表，但该操作同时改变召回目标权重、新增漏检目标监督信号、引入两组样本的概率竞争，无法单独度量各部分效应，也无法解释最终排序效果变化的原因，甚至可能带来负向收益。
### 方法关键点
- 设计三组参数完全匹配的损失函数，分步拆分候选补全的效应：1）Weighted Native（WN）：仅对召回候选做加权列表排序损失，权重与Full损失一致；2）Conditional（Cond）：新增漏检目标组的单独归一化排序损失，两组无概率竞争；3）Full：将两组样本放在同一softmax中计算损失，引入跨组概率竞争
- 通过WN→Cond、Cond→Full的对比，可单独度量新增漏检目标监督、移除跨组竞争的独立效应
- 提出落地选型规则：仅当漏检目标训练在验证集的增益调整后95%置信下界为正，才启用候选补全训练，否则保留原生训练方案
### 关键实验
基于公开OneRec模型与Amazon多品类数据集测试：移除跨组竞争在Amazon Video Games场景下FT-NDCG提升7.8%~22.2%；在A-Health场景下，一刀切启用候选补全会带来1.7%的FT-NDCG损失，使用论文提出的选型规则可完全规避该损失。
### 最值得记住的结论
生成式推荐的候选补全不是通用增益手段，需为每个生成器单独验证效果，避免跨组概率竞争的负向影响。
