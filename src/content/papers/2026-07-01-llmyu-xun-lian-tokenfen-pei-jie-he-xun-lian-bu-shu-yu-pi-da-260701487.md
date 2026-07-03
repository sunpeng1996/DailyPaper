---
title: How to Allocate Your Tokens? Scaling Laws with Training Steps and Batch Size
title_zh: LLM预训练Token分配：结合训练步数与批量大小的缩放定律
authors:
- Fabian Schaipp
affiliations:
- Inria
- École Normale Supérieure
- PSL Research University
arxiv_id: '2607.01487'
url: https://arxiv.org/abs/2607.01487
pdf_url: https://arxiv.org/pdf/2607.01487
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: LLM预训练 · 超参缩放定律
tags:
- Scaling Law
- LLM Pre-training
- Batch Size
- Training Steps
- Compute Efficiency
one_liner: 提出纳入模型大小、批量大小、训练步数的三项缩放定律，降低拟合成本且支持次优批量分析
practical_value: '- 训练垂直领域LLM（如电商生成式推荐、Agent专用模型）时，拟合最优batch size无需全量超参扫描，每类（模型大小+Token预算）仅需2个batch
  size跑数，用三项定律即可得到和全量扫描一致的最优batch size，节省72%训练成本

  - 硬件受限无法使用最优batch size时，可通过两阶段拟合方法计算ε-次优batch size区间，将计算浪费控制在5%以内

  - 自研小模型预训练可直接复用最优batch size与Token预算的幂律关系M⋆∝D^0.566，无需从零开始超参扫描'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统Chinchilla缩放定律仅考虑模型大小和总Token数，未拆分训练步数与批量大小，最优batch size的拟合需要大量全量超参扫，成本极高，也无法评估硬件受限下次优批量的性能损失，业界需要更高效、覆盖更全场景的缩放定律。
### 方法关键点
- 三项缩放定律（3TL）将损失建模为模型大小N、Token级批量大小M、训练步数K的幂律函数之和，最优分配下可自动退化为Chinchilla形式
- 支持次优批量数据拟合，无需每类配置都扫全量batch size就能得到稳定的最优batch size缩放关系
- 配套两阶段拟合方法可计算ε-次优batch size区间，量化次优配置的计算损耗
### 关键实验
在Li（公开LLM预训练日志）和OpenEuroLLM两个数据集上验证，对比直接拟合最优batch size的Step-Law：
- 仅保留每类（N+D）2个batch size的训练数据时，3TL拟合的最优batch size缩放关系和全量扫结果偏差<2%，而直接拟合方法偏差超过60%，所需训练跑数仅为原方法的28%
- 5%计算损耗下的次优batch size区间宽度约为4倍，跨模型大小、训练配置一致性高
- 3TL对临界批量大小的建模和已有实证结果完全匹配，且不存在旧模型最优batch size为1的理论矛盾
### 核心结论
LLM预训练最优批量大小仅和总Token预算相关，和模型大小无关
