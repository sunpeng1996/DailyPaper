---
title: Tail-Likelihood Reinforcement Learning
title_zh: 尾似然强化学习（TailRL）：面向连续奖励的高价值长尾样本优化框架
authors:
- Shrinivas Ramasubramanian
- Daman Arora
- Fahim Tajwar
- Guanning Zeng
- Qingyang Wu
- Zhongzhu Zhou
- Chenfeng Xu
- Haiwen Feng
- Yuda Song
- Aarti Singh
affiliations:
- Carnegie Mellon University
- University of California, Berkeley
- Impossible, Inc.
- Together AI
- Aurora Innovation
arxiv_id: '2609.02987'
url: https://arxiv.org/abs/2609.02987
pdf_url: https://arxiv.org/pdf/2609.02987
published: '2026-09-02'
collected: '2026-09-04'
category: Training
direction: 强化学习训练优化 · 高奖励长尾样本覆盖
tags:
- Reinforcement Learning
- Policy Gradient
- Best-of-k
- Continuous Reward
- Long-tail Optimization
one_liner: 提出无额外超参的TailRL强化学习目标，加权稀有高奖励样本，可直接适配现有RL pipeline
practical_value: '- 做LLM4Rec、广告文案生成、Agent交互的RL对齐时，可直接替换现有GRPO/RLOO的优势计算逻辑为TailRL的排序权重公式，无需改动其他pipeline，即可提升稀有高价值样本（如高转化长尾商品、高ROI创新文案、Agent高完成度路径）的梯度权重，避免收敛到次优解

  - 线上需要Best-of-k采样的低延时场景（如推荐猜你喜欢的Top-k召回、广告创意的多候选择优），TailRL训练的模型可在1/128~1/256的推理采样量下达到基线的同等效果，大幅降低推理成本

  - 当业务存在低风险次优解（如推荐只推爆款、文案直接复用历史模板）时，TailRL可有效避免模式坍缩，在保持基础效果的同时提升长尾高收益样本的产出概率，适合探索需求强的业务场景'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有RL普遍优化平均奖励，会隐式丢失稀有高奖励样本的分布覆盖度，训练时容易陷入低风险次优解，推理时增加采样量的边际收益极低；二进制奖励场景下已有MaxRL优化长尾成功概率，但连续奖励场景下缺乏通用的长尾优化方案。
### 方法关键点
- 将连续奖励拆解为不同阈值下的二分类超阈值事件，最大化均匀采样奖励阈值下的超阈值对数似然，无额外超参，二进制奖励场景下可完全退化为MaxRL
- 梯度天然是所有Best-of-k梯度的调和加权和，无需预设推理采样预算，训练出的模型适配任意推理采样量
- 仅需修改无critic策略梯度方法的优势计算逻辑：对同组N个rollout的奖励排序，按奖励排名给稀有高奖励样本分配更高权重，可作为GRPO/RLOO的drop-in替换，完全兼容现有RL pipeline
### 关键实验结果
在4类任务上验证效果：
1. ImageNet目标定位：仅用IoU标量奖励的TailRL效果超过有坐标监督的基线，16个训练rollout的TailRL效果超过1024个rollout的GRPO/RLOO
2. 文本迷宫导航：初始成功率仅0.01%的低冷启动场景下，GRPO/RLOO完全失效，TailRL可稳定提升Pass@k
3. GUI Grounding：3B/7B VLM模型下，TailRL仅用8/4个推理rollout就达到RLOO 1024个rollout的Pass@1024效果，推理成本降低128~256倍
4. 代码优化：TailRL的Best-of-1024速度提升达7.7倍，而GRPO/RLOO完全坍缩到复制输入的次优解

连续奖励不只是用于求平均的标量，它定义了每个奖励阈值下的成功事件集合，TailRL提供了优化这些事件似然的高效落地方案。
