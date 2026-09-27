---
title: 'EndoFSA: Endoscopic Few-Shot Image Generation via Rank-Constrained Parameter
  Adaptation'
title_zh: EndoFSA：基于秩约束参数适配的内窥镜少样本图像生成
authors:
- Panagiota Gatoula
- Grigoris Karypidis
- Dimitris K. Iakovidis
affiliations:
- University of Thessaly
arxiv_id: '2609.29930'
url: https://arxiv.org/abs/2609.29930
pdf_url: https://arxiv.org/pdf/2609.29930
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 少样本图像生成 · 秩约束参数适配
tags:
- Few-Shot Generation
- GAN
- Low-Rank Adaptation
- Synthetic Data
- Regularization
one_liner: 提出基于秩约束参数适配的GAN模型，实现无强标注的内窥镜病理少样本图像生成
practical_value: '- 少样本跨域适配架构可复用：预训练模型冻结主干权重，仅更新低秩子空间少量调制参数，大幅降低过拟合风险，适配电商冷启动品类生成、小众内容推荐场景

  - 感知边界正则化+簇级多样性控制的组合trick，可直接迁移到GenRec生成流程，缓解生成结果同质化、mode collapse问题

  - 无强标注即可完成跨域适配的方案，适合电商标注成本高的非标品、小众品类的样本扩充场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：无线胶囊内窥镜生成的胃肠图像中病理样本占比极低，现有合成数据生成方法直接在稀缺病理样本上训练易出现过拟合、结构失真问题，需同时兼顾保留解剖先验与生成病理变异的可控适配机制。

**方法关键点**：1. 基于GAN架构，先在大量正常样本上预训练生成器，适配病理域时冻结预训练权重，仅更新低秩子空间内的少量调制参数；2. 加入感知边界正则化、簇级多样性控制模块，缓解mode collapse，保留预训练学到的正常解剖先验；3. 无需像素级标注、掩码或边界框监督即可完成适配。

**关键结果**：在公开WCE基准数据集多类病理场景验证，生成图像可还原真实病灶形态；仅用合成病理图像训练的分类器，性能与用真实图像训练的结果相当。
