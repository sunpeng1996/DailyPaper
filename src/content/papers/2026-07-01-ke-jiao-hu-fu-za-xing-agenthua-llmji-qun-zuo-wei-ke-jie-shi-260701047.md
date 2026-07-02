---
title: 'Conversable Complexity: Agentic LLM Collectives as Interpretable Substrates'
title_zh: 《可交互复杂性：Agent化LLM集群作为可解释的人工生命基底》
authors:
- Elias Najarro
- Ane Espeseth
- Eleni Nisioti
- Sebastian Risi
- Stefano Nichele
affiliations:
- IT University of Copenhagen
- University of Oslo
- Østfold University of Applied Sciences
- Sakana AI
arxiv_id: '2607.01047'
url: https://arxiv.org/abs/2607.01047
pdf_url: https://arxiv.org/pdf/2607.01047
published: '2026-07-01'
collected: '2026-07-02'
category: MultiAgent
direction: 多智体集群 · 人工生命计算基底
tags:
- MultiAgent
- LLM Agent
- Interpretability
- Artificial Life
- Collective Intelligence
one_liner: 提出将具备自主能力的LLM集群作为兼具高复杂性与高可解释性的第四类人工生命研究基底
practical_value: '- 电商多Agent导购/客服集群搭建可复用「持久化记忆+共享工具库+自然语言交互」架构，无需硬编码协作规则，同时可通过交互日志、Agent自报告快速定位异常，解决多Agent系统黑盒问题

  - 做营销活动舆情、用户群体行为模拟时，可参考Agentic Substrate设计，用LLM多Agent替代传统规则式Agent-Based Model，模拟不同消费人群的互动、共识形成、舆论扩散动态，结果更贴近真实场景

  - 多Agent系统可解释性可复用文中6通道框架，优先采用Agentic（直接问询Agent决策原因）、Stigmergic（追踪共享文档/工具调用痕迹）通道，无需拆解LLM内部结构即可完成集群行为归因'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有传统人工生命三类基底（软/硬/湿）存在固有矛盾：简单规则驱动的基底复杂度不足，难以涌现类生命的复杂社会行为；高复杂度的基底可解释性极低，无法追溯宏观现象的微观成因。孤立LLM本身无类生命属性，现有LLM多Agent研究多聚焦短期特定任务，未被系统性作为复杂行为研究的通用基底。
### 方法关键点
- 定义第四类人工生命研究基底**Agentic Substrate**：核心单元为配备持久化记忆、共享可扩展工具库、具备自主决策能力（可主动发起行动/拒绝触发请求）的Agent化LLM，集群通过自然语言交互，嵌入共享持久运行环境
- 提出适配Agent集群的6维可解释性分析框架：在原有行为/归因/概念/机制通道基础上，新增Agentic（直接查询Agent决策过程）、Stigmergic（追踪环境中遗留的交互痕迹）两类轻量化可解释通道
- 梳理7类核心人工生命研究命题在Agentic Substrate下的新研究范式，明确其相较于传统基底的独特优势
### 关键结果
作为视角论文，系统梳理多个已落地的Agent集群实践：Agents of Chaos部署6个异构LLM Agent在开放环境长期运行，观测到知识共享、故障级联传播等集群动态；Moltbook数据集覆盖百万级Agent社交交互记录，验证了无中心化场景下群体规范形成、恶意行为自发矫正等现象；TerraLingua模拟有限资源环境下的Agent社会，涌现出文化传承、角色分化等类社会行为。
### 最值得记住的结论
LLM多Agent集群的复杂行为并非来自个体模型能力的提升，而是来自Agent在持久共享环境中的长期交互，交互层的自然语言属性让复杂系统第一次同时具备高复杂性与高可解释性。
