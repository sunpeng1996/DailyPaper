---
title: 'Answer-Distribution Trajectories: A Stochastic-Dynamics View of LLM Reasoning'
title_zh: 答案分布轨迹：从随机动力学视角理解大语言模型推理
authors:
- Mar Gonzàlez I Català
- Haitz Sáez de Ocáriz Borde
- Davide Murari
- Carola-Bibiane Schönlieb
- Pietro Liò
- George Montañez
affiliations:
- University of Cambridge
- Harvey Mudd College
arxiv_id: '2609.09030'
url: https://arxiv.org/abs/2609.09030
pdf_url: https://arxiv.org/pdf/2609.09030
published: '2026-09-08'
collected: '2026-09-09'
category: Reasoning
direction: 大模型推理 · 动力学表征
tags:
- LLM Reasoning
- Chain-of-Thought
- Stochastic Dynamics
- Reasoning Evaluation
- Dynamical Profile
one_liner: 提出比端点准确率、熵轮廓更细的答案分布轨迹表征，可分析LLM推理动力学机制
practical_value: '- 对Agent多步推理任务，可借鉴答案分布轨迹的探索/修正/移动/承诺4维度设计提前终止策略，避免overthinking，降低推理时延

  - 电商场景LLM生成文案/选品的推理过程监控，可通过成败机制分类定位错误根因，优化prompt或微调策略

  - 基于CoT的RAG系统，可通过监测候选答案的概率漂移动态调整召回chunk，提升输出一致性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有CoT推理仅靠端点准确率评估，忽略推理路径；熵轮廓仅能跟踪不确定性变化，无法识别具体哪些候选假设承载了概率质量，无法区分相同准确率/熵轮廓下的不同推理动力学机制。

### 方法关键点
- 定义答案分布轨迹：在CoT生成的每个前缀节点，通过Monte Carlo采样多条后续推理路径，统计各候选最终答案的概率分布序列
- 设计4维推理动力学轮廓指标：探索（有效候选数）、修正（主导答案切换/回溯次数）、移动（分布变化幅度与直接性）、承诺（分布收敛到稳定答案的时机）
- 划分8类推理成败机制：成功类含稳定成功、救援、迂回成功、脆弱成功，失败类含未发现、逃逸、救援失败、随机遗漏

### 关键结果
在GSM8K、ARC、SVAMP、MATH 4个推理基准、16个开源LLM上验证：
1. 相同准确率的模型，推理成功/失败机制占比差异可达30%以上
2. 熵轮廓RMSE小于0.2的相似轨迹，主导答案、黄金答案占比、成败机制的disagreement最高可达40%
3. 指令微调可使平均有效候选数降低0.83个标准差，主导答案切换频率降低0.68个标准差，推理准确率显著提升

### 核心结论
没有普适最优的推理动力学轮廓，高准确率要求窄分布、少切换、早收敛，而低时延要求则相反
