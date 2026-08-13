---
title: Are We Really Making Progress in Group Recommendation? Unmasking the Tie-Breaking
  Illusion
title_zh: 群组推荐进展是否真实？揭示平局打破的评估幻觉
authors:
- Song-Duo Ma
- Pu-Jen Cheng
affiliations:
- National Taiwan University
arxiv_id: '2608.11190'
url: https://arxiv.org/abs/2608.11190
pdf_url: https://arxiv.org/pdf/2608.11190
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 推荐系统评估 · 平局偏差消解
tags:
- Group Recommendation
- Ranking Evaluation
- Tie-breaking Bias
- BPR
- Metric Inflation
one_liner: 揭示群组推荐中得分压缩与确定性平局处理导致的指标膨胀，提出平局感知评估协议与温度缩放BPR优化方案
practical_value: '- 算法迭代不要盲目信任原始top-K指标，基于BPR训练的模型需新增平局感知的HR/NDCG计算逻辑，避免np.argsort等确定性排序默认正例前置带来的虚高收益误导

  - 若训练时使用额外sigmoid做BPR平滑，推理时直接用原始模型得分排序，或替换为温度缩放BPR，既保留训练平滑收益，又不会引发得分压缩产生大量平局

  - AB实验时同步统计top-K平局占比，若平局占比超过5%，统一使用平局感知指标计算实验收益，避免错误判断新算法的实际效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
近年来群组推荐SOTA在标准benchmark上报的提升显著，但这些收益是否来自真实的群体偏好建模能力存疑。现有大量基于BPR训练的方法会在损失计算前对单物品得分加额外sigmoid变换，导致得分动态范围压缩，推理时产生大量top-K平局；而评估环节的确定性平局处理（如正例默认放在候选集首位，排序时优先前置）会大幅虚高HR、NDCG等指标，甚至完全扭曲算法的相对排名。

### 方法关键点
- 提出平局感知评估协议：计算均匀随机平局打破下HR@K、NDCG@K的精确期望，完全消除确定性排序的实现细节带来的指标偏差
- 揭示额外sigmoid的双重作用：既是训练时的隐式边距平滑，提升训练稳定性，也会导致推理时得分压缩产生大量平局，引入评估偏差
- 提出温度缩放BPR作为替代方案：直接在损失层对pairwise得分差做温度缩放平滑，既保留训练侧的收益，又不会引发严重的得分平局

### 关键结果
在CAMRa2011、Mafengwo两个公开群组推荐数据集上，重跑5篇顶会SOTA与对应baseline：
1. 受影响方法的指标膨胀最高可达99.98%（如DHMAE在CAMRa2011群组推荐HR@1从原评估的0.9782跌到平局感知后的0.0002）
2. 指标下降幅度与top得分平局大小的皮尔逊相关系数达0.92~0.99，完全正相关
3. 移除额外sigmoid或替换为温度缩放BPR后，大部分SOTA方法相对baseline的优势基本消失

### 核心结论
推荐算法迭代中，评估协议的严谨性和模型本身的优化同等重要，得分平局不是可以忽略的实现细节，而是能完全改变实验结论的关键变量
