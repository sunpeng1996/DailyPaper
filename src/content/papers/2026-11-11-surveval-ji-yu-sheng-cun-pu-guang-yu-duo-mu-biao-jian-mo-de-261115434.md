---
title: 'SurvEval: Listwise Re-Ranking Evaluator via Survival-Based Exposure and Multi-Objective
  Value Modeling'
title_zh: SurvEval：基于生存曝光与多目标建模的列表式重排序评估器
authors:
- YaChen Yan
- Liubo Li
affiliations:
- Intuit Credit Karma
arxiv_id: '2611.15434'
url: https://arxiv.org/abs/2611.15434
pdf_url: https://arxiv.org/pdf/2611.15434
published: '2026-11-11'
collected: '2026-11-13'
category: RecSys
direction: 重排序优化 · 列表式评估
tags:
- Re-ranking
- Listwise Evaluation
- Survival Model
- Multi-Objective Learning
- Transformer
one_liner: 将用户级联浏览建模为离散生存过程，结合多目标价值建模实现高精度列表式重排序评估
practical_value: '- 重排序位置折扣可替换为生存模型导出的用户到达概率，无需人工设定固定位置衰减系数，更贴合真实级联浏览行为

  - 多目标训练可复用不确定性自动加权方案，无需人工调整不同目标（点击/加购/停留）的损失权重，适配不同噪声和尺度的信号

  - 现有多生成器重排序架构可直接接入该评估器，从候选列表中选择效用最高的列表上线，无需修改上游生成逻辑，改造成本极低

  - 用户编码器的「静态特征+多兴趣长序列+最近N个短序列」拼接方案可直接复用，提升用户表征的准确性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有重排序评估器存在两大缺陷：一是对用户浏览行为假设过度简化，忽略级联浏览的位置依赖，多采用固定人工折扣，无法匹配不同用户的浏览深度差异；二是将点击、停留时长、点赞等多目标交互信号强行聚合为单标量，抹平了不同目标的尺度、噪声差异，导致评估结果无法真实反映列表的用户效用，限制重排序效果上限。
### 方法关键点
- 列表效用拆解为各位置「用户到达概率 × 物品条件价值」的乘积和，将用户从上到下的浏览行为建模为离散时间生存过程，通过各位置的退出概率自动推导单调递减的到达概率，无需人工设计位置折扣函数。
- 多目标价值模块为每个交互目标设置独立预测头，采用带权重的逻辑回归处理稀疏非负的交互标签，引入不确定性驱动的多任务损失自动平衡不同目标的训练权重，适配不同噪声、尺度的信号。
- 曝光建模与价值建模共享Transformer骨干网络，用户编码器融合静态特征、多兴趣长序列、最近N个短时序交互三类信号，端到端联合训练。
### 关键实验
在KuaiRand（快手公开推荐数据集，含4类交互目标）和Avito（广告搜索数据集，单点击目标）上对比DNN、PRM、PIER、CAVE等基线：KuaiRand上NDCG达0.8523，较SOTA CAVE提升0.73pp，uAUC达0.7236，提升0.4pp；Avito上NDCG达0.7450，较CAVE提升0.79pp，uAUC达0.7326，提升0.68pp。
### 核心结论
列表级效用的本质是用户对每个位置的到达概率与该位置物品用户感知价值的乘积和，两者联合建模才能最大化评估准确度。
