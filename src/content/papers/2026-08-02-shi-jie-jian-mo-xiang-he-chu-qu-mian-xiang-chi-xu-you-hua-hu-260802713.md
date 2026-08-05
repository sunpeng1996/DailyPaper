---
title: Quo Vadis, World Modeling?
title_zh: 世界建模向何处去：面向持续优化Agent的交互式世界代理
authors:
- Yu Yang
- Xuemeng Yang
- Licheng Wen
- Lingdong Kong
- Xiaobin Hu
- Dongyue Lu
- Wei Chow
- Xiyan Huang
- Yuxiang Feng
- Yue Liao
affiliations:
- 上海人工智能实验室
- 浙江大学
- 新加坡国立大学
arxiv_id: '2608.02713'
url: https://arxiv.org/abs/2608.02713
pdf_url: https://arxiv.org/pdf/2608.02713
published: '2026-08-02'
collected: '2026-08-05'
category: Agent
direction: Agent 持续进化 · 世界代理框架
tags:
- World_Model
- World_Proxy
- Agent_Evolution
- Continual_Learning
- Interactive_Agent
one_liner: 将传统世界建模范式升级为面向Agent的6类功能3级赋能的交互式世界代理框架
practical_value: '- 搭建业务Agent低成本试错代理：参考6类世界代理划分，针对电商导购、广告投放、活动运营类Agent，优先搭建执行代理（模拟API调用/页面交互结果）、记忆代理（检索历史成功/失败案例）、验证代理（判断策略合规性/风险），替代高成本的真实用户/平台交互，降低试错的流量损失与合规风险

  - 分阶段落地Agent迭代：初期优先落地L1推理时指导，比如给选品Agent检索同类目历史爆款特征、给优惠券发放Agent模拟不同面额的转化效果，不改动现有Agent逻辑即可快速提升效果；成熟后升级为L2训练优化，用代理生成的大量仿真轨迹做SFT/PPO微调，降低真实样本采集成本；长期可探索L3协同进化，用真实线上反馈同步更新代理与Agent策略

  - 调整世界代理评估优先级：无需过度追求代理输出拟真度，优先评估代理反馈是否能提升Agent决策准确率、降低真实交互成本，与传统精度/拟真度指标形成互补'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
持续进化的Agent需要动态交互反馈突破静态训练的分布限制，但真实环境交互存在成本高、风险不可逆、反馈滞后、难并行四大瓶颈；传统世界模型仅聚焦物理状态预测，无法覆盖Agent对执行结果、经验检索、验证信号等多元可落地反馈的需求，亟需重构世界建模的核心范式。
### 方法关键点
- 范式重构：将传统以环境为中心的物理状态转换预测，升级为以Agent为中心的信息转换预测，提出Agent-Centric Interactive World Proxies统一概念
- 6类功能划分：按反馈模态将世界代理分为6种形式：动力学代理（预测环境状态变化）、空间代理（生成不同视角观测）、执行代理（模拟数字操作结果）、记忆/经验代理（检索历史交互案例）、技能代理（推荐可复用行为策略）、奖励/验证代理（评估行为合规性与效果）
- 3级赋能层级：按对Agent的价值从低到高分为三层：L1推理时指导（补充上下文优化当前决策，无模型更新）、L2训练时优化（提供奖励/仿真轨迹等训练信号，更新Agent策略）、L3 Agent-代理协同进化（用真实环境反馈同步更新代理与Agent，实现持续迭代）
### 说明
该工作是世界建模领域的范式重构综述，无具体实验数据，系统梳理了各功能、各层级的现有代表性工作，明确了未来研究方向。
### 核心结论
未来世界模型的核心价值不再由生成内容的拟真度决定，而是由其对Agent决策质量、学习效率、持续进化能力的提升效果决定
