---
title: 'RESKILL: Explicit Failure Attribution and Structured Repair for Interactive
  Language Agents'
title_zh: RESKILL：面向交互式语言Agent的显式故障归因与结构化修复框架
authors:
- Mengyi Deng
- Xin Li
- Duyi Pan
- Zilin Wang
- Zhiwei Li
- Zhijiang Guo
- Wei Wang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2609.15684'
url: https://arxiv.org/abs/2609.15684
pdf_url: https://arxiv.org/pdf/2609.15684
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: Agent技能迭代 · 故障修复与归因
tags:
- LLM Agent
- Skill Repair
- Failure Attribution
- Self-Improvement
- Interactive Agent
one_liner: 提出结构化故障修复框架，通过显式归因与多轮反馈优化Agent可复用技能
practical_value: '- 电商导购Agent/工具调用Agent的故障修复可复用这套逻辑：先枚举所有可能的故障假设，生成多个候选修复补丁，再通过补丁对假设的覆盖度加权选最优修复，不用依赖单次LLM生成的修复结果，降低错判概率

  - 推荐系统的prompt规则/召回规则迭代可参考归因-修复-验证的闭环：比如召回badcase出现后，先枚举多维度归因（query理解错/物料标签错/规则阈值错），生成多个规则补丁，小流量验证后再全量上线，还能把验证失败的结果作为下一轮迭代的输入

  - 可复用技能库的维护可参考覆盖度选择与权重更新机制：不用每次都全量重写技能，仅做局部补丁更新，同时记录每个补丁解决的故障类型，提升技能库迭代的可解释性与效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有交互式Agent依赖可复用技能，但故障后修复通常是黑盒单次反射，将诊断、修复生成、选择混在一个生成步骤里，既不记录故障解释和候选修复的关联，也不会把重测失败的结果引入后续迭代，容易反复应用无效补丁或过拟合错误诊断，修复效率和成功率低。

### 方法关键点
- 结构化维护修复状态：每轮修复都记录活跃故障假设、假设权重、历史尝试补丁与重测结果，不直接从失败轨迹重写技能
- 多源候选补丁生成：从失败轨迹、故障假设、定向提案、格式校验四个维度生成候选补丁，筛选仅保留可复用、落地到具体技能范围的局部补丁
- 覆盖度加权选择：对每个补丁标注覆盖的故障假设，按假设权重总和选最优补丁，优先选更局部、有证据支撑的补丁
- 结果驱动状态更新：重测失败后，根据反馈更新故障假设集合与权重，上一轮选中补丁覆盖的权重会分配给新暴露的故障假设，指导下一轮修复

### 关键实验
在ALFWorld（家庭交互任务）和TextCraft（符号合成任务）两个数据集，对比Direct Repair、Hypothesis Repair两个基线，覆盖Qwen3-1.7B、Qwen2.5-3B、Qwen3-4B三个模型尺寸：所有6个基准-模型设置下RESKILL都取得最优最终成功率，平均比直接修复高3.7个百分点，比假设条件修复高3.3个百分点，小模型的提升效果更显著。

### 核心结论
仅显式故障归因不足以实现性能提升，只有将归因与修复选择、持续的重测条件更新相结合，才能带来Agent技能的持久优化。
