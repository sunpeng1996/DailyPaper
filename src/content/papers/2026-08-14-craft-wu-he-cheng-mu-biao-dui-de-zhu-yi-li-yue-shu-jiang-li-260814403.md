---
title: 'CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization
  without Composed Targets'
title_zh: CRAFT：无合成目标对的注意力约束奖励微调主体个性化生成方法
authors:
- Jihun Park
- Kyoungmin Lee
- Jongmin Gim
- Hyeonseo Jo
- Jaeyeul Kim
- Han Zou
- Zhenpeng Zhan
- Yan Zhang
- Sunghoon Im
affiliations:
- DGIST, South Korea
- Baidu, Inc., China
- KAIST, South Korea
arxiv_id: '2608.14403'
url: https://arxiv.org/abs/2608.14403
pdf_url: https://arxiv.org/pdf/2608.14403
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态生成 · 主体个性化微调
tags:
- LoRA
- Diffusion Model
- Reinforcement Fine-Tuning
- Multimodal Generation
- Attention Alignment
one_liner: 提出无需合成目标对的ReFL微调框架CRAFT，仅用10K参考样本实现SOTA主体驱动图像个性化生成
practical_value: '- 电商商品图个性化生成场景可复用无合成目标对的微调思路，仅需少量商品参考图+主体mask就能训练专属生成模型，大幅降低训练数据标注成本

  - 可借鉴注意力级奖励+像素级奖励的双层校准机制，解决多模态生成中主体ID保留度低、生成内容与prompt不匹配的问题

  - 基于LoRA的轻量微调方案可直接复用在现有多模态生成模型的业务定制化迭代中，无需全量微调即可快速适配不同品类的生成需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有主体驱动图像个性化方法依赖数十万到数百万的（参考图-合成目标）配对数据，数据制作需要LLM prompt生成、T2I合成、质量过滤等多阶段流水线，成本高且与特定合成器强绑定，落地门槛高。
### 方法关键点
提出CRAFT单步ReFL微调框架，基于LoRA适配预训练参考感知MMDiT，仅需10K带主体掩码的参考图，无需合成目标监督；核心遵循「Where to look」原则：先通过注意力级奖励对齐噪声token、短语token与对应参考主体的注意力，再用生成的主体注意力掩码门控像素级身份奖励，保证图像空间监督与注意力路由一致。
### 关键结果
在FLUX.2-klein-9B上微调后，在XVerseBench达到SOTA性能，仅用10K无配对参考样本，比现有方法少用140K~2M+的合成配对数据，方案可迁移到其他参考感知骨干模型，性能稳定提升
