---
title: 'AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model
  Research'
title_zh: AutoWorldModel-Bench：面向自动世界模型研究的以状态为中心的基准
authors:
- Marjan Moodi
- Xuankang Zhu
- Fernando De Mesentier Silva
- Harold Chaput
- Mohammad Reza Taesiri
affiliations:
- Electronic Arts
- Simon Fraser University
arxiv_id: '2608.11216'
url: https://arxiv.org/abs/2608.11216
pdf_url: https://arxiv.org/pdf/2608.11216
published: '2026-07-19'
collected: '2026-08-13'
category: Agent
direction: Agent评测 · 世界模型自主优化
tags:
- Agent Benchmark
- World Model
- Coding Agent
- State Representation
- Autonomous Research
one_liner: 推出面向AI编码Agent自主优化世界模型的闭环基准，支持开放研究场景的Agent能力评估
practical_value: '- 可复用Agent闭环迭代优化框架：将业务模型的starter代码、评估脚本、实验日志标准化，让Coding Agent自主迭代优化推荐/广告模型的结构、损失、超参，替代部分人工调优工作，降低算法工程师重复劳动

  - 可迁移实体结构化状态建模思路：将电商场景的用户、商品、上下文拆分为实体-组件的结构化张量表示，隔离感知噪声，降低多场景动态行为建模的难度，提升长序列预测的一致性

  - 可复用多步长加权评估方案：评估序列推荐、用户行为预测模型时，提升长horizon预测的权重，避免模型仅优化单步拟合效果而忽略长期轨迹合理性，更贴合业务实际需求

  - 业务实验优先级参考：优先测试架构、损失、流程类非超参调整的改动，这类改动的效果ROI显著高于单纯超参调优，和论文中91%获胜改动为研究型修改的结论一致'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI研究Agent的评测基准多聚焦有明确交付要求的工程任务，缺乏开放探索型研究场景的标准化评测方案；同时世界模型领域设计空间复杂（涵盖状态表示、架构、训练目标、滚动策略等）、无统一最优范式，恰好适合作为测试Agent自主研究能力的场景，但现有世界模型基准多耦合感知任务，迭代速度慢，无法支撑Agent的快速闭环实验。
### 方法关键点
- 统一8个游戏环境的实体-组件-系统（ECS）结构化状态表示，将场景元素拆分为实体、属性、规则三类，隔离感知误差，仅保留动力学建模任务，单轮训练仅需10分钟，支持快速迭代
- 设计6小时固定H100算力预算的闭环评测流程：给Agent提供4种主流世界模型starter代码、标准化训练/评估脚本、结构化实验日志，Agent可自主修改代码、运行实验、分析结果迭代优化
- 评估指标采用多horizon加权设计，单步预测权重0.1、10步0.2、20步0.7，重点考核模型开环长序列滚动预测的准确性，同时增设场景规则测试集验证模型对底层逻辑的学习效果
### 关键结果
实验覆盖2款前沿Coding Agent（Codex-5.4、Claude Opus 4.6）、8个游戏、4种starter架构，共64组测试；两款Agent在63组测试中都实现了对starter模型的效果提升，平均测试分提升0.196（满分1）；91%的获胜改动为架构、损失、滚动策略、推理逻辑等研究型修改，而非单纯超参调整；效果提升主要集中在长horizon预测，20步预测准确率平均提升0.215，单步预测仅提升0.056。
### 最值得记住的结论
AI编码Agent已经能在开放的研究场景下自主产出有价值的模型改进，效果远优于单纯的超参搜索方案。
