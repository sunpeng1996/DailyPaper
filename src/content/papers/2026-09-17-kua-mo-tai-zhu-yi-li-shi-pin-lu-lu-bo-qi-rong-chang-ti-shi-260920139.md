---
title: 'Cross-Modal Attention Acts as a Frequency Filter: Why Verbose Prompts Improve
  Robustness in Vision-Language Models'
title_zh: 跨模态注意力是频率滤波器：冗长提示提升VLM鲁棒性的机制
authors:
- Farooq Ahmad Wani
- Maria Sofia Bucarelli
- Mujtaba Hussain Mirza
- Oleksandr Pryymak
- Aryo Pradipta Gema
- Iacopo Masi
- Pasquale Minervini
- Fabrizio Silvestri
affiliations:
- Sapienza University of Rome
- Université Côte d'Azur
- University of Edinburgh
- CNRS
- Inria
arxiv_id: '2609.20139'
url: https://arxiv.org/abs/2609.20139
pdf_url: https://arxiv.org/pdf/2609.20139
published: '2026-09-17'
collected: '2026-09-18'
category: Multimodal
direction: 多模态大模型 · 鲁棒性优化
tags:
- VLM
- Cross-Modal Attention
- Prompt Engineering
- Model Robustness
- Frequency Filter
one_liner: 揭示VLM跨模态注意力的频率滤波效应，提出冗长提示法提升图像损坏场景下的模型鲁棒性
practical_value: '- 电商多模态商品理解、审核场景中，可给VLM推理提示添加“请仔细观察图片后作答”类冗余前缀，提升低质模糊商品图的识别准确率

  - 处理用户细粒度多模态查询（如“这件T恤左胸印花是什么颜色”）时，可先改写prompt增加冗余描述，降低图像压缩、模糊等损坏带来的输出漂移

  - 可复用跨模态注意力的频率滤波视角，优化多模态召回、多模态推荐模型的抗噪能力，适配用户上传的低质UGC商品图场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
VLM广泛应用于图像理解、多模态Agent等场景，但输入图像存在压缩、模糊等损坏时模型鲁棒性极差，prompt措辞对VLM性能的影响机制此前未被明确，无法针对性优化低质输入场景的效果。
### 方法关键点
发现prompt措辞对VLM鲁棒性存在两种相反影响：冗长提示会拓宽跨模态注意力的频率支持范围，而细粒度语义查询会让频率范围集中在少量视觉尺度；当注意力滤波范围和图像损坏的空间频率重叠时，模型输出漂移最严重。
### 关键结果
在Qwen3-VL、LLaVA-OneVision 8B模型上跨GQA、CLEVR数据集验证，冗长改写可降低70%~81%的输出漂移方差，即使在图像损坏场景下也能带来可观测的准确率提升
