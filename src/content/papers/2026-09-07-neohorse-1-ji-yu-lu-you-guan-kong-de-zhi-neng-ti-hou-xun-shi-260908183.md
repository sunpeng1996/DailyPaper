---
title: 'NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with
  Routing Harness'
title_zh: NeoHorse-1：基于路由管控的智能体后训练实现递归自提升
authors:
- NeoHorse Team
- Guoliang Cao
- Guohao Dai
- Tianyu Guo
- Kai Han
- Hailin Hu
- Zihan Jiang
- Xiang Kuang
- Boxun Li
- Yulong Li
affiliations:
- TokenRhythm Technologies
- Infinigence AI
- Tsinghua University
- Peking University
- Alibaba Group
arxiv_id: '2609.08183'
url: https://arxiv.org/abs/2609.08183
pdf_url: https://arxiv.org/pdf/2609.08183
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: 智能体 · 递归自提升 路由引导训练
tags:
- Agentic Training
- Recursive Self-Improvement
- Curriculum Learning
- On-Policy Distillation
- LLM Routing
one_liner: 提出路由引导的智能体后训练框架，落地递归自提升机制，缩小小模型与大模型性能差距
practical_value: '- 可复用路由分级信号做训练课程设计，将业务现有多模型路由的能力需求打分用于训练样本排序，实现从易到难的课程学习，避免小模型直接学习高难度样本效果差的问题

  - 可迁移用户轮次训练单元构造方法，保留智能体交互上下文、工具调用、推理链，仅对当前轮assistant输出计算损失，适合多轮对话、导购Agent、智能客服的SFT训练，提升交互连贯性

  - 可借鉴「评价-选择-更新」闭环设计，将业务线上的智能体交互失败Case、用户反馈自动回灌到训练集，定向补充薄弱场景样本，实现模型持续迭代，减少人工标注工作量

  - 路由引导的On-Policy Distillation方法可直接复用，用大模型作为教师对小模型自主生成的交互前缀做监督，比离线固定轨迹训练更贴合实际部署分布，提升小模型工具调用、多轮交互能力，降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归自提升（RSI）是AI系统自主迭代的核心方向，但此前缺乏可落地的闭环机制，人工标注训练数据存在规模上限，通用小模型的工具调用、多轮交互、任务闭环能力弱，而大模型推理成本过高，亟需一套可利用线上交互数据自动迭代的训练框架，缩小小模型与大模型的性能差距。
### 方法关键点
- 数据构造：将路由管控层的交互轨迹按用户轮次拆分为训练单元，保留上下文、工具调用、推理链，经过结构校验、6维语义评估、子场景标签化后进入训练集，用路由的C0~C3四级能力需求打分作为样本排序依据。
- 训练流程：先开展三阶段课程式SFT，逐步引入高难度样本；再做路由引导的On-Policy Distillation，由教师模型在学生自主生成的交互前缀上提供监督，缩小训练与部署的分布偏差。
- 闭环设计：基于模型能力缺陷画像动态调整下一轮训练集构成，形成「线上交互-数据回灌-模型训练-上线迭代」的完整RSI闭环。
### 关键结果
在覆盖智能体、工具调用、编码、指令遵循的10个基准上测试：4B模型经过训练后平均得分从58.94提升至64.87，9B模型从65.60提升至69.04，4B微调后大幅缩小与9B基模的性能差距；采用线上路由轨迹训练比使用公开合成智能体数据的平均得分高6.26个百分点。
### 核心启示
路由管控层的日常运行已经自带了递归自提升需要的所有信号：交互轨迹做训练数据、路由打分做难度标签、执行结果做缺陷反馈，无需额外构建复杂的自迭代基础设施。
