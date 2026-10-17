---
title: 'Lexical Reference Frames: Interpreting LM Residual Streams in Native Semantics'
title_zh: 词汇参考框架：基于原生语义解读大语言模型残差流
authors:
- Jian Gu
- Hongyu Zhang
- Chunyang Chen
- Aldeida Aleti
affiliations:
- Monash University
- Chongqing University
- Technical University of Munich
arxiv_id: '2610.22169'
url: https://arxiv.org/abs/2610.22169
pdf_url: https://arxiv.org/pdf/2610.22169
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: 大语言模型可解释性 · 残差流解读
tags:
- Interpretability
- ResidualStream
- LogitLens
- EarlyExit
- ModelSteering
- Attribution
one_liner: 提出无需训练的自适应词汇参考框架，可精准解读LLM中间层隐藏状态，支持早退出、干预与归因
practical_value: '- 做LLM服务推理优化可直接复用LEXFRAME[1]做早退出，无需额外训练就能跳过40%+的层，推理延迟降低的同时精度损失极小，适配电商客服、商品文案生成等低延迟场景

  - 做LLM输出干预（如电商推荐话术调优、有害回复拦截）可复用词汇基地方案，相比传统激活加法干预，对其他token的干扰降低70%以上，能实现更精准的输出控制

  - 做LLM归因分析（如推荐话术转化效果归因、幻觉定位）可替换传统logit lens/归因修补方案，LEXFRAME[1]的归因相关性提升4倍以上，定位更精准

  - 做模型蒸馏/压缩时，可用词汇参考框架做中间层对齐，相比传统隐藏状态直接对齐，蒸馏后小模型的语义一致性更高，适配端侧推理场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM中间层隐藏状态解读方法存在明显缺陷：固定logit lens/调优lens无视上下文差异，在中间层偏差极大；点云统计方法仅描述状态分布，无法反映模型实际计算逻辑；两类方法都无法支撑早退出、输出干预、归因等落地需求，亟需能匹配模型自身计算逻辑的解读方案。

### 方法关键点
- 提出词汇参考框架（LEXFRAME），通过模型自身剩余层传输隐藏状态，无需拟合模型输出，自适应上下文和层位置
- 按保留的注意力轮次划分阶数：LEXFRAME[0]仅保留单位置传输、无视上下文；LEXFRAME[1]保留1轮前缀注意力，覆盖大部分语义；LEXFRAME[∞]等价原生模型
- 高阶框架仅需替换剩余注意力为预计算的典型注意力输出，无需额外训练，可在任意层快速计算隐藏状态的词汇语义映射

### 关键实验
测试数据集为WikiText-103，验证模型为SmolLM3-3B、OLMo3-7B，对比baseline包括logit lens、Jacobian lens、线性探针、点云距离等。核心结果：LEXFRAME[1]在中间层和原生框架的余弦一致性达0.97，远优于lens的0.3左右的理论上限；与模型输出的KL散度仅0.16/0.15 nat，top1 token匹配率达86%；支持早退出跳过45%/42%的层，归因相关性达0.88/0.90，输出干预的旁侧干扰降低70%。

### 核心结论
解读LLM隐藏状态的核心是用模型自身的方式读取：通过剩余层计算、结合上下文、基于原生词汇语义，效果远超任意固定映射方案。
