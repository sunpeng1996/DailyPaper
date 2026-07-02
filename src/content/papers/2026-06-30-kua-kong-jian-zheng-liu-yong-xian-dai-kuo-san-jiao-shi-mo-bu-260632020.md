---
title: 'Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion
  Teachers'
title_zh: 跨空间蒸馏：用现代扩散教师模型训练单步学生模型
authors:
- Anh Nguyen
- Ngan Nguyen
- Duc Vu
- Trung Dao
- Viet Nguyen
- Quan Dao
- Kien Nguyen
- Chi Tran
- Phong Nguyen
- Khoi Nguyen
affiliations:
- Qualcomm AI Research
- University of Wisconsin–Madison
- Johns Hopkins University
- Rutgers University
arxiv_id: '2606.32020'
url: https://arxiv.org/abs/2606.32020
pdf_url: https://arxiv.org/pdf/2606.32020
published: '2026-06-30'
collected: '2026-07-02'
category: Training
direction: 扩散模型跨空间蒸馏训练优化
tags:
- Diffusion Model
- Knowledge Distillation
- Latent Alignment
- Model Compression
- Efficient Inference
one_liner: 提出轻量Bridge模块实现跨VAE跨分辨率扩散蒸馏，无需修改学生模型主干
practical_value: '- 跨模型空间知识蒸馏可复用轻量映射桥思路，无需修改原有小模型主干，大幅降低业务侧模型升级成本

  - 跨域对齐可同时采用隐空间重构+注意力保真双目标，提升蒸馏稳定性，可迁移到搜推大模型蒸馏小模型场景

  - 保留原有小模型生态兼容性与低延迟的设计思路，适配端侧、在线服务等对性能要求高的业务场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单步扩散模型的分布式时间步蒸馏要求师生共享同一隐空间，无法将SD 3.5、Flux等高容量大教师的知识，迁移到SD1.5这类部署友好但VAE参数、隐空间分辨率不匹配的小模型。

### 方法关键点
1. 正式定义跨空间蒸馏任务，覆盖跨VAE、跨分辨率两类隐空间不匹配场景；
2. 提出轻量Bridge模块，由冻结的学生VAE解码器作为空间先验+小型可学习投影器组成，无需修改学生模型主干；
3. 训练采用隐空间重构+注意力保真双目标，实现稳定的教师空间对齐。

### 关键结果
SD1.5经Bridge蒸馏后，单步推理的HPSv3指标从5.4提升至9.4，同时保留原有低延迟、生态兼容特性，还解锁了1024分辨率生成能力
