---
title: 'EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in
  Conversation'
title_zh: EII-SCL：基于情绪惯性的对话多模态情绪识别方法
authors:
- Zilong Huang
- Kong Aik Lee
- Chong-Xin Gan
- Zezhong Jin
- Ruichen Zuo
- Man-Wai Mak
affiliations:
- The Hong Kong Polytechnic University, Dept. of Electrical and Electronic Engineering
arxiv_id: '2607.17366'
url: https://arxiv.org/abs/2607.17366
pdf_url: https://arxiv.org/pdf/2607.17366
published: '2026-07-19'
collected: '2026-07-24'
category: Multimodal
direction: 多模态对话情绪识别技术
tags:
- Multimodal Emotion Recognition
- Contrastive Learning
- Emotional Inertia
- MERC
- Supervised Contrastive Learning
one_liner: 提出融入情绪惯性先验的监督对比学习模块，无需额外数据即可提升对话多模态情绪识别性能
practical_value: '- 电商客服对话情绪识别、直播观众情绪感知场景，可直接将EII-SCL模块嵌入现有多模态识别模型，无需额外数据即可提升情绪判断准确率

  - 会话式推荐Agent可复用情绪惯性先验思路，在用户意图预测、情绪预判时加入历史会话窗口内的情绪一致性约束，降低情绪跳变误判

  - 时序类推荐任务（如会话推荐、用户行为序列建模）可借鉴该样本构造思路，针对时序惯性特征构造时间窗内正负样本优化对比损失'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前对话多模态情绪识别（MERC）方法多聚焦于建模复杂对话上下文依赖关系，忽略心理学中已被证实的情绪惯性规律对情绪转移的约束作用，导致情绪跳变预测准确率低、整体性能存在瓶颈。

### 方法关键点
1. 提出情绪惯性感知的监督对比学习模块EII-SCL，在时间窗口内构造受惯性影响的正负样本，将情绪惯性作为先验融入对比学习目标，拉近同情绪相邻样本表征、拉远情绪跳变相邻样本表征，强化模型对情绪平稳/跳转的区分度；
2. 模块可无缝集成到现有任意MERC模型中，无需额外补充训练数据，适配性强。

### 关键结果
在IEMOCAP、MELD两个对话情绪识别公开标准数据集上，性能持续超越现有SOTA方法，通用性得到验证。
