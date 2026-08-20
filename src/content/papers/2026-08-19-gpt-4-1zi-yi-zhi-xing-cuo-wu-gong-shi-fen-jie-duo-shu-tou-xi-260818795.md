---
title: 'Decomposing Wrong-Consensus Agreement in LLM Self-Consistency: A GPT-4.1 Case
  Study'
title_zh: GPT-4.1自一致性错误共识分解：多数投票失效原因定量分析
authors:
- Lizhuo Zhang
- Mengmeng Tang
- Chenfeng Long
- Xiaoyong Tang
- Xiang Luo
affiliations:
- Hunan Agricultural University
- Yuelushan Laboratory
- Changsha University of Science and Technology
- China Guangdong Tobacco Meizhou Ltd
arxiv_id: '2608.18795'
url: https://arxiv.org/abs/2608.18795
pdf_url: https://arxiv.org/pdf/2608.18795
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: LLM推理 · 自一致性可靠性评估
tags:
- Self-Consistency
- Majority Voting
- Uncertainty Estimation
- Error Decomposition
- GPT-4.1
one_liner: 定量拆分LLM自一致性错误共识的两类归因，给出不同任务下共识可靠性边界
practical_value: '- 用LLM做Agent推理、搜索Query理解、商品属性识别的多数投票时，不要盲目信任高共识：选择题类任务80%+错误共识来自问题本身的迷惑选项，开放域任务仍有20%-40%错误共识无法通过偏好解释，需额外搭配RAG校验

  - 做LLM输出置信度评估时，硬投票的共识占比和软加权的概率平方和的AUROC几乎无差异，无需做复杂软聚合，直接用硬投票共识占比做置信度即可，降低工程复杂度

  - 对高难度LLM任务（比如复杂用户需求解析、非标商品属性识别），多数投票反而会降低准确率，不要无脑加采样次数，建议搭配难度预判模块，硬任务直接走人工校验或RAG增强

  - 开放域生成场景的一致性校验中，即使共识度≥0.84，两次独立采样结果仍有78%概率不一致，不要把单次投票共识作为输出稳定性的判断依据，建议多轮采样交叉校验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM自一致性多数投票被广泛用于提升推理、生成任务的准确率，但在高难度任务上反而会失效，甚至出现多轮采样均指向错误答案的错误共识现象，此前无定量归因框架拆解错误共识来源，无法指导投票策略优化。

### 方法关键点
- 定义归一化错误共识指数Γ，衡量错误共识下采样结果的聚类程度，提出机械覆盖率ϕ，定量拆分错误共识的两类来源：per-case选项偏好（如题目本身的迷惑选项）、偏好无法解释的残差（如模型训练带来的共享偏差）
- 构建无泄漏的反事实模拟框架，每个case的偏好和准确率从其他轮次采样结果估计，避免数据泄漏
- 对比多层级反事实基线：均匀独立采样、单case偏好独立采样、运行级偏好异质性采样

### 关键结果
实验基于公开的GPT-4.1系列在GPQA-Diamond（4选1选择题）、AIME（开放域数学题）上的多轮采样数据，每case采样50次：
- GPQA上ϕ达80.6%-92.7%，80%+的错误共识可被per-case选项偏好解释；AIME上ϕ仅58.6%-78.1%，22%-41%的错误共识属于无法解释的残差
- 高难度任务下多数投票准确率比单采样低最多0.09；最高共识组的准确率仅0.42-0.83，仅比单采样提升1.2-3.6倍，共识仅为分级证据而非正确性保证

> 最值得记住的结论：LLM自一致性投票的高共识不等于高正确性，约束类任务的错误共识大多来自问题本身的设计，开放域任务的错误共识有近四成来自模型自身的共享偏差。
