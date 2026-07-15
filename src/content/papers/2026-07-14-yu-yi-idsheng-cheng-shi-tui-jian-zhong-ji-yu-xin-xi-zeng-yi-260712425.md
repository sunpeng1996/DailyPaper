---
title: 'Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based
  Generative Recommendation'
title_zh: 《语义ID生成式推荐中基于信息增益的推理资源优化分配》
authors:
- Shangxin Yang
- Min Gao
- Zongwei Wang
- Junliang Yu
arxiv_id: '2607.12425'
url: https://arxiv.org/abs/2607.12425
pdf_url: https://arxiv.org/pdf/2607.12425
published: '2026-07-14'
collected: '2026-07-15'
category: GenRec
direction: 生成式推荐 · 语义ID推理优化
tags:
- GenRec
- Semantic ID
- Information Gain
- Inference Optimization
- LLM4Rec
one_liner: 提出基于信息增益分配语义ID各位置潜层推理步的IBA框架，优化生成式推荐精度-算力trade-off
practical_value: '- 生成语义ID时无需给每个token分配固定推理步数，可按位置信息增益动态分配，在算力不变的前提下提升推荐准确率

  - 可复用信息增益（IG）的计算逻辑优化语义ID结构，优先保证高IG位置的编码/生成质量

  - 算力紧张的线上推理场景，可直接给低IG语义ID位置减少推理步，在精度损失可接受范围内降低推理时延'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有基于Semantic ID的生成式推荐通常给每个ID token分配固定数量的潜层推理优化步，未考虑不同位置token的信息贡献差异，存在算力浪费或高贡献位置优化不足的问题。
### 方法关键点
1. 定义位置级信息增益（IG）衡量每个Semantic ID位置对降低目标item不确定性的贡献度，观测到ID序列前序位置IG远高于后序位置；
2. 提出IBA框架，将潜层推理步作为有限算力资源，动态给高IG位置分配更多推理步，低IG位置少分配。
### 关键结果
在多个公开数据集上，IBA相比固定步数分配的强基线，相同算力开销下推荐准确率平均提升6%~12%，相同准确率下可降低约30%的推理算力消耗。
