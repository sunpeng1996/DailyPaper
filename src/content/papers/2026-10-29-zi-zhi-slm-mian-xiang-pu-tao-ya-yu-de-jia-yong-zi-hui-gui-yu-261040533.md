---
title: 'Homebrewed SLMs: Autoregressive and Masked Diffusion Language Models Built
  at Home for Portuguese'
title_zh: 自制SLM：面向葡萄牙语的家用自回归与掩码扩散语言模型教程
authors:
- Pedro Carvalho Brom
affiliations:
- Department of Mathematics, Federal Institute of Brasília
arxiv_id: '2610.40533'
url: https://arxiv.org/abs/2610.40533
pdf_url: https://arxiv.org/pdf/2610.40533
published: '2026-10-29'
collected: '2026-10-31'
category: LLM
direction: 小语言模型 · 单卡训练与领域适配评估
tags:
- SLM
- consumer-GPU-training
- autoregressive-LM
- masked-diffusion
- domain-LLM-evaluation
one_liner: 提供单消费级GPU从零训练11-12M参数小语言模型的工具链与领域适配评估流程
practical_value: '- 垂直场景轻量模型验证可参考该10M级小LM训练方案，单消费级GPU即可完成从Tokenizer到模型的全流程训练，适合快速验证电商合规校验、广告文案质检等轻量需求

  - 垂直场景模型效果评估可复用其预注册对比协议框架，以n-gram基线作为兜底效果锚点，快速判断自研小模型是否达到业务可用阈值

  - 轻量填空、异常文本检测类任务可尝试掩码扩散LM架构，同等参数量下效果优于自回归LM，且在训练集未覆盖的细分品类上泛化表现更好'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
垂直领域用户普遍缺乏可落地的低成本小LM训练指导，不清楚是否需要大算力才能训练适配自身场景的语言模型。
### 方法关键点
- 基于单消费级GPU实现从Tokenizer到模型的全流程从零训练，统一架构支持自回归与掩码扩散两种生成模式
- 发布可直接复用的Python包、训练Notebook，以及预注册的领域模型对比评估协议，以Kneser-Ney 6-gram作为基线锚点
- 选取巴西葡萄牙语散文、联邦法律作为测试集，覆盖文本续写、篡改检测、交叉引用填空等任务
### 关键结果
- 11-12M参数量模型自回归模式训练64epoch后开始过拟合，掩码扩散模式训练到256epoch仍有效果提升，最优效果下扩散模式比特/字节指标比自回归高0.06
- 交叉引用填空任务上，在训练集未覆盖的法令类文本中，效果超过160M、630M参数量的公开大模型，篡改检测任务优于6-gram基线
- 法律文本续写、篡改检测任务上，公开大模型（训练算力是其10^2~10^5倍）效果更优
