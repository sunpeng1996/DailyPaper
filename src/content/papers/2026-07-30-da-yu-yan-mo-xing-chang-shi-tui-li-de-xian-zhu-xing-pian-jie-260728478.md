---
title: Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language
  Models in Commonsense Reasoning
title_zh: 大语言模型常识推理的显著性偏差揭示与SaliTrap基准构建
authors:
- Zheng Wu
- Chenhao Xue
- Shijie Zheng
- Yijie Lu
- Cheng Yang
- Zhuosheng Zhang
affiliations:
- Shanghai Jiao Tong University
- ByteDance Inc
arxiv_id: '2607.28478'
url: https://arxiv.org/abs/2607.28478
pdf_url: https://arxiv.org/pdf/2607.28478
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: LLM常识推理·鲁棒性优化
tags:
- LLM
- Commonsense Reasoning
- Salience Bias
- Benchmark
- Prompt Engineering
one_liner: 识别LLM被显式干扰项劫持忽略常识的显著性偏差，构建SaliTrap基准验证其源于知识抑制而非缺失，轻量prompt可缓解
practical_value: '- 电商智能客服/导购Agent可前置系统prompt做任务前提校验，避免被用户提问中的数值等干扰项带偏，输出违反常识的错误建议，无需微调即可大幅降低低级错误率。

  - Agent做工具调用/任务规划前，增加1步轻量前提校验逻辑，要求模型先判断任务是否具备常识可行性，可有效减少无意义工具调用和错误规划。

  - 构建业务鲁棒性评测集时可复用SaliTrap构建流程：专家种子生成→LLM扩量→多层规则校验→真实模型验证筛选bad case，低成本产出高区分度的评测数据。

  - LLM出现常识类错误时优先尝试prompt干预而非微调，90%以上的这类错误属于知识被抑制而非缺失，prompt调整的投入产出比远高于微调。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在数学、代码、Agent任务上的训练范式默认输入给出的所有条件均有用，导致模型过度关注输入中的显式干扰项（如数值），忽略任务隐含的物理/常识前提，出现显著性偏差。但此前无法确定这类错误是模型真的缺乏对应常识，还是常识被误导性任务框架抑制，也缺乏专门基准系统性研究该问题。

### 方法关键点
- 正式定义显著性偏差：LLM被输入中无用的显式干扰项劫持，忽略任务隐含常识前提的错误模式
- 构建SaliTrap基准：覆盖4类陷阱维度（缺失前提、环境不匹配、时间/生理违反、规则不匹配）共1145个样本，每个样本嵌入数值干扰项，通过「专家种子生成→LLM辅助扩量→三层校验（真实性、对齐性、自然度）→Solver-Judge验证」流程构建，保证样本迷惑性与合理性
- 设计两类核心实验：12个主流SOTA LLM零样本评测，用TAR（陷阱规避率）、HFR（硬错误率）、SCR（奉承服从率）、SI（奉承指数）度量偏差程度；知识重唤起实验验证偏差成因，测试3种推理时prompt干预的缓解效果

### 关键实验结果
12个SOTA LLM全部存在显著性偏差：最强的Claude-Opus-4.7的TAR仅为54.8%，8/12的模型TAR低于30%；即使检测到陷阱，GLM-5.1和Kimi-K2的服从率仍高达86.2%和81.8%，检测与规避是完全独立的能力。数值干扰项密度每提升1个单位，TAR单调下降，CoT被劫持率单调上升。剥离任务框架的知识探针可恢复超过90%的奉承服从错误，证明偏差源于知识抑制而非缺失；仅用推理时系统prompt干预即可大幅提升TAR，弱模型提升幅度尤其显著。

### 最值得记住的一句话
LLM的常识推理瓶颈大多不在模型能力本身，而在知识的唤起方式，轻量推理时干预的投入产出比往往远高于重新训练。
