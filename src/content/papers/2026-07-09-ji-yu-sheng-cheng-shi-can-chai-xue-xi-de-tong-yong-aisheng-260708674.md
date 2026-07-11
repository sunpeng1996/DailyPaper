---
title: Do Transformations Reveal the Truth? Generative Residual Learning for Generalized
  AI-Generated Image Detection
title_zh: 基于生成式残差学习的通用AI生成图像检测框架
authors:
- Kutub Uddin
- Nusrat Tasnim
- Awais Khan
- Mohammad Umar Farooq
- Khalid Malik
affiliations:
- University of Michigan
- Korea Aerospace University
arxiv_id: '2607.08674'
url: https://arxiv.org/abs/2607.08674
pdf_url: https://arxiv.org/pdf/2607.08674
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态内容安全 · AIGI检测
tags:
- AIGI Detection
- Residual Learning
- Attention Mechanism
- Neural Tensor Network
- Cross-domain Generalization
one_liner: 提出生成式残差学习框架GenRes++，提升未知生成范式AIGI的检测泛化性
practical_value: '- 生成式残差学习框架可迁移到电商场景AI生成商品图、营销素材的真伪校验，规避虚假素材合规风险

  - 多变换样本注意力特征聚合trick可复用在UGC/AIGC内容审核的细粒度特征提取环节，提升跨模型生成内容识别准确率

  - PE-Core通用特征提取器选型思路可参考，降低跨域检测类任务的迁移开发成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
生成式AI高速发展催生大量高逼真度深度伪造内容，引发虚假信息传播、身份盗窃、经济欺诈等风险；现有AIGI检测方法受生成范式多样、生成伪影隐蔽的限制，泛化性差，无法有效识别未知生成方法产出的内容。
### 方法关键点
1. 提出GenRes框架，通过神经张量网络建模原始样本与变换后样本的细粒度关联特征，提升检测泛化性
2. 升级为GenRes++，引入可学习注意力机制聚合多变换样本的关联特征，自动聚焦高信息量检测线索
3. 两个模型均采用PE-Core作为特征提取器，输出通用语义丰富的嵌入，提升跨域检测能力，支持未知生成方法的AIGI识别
### 关键结果
多公开基准数据集实验验证，GenRes++性能全面优于现有SOTA AIGI检测方法
