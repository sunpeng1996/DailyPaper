---
title: 'SWIM: Step-Wise Integrated Measure for Session-supervised List Evaluation
  in Generative Re-ranking'
title_zh: SWIM：面向生成式重排序的会话级列表分步整合评估方法
authors:
- Yuanhao Pu
- Chenghao Zhang
- Chao Feng
- Xunyong Yang
- Xiang Li
- Yongqi Liu
- Defu Lian
- Kaiqiao Zhan
- Kun Gai
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
- State Key Laboratory of Cognitive Intelligence
arxiv_id: '2608.25104'
url: https://arxiv.org/abs/2608.25104
pdf_url: https://arxiv.org/pdf/2608.25104
published: '2026-08-25'
collected: '2026-08-27'
category: RecSys
direction: 生成式重排序 · 会话级列表评估
tags:
- Reranking
- Survival Analysis
- Generative Recommendation
- Session Recommendation
- Listwise Evaluation
one_liner: 提出基于生存分析的会话感知生成式重排序评估器，实现工业场景停留时长和留存双提升
practical_value: '- 生成式重排序G-E框架的Evaluator可复用SWIM核心设计：将用户连续浏览建模为生存过程，用因果掩码Transformer同时预测每步留存概率和对应位置奖励，加权求和得到列表价值，解决传统pointwise聚合忽略上下文依赖的问题

  - 工业部署可直接复用其低延迟架构：因果掩码Transformer支持一次前向传播并行计算所有位置的留存和奖励，无需自回归解码，快手实测对70个候选列表打分无显著
  latency 上涨，适配在线服务要求

  - 多目标奖励融合可参考其实现方案：离散目标（点击/点赞/关注）用sigmoid头预测，连续目标（如 dwell time）分桶预测分布再加权求和，训练时仅对用户实际到达的位置计算损失，有效降低样本噪声

  - 现有系统改造ROI极高：替换原有Evaluator时无需改动上游召回、排序、Generator模块，即可获得业务指标提升，快手线上仅替换CAVE即获得停留时长+0.351%的收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业推荐重排序阶段广泛采用Generator-Evaluator（G-E）框架，但传统Evaluator按请求独立打分，通过聚合pointwise分值得到列表价值，忽略了短视频、信息流、商品feed等场景下用户浏览是连续无列表边界的，无法捕捉跨请求上下文依赖、用户留存意愿、重复内容边际效用递减等会话级动态，导致列表评估偏差，长期用户engagement优化不足。

### 方法关键点
- 将会话浏览建模为有限时域生存过程，把列表总价值拆解为递归生存分布（用户到达每个位置的概率）和到达位置条件奖励的乘积和，同时考虑用户从历史会话进入当前请求的概率和列表内每步留存概率
- 采用带前缀token的因果掩码Transformer，前缀token编码历史会话特征，所有位置的留存概率和奖励在一次前向传播中并行计算，无需自回归解码，满足工业低延迟要求
- 训练损失仅对用户实际到达的位置计算生存分类损失和奖励回归/分类损失，无偏学习各步参数；在线推理时由于请求已触发，直接固定进入当前请求的概率为1，计算列表内加权总分排序即可

### 关键结果
在RecFlow、KuaiRand公开数据集和快手4亿DAU主feed场景验证：离线RecFlow数据集NDCG@6达0.2031，较最强基线CAVE提升3.78%，AUC达0.7185，提升1.44%；线上7天AB测替换CAVE后，APP停留时长提升0.351%，7日留存提升0.048%，均统计显著。

**最值得记住的一句话**：生成式重排序的列表评估要跳出单请求孤立建模的局限，从用户会话级连续行为的视角建模留存和奖励，才能获得真实的长期业务收益。
