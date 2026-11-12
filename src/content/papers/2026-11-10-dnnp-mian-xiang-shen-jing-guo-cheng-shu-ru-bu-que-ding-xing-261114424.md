---
title: 'DnNP: Denoising Input Uncertainty in Neural Processes'
title_zh: DnNP：面向神经过程输入不确定性的去噪方法
authors:
- Fatemeh Tohidian
- Chengzhi Shi
- Soomi Lee
- Matthew Elia
- Amy Mueller
- Stratis Ioannidis
- Jennifer Dy
affiliations:
- Northeastern University
arxiv_id: '2611.14424'
url: https://arxiv.org/abs/2611.14424
pdf_url: https://arxiv.org/pdf/2611.14424
published: '2026-11-10'
collected: '2026-11-12'
category: Training
direction: 元学习 · 带噪输入鲁棒训练
tags:
- Meta-Learning
- Neural Processes
- Denoising
- Uncertainty Quantification
- Variational Inference
one_liner: 扩展神经过程框架显式建模输入不确定性，通过变分推理联合训练去噪与元学习，提升带噪场景表现
practical_value: '- 推荐系统特征带噪场景（如埋点噪声、用户误操作数据）可参考联合去噪+模型训练的范式，替代先清洗再训练的两阶段流程，降低信息损失

  - 对需做不确定性估计的推荐/Agent决策场景（如冷启动推荐、风险敏感广告投放），可借鉴DnNP输入不确定性显式建模思路，避免固定观测方差带来的不可消除偏差

  - 小样本元学习场景（如新类目冷启动、多品类迁移学习）遇训练数据输入噪声大的问题时，可直接复用DnNP的变分推理训练框架提升鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Neural Processes（NPs）作为支持不确定性量化的灵活元学习模型，默认假设输入无噪声，和真实场景中测量误差、数据噪声普遍存在的现状 mismatch，会严重降低预测质量与不确定性估计可靠性。
### 方法关键点
1. 提出DnNP框架，显式对输入不确定性建模，通过变分推理实现端到端训练；
2. 联合学习输入去噪与元学习任务，无需额外预处理即可适配带噪训练数据；
3. 理论证明带噪输入下的贝叶斯最优预测器属于DnNP模型族，可避免固定观测方差插件模型存在的不可消除KL散度gap。
### 关键结果
在真实空气质量传感器PM2.5空间插值任务上，相比标准NPs，DnNP的RMSE最高降低30%，NLL最高降低73%，在合成与真实数据集上均实现预测与不确定性量化的一致性提升。
