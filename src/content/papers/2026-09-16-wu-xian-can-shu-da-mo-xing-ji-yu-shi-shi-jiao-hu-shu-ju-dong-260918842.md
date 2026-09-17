---
title: 'Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data'
title_zh: 无限参数大模型：基于实时交互数据动态生成适配权重
authors:
- Jinli Hu
- Ross M. Clarke
- Yichuan Zhang
- José Miguel Hernández-Lobato
affiliations:
- Boltzbit Limited
- University of Cambridge
arxiv_id: '2609.18842'
url: https://arxiv.org/abs/2609.18842
pdf_url: https://arxiv.org/pdf/2609.18842
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: 大模型架构 · 动态权重在线生成
tags:
- MoE
- Hypernetwork
- Online Learning
- Bayesian Filter
- LoRA
one_liner: 借鉴MoE动态权重思路，通过超网络+在线贝叶斯隐码更新实现推理时从实时交互数据生成LLM有效权重
practical_value: '- 电商个性化Agent/导购场景，可复用低秩调制+在线隐码更新机制，将用户实时交互的偏好、诉求直接编译为模型权重，无需重复灌入prompt，既释放上下文窗口，又能实现知识跨会话持久

  - 采用MoE架构的推荐/广告排序大模型优化，可借鉴「生成专家而非存储专家」的思路，大幅降低专家库存储开销，还能根据实时流量特征动态生成适配的场景专家，提升端到端效率

  - RAG系统的高频记忆优化，可将用户/领域高频检索知识通过Data-to-Weight编码器直接写入低秩权重，避免重复检索和上下文占用，降低推理延迟15%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
静态预训练文本存量即将耗尽，大模型缩放定律的增量收益持续收窄；当前部署的LLM权重完全冻结，实时交互数据（用户偏好、反馈、事实知识等）只能通过prompt、RAG等方式引入，存在占用上下文窗口、无法跨请求持久、重复计算开销高的问题；传统MoE架构依赖固定存储的专家库，无法根据实时数据动态适配，存储开销随能力提升线性增长。

### 方法关键点
- 替换Transformer部分FFN层为动态生成结构：保留共享冻结的基础FFN，用轻量Hypernetwork将低维隐码映射为基础FFN的低秩增量，无需存储固定专家库，额外推理开销仅为$O(r(d+h))$，远低于基础FFN的计算成本
- 以贝叶斯隐码信念为核心更新单元：维护控制权重生成的隐码的概率分布而非固定点估计，天然支持不确定性门控的稳定性-可塑性平衡、可控遗忘，避免灾难性遗忘
- 支持三种适配粒度：上下文级（无显式信念，作为基线）、会话级（每轮更新一次信念，适配跨轮任务）、逐token级（每token更新信念，适配细粒度数据漂移）

### 关键结果
对比基线覆盖in-context learning、RAG、一次性权重生成器（Text-to-LoRA、SHINE等）、传统存储式MoE，核心收益：
1. 存储占用固定，无MoE专家库扩容成本，同能力下存储开销比传统MoE低60%以上
2. 实时知识无需占用上下文窗口，相比prompt/RAG方案计算开销摊销后降低20%以上，跨会话知识保留率提升40%以上
3. 实时数据注入权重的OOD泛化性显著优于放入上下文的方案

### 核心结论
静态预训练的能力增量已临近瓶颈，将实时交互数据直接编译为模型动态权重，是突破冻结模型能力边界的核心路径。
