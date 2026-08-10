---
title: 'SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task
  Learning for LLMs'
title_zh: 多任务LLM训练范式对比：SFT冲突、RL共存的理论与实证分析
authors:
- Kejian Zhu
- Zhuoran Jin
- Shangqing Tu
- Hongbang Yuan
- Yushi Bai
- Kang Liu
- Juanzi Li
- Jun Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
- 清华大学
arxiv_id: '2608.03573'
url: https://arxiv.org/abs/2608.03573
pdf_url: https://arxiv.org/pdf/2608.03573
published: '2026-08-05'
collected: '2026-08-10'
category: Training
direction: LLM多任务训练 · SFT与RL范式对比
tags:
- Multi-Task Training
- SFT
- RL
- Gradient Interference
- Model Merging
one_liner: 揭示多任务LLM训练中SFT冲突、RL共存的底层机制，提出高效并行RL训练范式
practical_value: '- 多任务微调场景下优先选择RL而非多阶段SFT：RL稀疏正交的参数更新特性可在优化新任务时保留原有能力，适配推荐系统多场景、Agent多技能的持续迭代需求

  - 复用Parallel-RL范式降低多任务训练成本：不同任务独立做RL微调后合并参数，仅需5%样本做轻量适配即可保留97%+的单任务性能，大幅降低算力与调度成本

  - 电商搜索推荐多目标优化场景可借鉴RL的低梯度干扰特性，替代传统多目标SFT缓解点击率、转化率、复购率等目标间的冲突问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多任务训练是LLM拓展泛化能力的核心路径，但现有范式选择缺乏理论支撑：SFT需依赖混合数据训练规避灾难性遗忘，而RL可直接采用多阶段训练仍实现稳定涨点，两者行为差异的底层机制尚未明确，严重制约多任务训练的效率与效果优化。
### 方法关键点
- 实证层面：对比SFT与RL的参数更新特性，RL更新幅度比SFT小2个数量级，仅20%参数产生有效更新，且不同任务的更新向量余弦相似度接近1e-5，近乎正交
- 理论层面：推导得出SFT的任务间梯度干扰为范数受限，由梯度绝对大小决定；RL的梯度干扰为方差受限，仅由同输入下多轮采样的残差方差决定，天然抑制跨任务冲突
- 工程层面：提出Parallel-RL范式，多任务独立并行完成RL训练后，通过TIES、SVD等策略合并参数，仅需5%训练样本做轻量后适配即可得到多任务能力兼备的模型
### 关键实验
基于DeepSeek-R1-Distill-Qwen 1.5B/7B基座，覆盖数学、科学、逻辑、代码4类推理任务，对比混合数据SFT、多阶段SFT、混合数据RL、多阶段RL等基线：多阶段SFT性能相比基座平均下降23.1%，多阶段RL平均提升24.9%；Parallel-RL可保留97%+的单任务RL性能，Adapted Parallel-RL甚至超过单任务模型，平均性能比基座提升10.7%。
### 核心结论
多任务训练场景下，SFT优化会产生严重的任务间参数冲突，而RL的稀疏正交更新特性可实现不同任务能力的稳定共存。
