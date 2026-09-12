---
title: General Quantification of Covariate and Concept Shifts
title_zh: 协变量偏移与概念偏移的通用量化方法
authors:
- Hongbo Chen
- Li Charlie Xia
affiliations:
- School of Mathematics, South China University of Technology
arxiv_id: '2609.11918'
url: https://arxiv.org/abs/2609.11918
pdf_url: https://arxiv.org/pdf/2609.11918
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 分布偏移量化 · 泛化误差界评估
tags:
- distribution_shift
- generalization_bound
- entropic_optimal_transport
- concept_shift
- covariate_shift
one_liner: 基于熵最优运输提出γ*-概念偏移，推导统一误差界，开发可落地的分布偏移量化工具DataShifts
practical_value: '- 可直接复用DataShifts算法量化推荐/广告系统训练推理数据的分布偏移，提前预警线上性能掉点

  - 统一的协变量+概念偏移误差界可用于校准跨域模型的离线评估结果，缩小线上线下效果Gap

  - γ*-概念偏移的定义解决了支撑集不匹配下的偏移判定问题，可用于冷启动场景的分布差异评估'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有分布偏移下的学习泛化界仅适用于窄范围理想化场景，无法基于样本直接估算，且原有概念偏移定义在源域、目标域支撑集不匹配时失效，难以适配推荐、广告等真实业务的跨域泛化评估需求。
### 方法关键点
1. 基于熵最优运输提出γ*-概念偏移定义，解决支撑集不匹配下的概念偏移判定问题
2. 推导同时覆盖协变量偏移与γ*-概念偏移的通用误差界，适配任意损失函数、标签空间与随机标注场景
3. 开发带浓度保证的偏移量估算器，封装为可直接落地的DataShifts算法
### 关键结果
DataShifts可在绝大多数实际场景中直接量化分布偏移，快速估算模型在目标域的误差界，填补了分布偏移理论到工业落地的Gap
