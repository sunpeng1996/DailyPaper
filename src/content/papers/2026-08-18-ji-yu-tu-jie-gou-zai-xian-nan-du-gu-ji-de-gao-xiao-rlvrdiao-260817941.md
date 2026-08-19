---
title: Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
title_zh: 基于图结构在线难度估计的高效RLVR调度
authors:
- Zhizhao Liu
- Zhiliang Tian
- Xi Wang
- Zhihua Wen
- Yihang Xiong
- Zhiquan Lai
- Dongsheng Li
affiliations:
- National University of Defense Technology
arxiv_id: '2608.17941'
url: https://arxiv.org/abs/2608.17941
pdf_url: https://arxiv.org/pdf/2608.17941
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: LLM RL训练 · 自适应难度估计
tags:
- RLVR
- Difficulty Estimation
- Graph Learning
- Online Inference
- Training Scheduling
one_liner: 提出即插即用的图结构在线难度估计器，相同rollout预算下提升RLVR训练性能
practical_value: '- 做LLM RLHF/RLVR训练时，可直接复用该即插即用难度估计框架替换原有难度模块，在相同生成预算下提升训练效率，降低推理rollout成本

  - 推荐系统冷启动场景下，可借鉴该语义+特征相似度建图、跨相似样本共享反馈的思路，缓解新用户/新商品的反馈稀疏问题，提升难度/转化率估计精度

  - Agent多任务调度场景中，可复用该动态难度估计逻辑，给不同难度任务匹配对应能力的模型/计算资源，避免资源冗余分配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）是当前提升LLM推理能力的核心方案，但现有方法对所有训练样本分配统一rollout探索预算，容易导致简单样本冗余探索、高价值难样本探索不足，资源利用率极低。现有难度估计方案要么依赖额外探测开销极高，要么基于历史反馈存在冷启动、反馈滞后问题，且普遍忽略样本间的语义/推理关联，无法低成本得到准确的实时难度估计。
### 方法关键点
1. 构建难度感知样本图：通过加入难度感知指令的嵌入模型编码样本的语义、推理结构、难度特征，基于互近邻余弦相似度构建稀疏无向图
2. 图结构化潜在难度建模：对样本图做谱聚类得到初始难度簇，用Potts先验鼓励邻接样本共享潜在难度状态，搭配Beta-Binomial模型聚合同状态样本的rollout反馈
3. 在线变分推理：用平均场变分算法随训练实时更新样本的潜在状态分布和对应难度，不需要额外探测，可直接接入现有样本选择、rollout分配调度器
### 关键结果
在2个基座模型（Qwen2.5 1.5B、Llama3 1B）、3个主流RL调度器（GVM、PCL、GRESO）、4个数学推理基准上测试：相同rollout预算下，21/22个非平局实验设置性能提升，GVM+方案在MATH500数据集上精度从71.9%提升至74.7%；难度估计精度上，全训练轨迹的batch级Pearson相关系数最高达0.836，仅增加0.12A100小时的额外开销，冷启动阶段效果优势显著。
### 核心洞见
跨相似样本共享反馈的图结构动态估计，是低开销解决冷启动、时序反馈滞后问题的高效路径
