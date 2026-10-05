---
title: 'DEFINE: Exemplar-Guided Accent Control for Zero-Shot TTS'
title_zh: DEFINE：基于样本引导的零样本TTS口音控制框架
authors:
- Ambuj Mehrish
- Abhinaba Roy
- Alex Ivanov
- Tawsif Ahmed
- Dorien Herremans
affiliations:
- Ca’ Foscari University of Venice
- Kandinsky Lab
- Sleeping AI
- Singapore University of Technology and Design
arxiv_id: '2609.32777'
url: https://arxiv.org/abs/2609.32777
pdf_url: https://arxiv.org/pdf/2609.32777
published: '2026-09-29'
collected: '2026-10-05'
category: Other
direction: 零样本TTS · 口音解耦控制
tags:
- TTS
- LoRA
- Zero-Shot
- Accent Control
- F5-TTS
one_liner: 基于F5-TTS与LoRA实现零样本TTS中说话人身份与口音的独立可控调节
practical_value: '- 多属性解耦+推理端权重调节的设计思路，可复用在生成式推荐场景的可控生成（如指定风格的广告文案生成、定向属性的商品推荐）

  - 预训练大模型+LoRA适配的参数高效微调方案，可直接迁移到搜索推荐/Agent相关大模型落地，降低训练部署成本

  - 无推理标注依赖的原型监督训练方法，可用于低标注成本的用户行为语义特征提取、商品Semantic ID生成等场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有零样本TTS将说话人身份与口音耦合在同一参考音频中，无法独立控制；传统方案依赖口音标注或级联多模型，推理效率低、效果折损严重。

### 方法关键点
1. 基于F5-TTS架构搭建，用LoRA做参数高效适配，训练成本低；
2. 设计独立的样本编码器将短口音样本映射到条件空间，通过预学习的口音原型做监督，推理无需口音标签或后处理；
3. 仅调节推理阶段引导权重即可连续控制口音强度，无需重训练模型。

### 关键结果数字
可见口音场景下，提升口音探测准确率从6.5%到19.6%；在可见/域外口音场景下，口音迁移效果匹配TTS+语音转换的双模型级联方案，同时说话人相似度更高，语音质量相当，支持训练集未见过的口音控制。
