---
title: 'HOMIE: Human-object Centric Video Personalization via Multimodal Intelligent
  Enchancement'
title_zh: HOMIE：基于多模态智能增强的人-物中心视频个性化生成框架
authors:
- Yiyang Cai
- Nan Chen
- Rongchang Xie
- Junwen Pan
- Chunyang Jiang
- Cheng Chen
- Wen Zhou
- Zhenbang Sun
- Wei Xue
- Wenhan Luo
affiliations:
- Hong Kong University of Science and Technology
arxiv_id: '2607.18217'
url: https://arxiv.org/abs/2607.18217
pdf_url: https://arxiv.org/pdf/2607.18217
published: '2026-07-19'
collected: '2026-07-22'
category: Multimodal
direction: 多模态视频生成 · 人-物交互个性化
tags:
- MLLM
- Video Diffusion
- Personalized Generation
- Multimodal Fusion
- DiT
one_liner: 保留原生文本编码器融合MLLM知识，实现人-物中心视频个性化生成SOTA性能
practical_value: '- 做电商商品演示/数字人带货等个性化视频生成时，可复用「保留原生文本编码器+额外注入MLLM语义特征」的架构，无需重新对齐整个文本编码器，大幅降低训练成本

  - 处理多模态输入（商品图、人像图、文本prompt、OCR信息）时，可借鉴Modality-Reference Embedding（MRE）设计，区分模态和参考实体，避免不同参考的特征混淆，尤其适合同个商品多视角/多属性参考的场景

  - 做品牌logo/商品信息植入类生成任务时，可复用Global Multimodal Guidance（GMG）设计，将MLLM的语义推理能力注入扩散模型自注意力层，提升抽象概念和实体的绑定准确率

  - 训练多模态生成模型时可采用分阶段训练策略：先单主体学好特征一致性，再多主体学交互关系，最后高分辨率微调，平衡训练效果和成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
人-物中心视频个性化（HOCVP）是可控视频生成的高价值方向，可广泛应用于电商商品演示、数字人带货、品牌内容生成等场景，但现有方法存在两个核心痛点：一是跨主体场景下难以平衡主体保真度和人-物交互准确性，尤其无法处理logo这类抽象概念的自动关联植入；二是同主体多参考（如多视角图、OCR贴图）场景下缺乏语义关联机制，难以利用参考信息提升生成保真度；现有MLLM融合方案要么会破坏原生文本编码器的可控性，要么需要全量重新对齐，训练成本极高。

### 方法关键点
- 采用保留原生文本编码器的MLLM融合架构，避免重对齐成本，让MLLM专注于提取参考间的语义关联，无需承担基础文本控制任务
- 设计Global Multimodal Guidance（GMG）模块，在DiT自注意力的Query/Key计算阶段注入MLLM的全局语义特征，对齐MLLM语义和VAE token，提升人-物交互、抽象概念绑定的准确性
- 设计Modality-Reference Embedding（MRE）模块，通过可学习的模态嵌入和参考嵌入，区分不同模态的token，同时绑定同主体的多参考token，避免特征混淆
- 构建3类训练数据集，采用分阶段训练策略：先单主体训练学特征一致性，再多主体训练学交互关系，最后高分辨率微调提升画质

### 关键实验结果
基于Wan2.1/2.2-14B开源视频模型训练，对比Kling 1.6、Phantom、UniVideo等10+SOTA方案，在200个自研人-物交互测试样本上，OCR准确率较最优基线提升21.8%，多视角重建指标DINOrec达到0.685，40人用户调研中主体一致性、文本遵循度、整体质量三项指标均位列第一，训练仅消耗11K A100 GPU小时，仅为同类MLLM融合方案的1/3左右。

**最值得记住的一句话**：MLLM融合生成任务中，保留原生成熟模块的能力、让MLLM专注解决其擅长的语义推理问题，往往比替换整个模块的方案性价比高得多
