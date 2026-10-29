---
title: 'CausGround: Causal Interaction Grounding for Adaptive Embodied Planning'
title_zh: CausGround：面向自适应具身规划的因果交互接地框架
authors:
- Yijun Shen
- Diqi He
- Jinbang Guo
- Wanyue Zhang
- Jiaming Mi
- Huan Yang
- Zhongyuan Wang
- Zhiwei Yu
- Kai Zhang
affiliations:
- East China Normal University
- Beijing Academy of Artificial Intelligence (BAAI)
- Northwestern Polytechnical University
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2610.29702'
url: https://arxiv.org/abs/2610.29702
pdf_url: https://arxiv.org/pdf/2610.29702
published: '2026-10-20'
collected: '2026-10-29'
category: Agent
direction: 具身Agent · 因果交互规划
tags:
- Embodied Agent
- Causal Reasoning
- MLLM
- Planning
- Non-parametric
one_liner: 无需更新模型参数的因果交互接地框架 大幅提升多场景MLLM具身规划表现
practical_value: '- 可借鉴非参数因果知识蒸馏思路，将电商导购Agent、客服Agent的多轮交互经验，蒸馏为动作前置条件+效果的规则库，无需频繁微调LLM即可提升多步任务完成率，降低新场景适配成本

  - 因子化世界状态表示可迁移到推荐系统上下文建模，同时存储用户状态（购买力、偏好标签）、物品状态（库存、活动规则）、两者匹配关系，提升凑单、分期引导等多步推荐的合理性

  - 目标驱动的双向因果推理逻辑可用于任务型推荐/对话规划，从用户最终目标反向推导前置步骤，正向预判每步操作结果，减少无效交互，例如退换货、售后咨询场景下可自动补齐必要步骤'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
MLLM具备较强通用推理能力，但落地具身交互场景时，无法掌握环境专属的动作可执行前置条件、执行后状态变化规则，长序列规划时易出现前置条件遗漏、无效动作重复等问题；现有适配方案要么需要高成本的环境专属微调，要么依赖难以跨任务复用的非结构化交互经验，泛化性差。

### 方法关键点
1. 定义统一的因子化世界状态表示，同时包含物体属性键值对、物体间显式关系，作为观测解析和因果知识存储的共享接口
2. 从交互轨迹中蒸馏动作中心的因果知识，拆分通用动作规则和实例专属规则，存储每个动作的可执行前置条件、执行后状态变化，自动关联跨动作的因果依赖形成可复用知识库
3. 规划阶段基于当前任务和观测，通过目标反向推理+语义检索构建任务专属因果子图，给冻结的MLLM规划器提供结构化参考，全程无需更新模型参数

### 关键结果
在VirtualHome、RoboCasa模拟规划基准，SWITCH真实交互推理基准、真实机器人操控任务上验证，对比Vanilla、SelfReVision、LookPlanGraph等基线：VirtualHome平均任务成功率从24.9%提升到53.3%，RoboCasa闭环规划成功率从43.0%提升到57.0%，SWITCH交互推理准确率从25.8%提升到31.9%，增益覆盖不同参数规模、不同模型家族的MLLM backbone。

最值得记住的一句话：无需微调LLM参数，只需将交互经验蒸馏为可复用的动作因果规则库，就能系统性提升长序列规划的鲁棒性，可跨场景、跨模型迁移。
