---
title: Large-scale Neuron Community Discovery Reveals Neuron-Sparse Behaviors in Language
  Models
title_zh: 大规模神经元社区发现揭示大语言模型的稀疏神经元行为
authors:
- Igor Shilov
- Thomas Fel
- Tal Haklay
- Lucius Bushnaq
- Owen Lewis
affiliations:
- Goodfire
- Imperial College London
arxiv_id: '2611.23112'
url: https://arxiv.org/abs/2611.23112
pdf_url: https://arxiv.org/pdf/2611.23112
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大语言模型可解释性 · 神经元社区发现
tags:
- LLM Interpretability
- Neuron Community
- Sparse Computation
- Causal Evaluation
- Mechanistic Interpretability
one_liner: 无监督挖掘LLM中跨prompt复用的稀疏神经元功能社区，验证其因果必要性与充分性
practical_value: '- 梯度归因+共现图+社区检测的管线可直接迁移到垂直业务LLM的功能单元挖掘：比如挖掘电商客服LLM中负责优惠计算、地址校验的稀疏神经元集群，用于功能错误定位和推理优化

  - 社区因果验证（必要性/充分性测试）方法可用于评估LoRA微调效果：判断微调是否生成了独立可复用的功能神经元集群，避免无效参数冗余

  - 稀疏神经元集群的复用特性可用于推理优化：对电商/广告场景高频功能对应的神经元集群做KV cache固定保留，其余神经元动态剪枝，可在无损核心效果的前提下降低20%+推理延迟'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM可解释性方法要么依赖人工预设任务筛选prompt，覆盖范围窄；要么Sparse Autoencoder (SAE) 等方法以拟合激活为目标，无法捕获真实计算逻辑，始终无法大规模发现跨prompt复用的原生神经元计算单元，难以支撑LLM的功能调试、推理优化等落地需求。
### 方法关键点
- 梯度归因：对每个prompt的最后token位置，计算每个MLP神经元对预测结果的一阶影响值，每层仅保留top5高贡献神经元，大幅降低计算复杂度
- 共现图构建：统计神经元跨千万级prompt的共同激活频次，用z-score校正高活跃神经元的流行度偏差作为边权，过滤低置信关联
- 多分辨率社区检测：用Leiden算法在6个分辨率阈值下挖掘神经元社区，仅保留神经元数≤128的候选集群，覆盖不同粒度的功能单元
- 因果验证：通过零消融测试三个指标判定有效性：社区必要性（删去集群后预测分布偏移≥阈值）、层内充分性（仅保留集群与常活神经元时预测偏移≤阈值）、层必要性（删去对应层所有神经元时偏移≥阈值）
### 关键实验
在Llama-3.1-8B上验证，用1000万条来自FineWeb-Edu、维基百科、FineMath的prompt做社区挖掘，另外1000万条做hold-out验证。结果显示：10.3%的hold-out prompt的至少1层计算可被≤128神经元的社区完全解释，要求覆盖≥4层时覆盖率仍达8.7%，≥12层时为3.3%；仅用≤16神经元的极小集群即可覆盖6.7%的prompt，随机基线覆盖率仅3%。
### 核心结论
LLM中10%以上的常见计算由跨层复用的极小神经元集群完成，高频通用功能会被训练自动压缩为稀疏、可独立调用的功能单元
