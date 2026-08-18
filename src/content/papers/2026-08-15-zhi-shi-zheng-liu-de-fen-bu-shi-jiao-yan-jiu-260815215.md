---
title: The Distributional View of Knowledge Distillation
title_zh: 知识蒸馏的分布视角研究
authors:
- Gordei Verbii
- Juho Lee
affiliations:
- Independent Researcher
- KAIST
arxiv_id: '2608.15215'
url: https://arxiv.org/abs/2608.15215
pdf_url: https://arxiv.org/pdf/2608.15215
published: '2026-08-15'
collected: '2026-08-18'
category: Training
direction: LLM知识蒸馏 · 最优传输优化
tags:
- Knowledge-Distillation
- Optimal-Transport
- Wasserstein-Barycenter
- LLM-Compression
- Sinkhorn-Divergence
one_liner: 提出多温度视角+最优传输的KD框架，揭示KD效果由师生性能差决定的双 regime 规律
practical_value: '- 业务侧小模型蒸馏前先计算Γ=SFT学生PPL-教师PPL，Γ<0.1时不要硬上KD，优先用BaryOT类温和损失降低KD税

  - 多温度教师视图聚合优先选端点温度（如0.5、1.5），无需浪费算力增加中间温度视图，有效色散比视图数量更重要

  - LLM蒸馏优先用path模式（学生对应温度匹配教师各温度视图），可降低视图选择敏感度，缩小与SFT的性能差距

  - 语义容忍度高的任务（如推荐query生成、文案生成蒸馏）可优先用最优传输类损失，降低语义近邻误判的惩罚'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
传统Token级KD逐点匹配分布，KL梯度无法区分错分token的语义差异，且仅用单一温度的教师输出，丢失了退火路径上的多粒度信息，同时业界对KD效果波动缺乏可量化的决策依据，无法提前判断KD是否会带来收益。

### 方法关键点
- 提出分布视角KD框架，将教师建模为多温度退火路径下的视图集合，而非单一软化输出
- 证明对数线性池化多温度视图等价于单温度，仅算术混合、传输 barycenter 能带来多视图收益
- 基于token嵌入余弦距离构建最优传输ground cost，引入去偏Sinkhorn散度、Wasserstein barycenter等几何感知聚合算子，替代逐点KL损失
- 设计两种蒸馏目标：hub模式用学生固定温度视图匹配所有教师视图，path模式用学生对应温度视图匹配教师各温度视图
- 引入师生性能差Γ=SFT学生PPL-教师PPL作为核心诊断指标，划分KD效果的两个区间

### 关键实验
基于Dolly-15k数据集在Pythia模型对（160M→31M、410M→70M）上做8种方法对比：Γ=0.1（薄天花板）时无KD方法胜过SFT，BaryOT path模式仅比SFT高0.12 PPL，KD税最小；Γ=1.49（真实天花板）时JSKD比SFT低1.2 PPL，性能接近参数大5.8倍的教师。

### 核心结论
「哪种KD损失最优」不是损失本身的固有属性，而是由师生性能差Γ决定的函数，交叉点Γ*落在(0.10, 1.49)区间内
