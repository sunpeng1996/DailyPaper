---
title: 'InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations'
title_zh: InSight：面向交互式可视化的智能体主张验证基准
authors:
- Maeve Hutchinson
- Syed Mahbubul Huq
- Mohammad Albinhassan
- Radu Jianu
- Aidan Slingsby
- Pranava Madhyastha
affiliations:
- City, University of London
- Imperial College London
- The Alan Turing Institute
arxiv_id: '2609.01383'
url: https://arxiv.org/abs/2609.01383
pdf_url: https://arxiv.org/pdf/2609.01383
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 交互式可视化推理评测基准建设
tags:
- Agent
- Benchmark
- Claim Verification
- Visual Reasoning
- Interactive System
one_liner: 推出含21349条真实声明的交互式可视化智能体验证基准，支持模型推理过程可审计评估
practical_value: '- 开发电商BI分析Agent、运营数据校验Agent时，可复用「交互轨迹映射推理质量」的审计方法，快速定位Agent操作缺陷

  - 针对需交互才能获取全量信息的Agent任务（如多维度电商报表分析），可参考本数据集构造逻辑搭建内部评测集

  - 设计需主动探索信息的Agent workflow时，可新增「声明可验证性判断」前置模块，减少无效探索操作'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM评测多局限于静态图像、单轮问答，无法适配动态交互式可视化场景的推理需求：这类场景证据常分散在多关联视图、需主动交互才能暴露，现有基准无法评估Agent主动探询、合成证据的能力。
### 方法关键点
1. 构建InSight基准，包含21349条来自人工分析叙事的真实声明，绑定全交互Web可视化环境
2. 任务要求Agent在环境中自主导航操作，判断给定自然语言声明属于被支持、被反驳、无法验证三类
3. 首次将交互轨迹作为推理过程的代理指标，支持对模型证据检索、合成逻辑的严格审计
### 关键结果
测评多款SOTA模型后发现，交互式主张验证仍是极具挑战的任务，现有模型性能远未达落地可用水平
