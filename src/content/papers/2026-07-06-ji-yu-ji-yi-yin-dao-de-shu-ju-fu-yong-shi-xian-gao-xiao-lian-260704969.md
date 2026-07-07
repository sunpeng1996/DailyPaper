---
title: 'Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM
  Training'
title_zh: 基于记忆引导的数据复用实现高效LLM训练
authors:
- Jingwei Zuo
- Cong Zeng
- Ilyas Chahed
- Maksim Velikanov
- Dhia Eddine Rhaiem
- Pasquale Balsebre
- Abhay Kumar
- Younes Belkada
- Hakim Hacid
affiliations:
- Technology Innovation Institute, Abu Dhabi, UAE
arxiv_id: '2607.04969'
url: https://arxiv.org/abs/2607.04969
pdf_url: https://arxiv.org/pdf/2607.04969
published: '2026-07-06'
collected: '2026-07-07'
category: Training
direction: LLM训练 · 多轮数据复用优化
tags:
- Data Reuse
- Multi-epoch Training
- Memorization Window
- Efficient LLM Training
- Training Scheduling
one_liner: 提出记忆窗口框架指导数据复用调度，打破传统4 epoch复用限制，提升有限高质量数据下LLM训练效率
practical_value: '- 训练垂直领域LLM（如电商导购/广告文案生成LLM）时，可复用高质量行业数据远超过传统4 epoch限制，只要控制两次复用的间隔≥模型记忆窗口即可避免过拟合

  - 可通过简单的rollback loss方法快速估算目标场景下模型的记忆窗口，无需复杂的在线逐样本损失跟踪，快速制定多轮训练数据调度策略

  - 训练垂直小模型时，混入少量低质量通用数据（如通用公开语料）可显著提升模型泛化性，仅需增加极低的数据成本

  - 做LLM持续学习（如电商大促前增量训练新商品/活动知识）时，可基于记忆窗口设置旧知识回放间隔，避免灾难性遗忘同时减少冗余计算'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM训练普遍面临高质量数据稀缺瓶颈，传统多epoch训练多采用全局洗牌的固定复用策略，普遍遵循4 epoch复用上限，存在盲目复用导致过拟合或复用不足浪费优质数据的问题，缺乏可量化的原则指导数据复用的时机和轮次。
### 方法关键点
- 定义**Loss Retention Gap**量化样本记忆程度，基于该指标提出「记忆窗口」概念：包含保留窗口（样本被遗忘的最小token间隔）和泛化窗口（复用后出现过拟合的最小token间隔），有效记忆窗口为两者最小值
- 提出间隔复用规则：两次复用间隔<记忆窗口会引发过拟合；间隔≈记忆窗口时复用效率最高；间隔>记忆窗口时复用收益饱和，无额外增益
- 给出安全复用约束：复用间隔≥有效记忆窗口 + 总训练轮次不超过最大安全轮次 + 混入少量低质量数据补充分布多样性
### 关键实验
基于100M参数量Decoder-only Transformer，高质量数据采用0.8B OpenMathInstruct2，低质量数据采用FineWeb，对比不同复用间隔下的MATH500准确率：
1. 测得100M模型记忆窗口为1B~5B token，最优复用间隔约为0.95B token
2. 间隔足够时，高质量数据可安全复用最高190轮，远高于传统4 epoch上限，复用效率与新鲜数据无显著差异
3. 仅混入6%低质量数据，相同训练轮次下准确率较纯高质量数据提升超40%
### 核心结论
当数据复用间隔大于模型记忆窗口时，重复使用高质量数据的边际收益与使用新鲜数据完全一致，无需盲目扩充新数据即可提升训练效率
