---
title: General progress substitutes for specific training data in language models
title_zh: 大模型通用训练进展可替代特定技能的专属训练数据
authors:
- Mark Marosi
- Peter Antal
affiliations:
- Budapest University of Technology and Economics
arxiv_id: '2611.24844'
url: https://arxiv.org/abs/2611.24844
pdf_url: https://arxiv.org/pdf/2611.24844
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: 大模型训练 · 技能习得与数据过滤
tags:
- LLM Training
- Data Filtering
- Skill Acquisition
- Domain Adaptation
- Scaling Law
one_liner: 验证大模型通用训练可替代特定技能专属数据，小模型可预测大模型技能延迟与重训成本
practical_value: '- 训练电商/广告垂域LLM时，无需从零训练，足量通用预训练的模型仅需原训练数据0.1%~13%的领域专属数据即可补全垂域技能，大幅降低数据采集成本

  - 做模型安全管控（如过滤违规商品生成、虚假营销话术生成能力）时，优先选择预训练阶段直接过滤相关数据的方案，其后续被恶意恢复的成本是「学会后再卸载」方案的5~20倍，安全性更高

  - 大模型训练前可先用小参数版本做技能习得、数据需求的预实验，结果可迁移到同架构大模型，降低大模型垂域适配的实验成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前大模型训练普遍通过过滤特定敏感数据避免习得有害技能，但过滤操作能延迟技能习得多久、后续恢复技能需要多少数据，以及技能习得多大程度来自专属数据还是通用语料的溢出贡献，均缺乏量化结论。

### 方法关键点
1. 提出target thinning方法，保留全部输入文本，仅移除特定技能对应的next-token损失信号，避免输入侧信息对实验的干扰
2. 用background loss（非目标技能区域的预测损失）对齐不同模型的通用训练进度，隔离通用训练对技能习得的影响
3. 引入logit距离度量模型在目标技能上的进度差，量化预测技能恢复的训练成本

### 关键实验与结果
实验覆盖国际象棋、Othello、分子SMILES、括号语言、网页文本5个领域，模型参数范围0.76M~7B：
1. 完全未见过专属训练信号的模型可从通用语料习得部分技能，如未训练过应将应对的象棋模型，对合法走法的排序效果接近全监督模型
2. 恢复被过滤的技能仅需初始训练数据的0.1%~13%，通用训练每多1个logit进度，象棋/网页文本领域恢复成本降10倍，SMILES领域降4倍；7B模型恢复Rust编程能力仅需2.1%的原训练数据，编译准确率从18%提升至37%
3. 小模型上测得的技能延迟、恢复成本可直接预测同架构大模型的对应指标，平均误差仅0.058 nat

最值得记住的结论：大模型对特定技能的习得，很大程度上来自通用训练的溢出，而非完全依赖专属技能的训练数据。
