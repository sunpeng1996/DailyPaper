---
title: Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action
  Models
title_zh: 基于故障库自进化的视觉-语言-动作模型运行时反馈学习方法
authors:
- Mingyue Cui
- Zheyuan Liu
- Yihan Zhu
- Zheyuan Zhang
- Meng Jiang
affiliations:
- University of Notre Dame
arxiv_id: '2609.39820'
url: https://arxiv.org/abs/2609.39820
pdf_url: https://arxiv.org/pdf/2609.39820
published: '2026-09-29'
collected: '2026-10-05'
category: Training
direction: VLA模型 · 自进化训练优化
tags:
- VLA
- LoRA
- Runtime Feedback
- Self-Evolution
- Policy Optimization
one_liner: 提出四阶段FailBank框架，将VLA模型运行时反馈转化为持久策略优化，兼顾成功率与安全成本
practical_value: '- 可复用FailBank的运行时错误收集+结果感知准入机制，将推荐/Agent系统的线上runtime badcase转化为LoRA微调的监督数据，避免临时纠错治标不治本的问题

  - 可借鉴「成功未修正动作作为静默锚点」的训练思路，微调时保留模型原有正确能力，防止微调后出现能力灾难遗忘

  - 对于线上有实时拦截/纠错模块的系统，可参考本框架将拦截规则的反馈转化为模型迭代的监督信号，降低规则与模型的持续冲突'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型在复杂环境部署时存在任务成功率与安全成本的平衡问题，传统运行时拦截仅做临时动作修正，不更新底层策略，会导致策略与拦截规则持续冲突，阻碍任务完成。

### 方法关键点
提出四阶段FailBank自进化框架：1. 固定CBF安全模块作为观测教师，在策略执行时生成反事实修正方案；2. 结果感知准入模块筛选有效修正作为训练目标，同时保留未被修正的成功动作作为静默锚点；3. 基于筛选后的数据做 guarded LoRA 微调，实现策略的持久优化。

### 关键结果
在VLA-Arena benchmark测试，相比基线策略，两个VLA backbone的任务成功率分别提升8.5、6.9个百分点，策略累积成本分别降低35.6%、23.8%；相比仅用运行时拦截方案，成功率分别提升25.4、9.5个百分点，累积成本基本持平。
