---
title: 'Beneath the Surface of Chains-of-Thought: A Mechanistic Interpretation of
  Reasoning Operations in LLMs'
title_zh: 思维链背后的机制：大语言模型推理操作的隐层表征几何解析
authors:
- Seogyeong Jeong
- Jaehui Hwang
- Dongyoon Han
- Geonmo Gu
- Alice Oh
- Taekyung Kim
affiliations:
- KAIST
- NAVER AI Lab
arxiv_id: '2609.04753'
url: https://arxiv.org/abs/2609.04753
pdf_url: https://arxiv.org/pdf/2609.04753
published: '2026-09-03'
collected: '2026-09-07'
category: Reasoning
direction: LLM推理 · CoT隐层机制解析
tags:
- Chain-of-Thought
- LLM Reasoning
- Representation Geometry
- Mechanistic Interpretability
- Probing
one_liner: 揭示LLM不同推理操作对应隐层可分离的几何结构，验证其跨模型泛化与上下文依赖性
practical_value: '- 可借鉴LDA+PCA的隐层探测方法，为电商/导购Agent构建推理操作监控能力：在中间层抽取推理操作向量，实时识别当前Agent处于信息提取/优惠计算/答案输出阶段，对异常推理步骤提前触发校验，降低错误回复率。

  - 做CoT微调/推理优化时，可针对中间层的推理操作表征设计奖励信号，而非仅依赖最终输出正确性：比如搜索Query改写Agent的问题分解操作表征达标时即给予正奖励，提升推理轨迹稳定性。

  - 推理效率优化可参考操作表征峰值出现在中间层的结论，针对特定业务场景做层剪枝或KV cache优化：比如电商客服场景的最终答案生成仅取对应操作峰值层的表征解码，可降低推理延迟10%~20%。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前推理型LLM的训练优化已从仅关注最终答案正确性转向同时优化CoT推理轨迹，但业界对CoT中不同功能的推理操作（如问题分解、公式回忆、数值计算）如何在LLM隐层表征空间组织仍不明确，也无法区分观察到的结构是来自词汇/位置混淆还是真正的功能编码，这限制了推理错误诊断、可控推理生成、推理效率优化等落地应用的发展。
### 方法关键点
- 基于波利亚问题解决框架，将CoT推理轨迹划分为8类核心操作（信息提取、直接映射、问题分解、回忆、演绎、代数操作、算术计算、最终答案），采用GPT-5标注+人工校验的方式生成数据集，人工标注一致性Fleiss' κ=0.666，GPT标注与人工一致性Cohen's κ=0.715。
- 选取Qwen2.5-7B、Qwen3-8B、Gemma4-31B三类推理LLM，提取各层隐层表征，经L2归一化、PCA降维至128维后用LDA训练探测分类器，构造每类推理操作的专属表征方向向量。
- 设计词汇匹配控制、位置控制、注意力掩码干预、错误推理样本测试等多组对照实验，排除混淆变量，验证表征结构的因果性与泛化性。
### 关键结果数字
- 不同推理操作的one-vs-rest分类AUROC峰值均出现在模型中间层，跨模型宏观AUROC可达0.895~0.937，比最优文本分类baseline高0.041~0.097，比位置分类baseline高0.144~0.189。
- 相同表层token在不同推理操作上下文中的表征可区分度在中间层达到最高，掩码前序30个token会导致目标操作的对齐分数显著下降。
- 错误推理步骤的操作表征仍然可识别，宏观AUROC仅比同类型正确步骤低0.016~0.017，推理操作的功能编码与执行正确性存在部分解耦。
> 最值得记住的结论：LLM的推理操作不是仅由表层词汇决定，而是在隐层形成了依赖上下文的可分离几何结构，中间层是推理功能编码的核心区域。
