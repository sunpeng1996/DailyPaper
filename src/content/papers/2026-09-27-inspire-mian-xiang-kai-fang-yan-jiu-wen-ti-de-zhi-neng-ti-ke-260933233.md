---
title: 'Inspire: Benchmarking Scientific Literature Search for Open Research Problems'
title_zh: INSPIRE：面向开放研究问题的智能体科学文献搜索基准
authors:
- Jianrong Ding
- Zhengyan Shi
- Jianyuan Zhong
- Kai Qiu
- Qi Dai
- Yifan Yang
- Chong Luo
- Qiang Xu
affiliations:
- The Chinese University of Hong Kong
- Microsoft Research Asia
arxiv_id: '2609.33233'
url: https://arxiv.org/abs/2609.33233
pdf_url: https://arxiv.org/pdf/2609.33233
published: '2026-09-27'
collected: '2026-09-29'
category: Eval
direction: 智能体搜索 · 全链路评测基准
tags:
- Agent
- Evaluation
- Information Retrieval
- Scientific Search
- Benchmark
one_liner: 提出覆盖搜索全链路三阶段的开放语料科学文献搜索基准，支持端到端评测与瓶颈诊断
practical_value: '- 可复用三阶段漏斗诊断框架：将搜索/推荐系统的链路拆分为资源曝光、选择、排序三个环节，可精准定位业务瓶颈，比如电商搜索中可区分是召回侧漏召、粗排侧漏选还是精排侧排序错误，避免优化方向走偏

  - 可迁移hindsight SFT训练范式：利用业务侧已有的事后优质交互轨迹做监督微调，无需新增测试侧信息即可提升搜索/导购Agent的全链路表现，适合冷启动阶段的Agent快速迭代

  - 可借鉴脱敏评测集构造方案：通过回溯真实行为、隐藏后续结果的方式构造无泄露的评测集，解决推荐/搜索系统评测中数据泄露、和真实场景脱节的问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有科学文献搜索基准多预设明确的相关性规则或限定候选集，无法模拟真实开放问题场景下，搜索Agent自主构建相关性判断、迭代调整搜索策略的过程，也无法定位全链路中损失发生的具体环节，导致评测结果难以指导实际系统优化。

### 方法关键点
- **任务构造**：回溯已发表的计算机科学论文，移除其核心方法、结果信息生成脱敏研究问题，设置论文发表前3个月的时间截断，要求Agent在开放语料中搜索并提交最多10篇排序后的相关文献，评测时以原论文的分级引用文献作为隐藏真值。
- **三阶段评测框架**：基于交互日志拆分三个耦合环节的表现：资源曝光（是否检索到相关文献，对应G_exposed）、选择（是否保留曝光的相关文献，对应G_selected）、排序（保留文献的排序质量，对应G_final），通过指标差可直接定位损失发生的阶段。
- **事后监督方案**：基于历史成功轨迹构造hindsight SFT数据集，训练时用特权信息筛选有效轨迹，测试时不引入额外信息，即可提升Agent的搜索表现。

### 关键结果
在476篇目标论文的测试集上对比6款主流大模型Agent：最强的Claude Opus 5 nDCG@10仅为0.284，72.3%的case可至少召回1篇相关文献，但仅32.1%的case可召回至少3篇；全链路最大损失发生在资源曝光阶段，占比超50%，选择、排序阶段分别损失约10%、8%；基于INSPIRE的hindsight SFT将Qwen3.6-35B的nDCG@10从0.082提升至0.166，提升幅度超100%。

### 核心结论
当前智能体搜索的最大瓶颈是资源曝光而非后续的选择或排序，优化召回阶段的覆盖度优先级远高于优化排序策略。
