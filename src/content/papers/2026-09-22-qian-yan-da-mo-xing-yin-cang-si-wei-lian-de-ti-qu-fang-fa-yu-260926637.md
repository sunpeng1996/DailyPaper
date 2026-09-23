---
title: 'Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought
  in Frontier Models'
title_zh: 前沿大模型隐藏思维链的提取方法与推理特征分析
authors:
- Xiaoyu Luo
- Tao Ren
- Wenrui Yu
- Xiao Li
- Qiongxiu Li
- Johannes Bjerva
affiliations:
- Aalborg University
- Seafill
arxiv_id: '2609.26637'
url: https://arxiv.org/abs/2609.26637
pdf_url: https://arxiv.org/pdf/2609.26637
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: 大模型推理 · 隐藏思维链提取
tags:
- Chain-of-Thought
- Reasoning Extraction
- Closed-source LLM
- GPT-6 Astra
- Reasoning Efficiency
one_liner: 通过强制工具调用协议提取闭源大模型隐藏思维链，揭示不同前沿模型的推理效率差异
practical_value: '- 搭建电商/广告场景Agent决策系统时，可复用强制工具调用协议落盘LLM中间推理过程，无需依赖模型原生reasoning block即可实现bad
  case可追溯，降低问题排查成本

  - 训练场景专用小模型做推理蒸馏时，不要直接使用GPT-6 Astra等强模型的紧凑推理链作为训练数据，需先补全其隐含的基础步骤，否则小模型无法理解上下文，蒸馏性能会明显下降

  - 优化Agent推理响应速度时，可参考Astra的推理模式：将规则类、基础计算类步骤做内部处理不输出，仅对外暴露关键决策节点，可大幅降低推理链token消耗，提升接口响应速度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前闭源前沿大模型的原生CoT通常不对外暴露，仅靠benchmark准确率只能获知模型的解题能力，无法对比不同模型的推理过程差异，也无法验证答案是否来自合理推理，给需要可追溯决策的落地场景（如Agent合规决策、复杂权益核算）带来障碍。

### 方法关键点
- 设计**FORCED-REASONING**协议：仅通过标准API注册无实际计算功能的推理记录工具，强制模型首次调用该工具记录中间推理，后续自动选择工具调用或输出最终答案，全程无需访问模型内部
- 先在开源模型（DeepSeek-V4-Flash、GLM-5.2）上验证提取的推理链与原生CoT的性能、词汇、结构一致性，再迁移到闭源模型做跨模型推理特征对比
- 从长度/压缩率、局部推理粒度、全局推理树结构、跨模型推理链可迁移性四个维度量化分析不同模型的推理特征

### 关键结果
- 数据集：80道竞赛数学题MATH、100道代码题LiveCodeBench、100道跨学科题Humanity's Last Exam
- 对比baseline：原生推理高努力模式、原生推理关闭无工具模式
- 核心数字：提取的推理链在开源模型上达到接近原生CoT的性能，比无推理基线准确率高40%+；GPT-6 Astra的推理链长度仅为Claude Opus 4.8的28%，压缩率最低（冗余最少），推理树节点数仅为Claude Sonnet 5的20%，路径更线性少分支；弱模型使用Astra的紧凑推理链时准确率损失可达20%以上，同级别强模型使用时几乎无性能损失

**最值得记住的一句话**：推理链的监督价值不是内在固有，而是取决于使用它的模型能力，强模型输出的高密紧凑推理链反而不适合弱小模型做蒸馏训练。
