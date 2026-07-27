---
title: 'Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement
  Learning Mitigates Task Conflicts in LLMs'
title_zh: 强化学习缓解大语言模型合并任务冲突的系统性分析
authors:
- Zixuan Ren
- Jinliang Lu
- Junhong Wu
- Yang Zhao
- Dai Dai
- Hua Wu
- Haifeng Wang
- Chengqing Zong
affiliations:
- 中科院自动化所多模态人工智能系统全国重点实验室
- 中国科学院大学人工智能学院
- 百度
arxiv_id: '2607.22039'
url: https://arxiv.org/abs/2607.22039
pdf_url: https://arxiv.org/pdf/2607.22039
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: LLM训练范式 · 模型合并优化
tags:
- LLM
- Reinforcement Learning
- Model Merging
- Supervised Fine-tuning
- Task Conflict
one_liner: 实证RL训练的LLM模型合并后性能损失远低于SFT，揭示三大底层机制
practical_value: '- 多任务LLM基建优先选择RL范式微调各垂直任务（如商品文案生成、排序、Query理解），合并后性能损失比SFT低10%+，适合搭建统一多能力服务

  - 做LoRA多任务合并时，RL微调的LoRA权重冲突更少，可省略复杂的DARE/TIEs剪枝流程，工程上直接平均就能达到不错效果，降低合并复杂度

  - Agent多工具能力整合场景下，RL微调的单能力模块合并后能力保留率更高，无需重新训练统一底座，大幅节省算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前模型合并是低成本整合多个垂直领域LLM能力的核心方案，但此前研究均聚焦合并策略优化，忽略了训练范式对合并效果的影响；SFT训练的模型合并后任务冲突严重，性能掉点幅度大，亟需找到更适配模型合并的训练范式。

### 方法关键点
- 控制变量对比SFT与三类主流RL算法（PPO、GRPO、REINFORCE++）微调的模型，在不同合并策略下的任务保留效果
- 从on-policy数据特性、RL训练目标自适应衰减更新、正负样本联合优化三个维度，结合理论推导与实证实验分析RL缓解任务冲突的底层机制
- 提出冲突范数量化不同任务参数更新方向的冲突程度，支撑机制验证

### 关键实验
跨数学、代码、指令跟随、逻辑谜题、排序5类任务，采用Llama-3.2-3B、Llama-3.1-8B、Mistral-Small-24B三个底座，对比Averaging、TIEs、Task Arithmetic、DARE四种合并策略：SFT训练的模型合并后平均性能损失达18%~22%，单任务最高掉点65%；RL训练的模型用TIEs合并后平均损失仅7.1%，指令跟随任务几乎零损失，且该优势不受RL算法类型、底座模型大小影响。

### 核心结论
RL微调的参数更新天然与其他任务更正交，是低成本构建多能力统一LLM的最优训练范式。
