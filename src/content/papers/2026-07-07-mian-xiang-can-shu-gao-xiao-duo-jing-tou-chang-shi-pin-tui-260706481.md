---
title: Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video
  Extrapolation
title_zh: 面向参数高效多镜头长视频推演的提示适配器上下文路由方法
authors:
- Anna Córdoba
- Adam Puente Tercero
- Nerea Angulo Hijo
- Mar Linares Tercero
- Julia Barrientos
- Ainhoa Miranda
- Jesús Olivera
affiliations:
- Instituto de Investigación en Visión Artificial
arxiv_id: '2607.06481'
url: https://arxiv.org/abs/2607.06481
pdf_url: https://arxiv.org/pdf/2607.06481
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态长视频生成·参数高效微调 提示路由
tags:
- Parameter-Efficient Fine-Tuning
- LoRA
- Prompt Routing
- Diffusion Model
- Multimodal Generation
one_liner: 提出无需全量微调的PACR-Video框架，通过轻量适配器+提示路由实现连贯多镜头长视频推演
practical_value: '- 跨片段一致性维护架构可复用：递归上下文银行+依赖感知路由的设计可直接迁移到长会话Agent、多轮生成式推荐场景，解决上下文漂移、历史信息遗忘问题

  - 参数高效适配调度策略可借鉴：冻结主干+轻量适配器的组合调度思路，可用于多场景LLM/多模态模型微调，平衡基础能力保留与场景适配成本

  - 双粒度优化目标可复用：局部+全局联合损失的设计可用于电商短视频脚本生成、多轮推荐话术生成等多步生成任务，提升序列整体连贯性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有长视频生成普遍存在实体漂移、场景遗忘、因果逻辑断裂问题，全量微调生成模型算力成本高、泛化性差，难以平衡长序列内容一致性与后续内容创新性的需求。
### 方法关键点
1. 冻结文生视频扩散Transformer主干，插入低秩时序适配器，以可学习的镜头角色提示作为输入条件
2. 构建递归提示银行存储历史镜头的实体、位置、动作、风格特征，通过预测叙事依赖动态路由调用对应适配器
3. 采用镜头局部+故事全局联合优化目标，搭配适配器组合调度策略，平衡前期内容一致性与后期内容演化自由度
### 关键结果
在6个多镜头长视频基准上，全面优于全量微调、记忆增强、流式生成等基线，在语义对齐、实体一致性、时序平滑度、人类偏好等指标上实现领先
