---
title: Training Small Language Models for Transferable Tool Selection
title_zh: 面向可迁移工具选择的小语言模型训练方法
authors:
- Zhaoyi Zhou
- Akshayaa Magesh
- Jeongyeol Kwon
- Artem Kuriksha
- Daniel Jiang
- Andrea Zanette
- Ayush Jain
affiliations:
- Meta
- Carnegie Mellon University
arxiv_id: '2610.31483'
url: https://arxiv.org/abs/2610.31483
pdf_url: https://arxiv.org/pdf/2610.31483
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 工具选择 · 小模型训练与迁移
tags:
- Tool Selection
- Small LLM
- Reinforcement Learning
- Transfer Learning
- Agent
one_liner: 通过SFT+RL训练8B以下小模型完成工具选择，性能超402B Llama-4且支持跨域跨检索器零样本迁移
practical_value: '- 电商/广告Agent多工具调用场景可复用Plan-Retrieve-Select三阶段架构，用小模型替代闭源大模型降低推理成本与延迟，适配大规模落地需求

  - 训练流程可直接复用：先用大模型作为教师过滤噪声标注、生成SFT轨迹，再用GRPO做RL训练，奖励函数可直接套用检索F1+选择精确匹配的设计，无需额外人工标注

  - 跨业务场景迁移时不需要重新训练工具选择模型，仅需替换检索后端（如从BM25切换为业务域专属稠密检索器）即可继承检索性能，适配不同工具库需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent可用工具规模已达上万级，全量工具描述无法放入上下文，传统相关性检索仅做相似度排序，无法判断任务实际需要的工具；现有工具选择方案依赖Claude、ChatGPT等闭源大模型，成本高、可控性差，小模型落地又面临跨工具域、跨检索器迁移能力不足的问题。

### 方法关键点
- 采用Plan-Retrieve-Select三阶段工作流：同一小模型先将用户指令拆分为独立子步骤，每个子步骤调用检索器取Top-K候选，再从候选中匹配对应工具，单轮上下文长度不随工具库规模增长
- 训练流程：先以大模型为教师过滤噪声gold标注，生成指令分解轨迹与推理过程做SFT warm-up，再用GRPO做RL训练；Plan阶段奖励取检索召回率、精确率的F1值，Select阶段奖励为工具精确匹配的0/1 reward
- 训练时使用无训练成本的BM25作为检索器，推理时可任意替换为业务域稠密检索器，无需重训模型

### 关键实验
在ToolBench G3数据集训练Qwen3-1.7B/4B/8B，对比402B Llama-4-Maverick的prompt方案，8B模型成功率达41.5%，超出Llama4最优prompt方案（30.6%）10.9个百分点；零样本迁移到ToolBench G2、Gorilla、CRAFT等跨域数据集，性能均优于未训练的Llama4；检索器替换为ToolBench专属COLT稠密检索器后，8B模型成功率进一步提升，无需任何重训。

### 核心结论
工具选择的核心能力是指令拆分与语义匹配，不需要大模型的通用能力，小模型经过针对性训练后效果可远超大模型prompt方案，还能实现跨场景零样本迁移。
