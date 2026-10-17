---
title: Denoising Textures is a Different Ballgame Altogether!
title_zh: 纹理去噪是与通用图像去噪完全不同的独立研究任务
authors:
- Saptarshi Mandal
- Oindrila Haldar
- Chirayata Bhattacharya
- Chandra Sekhar Seelamantula
- Zhiwei Xu
- Thrasyvoulos N. Pappas
- Gaurav Sharma
affiliations:
- Indian Institute of Science Bangalore
- Northwestern University
- University of Rochester
arxiv_id: '2610.22258'
url: https://arxiv.org/abs/2610.22258
pdf_url: https://arxiv.org/pdf/2610.22258
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 图像纹理去噪 · 灾难性遗忘问题研究
tags:
- ImageDenoising
- TextureProcessing
- CatastrophicForgetting
- Fine-tuning
- ComputerVision
one_liner: 揭示SOTA通用去噪模型处理纹理表现差，微调纹理数据会灾难性遗忘，需专属纹理感知去噪器
practical_value: '- 电商商品图修图场景可针对性微调去噪模型，保留面料、雕花等商品纹理细节，提升商品展示质感降低退货率

  - 多模态生成式推荐的商品图生成环节，可引入纹理感知去噪模块优化生成图真实度，减少用户预期差

  - 特定域数据微调前需评估灾难性遗忘风险，可采用LoRA等轻量微调方案规避全参数微调的能力退化问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用图像去噪技术已取得长足进展，但纹理去噪方向研究相对不足，现有SOTA去噪模型处理含复杂精细纹理的图像时易出现过平滑问题，丢失纹理细节，严重影响生成式建模等下游任务效果。
### 方法关键点
对当前主流SOTA去噪模型在纹理数据集上的表现开展系统性分析，测试通用数据集预训练模型微调纹理数据集后的性能变化。
### 关键结果
- 仅在纹理数据集上微调后，SOTA去噪模型的纹理去噪表现才能获得显著提升
- 全量微调纹理数据集后，模型出现严重灾难性遗忘，通用图像去噪能力大幅下降
- 纹理去噪需设计专属纹理感知去噪器做专项优化，才能同时兼顾纹理保留与通用去噪效果
