---
title: 'Detecting an Effect Is Not Learning to Act on It: A Reward-SNR Floor for LLM
  Acquisition Agents'
title_zh: 《检测效应不等于学会利用：LLM采集代理的奖励信噪比阈值》
authors:
- Ying Yuan
affiliations:
- University of California, San Diego
arxiv_id: '2608.10441'
url: https://arxiv.org/abs/2608.10441
pdf_url: https://arxiv.org/pdf/2608.10441
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: Agent · LLM辅助信号采集可学习性
tags:
- LLM Agent
- Reward SNR
- Intent Embedding
- Recommendation System
- Policy Learning
one_liner: 提出奖励信噪比阈值，证明低于阈值时LLM辅助信号的逐例采集策略无法学习
practical_value: '- 上线LLM辅助特征前先计算奖励SNR，若样本量N < (2.8/ρ)²直接放弃逐例路由策略，避免拟合噪声浪费研发资源

  - 可直接复用SHE的多意图拆解方案：用冻结LLM生成带置信度、证据索引的多意图假设，作为召回/排序的补充特征，在冷启动、长多意图用户场景增益显著

  - 无法实现逐例路由时，用设计态规则门控（如用户历史长度<5/浏览类目数>2时触发LLM调用）可降低约14%的LLM调用成本且无精度损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前大量推荐、LLM Agent pipeline会按需调用LLM获取辅助推理/特征，但业界普遍混淆「检测到信号平均有效」和「学会逐例判断是否调用」，大量研发资源浪费在无法落地的逐例路由策略上，亟需明确这类策略的可学习边界。
### 方法关键点
- 提出Structured Hypothesis Embeddings (SHE)：用冻结LLM将用户行为历史拆解为3个带置信度、证据索引的结构化意图假设，嵌入后作为排序模型的补充输入分支，无需回传梯度到LLM；
- 定义奖励SNR ρ=µ/σ（µ为LLM信号的平均增益，σ为增益的方差），推导逐例采集策略可学习的必要条件：ρ ≥ 2.8/√N，即样本量需满足N≥(2.8/ρ)²；
- 设计匹配噪声安慰剂、半合成阳性对照，排除实验pipeline本身失效的可能性。
### 关键结果
在MIND（新闻）、Amazon-Beauty（电商）、REES46（电商）三个公开数据集测试：
① SHE本身grounded faithfulness提升0.0705，意图区分度达2倍，置信度校准后ECE从0.142降至0.031；
② 与GRU排序基线融合后NDCG@10提升0.0114（95%CI[+0.0030,+0.0209]），但全局冗余差与0无统计显著性差异；
③ 三个数据集的奖励SNR均低于阈值，所有逐例路由策略效果均不超过随机路由，匹配噪声安慰剂可复现≥100%的in-sample oracle增益。
### 最值得记住的话
低于奖励信噪比阈值时，in-sample的表观增益完全是噪声的顺序统计量，没有可利用的可学习结构。
