---
title: Minimally Invasive Steering of Language Models
title_zh: 大语言模型低侵入式预logit引导对齐方法
authors:
- Taha Entesari
- Jingyu Zhang
- Daniel Khashabi
- Mahyar Fazlyab
affiliations:
- Johns Hopkins University
arxiv_id: '2609.30218'
url: https://arxiv.org/abs/2609.30218
pdf_url: https://arxiv.org/pdf/2609.30218
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: LLM测试时对齐 · 预logit引导
tags:
- Test-time Alignment
- Pre-logit Steering
- Fisher Regularization
- LLM Alignment
- KL Divergence
one_liner: 提出基于Fisher正则的低侵入式预logit引导算法MISVO，实现无参数更新的测试时LLM对齐且避免过steering
practical_value: '- 做Agent/生成式推荐的个性化生成优化时，可复用MISVO的Fisher正则思路，无需微调LLM即可提升业务奖励（点击率、转化率等），同时避免生成内容偏离原模型的语义合理性，比无正则引导方法稳定性更高

  - 做测试时LLM对齐的工程落地时，可采用论文的无显式Fisher矩阵的矩阵-向量乘积计算方式，无需存储大维度Fisher矩阵，大幅降低内存开销，适配1B-14B量级开源模型的在线推理场景

  - 做生成式推荐的Reward优化时，可复用论文的留一法基线奖励梯度估计方法，降低小批量采样下的梯度估计方差，提升少样本迭代的优化效率，适合单prompt/单用户的个性化生成场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有测试时LLM对齐的预logit引导方法缺乏有效正则，易出现过steering问题，大幅偏离原模型输出分布，导致生成连贯性、多样性下降，甚至触发奖励黑客；而直接采用KL作为正则项的梯度估计方差过高，难以适配在线低延迟场景。
### 方法关键点
- 提出MISVO算法，仅在LM头前的隐层添加位置相关引导向量，全程冻结模型所有参数，无需反向传播到Transformer主体
- 基于局部KL几何推导Fisher二次正则项，将引导向量对输出分布的影响建模为Fisher矩阵二次型，正则梯度可通过冻结LM头的矩阵-向量乘积解析计算，无需蒙特卡洛估计
- 序列级KL梯度可分解为解析Fisher项和二阶后缀项，后者在引导幅度较小时可忽略，仅用初始化阶段参考分布的Fisher估计即可完成全迭代优化
### 关键实验
在1B-14B量级的4个开源LLM上实验，覆盖SHP偏好生成、MBPP+代码生成两个任务，对比Best-of-N、AISP等基线，7组模型-任务设置中6组取得最高平均奖励，生成多样性、连贯性指标与Best-of-N相当，参考前缀的KL偏差仅为AISP的1/6左右。
### 核心结论
测试时无参数更新的LLM对齐可通过引入分布敏感的Fisher正则，在不损失生成质量的前提下获得比传统采样选择方法更高的奖励。
