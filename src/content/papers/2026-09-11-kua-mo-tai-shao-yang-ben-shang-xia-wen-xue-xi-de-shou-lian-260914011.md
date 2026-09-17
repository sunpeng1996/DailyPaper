---
title: Convergent Emergence of In-Context Learning Across Modalities
title_zh: 跨模态少样本上下文学习的收敛涌现特性研究
authors:
- Nathan Breslow
- Seungwook Han
- Daniel Hyunsoo Lee
- Aayush Mishra
- Anqi Liu
- Daniel Khashabi
affiliations:
- Johns Hopkins University
- MIT
- University of Illinois Urbana-Champaign
arxiv_id: '2609.14011'
url: https://arxiv.org/abs/2609.14011
pdf_url: https://arxiv.org/pdf/2609.14011
published: '2026-09-11'
collected: '2026-09-17'
category: LLM
direction: 大模型能力 · 跨模态上下文学习涌现
tags:
- In-Context-Learning
- Cross-Modality
- Emergent-Ability
- Few-Shot-Learning
- Autoregressive-Pretraining
one_liner: 构建跨模态对照框架验证ICL收敛涌现假说，证实五类模态下ICL任务收益高度相关
practical_value: '- 跨模态推荐/广告场景可复用该研究的ICL任务设计范式，对用户行为序列、商品特征序列等非语言模态直接用few-shot ICL做零梯度适配，降低多模态大模型微调成本

  - 可借鉴跨模态ICL难度对齐结论，在多模态生成式推荐中，将NLP场景验证有效的ICL prompt策略直接迁移到用户行为、商品图像等模态，大幅减少prompt调优工作量

  - 针对新推荐任务冷启动场景，可参考自回归预训练+ICL的范式，替代传统特征工程和小样本微调，实现非结构化序列类任务的快速上线'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有ICL（上下文学习）研究多聚焦于NLP领域，近年在基因组等非语言模态也观测到ICL能力，但跨模态下ICL是否存在共通演化规律、是否会收敛涌现尚未得到验证。
### 方法关键点
提出标准化跨模态对照实验框架，在语言、基因组、整数序列、时间序列、图像、蛋白质共6类模态上复用同一套配对映射任务集，验证收敛涌现假说：即ICL生效的任务难度分布具有跨模态一致性，同一任务在一类模态下能通过ICL提效，在其他模态下也大概率适用。
### 关键结果
6类模态下均观测到稳定的配对映射型ICL能力，效果显著超过对照基线；其中5类模态的单任务ICL收益相关性达到统计显著水平，部分验证收敛涌现假说成立。
