---
title: 'MemLens: A Value-Aware Memory Management System with Interactive Analytics
  for LLM-based Agents'
title_zh: MemLens：面向LLM Agent的价值感知交互式分析记忆管理系统
authors:
- Shuyue Wei
- Chang Liu
- Zimu Zhou
- Yongxin Tong
- Lizhen Cui
affiliations:
- 山东大学
- 北京航空航天大学
- 香港城市大学
arxiv_id: '2607.25992'
url: https://arxiv.org/abs/2607.25992
pdf_url: https://arxiv.org/pdf/2607.25992
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: LLM Agent 长时记忆管理优化
tags:
- LLM Agent
- Memory Management
- Shapley Value
- Long-term Memory
- Interactive Analytics
one_liner: 提出基于Shapley边际贡献的LLM Agent记忆价值量化方案，实现低开销的高价值记忆存储与交互式分析
practical_value: '- 电商/推荐类Agent的长时记忆管理可复用Shapley值采样近似方法，量化用户历史交互、浏览记录对下游推荐任务的边际贡献，选择性留存高价值记忆，大幅降低token开销与检索延迟

  - 可借鉴分层记忆树结构，将细粒度用户交互记录和抽象用户偏好分层存储，兼顾召回精度与上下文利用效率，适配个性化推荐、客服Agent等场景

  - 可参考其交互式分析框架，搭建记忆策略对比看板，快速评估不同记忆留存策略的响应质量、延迟、token成本 trade-off，降低策略迭代成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent内存管理多为粗粒度，无差别留存所有交互记录或采用启发式摘要，未显式建模异质性记忆单元对下游任务的实际价值，导致低效用记忆冗余存储，既稀释上下文相关性，又增大检索空间、提升token开销。记忆的有用性非均匀也非静态，依赖当前任务和已有的记忆组合，通用摘要方法无法满足高效价值评估需求。

### 方法关键点
- 记忆单元构建：将原始交互记录拆分为句子级原子单元，再通过LLM生成多级摘要形成分层记忆树，保留原始数据溯源链路避免信息损失
- 价值量化：定义记忆Shapley值（MS-value），通过轻量代理模型结合LLM-as-Judge评估记忆单元的边际贡献，采用分层采样近似将计算复杂度降到O(ρM)，ρ仅需20~100即可满足交互级延迟要求
- 价值感知存储：设定价值阈值τ选择性留存高价值记忆，增量更新分层记忆树，通过语义相似度完成记忆的合并、更新、插入操作，消除冗余
- 响应生成：用户偏好摘要作为系统提示，检索时结合语义相关性与MS-value重排记忆单元，优先注入高价值记忆

### 关键实验
基于自建EduMemBench基准（包含2000+多轮对话、500条带参考答案的测试问答对），对比store-all、Agent启发式摘要等基线，价值感知策略在响应质量持平甚至提升的前提下，token消耗降低35%以上，检索延迟降低30%左右，记忆存储压缩率可达60%。

### 核心洞察
LLM Agent记忆的核心价值是对下游任务的边际贡献，而非存储的信息总量。
