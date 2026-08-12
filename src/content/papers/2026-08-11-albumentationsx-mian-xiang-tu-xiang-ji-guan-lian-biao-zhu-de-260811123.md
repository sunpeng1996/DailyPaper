---
title: 'AlbumentationsX: One Augmentation Pipeline for Images and Related Annotations'
title_zh: AlbumentationsX：面向图像及关联标注的统一增强管线
authors:
- Vladimir Iglovikov
affiliations:
- Albumentations LLC
arxiv_id: '2608.11123'
url: https://arxiv.org/abs/2608.11123
pdf_url: https://arxiv.org/pdf/2608.11123
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 多模态数据增强 · 标注对齐工具
tags:
- DataAugmentation
- AnnotationAlignment
- ComputerVision
- TrainingPipeline
one_liner: 提出统一增强库AlbumentationsX，解决图像与多类标注增强变换不一致的问题
practical_value: '- 做图文/短视频电商的多模态推荐、商品识别模型训练时，可直接引入该库，避免图像与对应标注（商品框、属性标签、语义掩码等）变换不一致导致的训练数据污染

  - 可借鉴其单Compose对象托管所有变换参数、随机种子的设计思路，优化自身多模态数据预处理管线的可复现性与可维护性

  - 做电商商品OCR、瑕疵检测等CV任务时，可复用其自定义扩展变换能力，降低标注对齐的工程开发成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态训练中图像与对应标注（掩码、检测框、关键点、视频帧等）分别执行增强时，容易出现空间变换不匹配，静默引入脏数据，严重影响模型训练效果，现有增强工具对多类型标注的统一对齐支持不足。
### 方法关键点
1. 设计单一Compose对象统一托管变换列表、概率、标注配置、随机种子，单次调用仅生成一次随机参数，批量应用到样本的所有关联元素上；
2. 自动绑定每个对象的掩码、框、标签，支持自定义扩展变换，可保存管线定义、回放单次增强过程，方便调试与训练复现；
3. 适配PyTorch等主流训练框架，嵌入位置位于数据解码后、组batch前的预处理阶段，无额外侵入性。
### 效果
从工程层面完全消除图像与多类标注的增强错配问题，支持图像、视频、3D体素等多类型样本增强，开箱即用可大幅降低多模态数据预处理的开发工作量
