---
title: 'Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for
  Selective Retrieval-Augmented Machine Translation'
title_zh: 仅在必要时检索有用内容：面向检索增强翻译的智能体强化学习框架
authors:
- Shijun Li
- Yang Liu
- Najmeh Sadoughi
- Dongmei Wang
- Xinjie Li
- Zhu Liu
- Rohith Mysore Vijaya Kumar
- Yuzong Liu
affiliations:
- The University of Texas at Austin
- Amazon
arxiv_id: '2610.19528'
url: https://arxiv.org/abs/2610.19528
pdf_url: https://arxiv.org/pdf/2610.19528
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 自适应检索优化 · RAG下游对齐
tags:
- Reinforcement Learning
- RAG
- Selective Retrieval
- GRPO
- Plackett-Luce
- Machine Translation
one_liner: 基于强化学习的选择性RAG框架，自适应决策检索时机与内容，对齐下游翻译质量优于固定检索策略
practical_value: '- 业务RAG系统可复用三阶段训练curriculum避免策略坍缩：先筛选高质量检索轨迹做SFT初始化，再用带临时检索惩罚的RL训练，最后移除惩罚优化最终目标，适配不同场景的检索率需求

  - 当语义相似度检索和下游业务目标不一致时，可复用对比式检索训练思路：固定生成模型，批量测试不同检索结果对下游效果的影响，将最优结果作为正样本微调检索器，比端到端联合训练梯度信号更稳定，credit
  assignment方差更低

  - 针对黑盒大模型的RAG优化可复用策略解耦思路：训练小参数Agent独立决策检索时机、生成检索query、组装上下文，用黑盒大模型的最终输出效果作为RL奖励，无需修改大模型参数即可提升整体效果，适合电商客服/商品翻译等依赖商用大模型的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索增强机器翻译系统对所有输入统一执行固定的语义相似度检索，忽略LLM自身参数知识已能覆盖大部分翻译需求的现状，无效检索不仅浪费算力，还可能引入噪声降低翻译质量，同时相似度检索的最优结果往往和最终翻译质量目标不匹配，亟需更灵活的自适应检索决策机制。
### 方法关键点
- SRAT框架将翻译过程建模为包含三类动作的序列决策问题：<think>推理判断现有知识是否充足，<tool_call>生成query调用检索并拼接结果到上下文，<answer>输出最终翻译，支持零检索直接翻译的合法路径
- 采用GRPO强化学习做端到端训练，奖励函数结合翻译质量（COMET+LLM评测）、格式惩罚、生成长度惩罚，通过同输入多轨迹的相对优势指导策略学习，无需人工标注哪些样本需要检索
- 设计三阶段训练curriculum避免策略坍缩：先筛选Top40%高质量检索轨迹做SFT初始化，再用临时检索惩罚训练避免策略收敛到永远检索，最后移除惩罚优化最终目标
- 两种检索器对齐方案：端到端联合训练用Plackett-Luce随机排序策略让检索器可导，承接轨迹奖励梯度；对比式训练固定翻译模型，用不同检索结果对应的翻译质量做对比监督，梯度信号更稳定
### 关键结果
在习语翻译、知识密集型翻译、文档级翻译三个场景下，SRAT相对固定永远不检索/永远检索的基线，MQM分别提升17.4%-20.6%、8%-12.8%、5.4%；当语义相似度检索准确率不足60%时，对比式检索对齐可进一步将MQM提升6.8%-7.4%；针对黑盒Claude模型，训练的独立检索策略可在知识密集型翻译场景下将MQM再提升12.4%-16.8%。

不要把检索当做固定的前置预处理步骤，而是将其作为可学习的决策动作，对齐下游最终业务目标才能最大化RAG的收益
