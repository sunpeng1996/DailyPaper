---
title: Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs
title_zh: 基于损失引导多专家GAN的手语视频合成框架
authors:
- Dingzhan Nong
- Zhihao Ren
- Ziqi Li
- Tim Lo
affiliations:
- Glassbox AI
arxiv_id: '2608.13368'
url: https://arxiv.org/abs/2608.13368
pdf_url: https://arxiv.org/pdf/2608.13368
published: '2026-08-13'
collected: '2026-08-16'
category: Multimodal
direction: 多模态生成 · 多专家GAN训练优化
tags:
- GAN
- MoE
- Multi-Discriminator
- Training Stability
- Video Generation
one_liner: 提出含多区域专用判别器、联合损失共识的多专家GAN手语视频合成框架，适配消费级硬件部署
practical_value: '- 多判别器引导生成器多分支分区域优化的设计，可复用在电商商品/广告视频生成任务中，无需额外多样性损失即可实现不同视觉域的特征专精

  - 多分支模型训练震荡问题可借鉴10%权重的联合损失共识机制，对齐各分支梯度方向，降低早期训练混沌度

  - 卷积+Transformer双通路加可学习自适应特征融合的结构，可迁移到需兼顾全局稳定和局部细节的广告排序、多模态召回任务

  - 三模式交替训练调度策略，可复用在多分支MoE类模型的训练流程中，平衡整体效果和分支专精能力'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统单判别器GAN在手语这类复杂视频生成场景中，难以捕捉手势、面部表情等细粒度细节，生成效果易失真；多判别器系统早期训练存在混沌震荡，稳定性差。
### 方法关键点
1. 设计全局、手部、头部3个专用判别器，分别引导生成器对应专家分支关注不同视觉区域，无需额外多样性损失即可实现隐式特征专精
2. 引入10%权重的联合损失共识机制，约束每个判别器向集成平均对齐，解决多判别器训练不稳定问题
3. 每个分支采用卷积+Transformer双通路加可学习自适应特征融合，平衡卷积的训练稳定性与窗口自注意力的细节捕捉能力
4. 采用判别器训练、整体生成、分支专精训练三模式交替的调度策略优化训练
### 关键结果
在156GB定制数据集的去重过滤测试集上，0.2B参数版本PSNR达29.8，推理显存仅1.5GB；1.3B参数版本PSNR达30.7，推理显存8GB，可直接在消费级硬件部署。
