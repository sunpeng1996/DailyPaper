---
title: 'PailitaoGR: Latent Think-with-Images for Generative Image Retrieval'
title_zh: PailitaoGR：基于隐式图像思考的电商生成式图像检索方法
authors:
- Xiaomeng Fan
- Yueran Liu
- Shengyu Zhou
- Chenghan Fu
- Wanxian Guan
- Feng Li
- Chuan Yu
- Jian Xu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2608.26658'
url: https://arxiv.org/abs/2608.26658
pdf_url: https://arxiv.org/pdf/2608.26658
published: '2026-08-27'
collected: '2026-08-28'
category: GenRec
direction: 生成式图像检索 · 多模态能力隐式内化
tags:
- Generative Retrieval
- Image Search
- Semantic ID
- Knowledge Distillation
- Multimodal LLM
one_liner: 无需额外裁剪/OCR工具，内建目标关注与辅助信息利用能力，电商图搜效果超基线13.8%
practical_value: '- 可复用「能力内化」思路：将离线工具（裁剪/OCR/细粒度识别）的能力通过蒸馏迁移到线上端到端模型，避免在线调用工具的额外延迟，适配搜推低延时场景

  - 目标关注蒸馏Trick可迁移：用on-policy蒸馏解决生成式任务训练推理分布错位问题，搭配ROT+熵约束的注意力引导，提升复杂输入（长query/多意图query/复杂背景图）下的有效信号聚焦能力

  - 选择性辅助蒸馏设计可复用：通过「辅助信息有用性+学生可及性」双门控筛选要迁移的辅助能力，避免无效/误导信息干扰，可用于多模态召回中多信号融合的门控设计'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商拍立淘等图搜场景下，用户上传的原始查询图往往同时包含目标商品、有用辅助信息（品牌/型号文字）、无关内容（水印/背景/其他物体），现有生成式检索要么依赖裁剪/OCR等外部工具引入额外推理延迟，要么直接输入全图易被无关信号干扰，检索精度不足。

### 方法关键点
- 目标关注感知机制：设计Target Enhancer对目标区域视觉token打分增强，以裁剪目标区域输入的Crop Teacher为监督做on-policy蒸馏，搭配ROT注意力损失+熵损失引导粗到细的注意力聚焦，实现「无需裁剪的隐式放大」
- 选择性辅助信息利用机制：设计Auxiliary Enhancer结合目标锚点打分增强有效辅助token，以带OCR输入的OCR Teacher为监督，通过「辅助信息有用性+学生可及性」双门控做增量对比蒸馏，实现「无需OCR的隐式文字识别」
- 推理阶段仅输入原始全图，无需额外工具和Teacher模型，无额外延迟开销

### 关键实验
基于拍立淘真实日志构建7大品类共115.9万训练样本、8647测试样本，对比DINOv3、CLIP、IRGen、GENIUS等基线，比直接SFT基线平均提升13.8%，甚至超过裁剪输入的Crop Teacher（+4.76%）和裁剪+OCR输入的OCR Teacher（+2.76%），目标占比<5%的小目标场景下H@1相对提升超100%。

### 核心洞察
工业搜推场景下，将工具能力通过蒸馏内生化到端到端模型，既可以获得工具增强的精度收益，又能满足在线低延迟要求。
