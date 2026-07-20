---
title: 'RESOURCE2SKILL: Distilling Executable Agent Skills from Human-Created Multimodal
  Resources'
title_zh: 从人类创建的多模态资源中蒸馏软件Agent可执行技能
authors:
- Yijia Fan
- Zonglin Di
- Zimo Wen
- Yifan Yang
- Mingxi Cheng
- Qi Dai
- Bei Liu
- Kai Qiu
- Yue Dong
- Ji Li
affiliations:
- Microsoft Research
- University of California, Santa Cruz
- Shanghai Jiao Tong University
arxiv_id: '2606.29538'
url: https://arxiv.org/abs/2606.29538
pdf_url: https://arxiv.org/pdf/2606.29538
published: '2026-07-15'
collected: '2026-07-20'
category: Agent
direction: Agent 多模态可执行技能库构建
tags:
- Agent Skill
- Multimodal Distillation
- Skill Library
- Procedural Knowledge
- RAG
one_liner: 提出Resource2Skill框架将多模态资源蒸馏为分层可执行Skill Wiki，提升跨7个领域的Agent任务表现
practical_value: '- 多模态技能库设计可直接复用：将电商场景的装修教程、作图案例、活动页开发指南等用户/运营生成资源，蒸馏为带文本说明、可执行代码、可视化样例的结构化技能条目，大幅降低Agent执行专业任务的
  hallucination

  - 分层索引+BM25召回+LLM筛选的检索策略可迁移到技能/工具召回场景，比纯向量检索高8.9pp、比纯BM25高2.9pp，适配万级以上大规模技能库的快速匹配

  - 离线蒸馏+在线补全机制可复用：高频操作离线批量蒸馏入库提升效率，长尾需求触发在线爬取蒸馏临时技能，长尾场景下性能提升21.6pp

  - 技能验收的5条规则（完整性、可溯源、去重、模态一致、可执行）可直接用到业务技能库的校验流程，避免无效技能入库'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能库多为手写、文本中心化或从Agent交互轨迹生成，大量教学视频、代码仓库、设计案例等人类多模态专业知识未被充分利用，纯文本技能无法传递操作时序、视觉效果等关键信息，导致Agent在活动页生成、商品作图、报表制作等需要标准化操作流程的场景表现极差。

### 方法关键点
- 分层多模态Skill Wiki结构：每个技能条目包含分类路径、文本说明、可视化样例、可执行代码、元数据5个部分，保留不同模态的互补信号
- 统一蒸馏算子：支持从视频、代码仓库、文章、参考作品4类资源中提取结构化技能，经过完整性、可溯源、去重、模态一致、可执行5条规则校验后入库，同一算子可在线调用补充长尾技能
- MetaBrowse检索策略：先用BM25结合分类路径召回Top20候选技能，再由LLM筛选Top5最相关技能用于执行组合

### 关键结果
在Web、Excel、PPT、Blender、UE5等7个创作领域共560个任务上测试，对比无技能Agent、ClaudeCode-H、Codex-H三个基线，平均总体得分提升11.9pp，28个模型-领域组合中26个优于现有基线；纯视频来源的技能库比无视频的多源技能库得分高7.4pp；长尾场景下在线技能补全提升21.6pp。

最值得记住的结论：多模态结构化技能库对Agent专业场景效能的提升远大于纯文本检索或通用推理，是落地垂直领域Agent的核心路径
