---
title: 'Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations'
title_zh: 兼顾正确性与类人性：结合可验证奖励与人类示范的LM训练方法
authors:
- Mehul Damani
- Isha Puri
- Idan Shenfeld
- Jacob Andreas
affiliations:
- MIT EECS
arxiv_id: '2607.01181'
url: https://arxiv.org/abs/2607.01181
pdf_url: https://arxiv.org/pdf/2607.01181
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: 大模型训练 · 可验证奖励与对抗学习融合
tags:
- RLVR
- Adversarial Training
- GRPO
- Reward Hacking
- Imitation Learning
one_liner: 提出VARL对抗训练框架，结合可验证RL奖励与人类示范，保留正确率的同时优化类人非可验证属性
practical_value: '- 做生成式推荐文案/商品标题优化时，可复用乘法奖励设计：先过点击率/转化率等可验证指标门槛，再用判别器奖励对齐人类偏好的风格，无需额外调权重

  - 做Agent工具调用/API调用训练时，可引入类人示范判别器，大幅降低奖励黑客行为（比如故意篡改返回值骗奖励），效果远优于KL正则

  - 做UGC/营销内容生成类任务时，可先把输出映射到高层语义特征空间（如风格、结构、主题标签）再训判别器，避免判别器只抓字数、格式等表面特征，训练更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）能大幅提升代码、数学推理等任务的正确率，但仅优化可量化指标，完全忽略风格、结构、类人性等非可验证属性，会出现多样性崩塌、输出生硬、奖励黑客等问题；而SFT能拟合人类示范分布，但正确率远低于RLVR，两类方法缺陷互补，亟需能同时兼顾两类目标的训练范式。

### 方法关键点
- 提出VARL框架，协同训练生成器与判别器：生成器用GRPO做RL训练，奖励为可验证正确性奖励与判别器输出的乘积，只有正确输出才会获得类人性奖励，天然优先保障正确性，无需额外调权重
- 判别器学习区分人类示范与模型生成的输出，可通过自定义特征映射φ（如代码的编辑特征、故事的叙事结构特征）控制需要对齐的类人属性，避免判别器抓取表面无关特征
- 对比KL正则的token级约束，判别器是序列级约束，能更精准捕捉输出的整体结构、风格等属性

### 关键结果
在三个任务上对比SFT、RLVR、仅判别器训练等基线：
1. 代码bug修复：VARL正确率达65%，和RLVR持平，同时代码编辑距离和人类示范几乎一致，远低于RLVR的大幅重写
2. 故事生成：VARL对人类故事的胜率达22%，接近RLVR的23%，同时特征熵比RLVR高18%，和人类分布的TVD距离比RLVR低40%
3. Countdown-Code奖励黑客基准：RLVR奖励黑客率达99%，VARL仅1%，同时正确率达60%，接近用金标准奖励训练的Oracle

最值得记住的一句话：乘法门控的可验证奖励+对抗判别器范式，是同时兼顾任务正确性与类人非可验证属性的低门槛、高鲁棒性方案，效果远优于SFT+RLVR加KL正则的传统方案。
