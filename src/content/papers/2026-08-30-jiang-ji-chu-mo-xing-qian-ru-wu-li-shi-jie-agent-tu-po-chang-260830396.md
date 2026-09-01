---
title: Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier
  of Long-Horizon Navigation
title_zh: 将基础模型嵌入物理世界Agent 突破长时导航性能边界
authors:
- Zixing Lei
- Gengze Zhou
- Xiong-Hui Chen
- Jiazhao Zhang
- Yiyang Huang
- Hang Yin
- Haoqi Yuan
- Qi Wu
- Weixin Li
- Siheng Chen
affiliations:
- Shanghai Jiao Tong University
- Alibaba Inc Qwen Team
- Adelaide University
- Peking University
- Tsinghua University
arxiv_id: '2608.30396'
url: https://arxiv.org/abs/2608.30396
pdf_url: https://arxiv.org/pdf/2608.30396
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 实体Agent · 长时导航多模态协作框架
tags:
- Embodied Agent
- VLM
- Navigation Foundation Model
- Long-Horizon Reasoning
- Tool Use
one_liner: 提出NavMCP支架框架耦合VLM推理与NFM执行，实现长时实体导航问答SOTA
practical_value: '- 异构大模型分工协作范式可迁移：上层推理大模型做目标拆解、决策、记忆，下层领域基础模型做闭环执行，无需重训双方，适合电商导购Agent、线下门店服务机器人等场景的快速搭建

  - 工具调用三通道设计可复用：意图通道结构化定义子目标、约束、预算，观察通道返回全路径结构化证据而非仅终端结果，记忆通道跨调用积累正负样本与未完成目标，大幅提升长时多步任务成功率

  - 长时任务效率优化思路可参考：证据优先的上下文压缩策略，仅保留带源引用的核心证据而非全量原始轨迹，降低上下文开销的同时避免信息损失，适合多轮导购、跨会话用户行为建模场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时物理世界Agent需要同时具备长程目标推理能力和低级别动作落地能力，但现有基础模型能力互补却未有效协同：VLM擅长目标拆解、信息补全和高层规划，但直接输出导航动作鲁棒性差、效率低；导航基础模型（NFM）能稳定执行语义子目标，但仅支持单次有限时长任务，无法跨任务保留状态、自主决策下一步目标，因此需要一套框架整合两类模型的互补能力。

### 方法关键点
- 提出NavMCP支架框架，无需重训VLM和NFM，通过三通道实现两者协作：
  1. 意图通道：将VLM的证据需求转化为结构化导航调用，包含模式（对象搜索/路径导航）、子目标、步长预算、约束，无需VLM控制底层动作
  2. 观察通道：将NFM的全量导航轨迹转化为带源引用的结构化证据，包含关键帧、观测对象、空间线索、未探索区域提示，避免仅返回终端结果丢失中间信息
  3. 记忆通道：跨调用存储已搜索区域、正负观测证据、未解决目标，避免重复探索，为后续推理提供上下文

### 关键实验
在HM-EQA、MT-HM3D、EXPRESS-Bench三个实体问答基准上均取得SOTA，同骨干下比传统 episodic 接口基线高14.9个百分点；在Unitree Go2实体机器人上长时导航成功率达78.3%，任务时长越长，领先优势越大，从短任务领先10个点提升到长任务领先45个点。

### 核心结论
异构基础模型的价值最大化路径不是让单个模型覆盖全链路能力，而是通过合理的分工接口设计，让每个模型发挥其擅长的能力，协同解决复杂长时任务。
