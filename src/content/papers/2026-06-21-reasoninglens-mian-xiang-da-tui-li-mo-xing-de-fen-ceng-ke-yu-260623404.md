---
title: 'ReasoningLens: Hierarchical Visualization and Diagnostic Auditing for Large
  Reasoning Models'
title_zh: 《ReasoningLens：面向大推理模型的分层可视化与诊断审计框架》
authors:
- Jun Zhang
- Jiasheng Zheng
- Boxi Cao
- Yaojie Lu
- Hongyu Lin
- Jia Zheng
- Xianpei Han
- Le Sun
affiliations:
- Chinese Information Processing Laboratory, Institute of Software, CAS
- University of Chinese Academy of Sciences
arxiv_id: '2606.23404'
url: https://arxiv.org/abs/2606.23404
pdf_url: https://arxiv.org/pdf/2606.23404
published: '2026-06-21'
collected: '2026-06-30'
category: Reasoning
direction: 大模型推理 · 可解释性与错误审计
tags:
- Chain-of-Thought
- Reasoning Audit
- Visualization
- Agentic Auditor
- LLM Interpretability
one_liner: 开源大推理模型CoT轨迹分层可视化、自动错误检测与系统盲点分析框架
practical_value: '- 可复用CoT分层拆解思路，对电商推荐/导购Agent的规划推理轨迹做拆分审计，快速定位决策错误环节

  - 借鉴Agentic Auditor设计，在业务Agent中接入工具增强的自动错误校验，降低错误推荐/违规回复概率

  - 参考系统推理画像构建方法，沉淀业务场景下大模型的常见盲区，定向做微调或Prompt工程优化'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
大推理模型生成的超长Chain-of-Thought轨迹核心逻辑被大量过程文本掩盖，推理可解释性差、错误排查成本极高，严重制约推理类Agent的落地优化。

### 方法关键点
1. 将非结构化CoT轨迹结构化分层，拆分高层推理策略与底层执行步骤，支持交互式可视化排查；
2. 构建Agentic Auditor自动识别推理逻辑错误，结合外部工具实现结果增强校验；
3. 生成系统级推理画像，挖掘不同模型的特有推理盲区，支撑定向优化。

### 关键结果
已开源完整框架、LensBench诊断数据集，可作为推理类AI系统的通用调试底座，CoT人工排查效率提升数倍，降低推理类模型优化成本。
