---
title: 'S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding'
title_zh: S³R：基于自稀疏投机解码的高保真RL Rollout加速方法
authors:
- Yuhang He
- Hongyu Ge
- Zihan Lin
- Siyi Liu
- Yongqi Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.13202'
url: https://arxiv.org/abs/2610.13202
pdf_url: https://arxiv.org/pdf/2610.13202
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: LLM RL训练 · 投机解码加速
tags:
- Speculative Decoding
- RL Training
- KV Cache
- Sparse Attention
- Rollout Acceleration
one_liner: 无需额外训练草稿模型，通过同策略自稀疏投机解码加速RL Rollout且不改变策略分布
practical_value: '- 做Agent/LLM4Rec的RL微调（如广告文案、商品推荐理由生成）时，可直接复用S³R自稀疏投机解码方案，无需额外训练小草稿模型，即可提升长文本Rollout吞吐量30%+且不影响训练稳定性

  - 长上下文场景（如用户长行为序列的生成式推荐）的KV缓存调度可借鉴其KV-aware AIMD策略，减少KV缓存颠簸，降低CPU-GPU数据传输开销近90%

  - 基于GRPO的多响应RL训练场景（如广告多候选文案优化），不要依赖单纯的重加权修正稀疏策略的分布偏移，易导致训练崩溃，优先用投机验证保障分布保真'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM的可验证奖励RL（RLVR）训练中，Rollout生成是核心瓶颈，注意力占自回归解码核时间的72%~76%；直接用稀疏attention会改变策略分布，导致GRPO类分组相对优化的训练崩溃；现有投机解码依赖额外训练的草稿模型，在RL迭代中容易过时，接受率持续下降。

### 方法关键点
- 自稀疏投机Rollout框架：草稿和验证共享同一份策略参数，无需额外训练草稿模型；用稀疏attention生成候选token，再经全attention验证+精确投机采样，输出完全匹配稠密策略的响应组分布
- KV感知AIMD调度器：根据GPU KV使用率、恢复队列长度动态调整并发数，减少KV缓存反复卸载重建开销，同时保障Rollout并行度
- 理论证明：分组相对优化（如GRPO）场景下，仅靠响应级重加权无法修正稀疏采样的分布偏移，必须在采样阶段保障分布保真

### 关键结果数字
在DAPO-MATH-17k数据集训练Qwen3-1.7B/8B模型，对比AR解码、N-gram查找、历史检索、辅助草稿模型4类基线，S³R端到端训练吞吐量分别达AR的1.39×、1.35×，任务精度与AR完全对齐；0.05激进稀疏预算下仍保持训练稳定，KV调度减少93%的跨设备KV页传输。

### 核心结论
RL训练中使用GRPO等分组相对优化算法时，稀疏策略的分布偏移无法通过事后重加权完全修正，必须在采样阶段保障输出分布与目标策略完全一致
