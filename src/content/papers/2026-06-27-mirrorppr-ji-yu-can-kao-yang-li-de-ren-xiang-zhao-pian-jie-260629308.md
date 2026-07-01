---
title: 'MirrorPPR: Exemplar-Based Portrait Photo Retouching'
title_zh: MirrorPPR：基于参考样例的人像照片结构化精修
authors:
- Zhihong Liu
- Zheng Li
- Jiachun Jin
- Siqi Kou
- Yitao Jian
- Fengpei Yu
- Zhijie Deng
affiliations:
- Shanghai Jiao Tong University
- Triverse AI
arxiv_id: '2606.29308'
url: https://arxiv.org/abs/2606.29308
pdf_url: https://arxiv.org/pdf/2606.29308
published: '2026-06-27'
collected: '2026-07-01'
category: Multimodal
direction: 多模态 · 人像图像精修与生成
tags:
- Diffusion Transformer
- LoRA
- Image Editing
- Data Augmentation
- Curriculum Learning
- Dataset
one_liner: 提出基于示例迁移的人像结构化精修框架MirrorPPR及47M规模数据集，效果优于现有基线
practical_value: '- 微调预训练DiT时采用LoRA+定制化特征连接器注入领域特征的方案，可迁移到电商商品图风格迁移、模特精修类业务

  - 针对对齐标注数据稀缺问题，采用自增强构造严格对齐训练对的思路，可复用在广告素材生成的标注数据构造环节

  - 用模拟+专业子集的课程学习范式优化生成模型，可借鉴到多风格商品素材生成的模型训练流程'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文本引导图像编辑难以传达人脸特征、身材比例等细粒度结构化人像精修需求，现有基于示例的编辑方法仅适配强视觉变换任务，无法捕获精修所需的极细微局部调整，同时存在跨身份训练对操作不对齐、标注数据稀缺的痛点。
### 方法关键点
1. 提出MirrorPPR框架：通过Retouching Operation Extractor提取示例对的精修操作特征，经连接器+LoRA模块注入预训练DiT实现操作迁移；
2. 设计数据自增强范式，构造操作严格对齐的跨身份训练对；
3. 发布MirrorPPR47M大规模数据集，含4700万+精修对，拆分模拟/专业子集支撑课程学习平滑优化。
### 关键结果
精修质量、身份保留两个核心维度均显著优于所有现有基线方法。
