---
title: 'Ream: Unfolding Mutual Awareness in Human-Agent Workspaces'
title_zh: Ream：人-Agent共享工作空间的双向感知协作系统
authors:
- Peiling Jiang
- Sangho Suh
- Varsha Kishore
- Jonathan Bragg
- Haijun Xia
- Pao Siangliulue
- Daniel S. Weld
- Amy X. Zhang
- Joseph Chee Chang
affiliations:
- University of California San Diego
- Allen Institute for AI
- University of Washington
arxiv_id: '2610.09497'
url: https://arxiv.org/abs/2610.09497
pdf_url: https://arxiv.org/pdf/2610.09497
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 人-Agent协作 · 共享工作空间双向感知
tags:
- Human-Agent Collaboration
- Shared Workspace
- Mutual Awareness
- Agentic Workflow
- Behavior Tracking
one_liner: 提出人-Agent共享文献综述工作空间Ream，通过双向行为追踪与可视化提升协作效率
practical_value: '- 电商人-Agent协作场景（如运营与选品Agent、客服与应答Agent协作）可复用双向感知设计：同时追踪用户和Agent的操作（浏览、标注、修改等），按行为权重聚合注意力分数，降低人对齐Agent工作的成本。

  - Agent辅助内容生产场景（如营销文案生成、商品卖点总结）可参考结构化artifact设计：将工作流拆分为可共享的结构化文件（如商品库、卖点集合、文案报告），所有行为痕迹绑定到对应文件，支持用户快速溯源Agent输出的依据，提升信任度。

  - 多Agent协作系统可复用基于共享artifact的状态同步机制：无需单独维护多Agent的上下文会话，所有Agent可通过查询共享文件的行为历史获取上下文，实现跨Agent的任务承接，降低工程复杂度。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前人-Agent共享工作空间存在双向感知缺失问题：Agent操作速度远超人类监控能力，用户在工作空间的隐性偏好（如反复浏览的文件、标注内容）无法被Agent感知，导致协作成本高、Agent输出难以对齐用户需求，该问题在文献综述这类长周期、多文档的知识工作场景尤为突出。

### 方法关键点
- 工作流结构化建模：将文献综述流程拆分为3类结构化共享文件（单篇论文`.paper`、论文集合`.papers`、综述报告`.report`），用户和Agent所有操作都基于这些文件展开，作为感知信息的载体。
- 双向行为追踪与量化：记录用户和Agent的所有操作（打开、编辑、标注、搜索等），给不同操作分配0.02~0.8的注意力权重，降噪后聚合为双方对每个文件的注意力分数。
- 双向感知机制：用户侧在文件树、文档内、PDF中嵌入本地化可视化组件，直观展示双方的操作痕迹和注意力分布；Agent侧提供`read_signals`工具支持Agent查询用户行为历史，主动对齐用户偏好，还可基于行为自动生成用户下一步任务建议。

### 关键实验
开展两组用户研究：12人实验室研究+6人纵向一周使用研究，参与者均为有Agent使用经验的研究者。结果显示10/12的实验室参与者主动要求继续使用Ream，用户发送的消息中11.9%来自系统自动生成的任务建议；纵向使用的参与者平均积累215篇论文、2.8小时使用时长，均认可Agent可通过行为历史感知自身意图、无需重复传递上下文。

### 核心结论
将人机协作的感知信息嵌入用户天然的工作流artifacts中，而非单独的监控面板，是提升人-Agent协作效率、降低对齐成本的核心路径。
