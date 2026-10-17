---
title: 'Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory
  Writing'
title_zh: Hy-Memory-30B-A3B：基于归因强化学习的LLM长期内存写入模型
authors:
- Tianxiang Fei
- Jiazheng Kang
- Mao Zheng
- Xingyan He
- Xiang Yu
affiliations:
- Tencent Hunyuan
arxiv_id: '2610.22196'
url: https://arxiv.org/abs/2610.22196
pdf_url: https://arxiv.org/pdf/2610.22196
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: Agent 长期内存写入优化
tags:
- GRPO
- Long-Term Memory
- LLM Agent
- On-Policy Distillation
- Reinforcement Learning
one_liner: 提出兼容多主流内存框架的归因强化学习内存写入模型，性能超越Claude Opus 5
practical_value: '- 电商/客服Agent记忆系统优化可直接复用三层奖励设计：per-chunk探针校验用户核心偏好/订单信息的写入准确性、归因奖励关联后续推荐/回答效果、存储惩罚抑制无效会话信息存储，同时降低检索噪声和存储成本

  - 跨系统适配的小模型训练范式可迁移：先通过on-policy蒸馏让小模型学习业务系统的接口协议，再用RL优化业务目标，可替代通用大模型prompt调用方案，大幅降低生成式推荐、个性化推送等场景的推理成本

  - 长链路决策信用分配trick可复用：Chunk-level GRPO按决策单元拆分奖励的思路，可直接用到推荐系统多步召回排序、用户长期兴趣建模的奖励计算中，解决全局奖励无法定位单个决策贡献的问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM长期内存系统的写入模块普遍依赖通用LLM搭配框架专属prompt实现，存在推理成本高、跨框架兼容性差、写入决策无下游效果反馈的问题；传统全链路最终奖励RL训练存在信用分配模糊、易错误奖励无关写入动作的缺陷，无法满足多框架兼容、低开销、高准确率的内存写入需求。
### 方法关键点
- 两阶段训练：第一阶段Memory On-Policy Distillation基于学生模型生成的内存状态，蒸馏学习Mem0、MemOS、Hy-Memory三类主流框架的写入协议，避免静态示范的分布偏移；第二阶段通过归因RL优化下游回答效果。
- 分层奖励设计：融合三类信号：per-chunk探针奖励（测试单chunk信息的可召回性、精准度、无关信息过滤效果）、跨chunk归因结果奖励（将下游问答效果映射到对应贡献chunk）、存储量惩罚（抑制无差别存储降低成本）。
- Chunk-level GRPO优化：按chunk位置分组计算优势，避免全局奖励广播的信用错配；训练过程中保留策略生成的内存状态跨窗口传递，完全对齐部署场景。
### 关键结果
在Mem0、Hy-Memory、MemOS、训练集未见过的EverMemOS四个框架的20%基准子样本上测试，对比Claude Opus 5、DeepSeek V4.1 Flash等基线，Hy-Memory-30B-A3B在四个框架上均排名第一，宏观平均得分55.49%，比Claude Opus 5高0.87pp，比基线Hy3-A3B Base高7.84pp，在OOD框架EverMemOS上领先Claude Opus 5达2.86pp。
### 核心洞见
内存写入是对外部状态的长horizon控制问题，而非简单的摘要任务，专用训练的写入能力可跨框架迁移，效果远优于通用LLM加prompt的实现。
