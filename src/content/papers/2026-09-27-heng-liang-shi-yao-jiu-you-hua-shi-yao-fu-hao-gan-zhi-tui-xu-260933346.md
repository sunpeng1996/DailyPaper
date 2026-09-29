---
title: 'What Gets Measured Gets Managed: Sign-aware Recommendation Needs Sign-aware
  Evaluation'
title_zh: 衡量什么就优化什么：符号感知推荐需要适配符号感知评估
authors:
- Minchan Kim
- Jungmin Hwang
- Hyunwoo Park
affiliations:
- Seoul National University
- Seoul National University of Science and Technology
arxiv_id: '2609.33346'
url: https://arxiv.org/abs/2609.33346
pdf_url: https://arxiv.org/pdf/2609.33346
published: '2026-09-27'
collected: '2026-09-29'
category: Eval
direction: 推荐系统评估 · 负反馈利用
tags:
- recommender-system
- negative-feedback
- evaluation-metric
- sign-aware-recommendation
- ranking
one_liner: 诊断符号感知推荐的效价盲缺陷，提出带负反馈惩罚的带符号评估指标体系
practical_value: '- 业务上线负反馈感知推荐模型前，除常规Recall/NDCG外，必须加入V-AUC、负样本透出率做校验，避免大量厌恶内容透出导致用户流失

  - 可直接复用Signed Recall/Signed NDCG作为评估指标，根据业务场景调γ：广告/推荐厌恶成本高的场景设γ>1，内容探索场景设γ<1，γ=0可完全兼容原有指标体系

  - 现有内积打分的推荐模型可快速复用效价增强方案：新增基于用户物品embedding element-wise乘积的正负分类辅助损失，推理时加入分类输出分值调整，可在不损失5%常规指标的前提下降低厌恶内容透出

  - 高负反馈比例场景（如短视频、内容推荐）优先选择loss-driven的符号感知模型，相比架构驱动的模型，正负样本排序准确率更高，带符号指标表现更优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有符号感知推荐（利用用户点赞、差评等正负反馈训练）看似训练时融入了符号信息，但实际推理阶段无法区分用户喜欢和厌恶的内容，常规评估指标（Recall、HR、NDCG）对负样本和未观测样本都赋0分，完全无法检测到这个效价盲问题，导致透出大量用户厌恶的内容，损伤用户体验。
### 方法关键点
- 诊断指标V-AUC：衡量同一用户的正样本排序高于负样本的概率，0.5为完全随机，1为完全区分
- 带符号评估指标族：包含Signed Recall、Signed HR、Signed NDCG，给负样本赋-γ的权重（γ为可调惩罚系数，γ=0时完全兼容原有常规指标），明确惩罚推荐列表中的厌恶内容
- 效价增强方案：基于用户与物品embedding的element-wise乘积训练正负分类器，推理时将分类输出加权加入排序得分，可在不损失常规指标的前提下提升效价区分能力
### 关键实验结果
覆盖5个公开数据集（Amazon-CD、Amazon-Music、Epinions、KuaiRand、KuaiRec，负正反馈比ρ从0.22到5.95），对比6个SOTA符号感知推荐模型、4个无符号基线模型：
1. 现有SOTA符号感知模型的V-AUC大多接近0.5，几乎无法区分正负样本，部分模型甚至低于0.5，把厌恶内容排到喜欢的前面
2. 用带符号指标重新评估后，原有常规指标排名靠前的模型大多排名下跌，loss驱动的符号感知模型排名普遍上升，在低中ρ场景下SNDCG比基线最高提升超40%
3. 增加效价增强的辅助损失后，SNDCG在Amazon-CD提升26%、Amazon-Music提升46%、Epinions提升187%；KuaiRand场景下原SNDCG为负（厌恶内容透出更多），调整后转为正，常规NDCG仅损失3.9%
### 核心结论
什么被衡量就会被管理，推荐系统评估不仅要考核召回了多少用户喜欢的内容，更要考核避免了多少用户厌恶的内容。
