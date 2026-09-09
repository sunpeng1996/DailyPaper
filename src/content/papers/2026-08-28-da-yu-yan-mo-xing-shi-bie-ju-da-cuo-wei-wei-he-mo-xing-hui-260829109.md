---
title: 'Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable
  Questions'
title_zh: 大语言模型识别-拒答错位：为何模型回应结构上不可回答的问题
authors:
- Yucheng Du
- Xiyang Hu
affiliations:
- University of Southern California
- Arizona State University
arxiv_id: '2608.29109'
url: https://arxiv.org/abs/2608.29109
pdf_url: https://arxiv.org/pdf/2608.29109
published: '2026-08-28'
collected: '2026-09-09'
category: LLM
direction: LLM对齐 · 内部表征与拒答路由
tags:
- LLM Alignment
- Activation Steering
- Representation Probing
- Safety Refusal
- Unanswerable Questions
one_liner: 发现LLM已编码结构不可答问题识别信号，其与安全拒答方向几乎正交，错误应答本质是路由失败
practical_value: '- 电商/广告Agent的工具调用链路中，可接入A-null探针预检测用户query是否为结构不可答请求（如计算除以0、查询不存在的商品属性），提前触发拒答，避免下游工具报错或返回错误结果，降低用户感知的幻觉率

  - LLM对齐优化时，无需额外训练模型识别不可答问题，仅需将已有的dimp识别信号与拒答路由做绑定，即可低成本提升结构不可答场景的拒答表现，无需全量微调

  - 生成式商品问答场景下，可在生成阶段沿dimp方向做轻量激活引导，减少对不存在的优惠规则、不符合规格的商品参数这类结构不可答问题的错误应答，提升回答可信度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM经常对结构上不可回答的问题（如计算cot(-540°)、调用整数不存在的startswith方法）输出错误答案而非拒答，此前无法明确该问题根因是模型无法识别不可答性，还是识别信号未正确路由到拒答模块，明确根因可大幅降低不可答场景的幻觉，提升模型可靠性。
### 方法关键点
- 提出CosNSRT探针：先将隐藏状态投影到可答问题的PCA子空间的补空间（A-null），过滤可答问题共有的表面特征噪声，再计算不可答与可答样本的均值差得到识别方向dimp
- 对比dimp与已有的安全拒答方向dref,safety的余弦相似度，量化两者对齐程度
- 采用生成时激活引导技术，沿dimp方向加减偏移量，验证该方向对拒答行为的因果性
- 对比基座与指令微调模型的方向夹角，判断错位的产生阶段
### 关键实验
覆盖1.7B~70B共11个主流开源模型，在math800、code800两个结构不可答数据集上验证：探针检测不可答性的平均AUC达0.939；dimp与安全拒答方向的平均余弦仅0.087，几乎正交；生成时沿dimp引导，结构不可答场景的拒答翻转率提升33~52pp；该错位关系在预训练阶段就已存在，指令微调仅平均改变0.037的余弦值。
### 核心结论
LLM对结构不可答问题的错误应答本质是路由失败，而非没有识别能力，现有安全拒答通路并未读取已存在的不可答识别信号。
