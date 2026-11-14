---
title: Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection
title_zh: 面向人脸呈现攻击检测的上下文预测低秩适配方法
authors:
- Aminu Yusuf
- Shakeel Muhammad Ibrahim
- Sulaimon Oyeniyi Adebayo
- Muhammad Sohail Ibrahim
- Muhammad Shahid Jabbar
- Shujaat Khan
arxiv_id: '2611.16534'
url: https://arxiv.org/abs/2611.16534
pdf_url: https://arxiv.org/pdf/2611.16534
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: 人脸反欺诈 · 预训练模型跨域微调
tags:
- LoRA
- CLIP
- JEPA
- Transfer Learning
- Face Anti-Spoofing
one_liner: 结合JEPA上下文预测目标与LoRA微调CLIP，提升人脸反欺诈跨域泛化性能
practical_value: '- 预训练视觉模型跨域微调可复用「LoRA+JEPA上下文预测目标+EMA教师模型」范式，无推理额外开销即可提升泛化性

  - 分类任务微调可叠加掩码分类、预测一致性辅助损失，强化局部关键特征学习能力，降低对全局分布的依赖

  - 该训练框架可直接迁移到电商内容风控场景（如人脸实名认证、虚假素材识别）的视觉模型调优'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
人脸呈现攻击检测（PAD）需要适配跨设备、主体、攻击介质的鲁棒特征，传统CLIP二分类微调仅监督最终决策，未约束局部人脸防伪线索的表征，跨域泛化能力不足。
### 方法关键点
提出CP-JEPA适配框架，对预训练CLIP图像编码器做LoRA微调，引入JEPA联合嵌入预测目标：学生网络预测掩码空间位置的全图教师特征，结合未掩码分类、掩码分类、预测一致性损失关联防伪二分类任务，EMA教师模型提供动态隐层目标，推理仅保留LoRA微调后的CLIP编码器+二分类头，无额外 overhead。
### 关键结果
- OCIM基准：3.74% mean HTER、98.73% mean AUC
- 单源跨12组源-目标组合：11.36% mean HTER
- 加入CelebA-Spoof训练后：mean HTER降至2.35%，AUC升至99.32%
- SiW-Mv2未见攻击类别：3.36% mean HTER
