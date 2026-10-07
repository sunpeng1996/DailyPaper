---
title: 'HuatuoGPT-3: RL-Only Domain Adaptation from Base Models'
title_zh: HuatuoGPT-3：基于纯RL范式的大模型领域自适应方法
authors:
- Junying Chen
- Xinyuan Xie
- Ziniu Li
- Wenyuan Gu
- Jianquan Li
- Xiang Wan
- Guangjun Yu
- Ruoyu Sun
- Haizhou Li
- Benyou Wang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Research Institute of Big Data
- Shenzhen Loop Area Institute
- National Health Data Institute, Shenzhen
arxiv_id: '2610.05966'
url: https://arxiv.org/abs/2610.05966
pdf_url: https://arxiv.org/pdf/2610.05966
published: '2026-10-04'
collected: '2026-10-07'
category: Training
direction: 大模型领域自适应 · RL训练优化
tags:
- RL
- Domain Adaptation
- LLM Training
- GRPO
- Medical LLM
one_liner: 提出单阶段纯RL领域自适应框架OnePO，仅用20K样本实现医疗领域效果超SFT+RL
practical_value: '- 训练垂直领域Agent（如电商导购、客服Agent）时，可复用OnePO纯RL范式替代传统SFT+RL，避免SFT导致的输出多样性下降，同时降低多阶段训练的复杂度

  - 可借鉴Adaptive Objective Evolution的概率floor+梯度重缩放机制，解决RL训练初期低概率高质量token梯度消失问题，加速冷启动阶段的领域知识吸收

  - 可复用Teacher Retirement机制，仅当教师输出reward超过当前策略最优输出时才保留，避免被劣质教师输出锚定，让策略有机会探索更优解

  - 做垂直场景RL训练时，可混合可验证奖励（如电商场景的点击、转化）和rubric评分奖励（如文案合规、用户体验），实现效果的均衡提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统LLM领域自适应采用SFT+RL多阶段流程，SFT会限制后续RL的探索多样性，还会增加优化复杂度、加剧模型遗忘；纯on-policy RL存在冷启动慢的问题，标准混合策略RL则存在「梯度饥饿」（初期高质量教师token梯度弱、学习速度慢）和「教师分布锚定」（后期过时教师输出拖慢优化）两个核心缺陷，亟需更高效的单阶段RL自适应方案。

### 方法关键点
- 提出OnePO单阶段RL自适应框架，将教师输出作为 transient 指导，初期强化学习、后期自动淘汰，无需手动调度
- Adaptive Objective Evolution：给教师token概率加floor，对低概率正优势token做梯度重缩放，解决梯度饥饿，学习效率达到SFT级别，训练后期自动切换为标准GRPO
- Teacher Retirement：仅当教师输出的reward严格超过同批次on-policy输出的最大reward时才保留，避免教师分布锚定，后期自动退化为纯on-policy RL

### 关键实验
基于20K医疗领域样本训练，对比SFT+RL、纯RL baseline，OnePO在HealthBench Total上达到67.2，比SFT+RL高2.7分，比纯RL高7.4分；基于OnePO训练的HuatuoGPT-3 27B在HealthBench Professional上达到71.4，超过GPT-6 Astra。

### 核心结论
只要设计合理的教师引导机制，纯RL训练完全可以替代SFT+RL的多阶段流程，实现更高效率、更好效果的领域自适应。
