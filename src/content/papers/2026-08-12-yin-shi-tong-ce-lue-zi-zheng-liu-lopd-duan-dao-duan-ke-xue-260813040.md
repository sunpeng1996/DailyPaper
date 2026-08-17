---
title: Latent On-Policy Self-Distillation
title_zh: 隐式同策略自蒸馏（LOPD）：端到端可学习的Agent自进化训练框架
authors:
- Guibin Zhang
- Jiayang Lyu
- Ran Sun
- Xinlei Yu
- Haoyu Zhao
- Qibing Ren
- Shuicheng Yan
affiliations:
- National University of Singapore
- Beijing University of Posts and Telecommunications
- Shanghai Jiao Tong University
arxiv_id: '2608.13040'
url: https://arxiv.org/abs/2608.13040
pdf_url: https://arxiv.org/pdf/2608.13040
published: '2026-08-12'
collected: '2026-08-17'
category: Agent
direction: Agent自进化 · 同策略自蒸馏优化
tags:
- Self-Distillation
- On-Policy Learning
- Agent Evolution
- Latent Representation
- OPSD
one_liner: 将OPSD的人工设计特权上下文改为端到端可学习隐式表征，实现更高效的Agent自进化
practical_value: '- 电商/广告Agent自蒸馏训练时，可替换人工设计的特权上下文，用LoRA+QFormer将历史成功轨迹压缩为隐式token输入教师模型，避免人工上下文适配性差的问题

  - 自蒸馏流程中新增特权边际约束，要求教师对学生生成token的对数概率优势不低于预设阈值，可直接复用于各类LLM对齐场景，避免教师向学生坍缩

  - 业务高频迭代场景可采用LOPD降低对齐成本：仅需GRPO/Skill-SD 30%的rollout预算即可达到更优性能，大幅减少采样开销

  - 训练完成后仅保留学生模型部署，推理侧无检索、隐式编码等额外组件，完全不增加线上延迟，可直接落地生产'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有同策略自蒸馏（OPSD）是Agent自进化的核心路径之一，但依赖人工设计的离散特权上下文（如正确答案、推理轨迹、成功rollout等），受限于设计者的先验经验，无法自适应不同任务、不同训练阶段的学生模型需求，限制了端到端学习能力和可扩展性。
### 方法关键点
- 特权上下文重构：将人工设计的离散特权上下文替换为端到端可学习的连续隐式表征，从历史成功轨迹库检索相关经验，通过冻结主干+LoRA编码器、QFormer压缩器生成固定长度的隐式token，作为自教师的额外输入
- 蒸馏流程：学生仅基于任务与交互历史生成on-policy轨迹，教师结合隐式特权上下文对学生访问过的每个前缀做token级监督，采用reverse-KL匹配top-M加尾桶的token分布，避免全词表蒸馏的冗余开销
- 稳定训练优化：引入特权边际对偶约束，要求教师对学生生成token的对数概率优势不低于阈值，同时加隐式上下文锚定损失防止漂移，避免教师向学生坍缩的 trivial 解
### 关键实验结果
在3个骨干模型（Qwen3-4B/8B、Olmo3-7B）、7个benchmark（工具调用类EnvScaler、BFCL-v3、ACEBench，代码生成类LiveCodeBench、HumanEval+、MBPP+）上对比GRPO、OPSD、SDPO、Skill-SD等主流基线，10组骨干-基准组合中LOPD全部取得最优性能，仅需GRPO、Skill-SD 30%的rollout预算即可超过二者性能。
### 核心结论
经验不应该被当做人工指定的输入artifact，而应该作为可学习的监督基底，让模型自主决定要保留哪些经验、如何编码为有效监督信号。
