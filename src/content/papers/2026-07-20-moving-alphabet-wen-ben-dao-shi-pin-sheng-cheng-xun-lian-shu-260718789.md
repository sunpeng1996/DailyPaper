---
title: 'Moving Alphabet: A Controlled Study of Training Data for Text-to-Video Generation'
title_zh: Moving Alphabet：文本到视频生成训练数据的对照研究
authors:
- Amber Yijia Zheng
- Lu Liu
- Raymond A. Yeh
- Xi Yin
affiliations:
- Meta Superintelligence Labs
- Purdue University
arxiv_id: '2607.18789'
url: https://arxiv.org/abs/2607.18789
pdf_url: https://arxiv.org/pdf/2607.18789
published: '2026-07-20'
collected: '2026-07-24'
category: Training
direction: 多模态生成 · 训练数据质量影响研究
tags:
- Text-to-Video
- Training Data
- Caption Quality
- Controlled Experiment
- Data Curation
one_liner: 构建可控合成测试床，揭示训练数据分布与标注质量对文本到视频生成模型的影响规律
practical_value: '- 电商商品短视频生成、广告素材生成等多模态业务的训练集，需优先保证内容、时长分布的均衡多样性，避免长尾品类缺失导致泛化性不足

  - 预训练阶段文本标注质量对模型效果、训练效率的影响远高于后处理手段，建议优先投入资源提升预训练数据标注准确率，而非依赖后续微调补救

  - 若已使用低质标注完成预训练，可结合classifier-free guidance + 小批量高质量标注数据微调，可部分恢复效果，降低数据迭代成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本到视频（T2V）生成研究多聚焦架构创新、算力与模型规模缩放，对训练数据的影响规律探索严重不足，真实场景数据构造环节复杂、变量不可控，无法开展精准对照实验。
### 方法关键点
构建可控合成测试床Moving Alphabet，生成字体、颜色、尺寸、运动方向/速度等参数完全可控的字母移动视频，可通过修改真值元数据精准控制数据分布、标注污染程度，开展变量隔离的对照实验。
### 关键结果
① 视频内容、时长的分布多样性与均衡性是模型泛化能力的核心影响因素；
② 标注质量同时显著影响模型性能与训练效率，T2V模型上限受视频理解能力约束；
③ classifier-free guidance、高质数据微调仅能部分修复低质预训练数据带来的效果损失，无法完全弥补预训练数据缺陷。
