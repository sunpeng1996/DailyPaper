---
title: 'Experience Memory Graph: One-Shot Error Correction for Agents'
title_zh: 经验记忆图：面向LLM智能体的单样本错误纠正框架
authors:
- Wenjun Wang
- Yuchen Fang
- Fengrui Liu
- Zibo Liang
- Kai Zheng
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2607.13884'
url: https://arxiv.org/abs/2607.13884
pdf_url: https://arxiv.org/pdf/2607.13884
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: LLM Agent · 结构化记忆与错误纠正
tags:
- Agent Memory
- Graph Matching
- LLM Agent
- One-shot Correction
- Error Recovery
one_liner: 将智能体错误纠正转化为图匹配问题，离线构建记忆图实现测试时无循环单步纠错
practical_value: '- 电商导购/售后Agent可复用该框架：离线将历史失败对话轨迹与专家成功轨迹转化为动作决策图，提取错误修正路径，避免测试时反复调用LLM反思，大幅降低API成本与延迟

  - 长链路选品/凑单等搜索推荐Agent可采用节点+边的记忆结构：节点存储单任务纠错规则，边存储跨相似任务通用流程，可提升小模型在长路径任务的表现，降低大模型依赖

  - 轨迹转动作决策图的工程trick可直接复用：节点复用+无效动作并行化设计，可过滤无意义观测干扰，让提取的修正规则更精准

  - 离线计算、线上检索的架构可迁移：将复杂错误归因从线上转移到离线执行，线上仅做embedding相似性检索，适合实时性要求高的电商业务场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的自纠错机制依赖prompt式反射，存在三个核心缺陷：对LLM自身推理能力依赖高，小模型难以完成长链路错误归因；测试时迭代试错带来极高的延迟与API成本；生成的记忆为任务专属，跨场景泛化性差，无法满足实时业务需求。

### 方法关键点
- 轨迹预处理：将训练集的失败探索轨迹、成功专家轨迹统一转化为有向动作决策图，节点为归一化动作元组，边为前置观测，采用节点复用、无效动作并行化设计，提升图的语义准确性
- 记忆图构建：节点存储单任务内的洞察，通过失败-成功轨迹对的图匹配提取公共子图（正确流程）与最短图编辑路径（纠错规则）；边存储跨相似任务的通用经验，通过匹配相似任务的专家轨迹公共子图得到
- 测试时推理：仅需通过query embedding检索top-K相关节点和对应边的经验，直接注入prompt引导Agent执行，无任何迭代试错循环

### 关键实验
在ALFWorld、ScienceWorld两个长链路Agent基准上对比ReAct、Reflexion、ExpeL等SOTA基线：Qwen3-4B小模型搭载EMG在ALFWorld unseen集上成功率比最优基线高17.9个百分点；DeepSeek-V4大模型搭载EMG在ScienceWorld unseen集上成功率比最优基线高9个百分点；推理时间仅为迭代基线的1/5左右，无测试时额外成本。

### 核心结论
把Agent的错误归因和经验提取从线上转移到离线，用确定性的图计算代替不确定的LLM反射，是兼顾效果与成本的可行路径。
