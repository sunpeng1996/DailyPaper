---
title: 'ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse
  Context Routing'
title_zh: ContextMaster：基于固定预算稀疏上下文路由的交互式多镜头视频生成
authors:
- Xu Guo
- Zhengxuan Wei
- Xinghui Li
- Hanzhuo Huang
- Xinyu Liu
- Xiangyang Luo
- Min Wei
- Yiran Zhu
- Qiulin Wang
- Yulong Xu
affiliations:
- Tsinghua University
- Nanjing University
- Kling Team, Kuaishou Technology
- ShanghaiTech University
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04956'
url: https://arxiv.org/abs/2608.04956
pdf_url: https://arxiv.org/pdf/2608.04956
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态视频生成 · 上下文路由优化
tags:
- Video Generation
- Context Routing
- Knowledge Distillation
- Inference Optimization
- Multimodal
one_liner: 提出固定预算稀疏上下文路由的多镜头视频生成统一模型，兼顾跨镜头一致性与推理效率
practical_value: '- 固定预算稀疏上下文路由思路可复用在长序列用户行为建模的推荐场景，解决历史行为越长推理延迟越高的问题

  - 两阶段特权上下文蒸馏框架可迁移到端侧/低算力场景的LLM/多模态模型压缩，兼顾小模型效果与推理速度

  - 角色感知上下文表示+ConstraintSink约束留存的设计，可优化多轮交互Agent的上下文记忆一致性，避免历史信息遗忘'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态视频生成模型通常将生成、参考条件控制、编辑作为独立操作，无法适配多镜头创作中复用历史上下文、保持跨镜头一致性的需求，且随交互历史变长，去噪步骤的上下文读取成本会线性增长。
### 方法关键点
1. 提出角色感知上下文表示，统一支持文本生成、参考遵循、素材编辑三类操作；
2. 结合可复用干净上下文状态+固定预算稀疏上下文路由，搭配ConstraintSink留存任务约束，控制推理成本不随历史增长；
3. 两阶段特权上下文蒸馏：先通过一致性蒸馏迁移稠密教师模型的全上下文行为，再用分布匹配优化部署效果。
### 关键结果
三类基础任务表现优于专用基线，跨镜头一致性显著提升，用户研究验证工作流灵活性，单GPU推理速度达16 FPS。
