---
title: 'PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable
  Worlds'
title_zh: PhysEvolve：基于验证器的可执行世界物理推理自进化框架
authors:
- Jinyuan Hu
- Yilei Jiang
- Chen Tang
- Minghong Cai
- Xinran Liu
- Xiangyu Yue
affiliations:
- MMLab, The Chinese University of Hong Kong
arxiv_id: '2610.34921'
url: https://arxiv.org/abs/2610.34921
pdf_url: https://arxiv.org/pdf/2610.34921
published: '2026-10-25'
collected: '2026-10-28'
category: Reasoning
direction: 多模态物理推理 · 自进化训练
tags:
- VLM
- Physical Reasoning
- Self-evolution
- GRPO
- Causal Reasoning
- Simulator
one_liner: 提出无人工标注的自进化框架，通过物理模拟器反事实分支训练提升VLM因果物理推理能力
practical_value: '- 可借鉴「生成+确定性验证器」的自进化范式，在搜索推荐Query改写、商品文案生成场景，用规则引擎/沙箱执行作为确定性验证器，让模型自主生成训练样本，降低人工标注成本

  - 可复用反事实分支构造思路：在推荐干预效果预估、搜索排序归因场景，构造对齐初始条件的对照组分支，生成带因果信号的训练样本，提升模型因果推理能力

  - 可复用GRPO结合自适应课程的训练策略：在LLM4Rec指令微调场景，根据模型在不同任务族的准确率动态调整采样权重，优先训练模型能力边界附近的任务，提升训练效率

  - 避免连续模糊奖励的坑：在RLHF/RLAIF微调场景，尽量用离散确定性反馈替代连续相似度打分，避免奖励黑客，保证模型真正学到目标能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM在物理动态、因果干预、反事实推理上表现远差于静态视觉识别任务，核心瓶颈是带标注的干预级训练数据极度稀缺：真实视频仅能捕捉已发生的事实轨迹，无法观测反事实结果；直接将代码/数学领域的自进化范式迁移到物理场景会出现两个致命缺陷：单轨迹执行无法生成因果干预类训练任务，连续相似度奖励会诱导奖励黑客，导致模型实际正确率停滞不前。
### 方法关键点
- 设计验证器锚定的自进化框架PhysEvolve，共享VLM同时承担Proposer（生成可执行物理世界程序和证据Schema）和Solver（回答物理推理问题）角色，以确定性物理模拟器作为验证器，严格隔离策略探索和标签生成链路，避免标注污染
- 干预驱动的任务合成：对Proposer生成的候选世界，模拟器先验证合法性并冻结场景参数，再执行相同初始条件下的基线轨迹和移除指定物体的反事实分支轨迹，基于轨迹差异自动生成绑定离散标准答案的多选择推理问题
- 联合进化训练：用GRPO同时优化Proposer和Solver的共享参数，基于各推理意图的实时准确率动态调整任务采样权重，优先训练处于模型能力边界的任务，提升训练效率
### 关键结果
基于Qwen3-VL-8B-Instruct底座训练，无人工标注干预数据：
- PhysBench基准上，投掷类任务准确率提升8.8pp，判断类任务提升5.1pp
- 仅在刚体模拟数据上训练的模型零样本迁移到包含布料、流体、软体的ContPhy数据集，反事实移除任务提升7.4pp，Goal-Pit任务提升24.4pp，表现超过32B参数量的底座模型
- 真实视频数据集CausalPhys上，预期类任务提升2.5pp，干预类任务提升2.3pp
> 最值得记住的结论：将连续的动态过程转化为离散的验证器合约，是避免自进化训练中因果盲和奖励黑客问题的核心
