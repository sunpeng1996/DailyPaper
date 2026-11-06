---
title: 'What Gets Hacked in a Collaborative Reward for LLM Recommenders: The Part
  That Does Not Depend on the User'
title_zh: LLM推荐协同奖励曝光塌陷归因：非用户依赖项均值分量的修正
authors:
- Zhuangsheng Li
- Liang Dong
- Yu Wu
- Dailin Li
- Yu Xia
- Yunhan C. Zhang
- Rui Cai
- Yi Wu
- Julian McAuley
affiliations:
- University of California, San Diego
- Google Inc.
- University of Virginia
- University of Melbourne
- University of California, Davis
arxiv_id: '2611.07588'
url: https://arxiv.org/abs/2611.07588
pdf_url: https://arxiv.org/pdf/2611.07588
published: '2026-11-05'
collected: '2026-11-06'
category: GenRec
direction: 生成式推荐 · RL奖励设计
tags:
- LLM4Rec
- Collaborative Filtering
- RLHF
- Popularity Bias
- Reward Engineering
one_liner: 分解CF奖励的item均值与残差分量，提出两种奖励修正策略，最高将跨用户distinct top-1商品数提升9.8倍
practical_value: '- 做LLM4Rec的RL对齐时，不要直接用原生CF分数作为奖励，优先加per-item standardization修正，可在几乎不损失排序精度的前提下大幅提升长尾商品曝光，缓解推荐马太效应

  - 修正的工程成本极低：仅需预跑4000条左右的训练样本统计每个item的CF分均值和标准差，RL阶段仅需查表做减法和归一化，不需要重训CF模型或LLM backbone

  - 可根据业务需求灵活调整修正强度：通过α系数控制item均值的移除比例（α越小曝光越分散），也可仅对top 10%高均值的热门商品做修正，平衡长尾曝光和头部转化效率

  - 该修正对不同item表示范式（Semantic ID/Atomic ID）、CF架构、LLM backbone均普适，不需要针对现有业务架构做额外适配'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于CF分数的协同奖励是LLM推荐器RL对齐的主流方案，但直接使用会引发**曝光塌陷**：即便冻结的CF模型本身可输出跨用户的个性化排序，训出的LLM推荐结果会集中在少量热门商品，跨用户distinct top-1商品数最多下降80%，但HR@10等排序精度指标几乎无损失，此前一直未定位到核心诱因，也缺乏低成本的解法。

### 方法关键点
- 奖励分解：将CF分数拆分为**item-mean分量**（item在全体训练用户历史上的平均CF分，与当前用户无关）和**残差分量**（当前用户的CF分减去item-mean，纯用户个性化分量），通过控制实验证实item-mean是曝光塌陷的核心诱因
- 两种轻量修正：
  1. per-item centering：预统计所有item的平均CF分，RL阶段直接从生成item的CF分数中减去对应均值
  2. per-item standardization：在centering基础上，再除以item的CF分数标准差（加极小值floor防止除0），统一残差的量纲
- 修正全程不需要重训CF模型或LLM backbone，仅需预跑少量训练样本统计item级统计量，推理零额外开销

### 关键实验结果
在Amazon Beauty、Amazon Sports两个公开数据集上，对比原生CF奖励、KL惩罚、Dr.GRPO、HiLaR标准化、流行度惩罚等baseline：
- 两种修正可将跨用户distinct top-1商品数分别提升1.5~4.1倍、1.6~9.8倍，Coverage@10最高提升187%，曝光Gini系数最高降低0.06，同时HR@10损失控制在1%以内
- 修正效果对Semantic ID/Atomic ID两种item表示、4种CF架构（SASRec/GRU4Rec/双塔/CTR头）、3种LLM backbone均普适
- 仅对top 50%高均值的热门商品做修正，即可恢复91%~99%的曝光增益

### 核心结论
CF奖励中与用户无关的item均值分量是LLM推荐RL训练时曝光塌陷的核心原因，简单的预统计修正即可用极低成本解决该问题。
