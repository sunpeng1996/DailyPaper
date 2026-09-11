---
title: 'T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks'
title_zh: T1：面向长序列任务的终端Agent强化学习框架
authors:
- Junyao Yang
- Yucheng Shi
- Zhongzhi Li
- Ruhan Wang
- Zongxia Li
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent Hy Foundation Model Frontier
- National University of Singapore
- University of Georgia
- Indiana University
- University of Maryland, College Park
arxiv_id: '2609.11042'
url: https://arxiv.org/abs/2609.11042
pdf_url: https://arxiv.org/pdf/2609.11042
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: 长序列终端Agent 强化学习优化
tags:
- Agent
- MoE
- Reinforcement Learning
- Long-Horizon Task
- Reward Engineering
one_liner: 122B参数量MoE终端强化学习Agent，通过训练对齐和密集奖励提升长周期任务性能
practical_value: '- 多轮工具调用类Agent（如电商导购Agent、运维Agent）做RL训练时，可复用TITO+R3机制解决训练-推理token/路由漂移问题，大幅提升MoE模型RL训练稳定性

  - 长周期多步决策场景（如推荐系统多轮转化优化、用户生命周期运营）的奖励设计可参考：放弃稀疏二元奖励，用可验证的分步骤绝对完成量作为密集过程奖励，大幅提升样本利用效率

  - MoE RL训练时可关闭负载均衡损失，用路由回放保证训练-推理专家选择对齐，避免梯度无效更新；同时预热critic（学习率设为actor的10-30倍）快速提升价值函数拟合精度

  - 训练任务构造时可引入多维度质检（指令-验证器对齐占最高权重），避免训练数据存在隐藏规则、验证不公等问题，保证RL学到的是泛化能力而非benchmark过拟合'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent正向长周期任务（如编码、系统运维、多轮导购）演进，核心面临两大痛点：一是MoE大模型RL训练时，训练与推理侧的token序列、专家路由选择不一致，导致梯度更新指向错误参数，训练不稳定；二是长序列任务传统稀疏二元奖励样本利用率极低，模型难以收敛，无法有效学习长程决策能力。

### 方法关键点
- 训练对齐机制：提出TITO（Token-In-Token-Out）对齐多轮交互的token序列，保证训练侧输入与推理侧采样token完全一致，损失区域token漂移率为0；提出R3（Rollout Routing Replay）记录推理时每层的专家选择，训练时直接回放，消除MoE路由漂移
- 密集奖励设计：放弃二元完成奖励，用任务验证器输出的通过断言绝对数量作为密集过程奖励，固定全局缩放系数，奖励跨任务可比，避免比例奖励弱化难任务的进度信号
- 训练流程优化：构造15k高质量离分布训练任务，经过8维度质检（指令-验证器对齐权重最高20%），避免过拟合；critic提前预热，学习率设为actor的15倍，快速提升价值函数拟合精度

### 关键结果
- 在Terminal-Bench 2.1上，122B MoE的T1得分64.0%，超过GPT-5.4（54.8%）、DeepSeek-V4-Flash（56.9%），接近Claude Opus 4.7（66.1%），为同尺寸最优模型
- 长周期终端任务bench上得分27.9%，超过GPT-5.4、GLM-5.1；调试类任务得分100%，系统运维类得分88.9%
- TITO+R3将训练-推理log概率差从0.021降至0.013，损失区域token漂移率为0

最值得记住的一句话：长周期Agent RL的核心瓶颈不是模型容量，而是训练-推理对齐程度、奖励信号密度与训练数据质量的共同作用
