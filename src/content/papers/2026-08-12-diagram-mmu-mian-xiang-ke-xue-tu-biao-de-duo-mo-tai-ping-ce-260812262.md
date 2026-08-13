---
title: 'Diagram-MMU: A Multi-Modal Benchmark for Scientific Diagrams'
title_zh: Diagram-MMU：面向科学图表的多模态评测基准
authors:
- Weihao Bo
- Shan Zhang
- Yanpeng Sun
- Jie Liu
- Yongke Yao
- Jinhao Du
- Wei He
- Kai Zou
- Zechao Li
- Jingdong Wang
affiliations:
- Nanjing University of Science and Technology
- Baidu Inc
- Adelaide University
- SUTD
- Southeast University
arxiv_id: '2608.12262'
url: https://arxiv.org/abs/2608.12262
pdf_url: https://arxiv.org/pdf/2608.12262
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: 多模态大模型 科学图表能力评测
tags:
- MLLM
- Benchmark
- Diagram Understanding
- Agent Evaluation
- Multimodal
one_liner: 构建含3.7k图表18.3k标注问题的多模态基准，评估MLLM科学图表解析理解及Agent场景下的任务表现
practical_value: '- 图表转代码类业务需求可优先引入Agent工作流，实测能显著提升多数MLLM的解析、编辑类生成任务表现

  - 多模态Agent效果验证可参考本基准的三层任务设计（解析/编辑/问答），覆盖不同难度的交互场景

  - 若业务同时涉及多模态内容生成+问答双需求，可优先选型Claude-4.6 Opus，其在Agent场景下三类任务性能均有提升'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有MLLM在科学写作协作场景下的图表解析能力缺乏统一评测基准，无法系统评估模型在图表转代码、编辑、问答等实际工作流任务的表现，尤其是Agent交互场景下的性能差距不明确。

### 方法关键点
构建Diagram-MMU基准，覆盖6个领域的3.7k人工筛选科学图表，配套18.3k人类验证的问题集，设置三类核心任务：diagram-to-code解析、diagram-to-code编辑、图表问答，同时新增每个任务的Agent交互评测范式。

### 关键结果数字
12款MLLM评测显示，图表转代码类任务难度显著高于问答类，模型在问答任务准确率领先解析任务32%以上；Agent模式下多数模型解析/编辑性能提升15%-28%，但问答性能平均下降9%，仅Claude-4.6 Opus三类任务性能均实现正向提升。
