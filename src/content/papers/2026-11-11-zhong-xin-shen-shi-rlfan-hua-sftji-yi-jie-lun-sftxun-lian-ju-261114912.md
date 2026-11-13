---
title: 'Rethinking "RL Generalizes, SFT Memorizes": The Role of SFT Data'
title_zh: 重新审视“RL泛化、SFT记忆”结论：SFT训练数据的核心作用
authors:
- Yunlong Hou
- Fengzhuo Zhang
- Yuan Cheng
- Jiachun Pan
- Xingyao Li
- Zhuoran Yang
affiliations:
- National University of Singapore
- Yale University
- Cisco Foundation AI
arxiv_id: '2611.14912'
url: https://arxiv.org/abs/2611.14912
pdf_url: https://arxiv.org/pdf/2611.14912
published: '2026-11-11'
collected: '2026-11-13'
category: Training
direction: 大模型微调 · SFT与RL泛化性对比
tags:
- SFT
- Reinforcement Learning
- Generalization
- LLM Training
- Reasoning
one_liner: 通过优化SFT数据的来源与规模，证明SFT可达到甚至超越RL的泛化能力
practical_value: '- 电商客服/导购Agent、推荐理由生成等场景的LLM微调，优先选择优化SFT方案而非RL，工程复杂度低、算力成本仅为RL的1/3左右，效果可持平

  - SFT数据构造优先混合70%-90%同基座模型生成的on-policy rollout+10%-30%强teacher模型数据，比单用强teacher数据的OOD泛化性提升10%以上

  - SFT数据规模不要仅按prompt数量对齐，要匹配RL的总rollout预算，可加入部分错误推理样本，其包含的正确中间步骤能进一步提升泛化能力

  - 做业务场景的推理类SFT时，刻意补充长尾推理模式的样本，可显著提升少见query、冷门需求的处理准确率'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
业界长期存在“RL微调泛化性强、SFT微调易过拟合记忆”的共识，但该结论的实验前提未对齐SFT与RL的训练数据资源，无法验证SFT的真实性能上限，需要重新明确两者泛化性差异的前置条件。
### 方法关键点
- 数据源对比：分别使用强teacher模型（Qwen3-14B）、同基座RL微调后模型生成的正确rollout作为SFT数据源，测试不同混合比例的效果；
- 数据规模对齐：按可解prompt数、正确rollout数、总rollout数三个维度对齐SFT与RL的训练数据量，验证规模对泛化的影响；
- 机理分析：通过LLM标注训练rollout的解法类型，验证长尾解法覆盖度与泛化性的关联，同时基于浅Transformer训练动力学提供理论支撑。
### 关键结果
基于Qwen2.5-7B、Qwen3-8B基座在DAPO数学数据集训练，测试覆盖数学推理、12个通用推理任务：
1. SFT使用70%同基座RL生成数据+30%强teacher数据，比单数据源通用推理得分提升12%；
2. 匹配总rollout数（13.8万样本）的SFT，通用推理得分与RL持平，混合最优数据源后比RL高3.2分；
3. 数据规模对齐RL总rollout时，SFT的长尾解法覆盖度提升47%，OOD场景准确率提升18%。

**核心结论**：“RL泛化、SFT记忆”仅在SFT数据资源不足时成立，只要SFT数据来源适配、规模对齐RL，泛化性可超过RL。
