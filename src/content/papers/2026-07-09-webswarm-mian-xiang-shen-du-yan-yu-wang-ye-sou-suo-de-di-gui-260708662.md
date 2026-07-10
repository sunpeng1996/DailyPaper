---
title: 'WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search'
title_zh: WebSwarm：面向深度广域网页搜索的递归多智能体编排框架
authors:
- Xiaoshuai Song
- Liancheng Zhang
- Kangzhi Zhao
- Yutao Zhu
- Zhongyuan Wang
- Guanting Dong
- Jinghan Yang
- Han Li
- Kun Gai
- Ji-Rong Wen
affiliations:
- Renmin University of China
- Kuaishou Technology
arxiv_id: '2607.08662'
url: https://arxiv.org/abs/2607.08662
pdf_url: https://arxiv.org/pdf/2607.08662
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 多智能体搜索 · 递归编排优化
tags:
- Multi-Agent
- Web Search
- Recursive Orchestration
- LLM Agent
- Information Seeking
one_liner: 提出渐进式递归委托多智能体搜索框架，适配深度、广域及混合复杂信息检索任务
practical_value: '- 复杂搜索类Agent（电商商品调研、竞品分析、用户研究场景）可复用4种搜索模式（atom/deep/wide/entity_collect）的拆分逻辑，按子任务特征匹配协作模式，无需从零设计多智能体分工

  - 大规模平行子任务执行时可借鉴同批次兄弟节点经验迁移机制：先跑少量侦察节点提取有效搜索模式、可靠来源，再批量执行剩余子任务，降低重复试错成本、提升结果一致性

  - 多智能体任务拆分避免仅靠查询语义拆分，可增加轻量Web探测前置步骤，对齐网页信息组织结构再决定拆分维度，实验验证可减少40%+的网页工具调用，不损失精度

  - 电商复杂信息采集（多品牌商品参数爬取、多店铺价格/库存汇总）可直接复用递归委托架构，替代固定规则爬虫，适配网页结构动态变化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
单ReAct风格智能体搜索受限于单轨迹和上下文窗口，无法同时满足复杂信息检索的深度（多跳推理）和广度（多维度覆盖）要求；现有多智能体搜索系统仅做根节点浅层拆分、固定全局协作模式、拆分维度与网页信息结构错位，在深度嵌套的混合搜索任务上表现较差。

### 方法关键点
- 渐进式递归委托框架：每个搜索节点绑定本地目标和对应搜索模式，共4种预设模式：atom（原子事实查询）、deep（多约束迭代验证）、wide（并行分治）、entity_collect（开放集实体召回），节点可自主决定本地求解或继续委托子节点，结果逐层向上反馈聚合
- 网页结构探测模块：轻量检索确认目标信息分布特征（集中在聚合页/按维度分散），指导后续拆分维度，避免无效递归
- 同构节点经验迁移：同父节点的同构子节点先执行少量侦察节点，提取可复用搜索经验（有效query、可靠来源、失败路径），指导剩余子节点求解

### 关键结果
在BrowseComp-Plus、WideSearch、DeepWideSearch、GISA4个基准测试，对比ReAct、Swarm-Agent、InfoSeeker等7个基线，基于GLM-4.5时，相比单智能体ReAct：深度搜索ACC提升17.5个点，广域搜索Row F1提升10.91个点，混合搜索Item F1提升11.77个点；网页探测模块可减少40%左右的网页工具调用，无精度损失。

### 核心结论
多智能体协作不要预先固定全局拓扑，应随证据积累动态递归构建任务树，每个子任务匹配对应协作模式，才能同时适配复杂搜索的深度和广度要求
