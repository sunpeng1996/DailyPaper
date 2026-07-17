---
title: 'ANet Patu-1: The Value of Connection in the Agent Network'
title_zh: ANet Patu-1：Agent网络连接价值与自组织共识协议
authors:
- Mu Yuan
- Jinke Song
- Zhaomeng Zhou
- Lan Zhang
affiliations:
- Agent Network Research
- The Chinese University of Hong Kong
- The Hong Kong University of Science and Technology
- University of Science and Technology of China
arxiv_id: '2607.15053'
url: https://arxiv.org/abs/2607.15053
pdf_url: https://arxiv.org/pdf/2607.15053
published: '2026-07-16'
collected: '2026-07-17'
category: MultiAgent
direction: 多Agent协作 · 网络价值缩放协议
tags:
- Multi-Agent Collaboration
- Self-Organization
- Consensus Protocol
- Collective Intelligence
- Network Value Law
one_liner: 提出Agent网络三类价值缩放定律，及实现指数级价值的自组织协议ANet Patu-1，验证异构众智胜强单模规律
practical_value: '- 多Agent协作系统可直接复用「能力加权共识+自主选组+动态重组」架构，替代传统中心化调度，适配电商大促预案生成、多场景推荐策略协同等复杂任务

  - 预算有限的场景优先选择小模型+异构能力配置的Agent集群，而非堆强模型副本，n≥3时效果即可超过强同质集群，可大幅降低推荐/广告多Agent系统推理成本

  - 可复用论文提出的6维度协议质量评分体系（价值缩放、自适应拆分、自组织、无瓶颈、O(1)轮次、收敛性），量化评估自有多Agent系统的协作效率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
单Agent大模型缩放的边际成本持续走高，未来海量异构Agent（不同基座、工具、专业能力）的协作将成为AI落地核心形态，但当前缺乏可量化的Agent网络价值评估框架，且现有中心化、固定拓扑的多Agent方案普遍存在价值天花板，无法最大化连接的协同价值。

### 方法关键点
- 借鉴互联网三类价值定律（Sarnoff线性V∝N、Metcalfe平方V∝N²、Reed指数V∝2ᴺ），推导最优协作协议需满足6个核心属性：可组建子网络、自适应任务拆分、自组织选组、无单点瓶颈、O(1)并行轮次、可共识收敛
- 设计ANet Patu-1协议：无固定拓扑，每轮执行「合并产物→代表共识决策（交付/拆分新任务）→Agent按能力affinity自主选组→并行执行子任务」的流程，共识采用能力加权评分而非投票，轮次复杂度不随Agent数量增长

### 关键实验
对比基线为同质强模型（GPT-5.6）集群、中心化调度/黑板模式/投票制等现有多Agent协议：
- 异构GPT-4o-mini集群单Agent的协议质量评分Q仅0.3，n≈2.6时就超过同质GPT-5.6集群的Q均值0.54，n=6时达到Q=1的最优值，进入Reed指数价值区间
- 仅10个异构Agent即可在无任何提示的情况下自主推导还原出ANet Patu-1协议本身
- 协作迭代2-3轮即可收敛，无振荡

最值得记住的结论：Agent网络的价值核心是连接的多样性，而非单个节点的强度，超过极小阈值后，低成本异构Agent集群的价值即可超过强模型同质副本集群。
