---
title: 'NS-ATTENTION: Newton-Schulz Transformations of Attention Outputs in Vision
  Transformers'
title_zh: NS-Attention：面向视觉Transformer注意力输出的Newton-Schulz变换
authors:
- Xiaohe Jiang
- Guoqiang Zhang
- Tianjin Huang
- Ronghui Mu
affiliations:
- University of Exeter
arxiv_id: '2609.27735'
url: https://arxiv.org/abs/2609.27735
pdf_url: https://arxiv.org/pdf/2609.27735
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: Transformer注意力训练优化
tags:
- Attention
- Vision Transformer
- Newton-Schulz
- Spectral Optimization
- Model Training
one_liner: 提出无参数NS-Attention，通过变换注意力头输出提升视觉Transformer分类精度
practical_value: '- 无参数NS变换可直接迁移到推荐/广告场景的Transformer类模型（如用户行为序列建模、多兴趣召回的注意力模块），无需新增参数即可获取效果收益，延迟不敏感的离线训练/召回链路可优先落地

  - NS变换通过调整特征谱分布、提升有效秩的思路，可复用在用户/物品表征归一化、多兴趣输出处理环节，缓解表征坍塌问题

  - 落地时优先选择1次NS迭代方案，消融验证其效果优于2次迭代，可平衡计算开销与效果收益，延迟敏感的在线推理链路需谨慎评估开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Newton-Schulz（NS）迭代此前被应用于Muon优化器的LLM训练更新矩阵变换，其谱调整特性可用于缓解Transformer注意力头输出特征谱过度集中、有效秩偏低的问题。
### 方法关键点
提出无参数的NS-Attention，作用于每个注意力头的输出：先将头输出整理为特征×token矩阵，用Frobenius范数归一化，执行有限步NS多项式变换后恢复原始范数，在头合并与输出投影前完成谱调整，降低特征集中度、提升有效秩。
### 关键结果
在CIFAR-10/100数据集上的ViT、Swin模型12组同种子对比实验中，NS-Attention均提升最终epoch精度，平均增益0.25~0.83个百分点；消融实验显示1次NS迭代效果优于2次，该优化会引入额外推理延迟
