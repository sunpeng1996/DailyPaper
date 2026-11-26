---
title: 'Put the World Back: Timestamps Matter in Time Series Reasoning'
title_zh: 时间序列推理中时间戳的核心作用与诊断协议
authors:
- Tingrui Huang
- Yuanyuan Deng
- Qingren Yao
- Joaquin Vanschoren
- Mykola Pechenizkiy
- Songgaojun Deng
affiliations:
- Eindhoven University of Technology
arxiv_id: '2611.34848'
url: https://arxiv.org/abs/2611.34848
pdf_url: https://arxiv.org/pdf/2611.34848
published: '2026-11-25'
collected: '2026-11-26'
category: Reasoning
direction: 时序推理 · LLM能力诊断
tags:
- Time Series Reasoning
- Timestamp
- LLM Evaluation
- Causal Reasoning
- Diagnostic Protocol
one_liner: 提出时序因果诊断协议TCDP，揭示LLM时序推理高准确率多依赖相关性捷径而非真实使用时间戳
practical_value: '- 做用户行为序列、时序召回排序等推荐任务时，不要仅依赖离线准确率评估，可通过打乱时间戳、替换为相对偏移等干预方式，验证模型是否真的学到时序因果关系，避免依赖位置、共现等捷径导致线上效果不达预期

  - 开发电商销量预测、广告投放时序决策类Agent时，需显式校验事件与时间序列的对齐逻辑，不能假设输入天然预对齐，避免线上事件时序错配引发决策错误

  - 基于LLM做用户行为解释、销量突增归因等时序分析场景时，优先保留真实时间戳而非仅用相对偏移，可利用LLM内置的大促、节假日等世界知识提升分析准确性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM被广泛应用于时间序列预测、归因、决策等推理场景，但现有基准普遍提供预对齐、按时序排列的事件与数值序列输入，无法区分模型是真正利用时间戳完成推理，还是依赖事件顺序、文本近邻等相关性捷径答题，高准确率存在严重误导性。
### 方法关键点
- 提出世界到序列的投射视角：将时间戳定义为连接数值观测、外部事件与真实世界状态的共享索引，可显式提供三类核心结构：时序因果结构（因果滞后时长）、时间语义（对应真实世界状态的知识索引）、事件-序列对齐关系（事件是否属于观测窗口）
- 设计**Temporal Causal Diagnostic Protocol (TCDP)**：通过对时间戳做三类可控干预（替换为相对偏移、删除所有时间戳、打乱事件与时间戳的对齐关系），结合推理轨迹审计，判断模型是否真的基于时间戳完成推理，而非仅靠准确率评估。
### 关键结果
在TSRBench两个任务上验证：
1. NBA补全事件任务（输入预对齐）：GLM-5.3-Flash、Sonnet-5等强模型删除时间戳后准确率仅下降2~3pp（从~97%到~94%），打乱时间戳对齐后仅下降10pp左右，说明预对齐输入下模型几乎不需要使用时间戳
2. GDELT事件排序任务（输入无预对齐）：GLM-5.3-Flash删除时间戳后准确率从52%暴跌至12%，替换为相对偏移后下降12pp至40%，说明无预对齐时模型会用时间戳召回世界知识，但打乱对齐后仅1/3的运行能发现时间戳错配，仍依赖相关性捷径。
### 核心结论
仅靠预对齐有序输入上的准确率，无法证明模型是通过时间戳将观测与真实世界同步来完成推理的。
