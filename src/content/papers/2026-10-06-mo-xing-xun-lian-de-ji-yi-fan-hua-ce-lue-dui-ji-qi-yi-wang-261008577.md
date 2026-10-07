---
title: How Learning Governs Unlearning across the Memorization-Generalization Spectrum
title_zh: 模型训练的记忆-泛化策略对机器遗忘效果的影响机制
authors:
- Hwiyeong Lee
- Hyelim Lim
- Ingyu Bang
- Hoki Kim
- Taeuk Kim
affiliations:
- Seoul National University
- Hanyang University
- Chung-Ang University
arxiv_id: '2610.08577'
url: https://arxiv.org/abs/2610.08577
pdf_url: https://arxiv.org/pdf/2610.08577
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: 大语言模型 · 机器遗忘机制
tags:
- LLMUnlearning
- Memorization
- Generalization
- Grokking
- MachineUnlearning
one_liner: 揭示模型训练时泛化依赖度越高，机器遗忘引发的保留集性能损失越大
practical_value: '- 做电商/推荐场景的LLM遗忘（如删除违规商品信息、用户隐私数据、错误营销规则）时，优先针对高记忆阈值的内容（如特定SKU的独有属性、独有的活动规则）操作，对模型通用语义/推荐能力的损伤更小

  - 执行遗忘时，将目标内容的概率质量重分配到符合原有泛化规则的选项上（如删除某品牌的错误描述时，将概率转移到同品类符合常识的其他描述，而非随机值），可降低30%以上的保留集性能损失

  - 需明确区分「移除训练数据贡献」和「抑制输出行为」两个目标：若要抑制的内容符合通用语义规则（如常识性的品牌归属、产品分类），仅重训练移除对应数据无法达成目标，需额外做行为对齐'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有机器遗忘方案普遍存在保留集性能损伤（retain damage）问题，但过往研究未关注模型训练阶段的记忆/泛化策略对遗忘效果的影响，无法解释不同内容遗忘后的性能损失差异，也缺乏降低损伤的明确指导原则。
### 方法关键点
- 利用模加法任务的grokking现象，得到训练准确率均为100%但分别依赖纯记忆、纯泛化的两类模型，对比两者遗忘后的性能表现
- 提出分桶模加法（BMA）任务，通过调整桶大小精准控制任务所需的记忆/泛化占比，定义「记忆阈值」为必须通过样本记忆获取的信息位数，实现记忆-泛化光谱的细粒度控制
- LLM场景下以参考模型与目标模型的输出概率差作为记忆阈值的代理，分别在逐字回忆、事实回忆两个通用场景验证规律
### 关键结果数字
- 模加法任务中，相同遗忘程度下，纯记忆模型的保留集准确率为59.5%，纯泛化模型仅为8.1%
- BMA任务中，记忆阈值每提升2bit，保留损伤平均下降15%以上，趋势呈单调变化
- LLM事实回忆场景中，低记忆阈值的属性（如符合命名规则的邮箱、国籍）遗忘后的保留损伤比高记忆阈值的属性（如随机UUID）高40%左右
### 核心结论
机器遗忘的保留损伤程度与模型对泛化规则的依赖度呈单调正相关，降低遗忘副作用的核心是保护共享泛化机制
