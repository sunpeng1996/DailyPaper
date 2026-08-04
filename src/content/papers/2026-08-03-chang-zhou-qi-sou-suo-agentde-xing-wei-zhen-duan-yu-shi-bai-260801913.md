---
title: Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents
title_zh: 长周期搜索Agent的行为诊断与失败模式分析
authors:
- Qi Liu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2608.01913'
url: https://arxiv.org/abs/2608.01913
pdf_url: https://arxiv.org/pdf/2608.01913
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索Agent行为诊断与优化
tags:
- Search Agent
- Long-Horizon Reasoning
- Failure Diagnosis
- Retrieval Gap
- Utilization Gap
one_liner: 基于轨迹级分析拆解长周期搜索Agent的检索/利用两类失败模式，提出定向优化路径
practical_value: '- 搭建电商导购/搜索Agent时不要盲目增加搜索步数，可采用20步的检索截断策略，仅损失最多14%准确率的前提下大幅降低token消耗；更长期可落地基于累计召回证据的动态停止规则，进一步提升效率

  - Agent效果差时可先做失败归因：属于检索缺口的优化query生成模块，增加去重逻辑避免重复检索；属于利用缺口的优化证据整合、答案校验模块，不要盲目堆检索资源

  - 上下文容量优化优先做搜索snippet的去重、旧证据老化，snippet占上下文总量的66%-85%，优化收益远高于限制visit文档数量

  - 单轮并行批量发起多个搜索query（如GLM 5.1单轮发1.87个query）可显著提升搜索效率，降低多轮交互的延迟和成本，适合业务降本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前长周期搜索Agent仅以最终准确率评估效果，无法区分错误是源于未检索到有效证据还是未正确利用证据，盲目拉长搜索周期反而导致大量无效算力消耗，也无法精准定位优化方向。

### 方法关键点
- 基于人工标注的文档级相关性，将Agent行为拆分为「证据检索」和「证据利用」两个独立阶段，对应失败分为**检索缺口**（未找到支撑答案的有效证据）、**利用缺口**（检索到有效证据但未正确生成答案）两类
- 控制检索模型、测试框架完全一致，对比6个不同量级的开源搜索Agent，覆盖120B参数以内的中尺度模型和前沿大模型
- 从结果归因、失败模式分类、轨迹/query策略三个维度做从粗到细的粒度分析

### 关键实验结果
在带人工标注相关性的BrowseComp-Plus数据集（830个问题）上测试，同时在开放网搜场景验证结论：
1. 搜索步数、上下文消耗与准确率的相关性仅为0.16，而累计检索召回率与准确率的相关性达0.99
2. 有效证据大多在轨迹早期出现，77%-94%的搜索步无新增证据，20步的搜索上限可保留86%-92%的准确率
3. 5个测试Agent的错误中51.6%-64.1%属于检索缺口，仅Kimi K2.6的错误中52%属于利用缺口

> 最值得记住的结论：搜索Agent的核心竞争力是query精准度而非搜索深度，高搜索量是失败的症状而非解决方案
