---
title: 'MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption
  Pairs'
title_zh: MiD-VLM：检测并定位图文对中的全局语义错误信息
authors:
- Tarunya Prasad
- Bharatesh Chakravarthi
affiliations:
- Arizona State University
arxiv_id: '2610.32967'
url: https://arxiv.org/abs/2610.32967
pdf_url: https://arxiv.org/pdf/2610.32967
published: '2026-10-23'
collected: '2026-10-26'
category: Multimodal
direction: 多模态图文语义不一致检测与定位
tags:
- Multimodal
- VLM
- LoRA
- Misinformation Detection
- Feature Fusion
one_liner: 融合SigLIP、DINOv2特征并LoRA微调Qwen2-VL，实现高准确率图文语义不一致检测与错误token定位
practical_value: '- 电商图文合规审核可复用特征融合方案：将SigLIP图文匹配特征与DINOv2视觉场景特征经MLP投影融合，提升商品主图与详情文案一致性校验准确率，识别货不对板虚假宣传

  - 业务侧可复用LoRA低参微调Qwen2-VL的架构，无需全量微调即可适配自定义图文违规检测需求，大幅降低算力成本

  - 搜索/推荐场景可借鉴token级定位能力，精准定位文案中与图不符的关键词，优化搜索结果图文一致性排序'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有像素级篡改检测方法无法识别「真实图像搭配误导性文案」类语义不一致问题，这类错误图文单独看均合理，仅在跨模态语义层面存在冲突，缺乏高效的检测与定位方案。
### 方法关键点
1. 特征层融合SigLIP的图文联合表征与DINOv2的视觉场景特征，经投影MLP对齐后输入Qwen2-VL-7B；
2. 采用LoRA对VLM做低参适配，同时完成三个任务：图文对真实性二分类、篡改类型识别、误导性caption token定位。
### 关键结果
在DGM4+验证集上，图文真实性二分类任务F1得分达0.9679，验证了低参微调VLM做跨模态语义不一致检测的优异效果。
