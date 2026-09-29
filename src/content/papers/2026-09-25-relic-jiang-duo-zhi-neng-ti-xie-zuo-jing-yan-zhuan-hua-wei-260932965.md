---
title: 'Relic: From Multi-Agent Collaboration to Persistent Organizational Capability'
title_zh: Relic：将多智能体协作经验转化为持久组织能力的框架
authors:
- Hongyi Du
- Tianyi Zhang
- Weijia Zhang
- Yi Yang
- Haofei Yu
- Kunlun Zhu
- Tianxiang Dai
- Shang Jiang
- Zhelun Gao
- Jiaxin Pei
affiliations:
- University of Illinois Urbana-Champaign
- Harvey Mudd College
- Yale University
- Stanford University
- Peking University
arxiv_id: '2609.32965'
url: https://arxiv.org/abs/2609.32965
pdf_url: https://arxiv.org/pdf/2609.32965
published: '2026-09-25'
collected: '2026-09-29'
category: MultiAgent
direction: 多智能体协作 · 持久组织能力构建
tags:
- MultiAgent
- Organizational Capability
- Protocol Learning
- Agent Collaboration
- LLM Agent
one_liner: 提出可自治生成、运行时绑定的多智能体组织协议框架，解决成员更替下协作经验无法复用的问题
practical_value: '- 电商多Agent链路（内容生成/审核/投放）可复用协议自治生成逻辑，将反复出现的协同摩擦（如素材不合规回退）转化为可执行触发规则，绑定任务调度层自动执行，减少人工干预

  - 多Agent团队成员/模型更替时，将历史协作规则以可执行协议而非纯文本prompt留存，实测比纯文本规则提升6.5pp行为正确率，适合规模化多Agent运维

  - 推荐/广告跨模块协同场景（如召回策略变更需对齐排序特征）可借鉴运行时绑定逻辑，自动触发校验、责任分配、证据留存，避免线上协作冲突'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent协作依赖临时对话或手动定义工作流，协作经验仅留存于成员本地记忆或历史对话中，一旦出现成员更替、场景迁移，已沉淀的协同规则会完全失效，反复出现相同协作故障（如多Agent开发时接口变更未同步导致下游报错），无法形成持久的组织级能力。

### 方法关键点
- 三级状态分离架构：拆分成员本地状态（私有记忆、工作区）、共享工作状态（代码、文档、任务）、协议状态（可执行规则、角色映射），协议状态完全独立于成员存在
- 自治协议生命周期：Agent从重复协作摩擦中自动生成规则提案，经校验审批后编译为运行时绑定协议，支持后续修订、退役
- 结构化决策层（SDL）将协议规则转化为动作选择权重因子，自动调整Agent动作优先级、分配责任、校验工作产物，无需修改LLM参数

### 关键结果
- 360组受控实验（覆盖10个软件生产任务、3款大模型）：对比无协议的结构化多Agent团队，完整合约交付率从14.06%提升至19.76%（+5.71pp）
- 新成员迁移场景：无继承协议时行为正确率25.4%，纯文本规则34.6%，可执行绑定规则41.2%，较纯文本规则高6.5pp
- CooperBench基准测试取得76.9%成功率，为当前peer结构系统最优效果，反转了多Agent协作的「协调诅咒」问题

### 核心结论
多Agent系统的能力不仅来自单个Agent的推理能力，更来自独立于成员的、可沉淀可复用的组织级规则层，运行时绑定的可执行规则比纯文本提示的经验复用效率高30%以上
