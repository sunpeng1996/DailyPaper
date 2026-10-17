---
title: 'CleanRM: Reward Modeling from Noisy Feedback with a Few Clean Feedback for
  RLHF'
title_zh: CleanRM：利用少量干净反馈处理噪声偏好的奖励建模方法
authors:
- Licheng Pan
- Haocheng Yang
- Yuzhou Chen
- Yichen Sun
- Yuan Lu
- Yunfei Teng
- Jiajun Fan
- Guangyi Liu
- Zhixuan Chu
- Hao Wang
affiliations:
- Zhejiang University
- Xiaohongshu Inc
- National University of Singapore
- New York University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2610.21138'
url: https://arxiv.org/abs/2610.21138
pdf_url: https://arxiv.org/pdf/2610.21138
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: RLHF 样本级噪声校正奖励建模
tags:
- RLHF
- Reward Modeling
- Optimal Transport
- Label Noise
- LLM Alignment
one_liner: 基于最优运输用少量干净反馈校准样本级噪声比，训练无偏奖励模型提升RLHF对齐效果
practical_value: '- 电商/推荐场景的用户隐式反馈（点击、收藏、点踩）普遍存在误触、主观歧义等样本级噪声，可借鉴CleanRM思路，抽取少量人工标注的干净反馈，用最优运输对齐噪声与干净样本的联合分布，估计每个样本的噪声比校正排序损失，提升推荐/广告模型的排序效果

  - Agent/LLM服务的用户反馈天然存在大量主观噪声，可复用本文的无偏代理损失公式，仅需5%左右的干净标注就能大幅提升奖励模型准确性，降低RLHF对齐的标注成本，提升Agent回答的用户满意度

  - 工程落地可将噪声比估计模块与主模型解耦，先用小批量干净数据预训练噪声估计器，再用校正后的损失训练主模型，不需要修改原有训练pipeline，落地成本极低

  - 对噪声较大的业务场景（如商品评论情感标注、短视频推荐负反馈），无需过滤低置信样本，通过样本级噪声校正即可保留全部数据的有效信息，避免优质硬样本被误删'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RLHF是LLM对齐的核心范式，奖励模型的准确性直接决定下游对齐效果，但偏好数据普遍存在样本级噪声：人工标注主观歧义、标注错误、LLM judge不准确都会导致反馈与真实偏好不符。传统去噪方法假设全局统一噪声比，与实际偏好噪声的样本级特性冲突，直接训练会导致奖励模型记忆噪声而非真实偏好，下游RLHF效果下降；现有方法无法有效利用少量易得的干净标注（专家审核、重复标注获得）解决样本级噪声问题。
### 方法关键点
- 两阶段训练架构：第一阶段基于Wasserstein最优运输，对齐噪声反馈还原的偏好与干净反馈的输入-偏好联合分布，估计每个样本的双向噪声比（正偏好翻转为负、负偏好翻转为正的概率）
- 基于样本级噪声比推导无偏代理损失，理论证明该损失对干净风险无偏，直接在全量噪声数据上训练奖励模型即可避免偏置
- 联合分布对齐成本同时融合偏好差异和输入语义嵌入距离，避免全局分布对齐但语义不匹配的问题
### 关键实验
在HelpSteer、UltraFeedback、PKU-SafeRLHF三个公开偏好数据集上，对比20余种去噪基线，R2分别比最优基线TrainRef提升0.052、0.013、0.032，MSE分别下降7.8%、2.9%、14%；下游RLHF阶段，在Qwen3-8B上FFT安全分比Naive基线提升79.45%，比最优基线高16.3%；仅需占总训练集3%的干净标注就能达到性能饱和，噪声越大增益越显著。
### 核心结论
偏好噪声是样本级而非全局统一的，仅需少量干净标注通过最优运输校准噪声比，就能用极低的标注成本获得无偏奖励模型，大幅提升RLHF对齐效果
