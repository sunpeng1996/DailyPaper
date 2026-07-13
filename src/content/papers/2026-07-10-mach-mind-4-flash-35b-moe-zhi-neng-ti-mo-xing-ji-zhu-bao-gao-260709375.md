---
title: Mach-Mind-4-Flash Technical Report
title_zh: Mach-Mind-4-Flash 35B MoE 智能体模型技术报告
authors:
- Foundation Model Team
affiliations:
- Li Auto Inc.
arxiv_id: '2607.09375'
url: https://arxiv.org/abs/2607.09375
pdf_url: https://arxiv.org/pdf/2607.09375
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent大模型 训练后优化与效率提升
tags:
- MoE
- RL
- On-Policy Distillation
- Agent
- Token Efficiency
- MOPD
one_liner: 35B参MoE智能体（仅激活3B参）通过训练后优化，性能追平10~30倍激活规模的大模型
practical_value: '- 可复用「分域RL专家训练+MOPD蒸馏融合」的训练流程，避免混合多奖励RL的能力跷跷板问题，适合电商多场景（推荐、搜索、客服）Agent的能力整合，无需重新训练全量模型即可快速新增场景能力

  - 直接复用HMPO长度压缩方案，用正确推理链的中位数做自适应长度预算，乘法奖励保证正确率优先，可用来压缩推荐理由、客服回复、搜索摘要的生成长度，降低推理成本的同时精度损失≤0.7pp

  - 参考统一RL/OPD训练基础设施的设计，用加权损失动态切换训练模式，减少多任务训练的工程复杂度，适合中小团队快速迭代多能力Agent，无需维护多套训练框架

  - 借鉴Agent训练的EnvScaling思路，不用静态标注轨迹，直接规模化构建可验证交互环境生成训练数据，适合电商导购Agent、工具调用Agent的训练，大幅降低数据标注成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型参数缩放带来的推理成本过高，latency敏感的生产场景（如电商实时推荐、端侧Agent）无法落地万亿参大模型；传统混合多奖励RL训练通用Agent易出现能力跷跷板，某领域提升伴随其他领域效果下降；强推理模型普遍存在“过度思考”问题，冗余推理链大幅提升服务成本。

### 方法关键点
- 基础设施层：统一RL/OPD训练范式，通过加权损失动态切换纯RL、纯蒸馏、联合训练3种模式，算子层集成SonicMoE内核+共享专家分段融合策略，端到端训练提速17%
- 训练流程层：采用「先专精再融合」pipeline，先并行训练推理、通用、Agent三大赛道的多个领域RL专家，再通过MOPD路由每个样本到对应专家蒸馏，彻底解决能力跷跷板问题
- 效率优化层：最后用HMPO做token效率优化，基于正确推理链的中位数生成自适应长度预算，乘法奖励强制正确率优先，从机制上避免短但错误的输出

### 关键结果
模型总参35B MoE，仅激活3B参，在AIME'26得分92.70、IFBench得分82.82、Behavioral-SafetyBench得分80.74、BrowseComp-zh得分72.31、ClawBench得分84.20，性能追平甚至超过10~30倍激活规模的大模型；HMPO可将推理链长度压缩19~46%，精度损失≤0.7pp。

### 核心结论
无需盲目缩放预训练参数量，通过高效的训练后优化流程，小参数激活的MoE模型完全可以达到百亿甚至千亿参大模型的性能，同时推理成本降低一个数量级以上。
