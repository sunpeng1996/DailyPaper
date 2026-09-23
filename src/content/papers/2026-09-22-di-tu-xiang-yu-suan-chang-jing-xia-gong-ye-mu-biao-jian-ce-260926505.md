---
title: Semantically-Guided Domain Randomization for Industrial Object Detection in
  Low-Image-Budget Regimes
title_zh: 低图像预算场景下工业目标检测的语义引导域随机化
authors:
- Jose Moises Araya-Martinez
- Gautham Mohan
- Jens Lambrecht
affiliations:
- TU Berlin
- University of Stuttgart
- TU Braunschweig
arxiv_id: '2609.26505'
url: https://arxiv.org/abs/2609.26505
pdf_url: https://arxiv.org/pdf/2609.26505
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 工业计算机视觉 · 小样本合成数据生成
tags:
- Synthetic Data Generation
- Domain Randomization
- VLM
- Diffusion Model
- Object Detection
- Data Scarcity
one_liner: 提出免标注语义引导域随机化合成数据pipeline，少量合成图即可提升工业目标检测性能
practical_value: '- 电商新品冷启动缺训练图场景，可复用VLM语义caption+扩散模型生成合成训练数据，大幅降低人工标注成本

  - 小样本训练场景，可参考语义引导的合成数据生成逻辑，用极少量样本就能实现模型效果达标

  - 跨域风格适配任务（如不同场景的商品图风格统一），可借鉴ControlNet+IP-Adapter约束扩散生成的架构，保障生成内容符合业务约束'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高混合低产量汽车制造场景下，目标检测模型重训存在标注、算力、时间三重预算约束，现有合成数据生成方案仍需数千张图像，无法适配小预算场景需求。
### 方法关键点
提出语义引导域随机化（S-GDR）免标注适配pipeline：1）用VLM对少量无标注真实参考集生成语义caption；2）基于ControlNet、IP-Adapter控制SDXL生成匹配真实场景的背景；3）基于掩码完成前景目标与生成背景的融合，得到合成训练数据。
### 关键结果
固定200张合成训练图像预算下，在汽车多目标检测基准的真实留出测试集上mAP50-95达0.739，较域随机化渲染基线（0.697）提升6%，同时优于同预算下的亮度过滤、感知哈希、CycleGAN风格迁移、无引导扩散等对比方案。
