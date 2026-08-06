---
title: Self-Evolving Coding Agents
title_zh: 自进化编码Agent研究综述
authors:
- Hao Zhou
- Haichuan Hu
- Ye Shang
- Quanjun Zhang
affiliations:
- Nanjing University of Science and Technology
- Nanjing University
arxiv_id: '2608.03392'
url: https://arxiv.org/abs/2608.03392
pdf_url: https://arxiv.org/pdf/2608.03392
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: Agent 自进化机制与分类体系
tags:
- Self-Evolving Agent
- Coding Agent
- Agent Taxonomy
- Multi-Agent Collaboration
- Feedback-driven Adaptation
one_liner: 系统梳理自进化编码Agent的分类框架、演化机制与核心挑战
practical_value: '- 落地业务Agent时可复用分层演化框架，优先从记忆沉淀、技能复用维度做轻量自进化，避免一开始调整模型或架构，降低落地试错成本

  - 可参考三类演化时序设计适配业务：任务内基于实时用户反馈调整当前策略、任务后将有效经验沉淀到RAG知识库、阶段化汇总有效数据做LoRA微调，兼顾响应速度与长期效果

  - 多Agent协作的推荐/广告系统可参考工作流动态演化思路，根据任务复杂度动态调整Agent交互拓扑，减少无效多轮交互，降低推理延迟

  - 自进化的反馈信号优先选择可量化、可复现的业务指标（如点击率、成交转化率）作为依据，避免纯LLM judge带来的主观偏差，提升进化可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent部署后架构多为静态，无法适配软件研发领域代码仓库持续迭代、依赖动态变更、反馈资源丰富的特性，易重复犯错且难以适配项目特定语境；同时通用自进化Agent研究未针对编码场景的可执行反馈、仓库上下文等独有特征做系统梳理，缺乏统一分析框架支撑高可靠自适应编码Agent的设计与落地。

### 方法关键点
- 明确定义自进化编码Agent的概念边界，区分于传统静态编码Agent、通用自进化Agent，核心特征是基于编码交互的可执行反馈持续更新自身内部组件
- 构建以演化对象为核心的分类体系，划分为五大演化方向：Agent框架自进化、内存自进化、技能与工具自进化、模型自进化、工作流与拓扑自进化，覆盖从上层架构到底层模型的全栈演化路径
- 补充两个正交分析维度：演化时序（任务内实时演化、任务后沉淀演化、阶段化批量演化）与演化证据（可执行结果、环境反馈、轨迹衍生经验），形成三维分析框架
- 系统性总结领域当前核心挑战：反馈可靠性、基准过拟合、安全性、可维护性、演化成本、跨场景泛化性

### 核心产出
作为该领域首篇系统综述，覆盖所有代表性技术方案与典型系统，配套开源了最全的自进化编码Agent论文合集，为后续研究提供了统一的分析框架与落地参考。

### 核心结论
自进化的核心不是盲目追求复杂架构，而是根据场景特性选择最轻量的演化路径，优先采用可验证的客观反馈作为进化驱动信号。
