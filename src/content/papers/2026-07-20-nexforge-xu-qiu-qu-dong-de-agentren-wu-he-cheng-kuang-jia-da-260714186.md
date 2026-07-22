---
title: 'NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis
  for LLMs'
title_zh: NexForge：需求驱动的Agent任务合成框架扩展大模型能力
authors:
- Jiarong Zhao
- Zhikai Lei
- Zhiheng Xi
- Rui Zheng
- Hang Yan
- Jie Zhou
- Qin Chen
- Liang He
affiliations:
- East China Normal University
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2607.14186'
url: https://arxiv.org/abs/2607.14186
pdf_url: https://arxiv.org/pdf/2607.14186
published: '2026-07-20'
collected: '2026-07-22'
category: Agent
direction: Agent 训练数据自动化合成
tags:
- Agent Training
- Task Synthesis
- SFT Data
- LLM Agent
- Data Scaling
one_liner: 提出需求驱动的统一Agent训练数据合成框架，无需领域定制即可跨域生成可执行任务与交互轨迹
practical_value: '- 构建电商/广告领域专用Agent时，可复用需求驱动的任务合成思路：先调研真实业务场景的能力需求构建任务分布profile，再匹配场景生成训练数据，避免绑定预设工具导致的任务分布与真实业务脱节

  - 跨业务场景迁移Agent能力时，无需重构数据生产管线，仅需更新能力需求描述即可批量生成新场景的SFT数据，大幅降低领域适配的人工成本

  - 生成Agent训练轨迹时，可借鉴其无人工标注参考、仅保留有效交互信号（如错误恢复、工具调用模式）的思路，降低训练数据的标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent训练数据合成方法绑定预设工具、仓库或技能图，扩展能力覆盖需大量人工领域定制，生成的任务分布受限于底层载体而非真实需求，跨域成本极高，成为Agent能力规模化的核心瓶颈。

### 方法关键点
- 需求调研阶段：基于用户输入的高层能力需求，通过网络调研+LLM生成构建加权任务需求profile（定义任务类型、交付物、运行环境等维度的分布）与场景库（覆盖真实工作上下文，去重过滤保证多样性）
- 分布感知任务编译：将任务profile与场景库做兼容性匹配，生成内部一致的任务指令，保证任务分布符合真实需求同时避免模式坍塌
- 可执行环境与轨迹生成：自动挖掘/生成任务所需的物料、依赖、运行环境，调用教师模型交互生成轨迹，仅做通用清洗（无需人工标注答案）即可输出SFT训练数据

### 关键实验结果
用同一管线生成两类任务数据集：3.6K终端任务、2K办公任务。基于Qwen3.5-35B-A3B Base训练，终端任务将Terminal-Bench 2.0准确率从22.5%提升至52%，规模扩展到43.2K任务时准确率达58.4%，追平Claude Opus 4.6搭配Claude Code的效果；办公任务将GDPval Elo从813提升至1338，超过Gemini 3.1 Pro；最终训练的Nex-N2模型在Terminal-Bench 2.1达75.3%，GDPval达1585 Elo，为开源SOTA。

### 核心结论
Agent训练数据合成的核心是先定义「需要练什么」，再匹配「用什么载体练」，而非反过来被预设载体限制任务分布。
