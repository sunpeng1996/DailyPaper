---
title: 'Beyond Pixels: From Video Priors to 4D Worlds'
title_zh: 超越像素：从视频先验到4D动态世界生成
authors:
- Zihao Liu
- Xiaolong Shen
- Zhenglin Zhou
- Ruijie Quan
- Yi Yang
affiliations:
- ReLER, CCAI, Zhejiang University
arxiv_id: '2608.10744'
url: https://arxiv.org/abs/2608.10744
pdf_url: https://arxiv.org/pdf/2608.10744
published: '2026-08-10'
collected: '2026-08-12'
category: Multimodal
direction: 多模态4D动态场景生成
tags:
- 4D Generation
- Video Diffusion
- Latent Space
- VAE
- Spatiotemporal Attention
one_liner: 提出Latent-to-4D框架，实现同VAE族视频模型间可迁移的4D场景生成
practical_value: '- 跨模型共享隐空间的复用思路可迁移到推荐系统：如果不同召回/排序模型共享同一特征编码器族，下游生成式推荐任务可直接复用上层隐向量，无需随上游模型迭代重训，降低迭代成本

  - 跳过中间显式信号直接做隐层到目标输出的对齐技巧，可减少多步pipeline的误差传播，比如电商文案/商品生成场景可直接对接内容模型隐层输出，避免中间生成结果的精度损失

  - 帧级+全局时空注意力融合机制可借鉴到时序用户行为建模，兼顾短期会话内行为序列和长期全局兴趣的特征对齐，提升时序推荐效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有4D生成方案存在两大缺陷：两步式（RGB视频生成+4D重建）存在分布不匹配与误差累积问题；单步绑定特定视频生成器的方案灵活性差，更换上游生成器就要重新训练。
### 方法关键点
提出Latent-to-4D框架，直接将共享同VAE的视频扩散模型输出的最终去噪隐向量作为输入，跳过RGB生成环节；将视频隐向量与预训练4D解码器的token网格对齐，通过帧级局部+全局时空注意力优化生成结果，仅需1K左右重建片段即可完成训练。
### 关键结果数字
在Text4D-200、I4D-200基准上，投影DINO-F1分别比同隐空间的Wan+4RC级联方案高2.88~3.45、5.81分，人类评估在几何精度、时序稳定性、整体质量上均更优；单个checkpoint可直接在同VAE族的多个视频扩散Transformer上无修改迁移使用。
