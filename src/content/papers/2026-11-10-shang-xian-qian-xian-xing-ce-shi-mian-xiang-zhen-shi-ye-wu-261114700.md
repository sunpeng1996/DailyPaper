---
title: 'Probe What-If Worlds Before You Ship: Persona Simulation for Real-World Decision
  Making'
title_zh: 上线前先行测试：面向真实业务决策的用户Persona仿真框架
authors:
- Julie Zhu
- Jianheng Hou
- Zhixu Silvia Tao
- Shi Bo
- Yilan Fan
- Yixuan He
- Zhiyuan Hu
- Shirley Huang
- Fangyu Liu
- Yijun Wang
affiliations:
- Massachusetts Institute of Technology
- Princeton University
- Harvard University
- MatrAIx
- New York University
arxiv_id: '2611.14700'
url: https://arxiv.org/abs/2611.14700
pdf_url: https://arxiv.org/pdf/2611.14700
published: '2026-11-10'
collected: '2026-11-13'
category: Agent
direction: Agent 用户Persona仿真 业务决策前置验证
tags:
- Persona Simulation
- User Agent
- LLM-based Testing
- What-if Analysis
- Decision Support
one_liner: 提出可复用的LLM驱动Persona仿真框架，支持业务上线前的离线用户反馈测试与决策验证
practical_value: '- 电商/推荐新策略上线前，可基于目标人群属性构建仿真Persona cohort，提前测试不同文案、定价、交互设计的用户反馈，避免上线后对真实流量造成负向影响，降低A/B测试试错成本

  - 可复用论文的三类实验设计范式：固定用户群测试产品变体（SUT）、固定产品测试不同用户群差异（PUT）、交叉设计同时验证两者交互，适配不同业务测试需求

  - 做用户仿真时务必保留完整Persona属性定义，论文实验显示移除Persona信息后，群体差异效应会从Cramér''s V=0.928降至0.063，甚至会反转设计方案的排序结果，严重影响结论可靠性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前产品迭代的真实用户测试存在三大痛点：特殊人群招募成本高、用户属性混杂难以隔离单一变量、未成熟方案上线易损害用户体验，严重拖慢数据驱动决策的效率，亟需可复用的离线仿真方案替代早期测试。

### 方法关键点
- 提出标准化实验设计范式，按用户群（cohort）和测试内容（stimulus）两个维度分为四类：单群单内容描述性评估、固定群测多产品（SUT）、固定产品测多人群（PUT）、交叉设计验证交互效应
- 支持5种用户群抽样策略：参考真实数据分布抽样、对比组均衡抽样、稀有群体过采样、全属性覆盖抽样、压力测试极端抽样，适配不同研究需求
- 工程框架支持多环境（调研、网页、聊天机器人、OS应用）大规模并发仿真，全链路可审计，自动输出跨组统计对比报告

### 关键结果数字
覆盖5个领域12个真实业务案例，跨3款主流LLM对比显示80%以上核心结论方向一致；移除Persona属性后，临床筛查案例的职业与决策的关联度从Cramér's V=0.928降至0.063，合同修订方案的偏好排序直接反转；车助手场景下主动询问用户偏好可将满意度提升18-44个百分点。

最值得记住的一句话：Persona仿真的价值是输出可验证的设计假设、缩小真人测试范围，而非完全替代真实用户的实验证据。
