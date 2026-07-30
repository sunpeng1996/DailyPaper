---
title: 'ASARL: Autonomous Social-Aware Relevance Learning for QQ Search'
title_zh: ASARL：面向QQ社交搜索的自主社交感知相关性学习框架
authors:
- Tao Su
- Jinjing Hu
- Xiao Wang
- Xingzhong Cao
- Hui Wang
affiliations:
- Tencent PCG
arxiv_id: '2607.26593'
url: https://arxiv.org/abs/2607.26593
pdf_url: https://arxiv.org/pdf/2607.26593
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 搜索相关性 · 多Agent协同数据生成
tags:
- MultiAgent
- Search Relevance
- DPO
- Knowledge Distillation
- LLM4Search
one_liner: 通过多Agent协同数据生成标注与三阶段对齐训练，提升社交场景搜索的相关性与用户参与度
practical_value: '- 多Agent数据标注流水线可直接复用：拆解为标注Agent、校验Agent、长尾数据生成Agent的闭环，替代人工标注，解决小众场景/黑话/长尾query标注难的问题，适合电商/内容平台的垂类搜索场景

  - 三阶段训练架构可迁移：先SFT做领域语义对齐，再用DPO基于用户行为信号做偏好对齐，最后蒸馏到小模型上线，兼顾效果和时延，平衡大模型能力与工业部署成本

  - 垂类场景CoT设计技巧：不要用通用CoT，定制领域专属推理步骤（如电商可拆解为品类、属性、价格、需求匹配），同时结合纯标签监督，效果优于单独用CoT或标签'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
社交搜索场景的query和内容多为非正式、社区专属的俚语/黑话，传统相关性模型存在三大痛点：通用语义表示与社区语境偏差大，长尾小众社区标注数据稀缺，静态人工标注无法匹配用户行为的动态变化，通用LLM的单Agent标注方案也存在一致性差、长尾覆盖不足的问题。

### 方法关键点
- 多Agent协同数据流水线：ReasonAgent生成带推理链路的相关性标签，CriticAgent校验标签逻辑一致性、识别数据分布缺口，GenAgent针对缺口生成补充query-title对，三者闭环自动产出高质量标注数据集，无需人工介入
- 三阶段训练流程：第一阶段Social Context Training（SCT）同时用「推理+标签」和「仅标签」两种prompt做SFT，兼顾模型推理逻辑可解释性和标注精度；第二阶段Preference-Guided Optimization（PGO）基于用户点击/加入等行为信号构造偏好对，用DPO损失做偏好对齐，贴合真实用户需求；第三阶段Social Distillation（SD）将大模型能力蒸馏到BERT等小模型，满足低时延部署要求

### 关键实验
基于QQ搜索1.1M标注样本训练，离线对比BERT、RoBERTa、0.6B Qwen3基线，8B版本ASARL的MacroF1达83.66，较Qwen3 SFT基线高15.31，准确率达84.52；在线A/B测试中，频道搜索场景CTR提升2.69%、加入率提升2.59%，群搜索场景GSB提升16.66%，部署规模达1200万DAU。

### 核心结论
垂类/社交搜索场景下，多Agent协同自动标注+用户行为偏好对齐的训练流水线，可在极低人工成本下实现远优于传统监督训练的相关性效果。
