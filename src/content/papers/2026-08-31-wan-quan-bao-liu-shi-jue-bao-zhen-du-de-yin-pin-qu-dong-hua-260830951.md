---
title: Audio-Driven Adversarial Defense for 3D Talking Face Generation with totally
  Visual Fidelity Preservation
title_zh: 完全保留视觉保真度的音频驱动3D说话人脸生成对抗防御
authors:
- Rui-Qing Sun
- Chen-Hao Cui
- Hui-Yang Zhao
- Tian Lan
- Zhijing Wu
- Xian-Ling Mao
affiliations:
- Beijing Institute of Technology
arxiv_id: '2608.30951'
url: https://arxiv.org/abs/2608.30951
pdf_url: https://arxiv.org/pdf/2608.30951
published: '2026-08-31'
collected: '2026-09-06'
category: Multimodal
direction: 多模态对抗防御 · 生成肖像隐私保护
tags:
- Adversarial Defense
- 3D Talking Face Generation
- Psychoacoustic Masking
- Audio Perturbation
- Privacy Protection
one_liner: 利用心理声学掩蔽在音频中注入不可感知扰动，实现无视觉损失的3D说话人脸生成伪造防御
practical_value: '- 电商数字人直播、虚拟代言人场景可复用该思路，对音频输入注入不可感知扰动，防止第三方盗用己方数字人形象进行语音驱动伪造

  - 涉及用户肖像上传的电商业务（如虚拟试妆、定制个人数字人），可采用音频侧扰动替代视觉侧扰动，不影响用户上传内容观感同时规避身份盗用风险

  - 心理声学掩蔽的扰动注入方法可迁移到语音类内容版权保护场景，避免生成式模型盗用商家专属配音、主播音色'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
生成式肖像模型快速迭代导致身份盗用、隐私泄露风险陡增，现有音频驱动3D说话人脸生成的防御方案依赖视觉域注入扰动，易破坏人脸观感、且经缩放、裁剪等常见变换后防御效果大幅下降。
### 方法关键点
将防御载体从视觉模态迁移至音频模态，利用心理声学掩蔽效应，将防护扰动隐藏在语音信号的人耳感知掩蔽频率区间，既不会造成可感知的语音畸变，又能破坏3D人脸生成模型对音频特征的可靠提取，同时完全不改动原视觉内容，不受视觉变换影响。
### 关键结果
实验验证该方法可在完全保留视觉保真度、语音感知质量无明显下降的前提下，有效抑制3D说话人脸的正确生成，抗变换鲁棒性显著优于传统视觉域防御方案
