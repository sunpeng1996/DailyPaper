---
title: 'ZoomCap: Evidence-Routed Visual Zooming for Recoverable Visual Information
  Transfer'
title_zh: ZoomCap：基于证据路由视觉放大的可恢复视觉信息传递框架
authors:
- Hao Shi
- Jiafeng Wang
- Yuzhuo Fu
- Tao Zhang
- Jian Bai
- Juelu Zhang
- Qing Cui
- Chao Huang
affiliations:
- Ant Group
- Zhejiang University
arxiv_id: '2610.21320'
url: https://arxiv.org/abs/2610.21320
pdf_url: https://arxiv.org/pdf/2610.21320
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态 · 高质量VLM训练字幕生成
tags:
- Visual Captioning
- Multimodal LLM
- VLM Training
- Fact Verification
- OCR Recognition
one_liner: 提出证据路由的视觉放大字幕框架ZoomCap与事实校验机制FactCycle，小模型生成质量远超10倍大模型的可信字幕
practical_value: '- 电商商品图/广告素材自动字幕生成可复用ZoomCap的自适应区域放大+OCR敏感识别逻辑，提升细粒度属性（小字体参数、边角细节）提取准确率

  - 多模态RAG的素材事实校验可复用FactCycle的双锚点（源图像真实性+重建可实现性）打分逻辑，降低图文不符的幻觉率

  - 小参数多模态模型预训练可直接复用公开的ZoomCap-450K字幕语料，无需调用大模型生成训练数据，降本提效'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有单轮生成的图像字幕易遗漏小物体、文字、空间关系，常将长度等同于质量，还会输出幻觉内容，无法为VLM训练提供高质量可信监督信号。
### 方法关键点
1. 将细粒度字幕生成定义为可恢复视觉信息传递任务，基于初稿字幕路由执行知识检索、OCR敏感识别、覆盖缺口补全、自适应视觉放大，仅对复杂区域做深层裁剪，结合几何信息推导空间关系，融合非重复证据生成字幕；
2. 提出FactCycle机制，从源图像真实性、重建可实现性两个锚点对原子描述逐句打分，精准区分幻觉内容。
### 关键结果
对比Qwen3.5-397B生成的字幕，仅为其1/10大小的ZoomCap教师模型获得81.9%的人工偏好率；单图有效事实点达52.4个，是ScaleCap的1.66倍；用其语料预训练的VLM在11个基准上平均提升1.31-2.38分，医疗VQA任务平均提升3.04分
