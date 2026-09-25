---
title: Coding Agents for Generalized Task and Motion Planning Problems
title_zh: 面向通用任务与运动规划问题的编码智能体
authors:
- Matteo Merler
- Bowen Li
- Josh Roy
- Yichao Liang
- Qianwei Wang
- Yixuan Huang
- Tom Silver
affiliations:
- Princeton University
- Fondazione Bruno Kessler
- Carnegie Mellon University
- University of Cambridge
arxiv_id: '2609.30233'
url: https://arxiv.org/abs/2609.30233
pdf_url: https://arxiv.org/pdf/2609.30233
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 通用任务运动规划优化
tags:
- CodingAgent
- TAMP
- GeneralizedPlanning
- LLM4Robotics
- ProgramSynthesis
one_liner: 验证现成编码智能体无需人工设计TAMP组件即可生成优于手工规划器的通用可执行策略
practical_value: '- 可借鉴编码智能体「交互-测试-迭代」闭环，用于生成电商场景可复用规则型策略（如大促活动规则、用户权益发放逻辑），替代人工开发降低维护成本

  - 智能体自主挖掘边缘case校准模型的思路，可迁移到推荐/搜索badcase治理：让Agent自动构造异常query/用户特征样本，测试召回排序逻辑，自动迭代优化

  - 训练阶段用LLM生成可执行程序、推理阶段冻结程序无LLM调用的架构，可大幅降低推理成本，适配推荐/广告低延迟高吞吐的业务要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
通用任务与运动规划（TAMP）需同时处理离散决策与几何、运动学、动力学约束，现有方法依赖大量TAMP领域专属人工工程，落地门槛极高，亟需探索无领域定制的通用解法。
### 方法关键点
- 采用现成编码智能体（Claude Code搭载Opus 5、Codex搭载GPT-5.6 Sol/GPT-6 Astra），仅提供任务描述与模拟器访问权限，无任何人工设计的TAMP谓词、采样器、技能组件
- 智能体在固定合成预算内自主选择交互方式、编写测试代码探测环境、迭代优化生成通用程序，测试阶段完全冻结程序，无LLM调用
- 额外设置环境源码访问对照组，验证源码信息对合成效果的增益
### 关键实验
覆盖28个TAMP模拟环境（含KinDER、PDDLStream基准），共生成980个程序，每个程序在100个未见过的实例上评估，总98000个评估episode。核心结果：3种智能体配置均优于手工规划器、单次生成、非Agent式LLM规划基线，其中GPT-6 Astra版Codex平均成功率95%，手工规划器仅47%；推理时单实例计算量比规划器低一个数量级，物体数量增长时成功率稳定性远超手工规划器。
### 核心结论
编码智能体无需领域定制组件，仅通过自主交互探测就能挖掘环境规律，生成高效的泛化策略，是通用规划类任务的强基线。
