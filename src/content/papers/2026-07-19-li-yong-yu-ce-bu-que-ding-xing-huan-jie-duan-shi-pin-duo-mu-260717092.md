---
title: 'Uncertainty as Remedy: Mitigating Satisfaction Label Bias in Short Video Multi-Objective
  Ensemble Ranking'
title_zh: 利用预测不确定性缓解短视频多目标融合排序的满意度标签偏差
authors:
- Zonghe Shao
- Tiantian He
- Xiaoxiao Xu
- Jiaqi Yu
- Minzhi Xie
- Jinfang Gu
- Yongqi Liu
- Kaiqiao Zhan
- Kun Gai
affiliations:
- Kuaishou Technology
arxiv_id: '2607.17092'
url: https://arxiv.org/abs/2607.17092
pdf_url: https://arxiv.org/pdf/2607.17092
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 多目标推荐 · 不确定性感知排序优化
tags:
- Multi-Objective Ranking
- Uncertainty Estimation
- Label Bias Mitigation
- Video Recommendation
- Pairwise Learning
one_liner: 引入预测不确定性的端到端多目标融合排序框架UAME，无需额外监督缓解满意度标签偏差
practical_value: '- 多目标融合排序场景可复用双分支输出设计，推理时仅输出均值分支作为排序分数，无额外 latency，完全兼容现有线上架构

  - 可直接复用不确定性驱动的样本自适应加权策略，无需额外引入问卷类监督信号，即可提升排序与真实用户满意度的对齐度

  - 损失设计可直接落地，包括概率化 pairwise 排序损失、不确定性正则项、pxtr 冲突对齐辅助损失，超参数参考默认值α=0.02、β=0.1、γ=2即可快速调优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业短视频/内容推荐的端到端多目标融合排序依赖点击、播放时长、点赞等pxtr行为信号作为用户满意度代理，但这类信号仅能捕捉碎片化的行为维度，天然存在跨目标冲突，会引入严重的满意度标签偏差；传统确定性排序模型对所有训练样本对平等加权，导致pxtr冲突大的高偏差样本被欠优化，模型容易收敛到局部最优，最终排序结果与用户真实满意度对齐度差。
### 方法关键点
- 权重共享双分支输出层：主干排序网络输出的特征共享，通过两个独立的轻量MLP分别输出满意度预测均值μ和预测不确定性σ²，将单样本得分建模为高斯分布变量
- 概率化pairwise排序损失：基于两个样本的得分分布差异计算排序概率，替代传统确定性的sigmoid计算逻辑
- 三重损失组合优化：加权概率pairwise损失+不确定性正则项（避免模型刻意放大σ规避排序学习）+辅助约束损失（强制σ与跨pxtr的排名冲突程度直接对齐）
- 样本对自适应加权：基于样本对的σ之和计算综合不确定性，归一化后作为样本对的训练权重，自动提升高冲突高偏差样本的优化优先级
### 关键实验
在快手亿级DAU的工业短视频推荐数据集上验证，对比EMER、EASQ两个工业界SOTA多目标排序基线，以及RankDist、EBRank等不确定性后处理方案；离线核心pxtr的GAUC最高相对提升14.2%，线上A/B测试长播放量+1.614%、点赞量+0.939%、7日留存+0.009%，基于用户问卷的真实满意度NDCG@5相对提升8.71%，目前已全量部署到生产环境。
### 核心结论
多目标排序场景下，样本对的预测不确定性和pxtr冲突导致的标签偏差正相关，将不确定性用于训练阶段的样本加权的收益远高于推理阶段的后处理排序调整，且无额外推理开销。
