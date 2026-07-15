---
title: Latent-Identity Tuning in Text-to-Image Personalization Models
title_zh: 文本到图像个性化模型的潜层身份调优方法
authors:
- Daniel Garibi
- Ronen Kamenetsky
- Hadar Averbuch-Elor
- Daniel Cohen-Or
- Or Patashnik
affiliations:
- Tel Aviv University
- Cornell University
arxiv_id: '2607.11885'
url: https://arxiv.org/abs/2607.11885
pdf_url: https://arxiv.org/pdf/2607.11885
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态个性化生成 · 潜空间编辑
tags:
- Text-to-Image
- Personalization
- Latent Space
- Identity Editing
- Frozen Encoder
one_liner: 无需额外训练，挖掘冻结文生图个性化编码器的潜层语义方向，实现保身份的细粒度人脸编辑
practical_value: '- 电商数字人/用户虚拟形象定制业务可复用「冻结预训练编码器+挖掘潜层语义方向」范式，无需额外训练即可实现属性调整，大幅降低迭代成本

  - 做身份类个性化生成（如商家专属数字人、用户虚拟头像）时，可参考潜token对应不同面部语义/空间区域的设计，实现局部属性细粒度修改，不破坏整体身份一致性

  - 上线C端AIGC个性化工具时，可直接基于预训练模型推理实现自定义属性编辑，避免微调带来的存储与算力开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图个性化模型的细粒度人脸编辑精度不足，调整属性时易破坏目标身份一致性，且多数方案需要额外训练，落地成本高。
### 方法关键点
1. 直接探索预训练冻结的文生图个性化编码器潜空间，无需新增训练步骤；
2. 定位潜空间中对应不同面部语义/空间区域的语义方向，通过调整选定token对应的子空间实现局部属性编辑；
3. 直接修改身份的潜表征而非单张生成图像，确保跨不同prompt、不同生成场景下的身份一致性。
### 关键结果
经定性定量实验验证，可稳定实现加胡须、加雀斑、修改鼻型等多种局部人脸编辑，跨生成图像的身份一致性表现优于现有方案。
