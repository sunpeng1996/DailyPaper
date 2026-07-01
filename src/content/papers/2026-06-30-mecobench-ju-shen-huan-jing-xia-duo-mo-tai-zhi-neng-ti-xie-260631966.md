---
title: 'MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied
  Environments'
title_zh: MECoBench：具身环境下多模态智能体协作的系统性研究
authors:
- Qingyun Liu
- Jiwen Zhang
- Jingyi Hu
- Siyuan Wang
- Zhongyu Wei
affiliations:
- Fudan University
- Shanghai Innovation Institute
- The Chinese University of Hong Kong
arxiv_id: '2606.31966'
url: https://arxiv.org/abs/2606.31966
pdf_url: https://arxiv.org/pdf/2606.31966
published: '2026-06-30'
collected: '2026-07-01'
category: MultiAgent
direction: 多模态具身多智能体协作评测
tags:
- MultiAgent
- Embodied AI
- MLLM
- Benchmark
- Collaboration
one_liner: 推出具身多模态智能体协作基准MECoBench，揭示协作效果的核心影响规律
practical_value: '- 多智能体团队规模选择可参考倒U型规律，中等规模（2-3个Agent）可平衡并行收益和协调 overhead，复杂任务下可适当扩大团队提升鲁棒性，可直接复用在电商内容生成、用户运营多Agent系统的人力分配上

  - 协作模式选型可参考结论：小团队用中心化Leader模式降低空间/任务冲突，大团队用去中心化广播模式避免Leader单点瓶颈；弱模型优先用结构化协作流程，强模型可简化协作机制，可迁移到电商客服、活动运营多Agent系统的架构设计

  - 沟通机制可优化：优先用动作级指令而非粗粒度任务分配提升执行效率；并行任务可引入共享内存替代文本沟通降低30%+ Token成本，顺序强依赖任务保留文本通信保证对齐，可直接用在Agent交互协议设计中

  - 鲁棒性优化可参考：多Agent协作可抵消噪声信息、错误先验的负面影响，在信息不确定的推荐场景（如用户兴趣模糊、商品信息不全）可引入多Agent交叉验证提升效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多模态大语言模型（MLLM）作为具身智能体的基础能力已得到验证，但视觉落地的具身环境下多智能体协作机制缺乏系统性研究。现有多智能体基准多基于纯文本输入或预定义符号状态，无法覆盖感知、探索、通信、协调深度耦合的真实协作场景，难以量化不同协作模式的实际收益与瓶颈。
### 方法关键点
- 构建MECoBench基准：基于VirtualHome家居模拟器，覆盖8类真实生活任务，支持并行（空间共享独立执行）、顺序（空间隔离需物品传递）两类协作结构，共192个测试用例
- 评测平台支持3类协作模式：无通信隔离模式、去中心化广播/讨论模式、中心化Leader调度模式，同时支持文本通信、共享内存、视觉增强Leader三类通信机制
- 设计多维度评测指标：覆盖有效性（SR成功率、CR完成率）、效率（Step-CR AUC、单步Token成本）、协作质量（分工度、冲突率、交接失败率）三个维度
### 关键结果
- 覆盖13款主流闭源/开源MLLM测试，团队规模缩放符合倒U型规律：2Agent相比单Agent平均SR提升4.4~16.5pct，超过3Agent后性能随协调成本上升下降；复杂任务下多Agent比单Agent SR高10pct以上
- 移除通信会导致平均SR下降9.2pct，大团队/顺序任务下降可达21pct；小团队用中心化模式SR比去中心化高3.1pct，4Agent以上去中心化模式反超4.2pct
- 噪声先验下2Agent相比单Agent的SR增益最高可达28.8%，远高于干净信息下的收益

> 最值得记住：多智能体协作的收益核心取决于并行增益与协调成本的平衡，无通用最优协作模式，需结合团队规模、模型能力、任务依赖特性灵活选择。
