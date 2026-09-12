---
title: 'AdamX: Cosine similarity meets gradient descent'
title_zh: AdamX：融合余弦相似度的梯度下降一阶优化器
authors:
- Francisco Caldas
- Ruben Belo
- Cláudia Soares
affiliations:
- NOVA School of Science and Technology, Universidade Nova de Lisboa
arxiv_id: '2609.11867'
url: https://arxiv.org/abs/2609.11867
pdf_url: https://arxiv.org/pdf/2609.11867
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 大模型训练 · 一阶优化器改进
tags:
- Adam
- Optimizer
- Cosine Similarity
- Gradient Descent
- Model Training
one_liner: 提出融合余弦相似度自适应控幅与方差校正的Adam系一阶优化器，跨场景收敛表现优于基线
practical_value: '- 训练LLM4Rec、电商推荐排序大模型时可直接替换Adam/AdamW作为优化器，无需修改现有训练pipeline，即可获得更快的收敛速度，降低训练成本

  - 优化器自带的早期训练方差校正机制，可缓解小batch、少样本场景（如冷启动推荐模型、小流量Agent策略微调）下的优化震荡问题，提升训练稳定性

  - 余弦相似度自适应调控更新幅度的思路可迁移到在线梯度更新场景，如实时推荐模型的FTRL类在线优化器改造，提升在线更新的稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Adam系自适应优化器的归一化机制易引发更新动力学异常，部分场景下存在收敛失效问题，且训练早期梯度方差不稳定容易导致优化震荡。
### 方法关键点
1. 将余弦相似度作为自适应调控因子，动态调整梯度更新幅度，平衡自适应步长与收敛稳定性；
2. 新增方差校正机制，平滑训练初期优化轨迹，降低早期迭代的震荡风险；
3. 优化器无模型依赖，可无缝嵌入现有训练pipeline，无需额外超参数调优成本。
### 关键结果
固定超参数预算下，在多类基准数据集、不同模型架构上验证，AdamX达到预设性能阈值所需epoch数显著低于Adam、AdamW等基线，收敛速度具备明显竞争力。
