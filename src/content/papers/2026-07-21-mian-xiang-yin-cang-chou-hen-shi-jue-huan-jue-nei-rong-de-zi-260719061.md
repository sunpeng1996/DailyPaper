---
title: 'Now You See the Hate: Adaptive View Retrieval for Hidden Hateful Illusions'
title_zh: 面向隐藏仇恨视觉幻觉内容的自适应视图检索检测方法
authors:
- Qianpu Chen
- Derya Soydaner
affiliations:
- LIACS, Leiden University
arxiv_id: '2607.19061'
url: https://arxiv.org/abs/2607.19061
pdf_url: https://arxiv.org/pdf/2607.19061
published: '2026-07-21'
collected: '2026-07-23'
category: Multimodal
direction: 多模态内容审核 · 隐藏幻觉内容检测
tags:
- Multimodal Safety
- Content Moderation
- Adaptive Retrieval
- CLIP
- Perceptual Retrieval
one_liner: 将隐藏仇恨视觉幻觉检测转化为感知检索问题，提出自适应视图检索框架大幅提升检测性能
practical_value: '- 电商/内容平台UGC/PGC合规审核场景，可借鉴「先做视图变换检索再判定违规」的框架，替代原图直接过分类器的传统流程，提升隐藏违规符号/内容的识别率

  - 现有多模态审核模型无需重新微调，基于冻结CLIP加视图检索校准的轻量流程即可大幅提升隐藏违规内容检测效果，降低迭代成本

  - 做合规检测时可提前构建违规内容模板库，配合自适应视图选择召回隐藏违规信息，效果优于固定图像变换的过滤方案'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前多模态安全系统对视觉幻觉中隐藏的仇恨内容识别能力极差，6款审核分类器最高准确率仅24.5%，9款SOTA VLM搭配幻觉感知prompt后准确率≤10.2%，绝大多数隐藏仇恨内容漏检。
### 方法关键点
将隐藏仇恨幻觉检测定义为感知检索问题，提出retrieve-and-calibrate框架：1）构建图像互补视图库与隐藏消息模板库；2）自适应筛选可信视图，检索匹配隐藏消息身份；3）校准恢复的内容是否违规。
### 关键结果
使用冻结CLIP编码器在HatefulIllusion留出测试集上达到93.2%的平衡准确率，大幅优于原图基线与固定单变换过滤器；效果超过官方微调CLIP基线，在IllusionMNIST等3个数据集上达到或超过人类性能，在HC-Bench的SemVink协议下优于缩小预处理方案。
