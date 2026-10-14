---
title: 'Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards'
title_zh: TEV：基于密集进度奖励的长程智能体训练环境扩量方法
authors:
- Wenbo Hu
- Shraman Pramanick
- Krishna Kumar Singh
- Nanyun Peng
- Kai-Wei Chang
- Yong Jae Lee
affiliations:
- Adobe Research
- University of California, Los Angeles
arxiv_id: '2610.18868'
url: https://arxiv.org/abs/2610.18868
pdf_url: https://arxiv.org/pdf/2610.18868
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 长程智能体 · 训练环境与奖励优化
tags:
- Long-Horizon Agent
- Reward Shaping
- Synthetic Environment
- Reinforcement Learning
- LLM Agent
one_liner: 提出潜世界优先任务合成框架与进度势能奖励塑造，训练长程智能体性能追平GPT-6 Astra等闭源模型
practical_value: '- 任务数据合成可借鉴「潜世界优先」思路：先构造完整的隐式任务状态/流程真值，再生成可见输入和故障场景，从根源避免任务、验证器、真值三者的漂移，适配电商客服/运营Agent、推荐系统模拟环境等场景的合成数据构建

  - 长程任务RL训练可复用PPRS方法：基于任务流程DAG定义每步进度得分，将稀疏终态奖励转换为密集中间奖励，解决GRPO等组归一化RL算法在长任务下信号匮乏的问题，可降低90%以上失败轨迹无法贡献梯度的资源浪费

  - 训练配方可跨尺度迁移：相同的数据集+奖励配置在9B~320B基模型上均能稳定增益，业务侧可先在小参数模型上验证方案再迁移到大模型，大幅降低试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长程智能体训练面临两大核心瓶颈：一是公开长程任务数据集规模极小，多为人工标注的评估集，无大规模可用于训练的语料；二是长任务奖励极度稀疏，仅终态有奖励信号，导致GRPO等主流组相对RL算法的大部分训练批次梯度为0，训练效率极低。

### 方法关键点
- **数据合成**：提出`latent-world-first`范式，先构造包含任务域完整规则、流程DAG、所有中间状态真值的潜世界，再对潜世界做可控渲染、缺陷注入生成Agent可见的任务环境，天然自带每步进度的验证真值，避免传统LLM生成任务的真值漂移问题，基于该范式构建TEV-GYM数据集，包含7个域共1170个验证通过的长程任务，单任务中位数执行时长12.4分钟，是现有公开语料的6倍
- **奖励设计**：提出Progress-Potential Reward Shaping（PPRS），基于潜世界的流程DAG定义每个中间状态的进度势能Φ(st)∈[0,1]，每步奖励为势能变化量，最终总奖励为终态成功信号加λ倍最终势能，既保证终态成功优先级高于中间进度，又让全失败的训练批次也能产生差异化梯度

### 关键结果
TEV-27B在ALE-CM基准上Pass@5达0.28，追平GPT-6 Astra和Claude Opus 5；在TB 4.0-CM基准上Pass@1较基模型提升150%，超过GLM 5.2、Gemini 3.7 Flash；在中长程TB 2.1基准上Pass@1达0.794，匹配Claude Opus 4.8水平。相同配方训练的TEV-320B在TB 4.0-CM上Pass@1达0.37，成为当前最强开源长程Terminal Agent，仅落后于3款顶级闭源模型。

### 核心洞见
长程智能体训练的核心瓶颈不是模型参数规模，而是有真值、带中间进度信号的高质量训练数据，从潜世界倒推生成任务的范式能从根源解决数据和奖励的双重难题。
