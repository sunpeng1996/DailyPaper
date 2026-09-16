---
title: 'ModularRSI: Modular and Generalizable Recursive Harness Self-Improvement'
title_zh: ModularRSI：可泛化的模块化Agent执行框架递归自进化方法
authors:
- Siwei Wu
- Jincheng Ren
- Yizhi Li
- Haau-Sing Li
- Chengran Yang
- Yuxuan Zhang
- Weicheng Gu
- Jian Yang
- Riza Batista-Navarro
- Chuanyi Zhang
affiliations:
- Beihang University
- University of Manchester
- IQuest Research
- Hohai University
- Langboat
arxiv_id: '2609.14857'
url: https://arxiv.org/abs/2609.14857
pdf_url: https://arxiv.org/pdf/2609.14857
published: '2026-09-13'
collected: '2026-09-16'
category: Agent
direction: Agent执行框架自进化优化
tags:
- Recursive Self-Improvement
- Agent Harness
- Modular Design
- Generalization
- Contrastive Trajectory
one_liner: 提出模块化、基准隔离的Agent执行框架自进化方案，解决通用递归自改进的信用分配难题
practical_value: '- 可将业务Agent的执行逻辑拆分为流程控制、工具调用、上下文管理、观测处理、终止判断5个独立模块，分别迭代优化避免模块间干扰，适配电商导购、客服Agent的迭代场景

  - 同任务成功/失败轨迹对比+跨任务证据聚合的缺陷定位方法，可复用在推荐系统召回/排序策略的badcase归因流程，避免单条轨迹偶发问题的误导

  - 自进化训练数据集与下游评估基准完全隔离的构造思路，可借鉴到搜索推荐策略的离线训练数据构建环节，避免离线涨点线上掉点的过拟合问题

  - 静态校验、泛化性审核、小流量验证三道上线门槛，可直接复用在业务Agent或推荐策略的迭代上线流程，过滤无效修改'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent递归自改进（RSI）方法多直接在下游基准集上优化，易过拟合到基准特有模式；单条轨迹的优化信号易混淆框架系统性缺陷和任务特有细节；整体式Harness优化难以定位问题模块，导致进化后的框架泛化性差，难以迁移到未知任务。

### 方法关键点
- 模块化Harness设计：拆分为Agent Loop、Observation Management、Tool Use、Context Management、Task Completion Detection 5个独立功能模块，每个模块在限定范围内独立进化后再做跨模块冲突整合
- 基准隔离数据集：构造2000个与下游评估基准完全无重叠的可执行进化任务，覆盖终端操作、软件工程等9个领域，从数据层面避免过拟合
- 对比式缺陷定位：同任务多次执行生成的成功/失败轨迹配对，跨任务聚合证据定位可复用的框架共性缺陷，而非任务特有补丁
- 三道校验门：静态程序校验、diff泛化性审核、执行验证，过滤无效或过拟合的修改

### 关键实验
在TerminalBench 2.0、SWE-Bench Verified上测试，对比无进化基线、Meta-Harness、AHE等现有RSI方法：以DeepSeek-V4为backbone时，TerminalBench 2.0准确率从47.57提升到52.43，Pass3从30.34提升到35.96；进化后的框架可跨模型迁移，在GLM-5.2、MiniMax-2.5上均稳定涨点，比现有RSI方法准确率高5pct以上。

最值得记住的一句话：Agent自进化要获得泛化性，核心是模块化拆分问题、用隔离数据集训练、基于跨任务的共性缺陷做优化，而非针对单个任务或基准做补丁式修改。
