---
title: Credal Large Language Models for Semantic Commitment under Uncertainty
title_zh: 面向不确定性场景下语义承诺的Credal大语言模型（CLLM）
authors:
- Shireen Kudukkil Manchingal
- Sofiia Nikolenko
- Fabio Cuzzolin
affiliations:
- Oxford Dynamics
- Ludwig-Maximilians-Universität München
- Oxford Brookes University
- Institute for Artificial Intelligence, Data Analysis and Systems (AIDAS)
arxiv_id: '2608.23244'
url: https://arxiv.org/abs/2608.23244
pdf_url: https://arxiv.org/pdf/2608.23244
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: 大语言模型 · 不确定性量化与校准
tags:
- LoRA
- Uncertainty Quantification
- Hallucination Detection
- Calibration
- Ensemble
one_liner: 通过LoRA集成构造credal集输出概率上下限，配套两类承诺得分提升LLM不确定性量化性能
practical_value: '- 电商智能客服/导购Agent场景可直接复用低成本CTC得分，快速检测回答可信度，对低置信度结果触发兜底/转人工，无需额外生成开销，降低幻觉带来的客诉风险

  - 生成式推荐/商品文案生成场景可复用SCC得分，交叉校验token级和语义级一致性，过滤表面通顺但事实错误（如参数标错、品牌错配）的生成内容

  - 现有LoRA微调管线无需改造，仅训练5个不同初始化的LoRA即可构造credal集，工程成本极低，可快速获得可靠的不确定性信号

  - 高可靠性QA场景（如售后咨询）可复用选择性预测策略，80%覆盖率下可将回答准确率提升至99%级，兼顾用户体验与回答正确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM仅通过单个softmax分布表示不确定性，混淆认知无知与真实歧义，易输出高置信度幻觉回答，在高可靠性场景存在明显风险；现有贝叶斯LoRA、集成等方法仅输出单值不确定性统计量，丢失了预测概率本身的分布差异信息。
### 方法关键点
- 用M=5个仅初始化种子不同的LoRA适配器集成，在冻结骨干上构造credal集，输出每个token的概率上下限，避免平均化ensemble的分布差异
- 提出Credal Token Commitment（CTC）得分，融合token下界支持度、credal宽度、交叉熵三类信号，无需额外采样生成即可计算
- 提出Semantic Commitment Consistency（SCC）得分，交叉校验token级承诺与语义聚类结果的一致性，配套SCC-Gap衡量两者不匹配度
### 关键结果
在Gemma-2-9B、Llama-3.1-8B、Qwen2.5-7B三个开源模型上跨OpenBookQA、CoQA、TriviaQA、ARC-Challenge 4个数据集测试，对比标准LLM、LoRA集成、贝叶斯LoRA等6类基线：
1. 80%覆盖率下，SCC得分在OpenBookQA上达到99.0%准确率
2. ARC-Challenge任务中，Csem置信度跨三个骨干ECE均≤0.6%，Qwen2.5-7B上ECE<0.1%
3. 幻觉检测任务中，CTC无需额外生成即可在7/8设置下与最优基线差距小于1.5pp
### 核心结论
基于LoRA集成的credal集表示可在极低工程开销下，获得比单分布/平均集成更可靠的LLM不确定性信号，有效区分认知不确定性与真实歧义
