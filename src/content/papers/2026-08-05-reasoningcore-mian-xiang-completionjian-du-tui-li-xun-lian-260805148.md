---
title: 'Reasoning Core: Designing Broad Procedural Data for Completion-Supervised
  Reasoning Training'
title_zh: ReasoningCore：面向Completion监督推理训练的通用程序式数据集设计
authors:
- Damien Sileo
- Valentin Lacombe
- Dimitri Kachler
affiliations:
- Univ. Lille
- Inria
- CNRS
- Centrale Lille
- CRIStAL
arxiv_id: '2608.05148'
url: https://arxiv.org/abs/2608.05148
pdf_url: https://arxiv.org/pdf/2608.05148
published: '2026-08-05'
collected: '2026-08-06'
category: Reasoning
direction: LLM推理训练 · 程序式数据生成
tags:
- Procedural Data
- Reasoning Training
- SFT
- RL
- Synthetic Dataset
- LLM Reasoning
one_liner: 开源覆盖9大领域的50个程序式推理数据生成器，适配SFT与RL训练，推理性能优于现有同类数据集
practical_value: '- 电商/导购Agent的域内推理SFT训练可复用本文设计思路：生成可验证的结构化样本（如优惠规则计算、订单状态跟踪类任务），采用紧凑答案代替冗余思考链，相同token预算下训练效率提升显著

  - 搜索推荐场景下生成式训练数据的质量校验可参考本文审计流程：小模型初筛+人工抽检+回归测试三层校验，快速定位prompt、答案、打分逻辑不一致的脏数据，降低训练噪声

  - 跨SFT/RL两阶段训练的Agent系统可复用本文统一接口设计，同一套生成器同时适配两个阶段的训练需求，减少数据适配开发成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有程序式推理数据集多面向RL场景设计，针对Completion监督SFT场景的适配优化不足，且普遍存在生成逻辑、渲染格式、目标答案、打分规则不匹配的隐性缺陷，同时缺乏统一的任务接口和难度控制机制，难以高效转化为SFT阶段的推理能力增益。

### 方法关键点
- 开源REASONINGCORE资源，包含覆盖数学、逻辑、规划、代码、因果推断等9大领域的50个程序式数据生成器，原生支持语义打分、难度动态调节、任务自动评估，同时适配SFT和RL训练需求
- 针对SFT场景做定向优化：采用紧凑规范化的答案格式代替冗长的 step-by-step 思考链，相同token预算下可覆盖更多独立样本；训练阶段使用唯一标准答案做监督，评估阶段接受所有语义等价的答案
- 提出全链路数据集审计方案：通过大模型辅助审查、人工裁定、回归测试三层校验，系统性排查生成、渲染、目标、打分四个环节的一致性问题

### 关键结果
在135M~3B共4个基座模型上与PROCEDURALWARMUP、REASONINGGYM、SYNLOGIC三类同类数据集做对比实验：3B模型SFT训练后，REASONINGCORE在DROP F1、LogiQA Acc、ARC-Challenge Acc上分别达到41.7、47.8、51.3，全面优于无程序式数据的基线及其他三个对比数据集，同时无通用能力遗忘问题；RL训练场景下，基于REASONINGCORE训练的Qwen2.5-3B在BBH-test上准确率比REASONINGGYM高15.5个百分点。

### 核心结论
程序式生成的数据并非天然正确，面向训练目标优化答案格式、做好全链路一致性校验，比单纯扩大任务覆盖度更能提升训练效率。
