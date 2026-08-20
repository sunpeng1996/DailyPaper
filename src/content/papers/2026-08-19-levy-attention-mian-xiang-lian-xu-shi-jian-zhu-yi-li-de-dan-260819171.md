---
title: 'Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention'
title_zh: Lévy Attention：面向连续时间注意力的单遍预测不确定性估计
authors:
- Sotirios P. Chatzis
- Loukas Papadoulas
affiliations:
- Cyprus University of Technology
- Ethical AI Novelties
arxiv_id: '2608.19171'
url: https://arxiv.org/abs/2608.19171
pdf_url: https://arxiv.org/pdf/2608.19171
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 连续时间注意力 · 预测不确定性估计
tags:
- Attention Mechanism
- Predictive Uncertainty
- Continuous Time Series
- Poisson Process
- Single-Pass Inference
one_liner: 基于非齐次泊松随机测度重构注意力层，单遍推理无额外成本输出预测置信度
practical_value: '- 可替换推荐/广告系统中处理用户不规则行为时序的注意力模块，单遍推理即可输出预测置信度，无额外计算成本，解决稀疏行为用户的推荐结果可信度评估问题

  - 置信度输出无需额外训练头，仅需替换softmax层即可适配现有模型，迁移成本极低，可直接用于异常流量识别、低置信推荐结果兜底等业务场景

  - 稀疏数据下证据因子对置信度贡献更高，可针对冷启动用户、小众商品的稀疏行为序列单独调整置信度加权策略，提升冷启动场景的校准效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

## 动机
现有不规则采样时序深度学习模型可输出任意连续时间戳的预测结果，但无法量化预测可信度，MC Dropout等不确定性估计方法需要多遍推理，成本过高。
## 方法关键点
1. 基于非齐次泊松随机测度重构交叉注意力算子，query-key匹配度映射为连续（时间×通道）空间的强度场，输出期望等价于平滑余弦核注意力，可直接替换softmax层训练，梯度计算精确。
2. 保留softmax归一化丢弃的总匹配质量（证据Λ_q）和注意力值方差（分歧trΣ_V(q)），通过方差恒等式组合得到预测RMSD $&#770;σ$，单遍推理即可输出，无需额外训练头。
## 关键结果
t-PatchGNN基准上替换算子最多损失5.6%精度，稀疏数据集无精度损失；单遍置信度效果优于20遍MC Dropout，基于$&#770;σ$校准的高斯分布零样本CRPS优于50次采样方法，1.4秒可完成3383个样本的置信度排序
