---
title: 'Web Scale on a Budget: Tail-Aware Retrieval Evaluation'
title_zh: 低成本Web级检索评估：尾部感知的大规模指标预测方法
authors:
- Boaz Meivar
- Shai Avidan
affiliations:
- Tel Aviv University
arxiv_id: '2610.17986'
url: https://arxiv.org/abs/2610.17986
pdf_url: https://arxiv.org/pdf/2610.17986
published: '2026-10-13'
collected: '2026-10-15'
category: Eval
direction: 检索系统评估 · 大规模指标外推
tags:
- Retrieval Evaluation
- Extreme Value Theory
- Scaling Law
- Low-cost Benchmark
- Instance Retrieval
one_liner: 仅用5%随机样本加尾部感知EVT估计，可预测100M规模检索mAP，误差0.005，评估成本降20倍
practical_value: '- 电商/内容平台的大规模召回评估无需全量索引千万/亿级item库：抽取5%均匀随机样本，用EVT尾部感知方法外推全量mAP/Recall，评估成本降20倍，误差控制在0.01以内

  - 替换推荐系统常用的Krichene-Rendle采样无偏指标：原有方法对尾部hard query/item预测偏乐观（误差≥0.037），EVT外推可将尾部预测误差降低一个数量级

  - 模型迭代AB测提速：无需每次全量跑索引，仅在小样本子集上计算得分分布，外推全量效果即可对齐线上表现，迭代周期从几天缩短到几小时'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Web级实例检索评估需索引上亿级干扰样本，单模型跑100M样本需消耗556 GPU小时、生成200GB描述符，每次模型迭代、消融实验都要重复支付该成本；直接用小样本子集评估的指标偏乐观，无法和全量结果对齐，也不具备跨工作可比性。
### 方法关键点
- 定义与检索库大小无关的per-query hardness：即随机干扰样本得分超过正样本的概率，证明正样本排名服从 `1 + Binomial(N, x_q)` 分布，可直接推导任意库大小下的mAP指标
- 针对小样本下hardness低于采样下限无法计数的问题，用极值理论(EVT)拟合得分尾部的广义帕累托分布，外推得到小样本下不可见的尾部hardness
- 评估流程仅需索引均匀随机抽取的小比例干扰样本，拟合per-query尾部分布后即可外推任意库大小的mAP，无需全量索引
### 关键结果
在ILIAS、INSTRE（100M干扰样本）、GLDv2（759k干扰样本）3个基准数据集、5个不同backbone上验证：仅用5%样本（20倍降本），EVT估计的全量mAP平均绝对误差仅0.005；远优于直接在子集评估（误差0.08~0.13）和推荐系统常用的采样无偏count估计（误差0.037~0.068），还能100%保留不同backbone的性能排序。
最值得记住：Web级检索/推荐的评估本质是预测问题而非全量索引问题，均匀小样本加尾部外推即可替代昂贵的全量评估
