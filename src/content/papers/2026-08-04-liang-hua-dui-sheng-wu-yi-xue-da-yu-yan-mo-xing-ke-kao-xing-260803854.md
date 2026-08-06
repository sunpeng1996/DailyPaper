---
title: Quantization Effects on Biomedical LLM Reliability
title_zh: 量化对生物医学大语言模型可靠性的影响研究
authors:
- Anton Rasmussen
- Hong Qin
affiliations:
- Old Dominion University
arxiv_id: '2608.03854'
url: https://arxiv.org/abs/2608.03854
pdf_url: https://arxiv.org/pdf/2608.03854
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM可靠性评估 · 量化与校准优化
tags:
- Quantization
- LLM Calibration
- Prompt Engineering
- Model Evaluation
- Inference Optimization
one_liner: 通过受控实验量化提示模板、打分规则、量化精度对LLM分类准确率与校准度的影响幅度
practical_value: '- 落地LLM分类类任务（如query意图识别、用户评论情感分类）时可优先选用INT8量化，准确率/F1损失仅1-2pp，可大幅降低推理成本

  - 做分类置信度校验、召回排序得分校准时，需对比求和/均值token log-likelihood两种打分策略，其对校准度的影响远大于量化精度

  - 提示模板对准确率的影响可达7-24pp，超过模型选型差异，业务上线前需做多模板AB测试，不要盲目迷信通用指令微调模型'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM作为分类器落地时，提示模板、打分规则、量化精度等实现选择对结果的影响极少被系统量化，难以指导工程选型与效果优化。
### 方法关键点
针对3款Mistral-7B变体（Base、BioMistral、Instruct），在PubMed RCT句子分类任务上做控制变量测试，覆盖FP16/INT8/INT4三种推理精度、4种提示模板、求和/均值token log-likelihood两种打分规则。
### 关键结果数字
1. 打分规则直接逆转模型校准度排名：BioMistral平均ECE从0.097升至0.289，Instruct从0.237降至0.096，专业微调模型准确率波动<1pp；
2. 提示模板带来7~24pp的准确率差异，影响幅度超过模型选型；
3. INT8量化对微调模型的准确率/F1影响仅1~2pp，INT4无灾难性精度损失；
4. 温度缩放仅对求和打分规则的校准度有优化效果。
