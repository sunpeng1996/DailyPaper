---
title: Measuring Collapse and Correction in Homogeneous-Panel LLM Debate
title_zh: 同构面板LLM辩论的坍缩与校正量化评估方案
authors:
- Xin Li
- Mengbing Liu
- Chau Yuen
affiliations:
- Nanyang Technological University
arxiv_id: '2609.35279'
url: https://arxiv.org/abs/2609.35279
pdf_url: https://arxiv.org/pdf/2609.35279
published: '2026-09-27'
collected: '2026-09-29'
category: Agent
direction: 多Agent LLM辩论 效果评估
tags:
- MultiAgent
- LLM
- Debate
- Evaluation
- Utility Modeling
one_liner: 提出可审计的多Agent辩论评估协议，拆分坍缩/校正方向并计算加权净效用
practical_value: '- 多Agent协作场景不要只看最终准确率，要拆分「初始正确变错误的坍缩」和「初始错误变正确的校正」两个方向，加权计算净收益再做方案选型，避免只追求防坍缩反而损失更多业务收益

  - 可复用8-probe预辩论筛查方案，快速预判不同模型在多Agent协作中的坍缩风险，优先给高风险模型配置更严格的一致性校验逻辑，节省全量trace日志的存储和计算成本

  - 多Agent辩论58.9%的坍缩发生在第一轮，对电商选品、广告审核等高风险决策场景，可把第一轮分歧作为熔断信号，提前介入人工校验或采信初始多数结果，平衡效率和风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往多Agent LLM辩论的评估仅看最终准确率提升，混淆了两种完全相反的机制：辩论既可能校正初始错误的多数答案，也可能将初始正确的多数答案坍缩为错误共识，导致干预策略选型出现系统性偏差。

### 方法关键点
- 构建四象限过渡账本，将辩论结果分为「正确保留、坍缩、校正、错误未修复」四类，同时记录坍缩发生轮次、干预的正负效用
- 设计8-probe预辩论筛查工具，交叉2种社会压力（无压力/同伴从众压力）和4级反论强度，统计模型的答案翻转率αtot，作为模型级坍缩风险的分诊信号
- 提出带权重的重放评估框架，干预净效用= 预防坍缩数×坍缩权重 - 损失校正数×校正权重，避免仅追求防坍缩的短视策略

### 关键实验
在6925条MMLU-Pro数据集的三同构Agent辩论实验中，共观测到253次坍缩，部分开源模型的坍缩率超过10%；8-probe筛查的家族级坍缩风险相关性Spearman ρ=0.893，p=0.0123；58.9%的坍缩发生在第一轮辩论；留一模型的探针门控冻结策略可预防29次坍缩，但损失108次校正，等权重下净效用为-79。

**最值得记住的结论**：多Agent辩论的效果评估不能只看最终准确率，必须同时统计坍缩和校正的加权净效用，否则会选出表面防坍缩但实际损失更多收益的错误策略。
