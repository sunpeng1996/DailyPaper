---
title: 'Adapting Without Gradients: Affine Statistics Transport and What Its Certificate
  Can Tell You'
title_zh: 无梯度测试时适配：仿射统计迁移及其可迁移性证书研究
authors:
- Salim Khazem
- Ibrahim Mohamed Serouis
affiliations:
- Talan Research Center
arxiv_id: '2609.00374'
url: https://arxiv.org/abs/2609.00374
pdf_url: https://arxiv.org/pdf/2609.00374
published: '2026-08-30'
collected: '2026-09-03'
category: Training
direction: 无梯度测试时冻结模型适配
tags:
- Test-time Adaptation
- Gradient-free
- Frozen Model
- Model Deployment
- Distribution Shift
one_liner: 提出无梯度冻结模型适配方法CASTER及可迁移性证书，轻量效果优于同配置k-NN
practical_value: '- 无梯度适配思路可直接复用在电商推荐/广告场景的冻结排序模型、第三方LLM部署中，无需反传即可缓解测试时分布漂移，算力开销极低

  - 可迁移性证书的门控逻辑可借鉴，用于拦截分布差异过大时的有害适配操作，避免适配反而导致业务效果下降

  - 轻量状态存储设计适合内存受限的端侧推荐、边缘推理场景，无需存储全量源特征库即可实现适配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有测试时适配（TTA）依赖推理阶段更新模型参数，不适用于冻结/第三方模型、无BatchNorm架构、内存受限的部署场景，普适性差。
### 方法关键点
1. 提出CASTER无梯度适配方案：在判别子空间存储源类统计量，基于目标批次的矩估计类共享仿射变换，分类前完成源类分布迁移，无需反向传播、优化器状态、源特征库。
2. 设计残差-边际比可迁移性证书，判定仿射迁移的可靠性，通过门控拦截有害适配。
### 关键结果数字
28组骨干-数据集设置中27组优于同冻结特征下的k-NN，状态存储中位数低18倍；加门控后无条件适配的平均-3.35点效果转为+1.69点增益，宽阈值范围内性能距最优阈值差不超0.3点；证书为机制专属，对Tent类适配方法仅能保留0.6%的增益。
