---
title: Attention-Guided Saliency Maps for Interpreting Visualization Literacy in VLMs
title_zh: 基于注意力引导的显著性图解释多模态大模型的可视化理解能力
authors:
- Maeve Hutchinson
- Abderrahmane Wassim Mehdaoui
- Pranava Madhyastha
affiliations:
- City St George’s, University of London
- The Alan Turing Institute
arxiv_id: '2607.16105'
url: https://arxiv.org/abs/2607.16105
pdf_url: https://arxiv.org/pdf/2607.16105
published: '2026-07-17'
collected: '2026-07-20'
category: Multimodal
direction: 多模态大模型可解释性 · 注意力引导显著性图
tags:
- VLM
- Saliency Map
- XAI
- Attention Mechanism
- Visual Interpretation
one_liner: 提出轻量无梯度的注意力聚合显著性图方法，可定位VLM生成文本对应关注的图像区域
practical_value: '- 做多模态商品理解、广告图点击率预估的VLM可解释性时，可复用该无梯度注意力聚合方案，快速定位模型对商品/广告图的关注区域是否匹配卖点等业务预期

  - 做图文生成式推荐、智能导购Agent的VLM推理校验时，可通过该方法生成的显著性图验证模型回答商品咨询时是否正确关注对应图表/图片区域，降低幻觉

  - 该方法无需反向传播，计算 overhead 极低，可直接集成到现有VLM服务的诊断模块，无需修改模型结构，工程落地成本低'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLM已广泛用于图表问答、趋势总结、数据提取等分析任务，但现有基准仅验证输出文本的正确性，无法判断模型是否正确关注可视化图像中的对应语义区域，推理可靠性无法保障

### 方法关键点
1. 聚合Transformer语言模型所有头、所有层对视觉token的注意力权重，映射回视觉编码器的图像patch网格，直接建立每个生成答案token与对应关注图像区域的对应关系
2. 完全无需梯度计算，轻量高效

### 关键结果
通过删除度量（deletion metric）验证，生成的显著性图与模型实际行为的因果一致性达标，可有效检验模型注意力是否与语义相关区域对齐
