---
title: Self-Evolving Search Index
title_zh: 自进化搜索索引框架SELF-INDEX
authors:
- Sangam Lee
- Wonjae Lee
- Sunghwan Kim
- Deogyong Kim
- Jaehoon Kim
- Daye Nam
- SeongKu Kang
- Dongha Lee
affiliations:
- Yonsei University
- Samsung Research
- University of California, Irvine
- Korea University
arxiv_id: '2609.19656'
url: https://arxiv.org/abs/2609.19656
pdf_url: https://arxiv.org/pdf/2609.19656
published: '2026-09-17'
collected: '2026-09-18'
category: RAG
direction: RAG检索 · 自进化索引优化
tags:
- Self-Evolving Index
- Retrieval Optimization
- RAG
- Agent Memory
- Query Simulation
one_liner: 无需人工干预的自进化索引框架，适配多检索场景，提升搜索Agent与记忆系统效率
practical_value: '- 电商搜索/推荐的倒排、向量索引可复用三阶段优化逻辑：基于用户检索日志自诊断缺陷，仅修改召回效果差的item索引键，通过忠实度/特异性/区分度校验后再上线，避免全量重刷的高昂成本

  - Agent记忆系统可直接套用SELF-INDEX逻辑，无需改动原有记忆存储结构，即可提升历史交互信息的召回率，减少Agent重复调用工具的次数，降低线上开销

  - 缺乏标注检索样本的冷启动场景，可复用Query Simulator的思路：从item/记忆内容生成合理查询，过滤与现有样本重复的内容，补充优化数据，提升冷启动索引效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有索引优化依赖人工设计策略，适配不同语料、检索器时效果波动大，优化过程需要人工标注数据、全量重刷索引，人力与计算成本高，无法适配动态变化的检索需求，严重制约RAG系统、搜索Agent、Agent记忆系统的效果与效率。
### 方法关键点
- 核心框架SELF-INDEX包含Optimizer与Query Simulator两个模块，无需人工干预即可迭代优化索引
- Optimizer执行三阶段循环：自诊断通过共检索画像识别索引缺陷；自修订仅针对有缺陷的文档索引键做整体更新，避免冗余；自校验按忠实度（与原文档一致）、特异性（区分于通用内容）、区分度（与其他索引键无重合）三个规则过滤，仅保留合格键更新索引
- Query Simulator主动从语料生成未覆盖的检索需求查询，过滤重复后输入Optimizer，实现主动进化而非仅响应现有查询
### 关键实验
在BRIGHT（覆盖自然语言、代码、数学）、表格检索数据集、搜索Agent数据集BrowseComp-Plus、Agent记忆数据集LongMemEval-V2上测试，对比Doc2Query、SPIKE、RL-Index等基线：稀疏检索下nDCG@10最高提升40.4%，稠密检索下最高提升57%；搜索Agent准确率最高提升89.5%，搜索调用次数降低21.46%，线上成本显著下降；Agent记忆召回准确率最高提升13.9%。
### 核心结论
索引优化无需固定人工策略与标注数据，通过自诊断、自修订、自校验的闭环迭代即可适配多场景，同时兼顾效果与成本。
