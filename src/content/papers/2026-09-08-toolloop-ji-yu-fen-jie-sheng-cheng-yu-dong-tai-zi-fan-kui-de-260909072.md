---
title: 'ToolLoop: Closed-Loop Tool-Use Data Synthesis via Decomposed Generation and
  Dynamic Self-Feedback'
title_zh: ToolLoop：基于分解生成与动态自反馈的工具调用数据闭环合成框架
authors:
- Min Zeng
- Yuzhou Liu
- Zhenyu Cao
- Hanxiu Chen
- Heng Li
- Caiquan Liu
- Yafei Wen
- Xiaoxin Chen
affiliations:
- vivo AI Lab
arxiv_id: '2609.09072'
url: https://arxiv.org/abs/2609.09072
pdf_url: https://arxiv.org/pdf/2609.09072
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent工具调用 · 合成数据生成
tags:
- Tool-Use
- Synthetic Data
- Self-Feedback
- Closed-Loop
- Function Calling
one_liner: 提出三阶段生成-验证-优化闭环框架，仅用11K样本让4B模型工具调用精度达86.4%
practical_value: '- 电商导购Agent、搜索Agent的工具调用训练数据可复用三阶段合成流程：先确定待调用API组合（如查库存、算优惠、查物流），反向生成真实用户查询，正向生成标准工具调用，可替代80%以上的人工标注工作

  - 合成数据质量校验可复用「LLM语义校验+规则格式校验+AST语法校验」的组合方案，搭配分阶段动态反馈优化，比全量事后过滤的有效数据利用率提升60%以上，减少训练噪声

  - 业务侧小模型工具调用能力优化可参考该方案，仅需万级高质量合成样本做LoRA微调，即可接近甚至超过通用大模型的工具调用效果，大幅降低推理部署成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有工具调用数据合成普遍采用「生成后过滤」范式，静态事后校验仅做二元accept/reject决策，丢弃大量可修复样本，导致数据分布失衡、训练信号噪声高；单步生成难以保证用户查询、目标工具、调用参数三者的逻辑一致性，高质量工具调用数据稀缺严重制约Agent落地。
### 方法关键点
- 三阶段分解式生成：1）API语义聚类后采样同场景函数组合作为真值；2）反向推导完全匹配真值需求的自然用户查询；3）正向生成符合API Schema与查询意图的结构化工具调用
- 每阶段集成动态自反馈：组合LLM语义校验、规则格式校验、AST语法解析三类验证能力，输出具体可落地的优化建议，引导模型迭代修正，单阶段最多重试3次
- 范式从「生成后过滤」升级为「生成-验证-优化」闭环，仅丢弃经过3次重试仍无效的样本，大幅提升数据利用率
### 关键结果
- BFCL基准：11K合成样本训练的Qwen3-4B非推理模式精度达86.40%，比使用60K样本的APIGen-4B高3.29个百分点，移除与基准重叠的候选函数后精度仍达86.07%
- ACEBench基准：仅用基线18.3%的训练数据就达到72.1%总体精度，比APIGen-4B高5.1个百分点
- 消融实验：移除自反馈机制后精度下降6.43个百分点，验证了动态反馈的核心价值
### 核心结论
工具调用合成数据的核心价值不是样本量，而是用户查询、目标函数序列、可执行工具调用三者的内部一致性
