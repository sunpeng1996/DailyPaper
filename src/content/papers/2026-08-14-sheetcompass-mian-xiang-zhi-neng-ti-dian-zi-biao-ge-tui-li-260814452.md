---
title: 'SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning'
title_zh: SheetCompass：面向智能体电子表格推理的层级关系图框架
authors:
- Panjing He
- Mingyue Cheng
- Yucong Luo
- Li Li
- Xiaohan Zhang
affiliations:
- State Key Laboratory of Cognitive Intelligence, University of Science and Technology
  of China
arxiv_id: '2608.14452'
url: https://arxiv.org/abs/2608.14452
pdf_url: https://arxiv.org/pdf/2608.14452
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多智能体协作 · 半结构化表格推理
tags:
- Multi-Agent
- Graph Representation
- Spreadsheet Reasoning
- LLM Agent
- Structural Perception
one_liner: 通过层级图建模+多智能体协同解决表格扁平化处理的结构丢失问题，实现推理SOTA
practical_value: '- 处理电商/广告多表经营数据时可复用层级图建模方法，以表/列为节点，融合结构边+语义边建模跨表依赖，避免将表格打平为文本丢失关联信息，提升数据处理准确率

  - 复杂结构化数据处理任务可拆分三类Agent角色：导航探索Agent定位数据、逻辑编程Agent生成执行代码、校验反思Agent核对结果，比单Agent处理鲁棒性更高

  - 双内存机制可迁移到业务Agent开发：静态专家知识内存存储业务通用规则（如电商营收计算公式），动态经验内存存储历史执行错误，减少大模型重复幻觉'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有电子表格处理方法多将多维结构打平为文本序列，丢失表内空间布局与表间语义关联，导致LLM在复杂跨表推理任务上性能骤降；企业经营、电商交易、广告效果等数据大量以表格形式存储，自动化处理需求旺盛但现有方案准确率不足。
### 方法关键点
1. 层级关系图建模：节点分为表节点、列节点，边分为结构边（表-列归属、列相邻关系）和语义边（结合向量相似度+LLM校验生成，阈值过滤低置信度连接）
2. 双层内存机制：静态专家知识内存存储工具使用、通用规则，动态推理经验内存记录当前任务执行轨迹、错误信息，成功经验可沉淀到静态内存
3. 三智能体工作流：导航探索Agent完成任务拆分、相关子图检索；逻辑编程Agent基于子图生成可执行代码；校验反思Agent核对结果，反馈错误触发迭代
### 关键结果
在SCB、SB、SheetRM三个表格推理数据集上对比SheetAgent、SheetCopilot等基线，以GPT-5为骨干时，SCB pass@1达71.3%，SB hard restriction达22.0%，SheetRM pass@1达52.3%，均显著领先SOTA基线；消融实验显示移除层级图会导致SCB pass@1下降14.9%，是核心贡献组件。

最值得记住的结论：半结构化数据处理优先恢复原生结构拓扑再做推理，效果远好于直接扁平化输入大模型。
