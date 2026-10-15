---
title: 'Apertus 1.5: From Open Text Models to Open Multimodal Reasoners'
title_zh: Apertus 1.5：从开源文本模型到开源多模态推理模型
authors:
- Project Apertus
- Yixuan Xu
- Yassine Turki
- Vinko Sabolčec
- Valentina Pyatkin
- Tommy Chu
- Sven Najem-Meyer
- Sean F. Carroll
- Robert Smith
- Raphael Kreft
affiliations:
- ETH Zurich
- EPFL
- HES-SO Valais-Wallis
- FHNW
- SDSC
arxiv_id: '2610.15542'
url: https://arxiv.org/abs/2610.15542
pdf_url: https://arxiv.org/pdf/2610.15542
published: '2026-10-10'
collected: '2026-10-15'
category: LLM
direction: 开源多模态大模型训练与优化
tags:
- Multimodal LLM
- Open Source
- Long Context
- Discrete Tokenization
- Alignment
one_liner: 推出全开源8B/70B多模态大模型，支持262k上下文、可选思考模式，全训练链路公开
practical_value: '- 多模态融合可复用离散Token扩展方案：无需修改LLM主干架构，仅通过扩展词表加入图像/音频离散Token，训练吞吐量接近纯文本训练，适合业务快速迭代多模态导购Agent

  - 长上下文扩展分阶段训练范式：预训练+SFT均加入长上下文专项阶段，上下文窗口从8k逐步扩容到262k，可复用在电商长文档（商品说明书、用户评价汇总）理解场景

  - 低资源多模态数据利用技巧：先通过无配对图像/音频数据学习模态表示，再用配对数据做模态对齐，减少对高质量标注多模态数据的依赖，适合垂类电商（服饰、家居）多模态理解模型训练

  - 思考模式轻量实现方案：无需训练独立模型，仅通过聊天模板开关控制推理链路，8B模型数学推理提升20个点，可复用在电商Agent复杂用户需求推理场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前高能力大模型多为闭源，开源模型普遍缺失全链路数据、训练配方与对齐规则，且多模态能力、长上下文、推理能力落后于闭源方案，面向业务的可定制化开源多模态基座存在明显缺口。

### 方法关键点
- 架构设计：不修改原Apertus 1.0文本模型主干，仅扩展词表加入131072个图像Token、4096个音频Token，多模态输入通过离线离散Token化处理，模型训练无需额外模态编码器，输出层仅保留文本词表
- 训练Pipeline：分四阶段持续预训练（无配对多模态训练→配对多模态对齐→高质量数据冷却→长上下文扩容），后续叠加SFT、长上下文SFT、RLVR、DPO、SDPO对齐，上下文窗口逐步从8k提升到262144 Token
- 思考模式：无需独立训练模型，仅通过聊天模板的请求时开关控制，开启后自动启用推理链路提升复杂任务表现
- 全链路开源：所有权重、训练代码、数据配方、对齐规则均以Apache 2.0许可证发布

### 关键结果
- 8B模型在知识、指令遵循、文化基准上领先同量级全开源模型，指令遵循能力超过所有对比开源模型；开启思考模式后数学推理最高提升20个点
- 多模态能力与同级别开源多模态模型持平，文档理解、长序列低资源语音识别表现突出
- 多模态训练吞吐量接近纯文本训练，256节点8192序列长度下，GPU每秒处理Token数达5474，和纯文本训练的5300-5500基本持平

最值得记住的一句话：全开源多模态大模型可通过无侵入的词表扩展方案实现多模态能力，无需修改主干架构即可兼顾性能与训练效率，是业务侧定制垂类多模态基座的高性价比路径
