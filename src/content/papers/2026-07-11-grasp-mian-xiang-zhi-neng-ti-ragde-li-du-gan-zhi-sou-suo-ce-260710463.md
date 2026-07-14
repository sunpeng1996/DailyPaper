---
title: 'GRASP: GRanularity-Aware Search Policy for Agentic RAG'
title_zh: GRASP：面向智能体RAG的粒度感知搜索策略
authors:
- Varun Gandhi
- Jaewook Lee
- Shantanu Todmal
- Franck Dernoncourt
- Ryan Rossi
- Zichao Wang
- Andrew Lan
affiliations:
- University of Massachusetts Amherst
- Adobe Research
arxiv_id: '2607.10463'
url: https://arxiv.org/abs/2607.10463
pdf_url: https://arxiv.org/pdf/2607.10463
published: '2026-07-11'
collected: '2026-07-14'
category: Agent
direction: Agent 检索决策优化 · 粒度感知
tags:
- Agentic_RAG
- Reinforcement_Learning
- Retrieval_Policy
- Context_Granularity
- GRPO
one_liner: 用RL训练Agent动态协调多检索工具与上下文粒度，提升多跳RAG性能
practical_value: '- 多检索工具动态调度可直接复用：电商导购/商品问答Agent可搭建语义搜索/关键词搜索/详情页读取三个动作，根据用户query和中间推理状态切换，既减少无关内容占用上下文窗口，又提升召回准确率

  - 奖励设计可迁移到Agent调优：做电商多跳任务（比如用户问「适合敏感肌的100元以内洁面」，需跨属性、价格、标签多维度检索）时，可组合答案准确率、证据相关性、检索效率多维度奖励，用GRPO训练小模型即可获得接近大模型的效果

  - 分粒度索引设计可直接落地：商品/内容库可同时做句子级（卖点/参数）和段落级（详情页）双索引，Agent先召回细粒度信息定位关键证据，必要时再调用粗粒度上下文验证，降低上下文冗余'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agentic RAG存在三大核心痛点：一是无法动态适配语义与lexical检索信号的互补需求，固定混合检索策略适配性差；二是固定粗粒度chunk检索容易引入大量无关token挤占上下文窗口，干扰推理；三是多步推理过程中错误检索决策会累积扩散，小模型推理准确率尤其受限。
### 方法关键点
- 动作空间设计：开放4种可调用动作：语义搜索（返回句子级结果）、关键词搜索（返回句子级结果）、读取父段落（扩展上下文）、终止并输出答案，支持细粒度证据定位与按需扩段
- 多维度奖励函数：聚合答案准确率（回答与金标准的token级F1）、证据落地性（读取段落与金标准的F1）、互补检索（两类搜索均命中金标准才得分）、轮次效率（回答正确前提下鼓励少用轮次），总权重向答案准确率倾斜，避免奖励黑客
- 训练策略：采用GRPO做策略优化，仅对Agent生成的推理、工具调用、答案token计算损失，屏蔽检索返回结果的梯度，防止模型无意义记忆检索内容
### 关键结果
在HotpotQA、2WikiMultiHopQA、MuSiQue三个多跳推理数据集上测试，对比单步混合检索、IRCoT、Search-R1等基线：HotpotQA上EM达0.53，较最强基线Search-R1(GRPO)高0.08，检索召回达0.90，较单步混合检索高0.04；2WikiMultiHopQA上EM达0.52，较基线高0.07，跨数据集泛化性明显优于所有基线。
最值得记住的一句话：让Agent学习类人的信息搜寻行为——先用语义搜索做宽泛探索，再用关键词搜索定位实体，必要时读取完整上下文验证，是小模型Agentic RAG提升多步推理性能的核心路径。
