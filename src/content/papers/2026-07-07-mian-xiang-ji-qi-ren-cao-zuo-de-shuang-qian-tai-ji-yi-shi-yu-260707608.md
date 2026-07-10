---
title: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
title_zh: 面向机器人操作的双潜态记忆视觉-语言-动作模型
authors:
- Hongyu Qu
- Jianzhe Gao
- Xiaobin Hu
- Shaohuan Yang
- Xinlei Yu
- Rui Yan
- Wenguan Wang
- Xiangbo Shu
- Shuicheng Yan
affiliations:
- 南京理工大学
- 浙江大学
- 新加坡国立大学
arxiv_id: '2607.07608'
url: https://arxiv.org/abs/2607.07608
pdf_url: https://arxiv.org/pdf/2607.07608
published: '2026-07-07'
collected: '2026-07-10'
category: Agent
direction: 多模态Agent · 潜态记忆增强推理
tags:
- VLA
- Latent Memory
- Multimodal Reasoning
- Long-Horizon Task
- Agent
one_liner: 提出原生潜态记忆VLA框架，将长短时记忆融入推理空间提升长时序任务表现
practical_value: '- 长短时双记忆库架构可直接迁移至多轮对话Agent、会话推荐的记忆模块，优化长时序用户意图理解准确率

  - 全潜空间记忆存储-检索-推理的设计可改造现有RAG流程，解决外挂记忆和模型推理脱节的问题，提升结果相关性

  - curator-seeker-condenser-weaver四组件记忆流水线可复用到用户长短期兴趣建模，压缩兴趣表征降低推理context占用'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
主流Vision-Language-Action (VLA) 基于马尔可夫假设仅依赖当前观测预测动作，长时序依赖任务表现差；现有记忆增强VLA将记忆放在模型原生潜空间外，无法与多模态推理、动作生成流程流畅融合。
### 方法关键点
提出LaMem-VLA原生潜态记忆框架，核心包含4个协同组件：1. curator将历史经验划分为互补的长短时记忆库；2. seeker基于多模态认知检索记忆库中的上下文相关证据；3. condenser将检索结果重构为紧凑的长短时潜态记忆token；4. weaver将记忆token、当前观测、指令拼接为统一嵌入序列，全流程都在同一潜空间完成，记忆直接参与VLA推理。
### 关键结果
在SimplerEnv、LIBERO两个机器人操作基准数据集上，性能显著优于所有现有记忆增强VLA方案。
