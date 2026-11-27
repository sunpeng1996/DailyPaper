---
title: 'StateWeaver: Multi-Agent Coordination of Story-State Transitions for Long-Horizon
  Video Generation'
title_zh: StateWeaver：面向长视频生成的故事状态迁移多智能体协调框架
authors:
- Modi Jin
- Xuying Zhang
- Yijing Guo
- Haoran Li
- Yanwen Ma
- Jing Wang
- Chenyu Ge
- Ming-Ming Cheng
- Haoyang Huang
affiliations:
- Nankai University
- Joy Future Academy, JD
- ShanghaiTech University
- Beihang University
arxiv_id: '2611.34290'
url: https://arxiv.org/abs/2611.34290
pdf_url: https://arxiv.org/pdf/2611.34290
published: '2026-11-24'
collected: '2026-11-27'
category: MultiAgent
direction: 多智能体协作 · 长序列生成一致性保障
tags:
- MultiAgent
- Hierarchical Memory
- State Consistency
- Long-Horizon Generation
- Workflow Orchestration
one_liner: 提出结合Active States与层级协作的多智能体框架StateWeaver，提升长视频跨镜头一致性
practical_value: '- 多智能体分工按任务/生成轮次隔离执行上下文，可直接复用在电商多Agent商品文案、种草长视频生成工作流，大幅降低长上下文累积的推理开销

  - Active States机制把校验发现的不一致转化为明确的资产修复要求，仅修改错误属性保留正确内容，适合直播切片拼接、商品短视频的一致性修复，降低重生成成本

  - 层级内存绑定生成结果与资产状态、时间戳、版本号，可用于电商多场景素材资产库管理，避免重复生成同质化内容，提升素材复用率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频基础模型仅能生成高质量短片段，长视频生成普遍存在跨镜头一致性差、事件驱动的状态变化刻画不准确问题；已有Agent工作流持续规划修复会导致上下文冗余累积，参考更新能力严重受限。
### 方法关键点
1. 设计**Active States**机制：将审核阶段识别的状态差异转化为具象的视觉资产需求，指导参考构建、校验与重生成，保留身份等已正确内容仅修复目标属性；同时将确认的生成结果绑定对应资产状态、故事时间、参考版本，供后续镜头验证复用。
2. 提出**Hierarchical Collaboration**架构：按任务、片段、修复轮次隔离执行上下文，通过层级内存组织多集合的跨流程协作。
### 关键结果
在多个基准测试中效果超过现有SOTA方法，在预定义和自主规划两类故事板下，均可生成跨镜头一致性持续稳定的长视频
