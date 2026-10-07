---
title: 'AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents'
title_zh: AutoSciBench：面向科学Agent评估的自主基准生成框架
authors:
- Dongki Kim
- Namkyeong Lee
- Surag Nair
- Carl Edwards
- Xiner Li
- Edward De Brouwer
- Jenna Lynn Collier
- Sung Ju Hwang
- Gabriele Scalia
- Ehsan Hajiramezanali
affiliations:
- Genentech
- KAIST
arxiv_id: '2610.05140'
url: https://arxiv.org/abs/2610.05140
pdf_url: https://arxiv.org/pdf/2610.05140
published: '2026-10-03'
collected: '2026-10-07'
category: Agent
direction: Agent 评测基准自动生成
tags:
- Agent Evaluation
- Benchmark Generation
- Autonomous Agent
- Iterative Refinement
- Scientific Agent
one_liner: 提出可随Agent能力迭代升级的科学领域Agent评测基准自动生成框架AutoSciBench
practical_value: '- 可复用「基于Agent求解轨迹+反馈迭代优化评测集」的思路，解决电商导购/搜索推荐Agent现有评测用例饱和、无法区分高阶能力的问题

  - 借鉴「高层任务概念+低层落地配方」的两级任务定义范式，自动化生成Query理解、多轮导购、广告创意生成Agent的评测case

  - 迭代式基准生成逻辑可直接迁移到A/B测试用例生成环节，持续挖掘现有系统短板，避免测试用例老化失效'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有Agent评测基准极易饱和，科学领域基准构建需大量人力与领域知识，更新速度远跟不上Agent能力迭代，无法有效识别Agent能力短板。

### 方法关键点
1. 采用两级任务定义范式：高层概念指定科学领域、数据模态、推理要求，低层配方明确问题、环境、真值的构建与校验逻辑
2. 基于Agent求解轨迹和裁判反馈迭代修订任务配方，封堵解题捷径，引导任务向原始数据校验、中间结果解读、多证据融合方向升级
3. 蒸馏过往迭代经验指导新任务概念生成，实现基准随Agent能力持续自适应升级

### 关键结果
在计算生物学、材料科学、临床影像三个领域验证，生成的基准相较人工基准分别使Agent求解准确率下降22.4、25.5个百分点，任务质量评分在三个领域均高于人工基准。
