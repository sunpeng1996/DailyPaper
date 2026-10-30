---
title: 'Statistical Detection of Positional Bias in LLM-Based Recommender Systems:
  Methodologies and Empirical Evidence'
title_zh: 基于大语言模型的推荐系统位置偏差统计检测方法与实证证据
authors:
- Carlos Peláez-González
- Francisco Herrera
- Andrés Herrera-Poyatos
affiliations:
- University of Granada, Spain
- Andalusian Institute of Data Science and Computational Intelligence (DaSCI)
arxiv_id: '2610.37962'
url: https://arxiv.org/abs/2610.37962
pdf_url: https://arxiv.org/pdf/2610.37962
published: '2026-10-27'
collected: '2026-10-30'
category: RecSys
direction: 推荐系统 · LLM推荐偏差检测
tags:
- PositionalBias
- LLM4Rec
- RAGRecommendation
- StatisticalTesting
- BiasDetection
one_liner: 提出两种带统计保障的LLM推荐位置偏差检测方法，验证该偏差为模型相关结构性属性
practical_value: '- 上线RAG架构的LLM推荐前，可复用POB-UNBP方法做低成本位置偏差审计，仅需少量样本即可获得统计显著性结论，尤其适配闭源大模型的低成本校验需求

  - 电商会话式Top-1推荐场景可直接对prompt中的候选商品做随机shuffle，零成本降低结构性位置偏差对推荐公平性、相关性的负面影响

  - 可直接复用permutation sensitivity、positional bias、strong positional bias三个指标，作为LLM推荐上线前的必过校验项，量化输出稳定性和偏差严重程度

  - 若检测到强位置偏差过高，优先优化prompt模板或更换LLM模型，该偏差属于LLM本身的结构性属性，与检索侧逻辑无关，调整召回排序无 mitigation
  效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG架构的LLM推荐已广泛应用于电商会话推荐场景，但prompt内候选商品的排序会隐性影响LLM输出，传统推荐的位置偏差检测方法不适用于LLM黑盒场景，缺乏带统计保障的标准化检测方案，也无法验证偏差是实验artifact还是模型固有属性。

### 方法关键点
- 两种互补检测方案：①POB-ICM：基于列联表卡方独立性检验+query级置换校准，可解释性强但样本需求量大；②POB-UNBP：基于无偏差时位置选择概率均匀的理论证明，仅需验证选择分布与均匀分布的总变分距离，样本效率高，支持随机解码场景的统计显著性校验
- 三类量化指标：permutation sensitivity（置换敏感度，衡量候选重排后推荐结果的变动比例）、positional bias（位置偏差，衡量选择分布与均匀分布的总变分距离）、strong positional bias（强位置偏差，衡量推荐结果掉出相关候选集的比例）
- 偏差分层定义：软偏差仅在同等相关候选中做选择，不影响推荐相关性；硬偏差会推荐明显不相关的商品，直接损伤用户体验

### 关键结果
基于亚马逊2023电商数据集构造2000条用户查询，每个查询对应5个召回商品，每个候选集做20次随机置换，共4万测试样本，在8款SOTA LLM上验证：①两种方法均在100%测试模型上拒绝无位置偏差的原假设；②permutation sensitivity最高达60%，即60%的推荐结果会因候选重排发生变化；③强位置偏差最高达22%，即22%的推荐会因位置原因选择明显不相关商品；④偏差程度与候选集大小、解码温度无关，是模型依赖的结构性属性。

**最值得记住的结论**：所有主流LLM做推荐时都存在结构性位置偏差，不是实验误差，上线前必须做位置偏差审计与针对性优化。
