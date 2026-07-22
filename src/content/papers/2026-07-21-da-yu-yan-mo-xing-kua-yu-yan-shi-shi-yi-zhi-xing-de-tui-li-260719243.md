---
title: Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs
title_zh: 大语言模型跨语言事实一致性的推理阶段调控方法
authors:
- Alexander Manev
affiliations:
- Technical University of Munich
arxiv_id: '2607.19243'
url: https://arxiv.org/abs/2607.19243
pdf_url: https://arxiv.org/pdf/2607.19243
published: '2026-07-21'
collected: '2026-07-22'
category: LLM
direction: LLM跨语言事实一致性推理对齐
tags:
- Cross-lingual Alignment
- Inference Steering
- Persona Prompting
- CAA
- DPO
one_liner: 对比三类跨语言事实对齐方案，证实零样本角色提示综合表现最优
practical_value: '- 做跨语种电商/广告Agent时，优先用零样本角色提示（如添加「你是德国本地消费者视角」的系统前缀）实现本地化对齐，开发成本远低于微调或激活干预

  - 若需训练跨语言偏好LoRA适配器，优先选v1版对比对构造策略（排除相同选项的全叉乘对比），平衡数据量和信号纯度，提升对齐效果的统计显著性

  - CAA激活调控仅适合特定场景的窄域事实修正，需针对不同语言单独调优干预层、缩放系数等超参，避免普通事实问答效果退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM内部知识表示严重偏向高资源语言（尤其是英语），相同问题使用不同语种prompt时答案分布差异显著，跨语言事实不一致问题极大影响全球用户场景下的服务可靠性，现有预训练/全量微调方案计算成本过高，亟需推理阶段可落地的轻量化干预方法。

### 方法关键点
- 对比三类干预方案：零样本角色提示（Persona Prompting）、基于对比激活加法（CAA）的隐状态操纵、基于DPO的轻量LoRA微调，其中DPO又分为基准事实数据训练版和泛化文化数据训练版
- 构造两类评测数据：多语言事实基准数据集（覆盖英、德、西、保等6种语言7类事实关系）、文化泛化评测集（每语言50道英文表述的本地化场景题）
- 采用重复采样下的答案分布Jensen–Shannon距离（JSD）、目标答案概率质量（TPM）作为核心评测指标，同时评测普通事实扰动率和跨场景泛化性

### 关键结果
在Gemma 3 12B Instruct上测试：
- 角色提示在9个测试场景中8个优于基线，德语/保加利亚语场景JSD最高降低24.4%，泛化文化场景下目标文化选项选择率从基线32.7%提升至86.0%，普通事实问答的JSD扰动仅0.0034
- CAA和DPO在窄域事实对齐上有提升，但泛化能力极弱，文化场景目标选择率仅33%左右，且CAA配置敏感，易导致普通事实问答效果退化

### 核心结论
跨语言事实不一致本质是模型输出选择偏向问题而非知识缺失问题，简单的上下文干预在综合效果、安全性、泛化性上远优于侵入式的激活或参数修改方案
