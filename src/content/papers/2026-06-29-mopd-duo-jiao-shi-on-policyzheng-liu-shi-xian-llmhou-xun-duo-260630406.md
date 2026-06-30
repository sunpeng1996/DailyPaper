---
title: 'MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM
  Post-Training'
title_zh: MOPD：多教师On-Policy蒸馏实现LLM后训练多能力整合
authors:
- Wenhan Ma
- Jianyu Wei
- Liang Zhao
- Hailin Zhang
- Bangjun Xiao
- Lei Li
- Qibin Yang
- Bofei Gao
- Yudong Wang
- Rang Li
affiliations:
- Peking University
- Xiaomi LLM Core
- University of Hong Kong
- Renmin University of China
arxiv_id: '2606.30406'
url: https://arxiv.org/abs/2606.30406
pdf_url: https://arxiv.org/pdf/2606.30406
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: LLM后训练 · 多能力整合蒸馏
tags:
- On-Policy Distillation
- LLM Post-Training
- Capability Integration
- Multi-Teacher Distillation
- RL
one_liner: 提出多教师On-Policy蒸馏范式，解决LLM多领域RL能力整合效率低稳定性差问题
practical_value: '- 做多领域大模型能力整合时，可采用该模块化架构：各领域团队独立并行训练专属RL专家教师，解耦开发流程，实现风险隔离，单领域调整不影响全局

  - 工程上可借鉴异步服务部署方案：将每个领域教师部署为独立的prefill服务，教师计算与学生采样并行重叠，几乎不增加训练wall-clock耗时

  - 蒸馏时必须采用同源教师（所有教师从同一初始SFT checkpoint训练而来），分布对齐是训练稳定的核心保障，不要盲目引入能力更强但分布差异大的外部教师

  - 支持多轮迭代优化：可将一轮蒸馏后的整合模型作为新初始化，重新训练领域教师再蒸馏，持续提升模型整体能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM后训练中，推理、代码、工具调用、指令遵循等不同领域都需要定制化RL优化，但现有多能力整合方法都存在明显缺陷：Mix-RL存在跨域干扰，Cascade RL会导致旧能力遗忘，Off-Policy FineTune存在暴露偏差，参数合并效果不稳定，始终无法同时满足稠密优化、on-policy训练、可并行开发三个核心需求，因此需要新的整合范式。

### 方法关键点
- 三阶段流水线：通用SFT得到共享初始化 → 各领域独立并行训练RL专家教师 → 多教师on-policy蒸馏整合到单个学生模型
- 蒸馏设计：用学生自身生成的rollout做训练，按prompt路由到对应领域教师，教师输出token级对数概率，学生优化最小化与教师的反向KL散度，既消除暴露偏差，又提供稠密梯度信号
- 提供两种可落地实现：policy-gradient形式可直接接入现有PPO/GRPO训练框架，top-k蒸馏形式大幅降低计算与存储开销

### 关键实验结果
在Qwen3-30B-A3B上整合数学、指令遵循、软件工程三个领域，对比5种主流基线，MOPD归一化得分0.937，比最强基线Mix-RL高5.5个点，可关闭每个领域91%~95%的学生-教师能力缺口；在工业级309B参数的MiMo-V2-Flash模型上验证，多数基准指标达到甚至超过对应领域单独训练的教师水平；ablation验证了同源教师对训练稳定性的核心作用，多轮迭代可进一步将归一化得分从0.937提升到0.986。

### 核心结论
多领域能力整合在策略空间做路由蒸馏，比权重空间融合、离线微调更稳定高效
