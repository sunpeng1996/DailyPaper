---
title: Discretizing Reward Models
title_zh: 奖励模型离散化：缓解过敏感性与奖励黑客效应
authors:
- Vijay Viswanathan
- Shiqi Wang
- Devamanyu Hazarika
- Chirag Nagpal
- Tongshuang Wu
- Graham Neubig
- Yuning Mao
affiliations:
- Carnegie Mellon University
- Meta Superintelligence Labs
arxiv_id: '2606.21795'
url: https://arxiv.org/abs/2606.21795
pdf_url: https://arxiv.org/pdf/2606.21795
published: '2026-06-18'
collected: '2026-06-27'
category: Training
direction: RLHF训练 · 奖励模型离散化优化
tags:
- Reward Model
- Discretization
- RLHF
- MC Dropout
- Reward Hacking
one_liner: 提出基于MC dropout的奖励聚类方法，离散化连续奖励，缓解RM过敏感，提升RL策略效果
practical_value: '- 电商/广告推荐的排序/奖励模型（如pCVR、用户满意度模型）可直接复用reward clustering思路：用MC dropout估计预测不确定性，对连续得分做层次聚类离散化，缓解模型对同等质量item的过敏感问题，减少reward
  hacking（如广告主利用边缘特征刷分）

  - 模型评估不要只看AUC/准确率（区分好坏的能力），需新增「同档位得分一致性」指标（对应论文specificity），避免模型靠学习噪声特征刷高离线指标却损害线上业务稳定性

  - 工程上MC dropout后处理无需重训模型，论文验证T=4次前向、dropout率0.02即可生效，仅增加15%左右推理/训练耗时，适合业务快速灰度验证'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前reward model (RM) 广泛用于RLHF等强化学习场景，但普遍存在**过敏感性**：对效用完全相同的响应给出差异极大的连续分数。这些虚假的分数差异会被策略模型 exploit 形成reward hacking，最终导致策略退化。现有RM评估体系仅关注“区分好坏响应的准确率”，完全忽略了“同等质量响应得分是否一致”的维度，导致很多离线指标很高的RM在线上RL训练中表现很差。

### 方法关键点
- 提出两套独立的RM评估维度：**discriminative ability**（正确区分不同效用响应的概率）和**specificity**（同等效用响应得分一致的比例，是过敏感性的补集），并证明传统准确率是两者的加权和
- 提出训练无关的**reward clustering**算法：用Monte Carlo (MC) dropout对神经RM做T次随机前向，估计每个奖励的预测均值和方差；基于“两个奖励差值在Δ内的概率大于p*”的规则做层次聚类，同一聚类内的响应赋予相同的离散整数奖励（按聚类均值排序）
- 理论证明：存在最优离散化阈值，可在几乎不损失discriminative ability的前提下，将specificity提升到接近1，显著优于原始连续奖励的表现

### 关键实验结果
- 验证集：RewardBench 2的Ties子集（专门验证同等质量响应的得分一致性），RL训练覆盖IFEval、GSM8K、MATH + 30K WildChat无标注prompt
- 对比baseline：原始RM、reward clipping、dropout ensemble、binary thresholding
- 核心数字：4个主流RM上，reward clustering均提升discriminative ability与specificity的平均分；RL训练中离散化奖励从未显著差于原始奖励，10/24的场景有显著提升——低KL惩罚下Skywork V1在GSM8K上准确率从77.0升至84.4，ArmoRM在IFEval上从53.0升至77.8；训练耗时仅增加15%

> 最值得记住的一句话：连续奖励的「细粒度」很多时候是过敏感的噪声，将奖励离散化为等价档位，反而能让RL学到更鲁棒的策略
