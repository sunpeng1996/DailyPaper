---
title: 'CoDA: Co-Evolution of Data Engines and Action Policies'
title_zh: CoDA：数据引擎与行动策略的协同进化
authors:
- Tianjiao Yu
- Zhilin Ou
- Yifan Shen
- Xinzhuo Li
- Yuanzhe Liu
- Onkar Kishor Susladkar
- Fan Wang
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
- The Chinese University of Hong Kong, Shenzhen
- Amazon
arxiv_id: '2610.22362'
url: https://arxiv.org/abs/2610.22362
pdf_url: https://arxiv.org/pdf/2610.22362
published: '2026-10-14'
collected: '2026-10-18'
category: Other
direction: 具身Agent·数据策略协同进化框架
tags:
- Generative Simulation
- Embodied Agent
- Co-Evolution
- Reward Shaping
- Policy Learning
one_liner: 基于共享异构记忆的CoDA框架，实现仿真数据引擎与具身Agent策略协同进化，提升分布外任务表现
practical_value: '- 共享异构记忆驱动的<数据生成-策略迭代>闭环可直接迁移到推荐系统难负例生成场景：记忆存储排序bad case、负例生成效果、模型精度变化三类信息，动态生成能精准补全排序模型短板的难负例，同等训练数据量下可提升排序效果

  - Text2potential将语义诊断转为分阶段密集监督信号的思路，可解决推荐大模型微调中用户反馈稀疏问题：把用户负反馈（如划走、跳过）的语义归因拆解为多阶段奖励信号，替代单点稀疏反馈，提升微调效率

  - 基于学习进度动态调整训练数据分布的机制，可用于电商Agent的任务训练课程设计：自动匹配当前Agent能力边界的训练数据，避免过难或过易的无效训练，降低训练成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
生成式仿真可自动化构建机器人训练环境，但物理合法的环境未必能有效补全策略短板，核心痛点是无法精准定位适配策略缺陷的训练环境与对应监督信号。
### 方法关键点
1. CoDA框架通过共享异构记忆实现仿真数据引擎与行动策略的协同进化，记忆存储环境构建记录、策略失败Case、训练进度三类异构信息
2. 视觉语言Critic输出的验证后诊断会被编译为两类程序：复现困难场景的生成程序、帮助策略补全短板的训练程序
3. 配套Text2potential模块，将诊断文本转换为动作块价值学习的分阶段势能，为策略更新提供密集监督的同时，保证标准塑形假设下任务最优策略不变
### 关键结果
四类操作任务上，分布外成功率从SFT后的5.3%提升至27.6%，同等生成预算下比最优闭基线高9.5个百分点；LIBERO-Pro数据集上15轮迭代后，位置扰动下成功率从25%升至84%，指令扰动下从1%升至76%。
