---
title: 'LaRec: Unleashing LLM-based Latent Reasoning for Generative Recommendation'
title_zh: LaRec：基于LLM隐式推理的高效生成式推荐框架
authors:
- Yu Xia
- Zihan Lin
- Wei Yang
- Rui Zhong
- Cheng Chen
- Huan Ren
- Yao Hu
affiliations:
- University of Chinese Academy of Sciences
- Xiaohongshu
arxiv_id: '2607.24617'
url: https://arxiv.org/abs/2607.24617
pdf_url: https://arxiv.org/pdf/2607.24617
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · LLM隐式推理优化
tags:
- Generative Recommendation
- Latent Reasoning
- LLM4Rec
- RL Alignment
- Contrastive Learning
one_liner: 提出两阶段训练的LaRec生成式推荐框架，用LLM隐式推理兼顾推荐效果与低延迟
practical_value: '- 落地LLM生成式推荐可直接复用两阶段训练范式：先通过显式CoT蒸馏做隐式预训练保证推理逻辑正确性，再做RL调优，推理延迟比显式CoT降低80%以上，满足线上吞吐要求

  - 兴趣探索场景可借鉴锚定探索思路：基于用户历史交互item的语义向量构建个性化高斯混合分布作为扰动源，避免随机噪声导致的推荐结果偏离用户兴趣域

  - RL调优阶段可直接复用复合奖励设计：采用「是否命中的稀疏奖励+预测item与目标item语义相似度的稠密奖励」组合，解决推荐任务反馈稀疏导致的RL收敛慢问题

  - 可快速上线验证：将LaRec输出的用户隐式推理向量作为新增召回通道的Query向量，实测能提升电商/广告场景转化2%+，改造成本低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强推荐方案依赖显式CoT推理，会生成大量冗余推理文本，延迟高达数秒无法满足线上业务高吞吐要求；已有的隐式推理方案存在两大核心痛点：一是仅靠最终推荐标签提供稀疏监督，中间隐式推理步骤缺乏约束易退化为浅层模式匹配，二是确定性推理路径无法覆盖用户多元兴趣，推荐效果上限低。

### 方法关键点
- 隐式预训练阶段：设计双对齐约束，step-level对齐将大模型生成的显式CoT推理状态作为监督信号，通过InfoNCE损失将显式推理逻辑蒸馏到隐空间；process方向对齐约束每步隐状态更新方向指向目标item语义，避免语义空转。
- 个性化RL调优阶段：基于用户历史交互item的语义向量构建个性化高斯混合分布，从该分布采样推理初始扰动实现锚定探索，避免随机噪声破坏预训练得到的推理逻辑；采用GRPO算法做强化对齐，复合奖励由命中指示+item语义相似度组成，兼顾稀疏反馈和稠密引导。

### 关键结果
在3个公开数据集+小红书工业数据集上对比11个基线：工业数据集H@10达0.409，较次优基线提升1.7%；推理延迟仅0.67s/样本，比显式CoT低83%，与无推理的LLM推荐延迟基本持平；线上A/B测试作为新增召回通道，广告转化提升2.93%、曝光提升0.46%。

### 核心结论
隐式推理是LLM推荐实现效果与效率平衡的可行落地方向，核心是用显式知识锚定推理逻辑，用个性化RL平衡兴趣探索与推荐精准度。
