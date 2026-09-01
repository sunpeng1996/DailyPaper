---
title: 'Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence'
title_zh: 突破人类监督限制的大推理模型规模化：通向超智能的路径
authors:
- Zhiqin Yang
- Jingwen Fu
- Yuhan Liu
- Hengyu Liu
- Yonggang Zhang
- Kainan Cao
- Zizhuo Zhang
- Chenxin Li
- Ruibin Yuan
- Jiahao Pan
affiliations:
- The Hong Kong University of Science and Technology
- Xi'an Jiaotong University
- The Chinese University of Hong Kong
- The University of Hong Kong
- Tencent Hunyuan
arxiv_id: '2608.31075'
url: https://arxiv.org/abs/2608.31075
pdf_url: https://arxiv.org/pdf/2608.31075
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 大推理模型 · 无人类监督规模化训练
tags:
- Large Reasoning Model
- Reinforcement Learning
- Reward Model
- GRPO
- Autonomous Learning
one_liner: 提出人类监督退去五阶段阶梯框架，梳理大推理模型脱离人类监督规模化的方法、风险与评估体系
practical_value: '- 电商/广告Agent的RL训练可参考L0-L2的奖励演化路径：先做单样本人工标注打标（L0），再训练通用可复用的领域奖励模型/LLM
  judge（L1），最终逐步替换为点击、转化等规则可校验的环境反馈，降低对人工标注的依赖

  - 训练推荐场景大模型（如文案生成、选品推理）时，可复用共识奖励方法：同query多采样结果做多数投票作为伪标签，搭配熵正则防止训练崩溃，大幅减少标注成本

  - 可复用GRPO的无critic优化方案，避免PPO训练需要额外价值网络的显存开销，适配推荐/广告场景大模型的低资源训练需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大推理模型（LRM）在数学、代码等可校验任务上通过带可验证奖励的强化学习（RLVR）取得了显著进展，但推广到开放域、多轮Agent任务时，人工标注成本随推理步数指数级上升，无法跟上模型生成经验的规模与复杂度增长，亟需探索逐步脱离人类监督的规模化训练路径。
### 方法关键点
- 从「奖励来源」和「经验生成」两个核心维度，构建L0-L4的人类监督退去阶梯框架：L0单样本人工标注监督、L1复用人类规则的奖励模型/LLM Judge、L2无人类直接评估的自生成奖励（模型置信度、共识投票、参考锚定、环境反馈）、L3自适应生成任务/训练课程、L4策略-奖励-经验完全自主协同进化
- 系统梳理各层级的技术实现方案，覆盖过程奖励模型（PRM）、自训练验证器、无critic强化学习优化器（GRPO）、共识奖励、环境可执行反馈等数十类主流方法
- 提出三维评估体系，分别从策略能力、反馈保真度、经验质量三个维度定位奖励黑客、反馈漂移、课程崩溃等无监督训练的典型风险
### 关键结果
作为综述类研究，梳理了100+现有工作的性能：GRPO相比传统PPO减少40%训练显存开销，无标注共识奖励方法在数学推理任务上可保留90%以上全监督性能，规则化RLVR方案在GSM8K数学数据集上最高达到92%精度。
### 核心结论
人类监督的退去不是完全移除人类影响，而是将人力投入从逐样本标注转移到目标定义、安全约束和独立审计层面，在实现能力规模化的同时保留系统可控性。
