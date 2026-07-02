---
title: 'Persona Non Grata: LLM Persona-Driven Generations in MCQA are Unstable in
  Distinct Dimensions'
title_zh: MCQA任务中LLM人设驱动生成的多维度不稳定性研究
authors:
- César Guerra-Solano
- Xiang Lorraine Li
affiliations:
- Department of Computer Science, University of Pittsburgh
arxiv_id: '2607.00937'
url: https://arxiv.org/abs/2607.00937
pdf_url: https://arxiv.org/pdf/2607.00937
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM人设驱动生成稳定性评估
tags:
- LLM
- Persona-Driven Generation
- MCQA
- Stability Evaluation
- Prompt Engineering
one_liner: 提出三类稳定性度量指标，量化MCQA场景下LLM人设驱动生成的多维度不稳定性及核心影响因素
practical_value: '- 搭建人设驱动的Agent客服/导购系统时，优先对齐prompt格式而非仅调整temperature，可大幅降低输出不稳定

  - 针对数学/常识类用户咨询（如促销规则计算、商品使用常识），需额外做人设输出稳定性校验，避免前后矛盾

  - 做Agent人设选型时，需覆盖不同任务场景、prompt模板做稳定性评测，不能仅靠单一任务准确率选最优人设'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
人设驱动生成（PDG）已广泛应用于产业场景，但现有稳定性研究多聚焦自由文本对话场景，多选问答（MCQA）这类短输出场景的PDG稳定性长期被忽视，缺乏系统度量方法。
### 方法关键点
设计三类稳定性指标，分别度量性能稳定性、输出结果稳定性、单题回答正确性稳定性，从模型家族/尺寸、问题域、超参数三个维度系统评估PDG的不稳定程度。
### 关键结果
1. 数学/常识类问题的PDG不稳定程度显著高于其他领域；
2. 任务prompt格式对输出不稳定的影响远大于temperature等超参数；
3. 不稳定性与任务准确率强相关，同类人设的优劣排序在不同实验设置下差异显著，无通用最优人设。
