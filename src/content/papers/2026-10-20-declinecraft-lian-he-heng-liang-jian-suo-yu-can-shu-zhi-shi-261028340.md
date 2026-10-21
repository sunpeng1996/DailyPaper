---
title: 'DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval
  and Parametric Knowledge'
title_zh: DeclineCraft：联合衡量检索与参数知识的RAG拒答能力动态基准
authors:
- Atharva Thakur
- Abulhair Saparov
- Bruno Ribeiro
affiliations:
- Purdue University
arxiv_id: '2610.28340'
url: https://arxiv.org/abs/2610.28340
pdf_url: https://arxiv.org/pdf/2610.28340
published: '2026-10-20'
collected: '2026-10-21'
category: RAG
direction: RAG拒答能力评估基准
tags:
- RAG
- Abstention
- Benchmark
- KnowledgeGap
- LLMEvaluation
one_liner: 构造区分知识缺口承认与前提否定的动态RAG拒答基准，测试27款LLM多配置下的表现
practical_value: '- 电商客服/商品问答RAG系统可复用该评估逻辑，区分「真知识缺口」和「无依据否定商品/活动存在」的错误，降低客诉

  - 迭代RAG架构不要盲目增加检索轮次，实验显示多轮检索会让CAR平均下降10个百分点，准确率几乎无提升，可优先优化单轮检索质量

  - 不要迷信大模型/新模型的知识边界感知能力，模型尺寸、发布时间和拒答准确率无显著相关性，需专门做拒答微调或prompt引导

  - RAG加query改写、rerank时要做拒答效果校验，实验显示这两个模块会降低所有测试模型的CAR，可补充知识存在性校验逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG评估框架无法区分模型是主动承认知识缺口，还是无依据否定问题前提（如断言超出知识库的商品/功能不存在），下游Agent、智能客服场景会将前提判定为事实，引发业务错误，亟需可联合衡量检索知识与参数知识覆盖边界的拒答能力评估基准。
### 方法关键点
- 基于Minecraft wiki时间切分语料构建动态基准：将2025年3月31日前的wiki内容设为RAG唯一可检索库Cpre，之后新增内容设为Cpost，分别生成700道可答、300道不可答问题，剔除所有时间相关提示词避免泄露问题属性
- 定义Correct Abstention Rate（CAR）为核心指标，严格区分正确拒答、无依据前提否定、虚构回答三类响应
- 覆盖无检索、单轮RAG、迭代RAG、多检索pipeline等多场景，测试27款不同规模、不同发布时间的LLM表现，同时做知识泄露审计
### 关键实验结果
- 单轮RAG较无检索，38/40个测试配置的CAR显著提升，平均从17.1%升至56.4%
- 迭代RAG较单轮RAG，30/40个配置CAR显著降至46.4%，但答案准确率仅从68.5%微升至69.3%；给混合检索加query改写与rerank会降低所有12款测试模型的CAR
- 模型参数量、发布时间与CAR无显著相关性；无检索时开启thinking会让8/13款模型CAR平均下降14个百分点，响应多从承认不确定转为前提否定
### 核心结论
RAG系统的知识缺口识别能力不会随模型规模增大自动提升，盲目增加检索轮次、叠加rerank/query改写反而会劣化拒答表现，需单独针对性优化
