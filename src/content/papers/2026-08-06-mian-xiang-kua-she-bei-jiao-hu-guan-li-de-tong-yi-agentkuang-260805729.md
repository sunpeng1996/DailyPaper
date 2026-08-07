---
title: 'Unified Agent: Managing Interactions across Devices'
title_zh: 面向跨设备交互管理的统一Agent框架
authors:
- Xinshuang Liu
- Runfa Blark Li
- Shaoxiu Wei
- Xin Lin
- Truong Nguyen
affiliations:
- University of California, San Diego
arxiv_id: '2608.05729'
url: https://arxiv.org/abs/2608.05729
pdf_url: https://arxiv.org/pdf/2608.05729
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: 跨设备Agent · 状态管理优化
tags:
- Cross-Device Agent
- State Management
- MLLM
- Agent Benchmark
- Long-term Memory
one_liner: 提出携带三类结构化紧凑状态的跨设备统一Agent，在跨设备交互任务上显著优于各类基线
practical_value: '- 做多端用户服务的推荐/电商Agent时，可复用三类结构化状态设计：仅存设备交互活跃度、分设备分主题事实、待处理请求，不用全量存交互历史，既省上下文窗口，又能对齐多端用户行为意图

  - 跨端意图理解场景可优先上轻量显式状态累加方案，效果优于全量上下文和现有记忆/多Agent基线，还能避免上下文线性膨胀的工程问题

  - 做跨端场景效果评测时，可参考配对样本设计：固定用户请求，仅替换前序交互行为，精准隔离状态设计/记忆模块的贡献，降低评测噪音

  - 显式结构化状态天然支持用户可查可删，符合多端数据合规要求，比隐式向量记忆方案更易落地到电商等合规要求高的场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI Agent已逐步从单应用内服务转向跨用户多设备提供服务，但现有方案存在明显缺陷：单Agent将设备作为工具调用，缺乏跨时间跨设备的有效状态管理，无指定设备的请求（如“订我之前看的餐厅”）无法回答；多Agent系统虽支持跨端协作，但没有紧凑统一的状态承载跨端跨时间的交互证据，全量存历史会占用大量上下文，效果也不佳。

### 方法关键点
- 设计三类结构化紧凑状态：设备级交互活跃度证据、分设备分主题的用户陈述事实、当前待处理请求，不存储全量交互历史
- 交互流程为「折叠更新状态→结合状态与当前观测决策」，每一步先将当前观测的有效信息更新到状态，再做决策
- 构造UA-BENCH跨设备交互基准，包含200个配对样本，覆盖不同室内场景、设备布局、任务类型，所有标签为构造式真值，无标注噪音

### 关键结果
对比全上下文、Self-notes、Mem0、Mixture-of-Agents等9种基线，在默认GPT-5.6-Luna设置下，Unified Agent整体得分0.668，比最强基线全上下文高0.055，比现有公开基线高0.194~0.408；状态大小仅为全上下文的1/11，无随交互长度线性膨胀问题，且性能优势在不同MLLM家族、模型能力、推理开销下均稳定存在。

### 最值得记住的结论
对跨设备Agent而言，合理的结构化紧凑状态设计带来的收益，可超过堆模型能力与全量历史上下文，同时兼顾效率与隐私。
