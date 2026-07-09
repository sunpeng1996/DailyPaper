---
title: Interpretable Uncertainty for Adaptive Retrieval and Reasoning in Question
  Answering
title_zh: 面向问答系统自适应检索与推理的可解释不确定性建模
authors:
- Ritajit Dey
- Iadh Ounis
- Graham McDonald
affiliations:
- University of Glasgow
arxiv_id: '2607.07380'
url: https://arxiv.org/abs/2607.07380
pdf_url: https://arxiv.org/pdf/2607.07380
published: '2026-07-08'
collected: '2026-07-09'
category: RAG
direction: RAG自适应触发 · 可解释不确定性估计
tags:
- RAG
- Uncertainty Estimation
- LLM
- Question Answering
- Interpretability
one_liner: 从LLM隐状态提取两类可解释不确定性信号，单轮前向传播即可自适应触发RAG或额外推理
practical_value: '- 可复用不确定性分解思路优化电商导购Agent/搜索问答模块的RAG触发策略，区分「知识不足需检索商品/活动库」和「知识冲突需多步推理选优」两类场景，降低无效检索带来的延迟与噪声

  - 轻量化隐状态探针方案可直接迁移，无需多轮prompt或重复采样，单轮前向传播即可获取决策信号，适配线上高吞吐的服务要求

  - 阈值决策逻辑可解释性强，可对应透出「正在查询最新商品信息」「正在为您对比活动规则」等用户引导文案，提升交互信任度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统普遍采用全量检索策略，对LLM已掌握的知识仍触发检索，既增加 latency 还易引入噪声；现有自适应RAG的决策逻辑多为黑盒模型或依赖多步prompt，可解释性差、计算效率低，且未区分知识不足和知识冲突两类需要不同干预方式的不确定性场景，无法适配需要透明决策的用户-facing系统。
### 方法关键点
- 针对输入query，从LLM单轮前向传播的隐状态训练两个轻量化回归探针，分别估计两类不确定性：知识不足（对应目标事实在预训练语料的出现频次，频次越低则不足程度越高）、知识歧义/冲突（对应目标事实不同版本在预训练语料的分布熵，熵越高则冲突程度越高）
- 采用简单阈值决策路由：知识不足超阈值时触发RAG补全外部信息，歧义冲突超阈值时触发CoT/自一致性等额外推理逻辑，两类信号均低于阈值时直接输出答案
### 关键实验
在NQ事实问答数据集上测试，基座采用Llama-2-7b-chat，对比LLM-only基线、always-on RAG基线：相对LLM-only最高提升5.9%准确率，相对always-on RAG最高提升3.3%准确率，结果均通过McNemar统计显著性检验。
### 核心结论
可解释的不确定性分解是自适应RAG兼顾效果、效率与透明度的核心路径，无需牺牲性能即可实现可审计、可解释的系统决策。
