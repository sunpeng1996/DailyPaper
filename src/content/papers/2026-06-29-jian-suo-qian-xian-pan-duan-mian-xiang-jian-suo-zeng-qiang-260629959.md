---
title: 'Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented
  Generation'
title_zh: 检索前先判断：面向检索增强生成的校准检索预算分配
authors:
- Zhe Dong
- Fang Qin
- Manish Shah
- Yicheng Wang
affiliations:
- University of Maine at Presque Isle
- Stanford University
- Independent Researcher
arxiv_id: '2606.29959'
url: https://arxiv.org/abs/2606.29959
pdf_url: https://arxiv.org/pdf/2606.29959
published: '2026-06-29'
collected: '2026-06-30'
category: RAG
direction: 自适应RAG · 检索成本优化
tags:
- RAG
- Adaptive Retrieval
- Calibration
- LLM
- Cost Optimization
one_liner: 为RAG提供校准概率接口，实现分级检索预算分配，优化准确率与成本的trade-off
practical_value: '- 做Agent/RAG落地时，可借鉴分级预算分配思路：不固定每查询检索k篇文档，根据LLM置信度分为不检索/少量检索/全检索三级，既能降低token和检索成本，还能减少冗余检索引入的干扰错误

  - 自适应检索不是一定能降延迟，需先算盈亏平衡点：只有跳过检索的比例足够高，才能抵消前置闭卷探测的额外生成成本，大模型更容易满足条件，小模型反而可能升高延迟，该结论可直接用于架构选型

  - 无需微调就能实现可靠的自适应决策：仅需对LLM原生输出的不确定性信号（序列对数概率、前缀熵）做简单logistic校准，就能得到可用的回答正确概率，业务部署成本极低'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG普遍对所有查询固定检索固定数量的文档，存在两个核心问题：一是多数常用查询LLM的参数化记忆已经能正确回答，额外检索浪费了延迟、带宽和上下文token；二是不相关或冗余检索会引入干扰，反而把原本正确的闭卷答案改错。过往自适应RAG仅做「要不要检索」的二元决策，使用未校准的原始不确定性分数，难以跨模型跨任务调阈值，也没有对检索预算做精细分配。

### 方法关键点
- 将自适应RAG建模为校准后的检索预算分配问题，每个查询可选择四种动作：闭卷回答(k=0)、紧凑检索(k=1)、全检索(k=5)、 abstain拒绝回答
- 对LLM原生输出的不确定性信号（长度归一化序列对数概率、或TARG的前缀熵/边际分数），用简单logistic回归校准得到「回答正确的概率」，不需要微调LLM或检索器
- 用双阈值实现分级决策，明确区分检索调用次数、全检索占比、总passage预算三个不同成本维度，推导了自适应检索的延迟盈亏平衡公式

### 关键结果
在TriviaQA、Natural Questions、MS MARCO三个主流QA数据集实验，对比了TARG、Self-RAG、Adaptive-RAG等基线：校准后预测置信度的ECE大幅下降，TriviaQA上序列对数概率ECE从0.275降至0.062，NQ从0.643降至0.009；分级分配比二元门显著优化了passage预算-准确率 frontier；实测显示匹配准确率下，Qwen3-8B自适应门延迟升高27%，Qwen3-32B延迟降低8%，完全符合盈亏平衡结论。

最值得记住的结论：校准后的概率是跨场景可复用的决策接口，比仅能排序的原始分数更适合业务部署，自适应检索必须算清不同成本维度的盈亏平衡。
