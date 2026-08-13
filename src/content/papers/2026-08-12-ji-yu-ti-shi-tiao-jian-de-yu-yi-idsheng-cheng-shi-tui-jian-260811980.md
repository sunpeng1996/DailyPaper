---
title: 'HCGRec: Hint-Conditioned Generative Recommendation with Semantic IDs'
title_zh: 基于提示条件的语义ID生成式推荐框架HCGRec
authors:
- Kangning Zhang
- Haotian Fang
- Xukun Luo
- Hao Yin
- Yang Gao
- Peng Yan
- Weiwen Liu
- Weinan Zhang
- Yong Yu
affiliations:
- Shanghai Jiao Tong University
- Meituan
arxiv_id: '2608.11980'
url: https://arxiv.org/abs/2608.11980
pdf_url: https://arxiv.org/pdf/2608.11980
published: '2026-08-12'
collected: '2026-08-13'
category: GenRec
direction: 生成式推荐 · Semantic ID 训练优化
tags:
- Generative Recommendation
- Semantic ID
- GRPO
- Sequential Recommendation
- Reward Optimization
one_liner: 针对语义ID生成式推荐GRPO训练零优势样本问题，用前缀提示+信用分解提升训练效率与推荐效果
practical_value: '- 语义ID生成式推荐的GRPO后训练阶段，可直接复用本方法的离线可达性诊断逻辑：先检测SFT checkpoint下每个训练样本是否能生成目标item，仅给不可达样本加最短目标前缀提示，不改变推理逻辑即可降低零梯度样本占比，提升训练效率

  - 带前缀提示的训练样本需做hint-aware信用分解：前缀用SFT损失做语义锚定，后缀仅用GRPO优化，避免将oracle提供的前缀当作模型生成动作算入策略梯度，前缀锚定的权重λ建议取0.001-0.01区间，不要过高

  - 若GRPO后训练阶段出现大量零奖励方差的死样本，优先排查是否是多token生成的早期错误导致的可达性问题，不要盲目加reward shaping或者增大采样batch，低成本的前缀提示比复杂的奖励设计更有效'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前语义ID生成式推荐普遍采用「SFT预训练+GRPO后训练」的两阶段流程，但GRPO训练时存在严重的有限采样不可达问题：如果生成的前几个语义token进入错误分支，后续生成的所有序列都无法命中目标，导致整组样本奖励全为0，没有相对优势可用于梯度更新，实测中这类零优势样本占比可超过70%，严重浪费训练资源，限制生成式推荐效果提升。

### 方法关键点
- 离线可达性诊断：用SFT checkpoint对每个训练样本做预检测，从0开始逐步增加目标前缀长度，找到能让模型采样到至少1个目标item的最短前缀长度作为该样本的训练提示
- 提示条件化训练：训练时给不可达样本拼接最短目标前缀作为输入，仅要求模型生成剩余的后缀token，将原本完全不可达的样本转化为有奖励区分度的后缀生成任务，提示仅在训练阶段使用，不影响推理逻辑
- 提示感知信用分解：对带提示的样本，前缀token是oracle提供的上下文，仅用SFT损失做语义锚定，不需要纳入GRPO优化；后缀token是模型生成的动作，仅用GRPO优化，避免梯度分配错误

### 关键结果
在Amazon三个公开数据集（Musical Instruments、Arts、Video Games）上对比SASRec、BERT4Rec、TIGER、MiniOneRec等基线，HCGRec在NDCG@10上相对基线最高提升2.6%，HR@50最高提升8.4%，同时将GRPO训练的零梯度样本占比从超过55%降低到17%以下。

**最值得记住的一句话**：语义ID生成式推荐的GRPO训练瓶颈往往不是奖励稀疏，而是有限采样下的目标可达性问题，针对性的前缀提示比复杂的奖励设计投入产出比更高
