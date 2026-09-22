---
title: 'Attributable Post-Rationalization in RAG Citations: A Controlled Reproduction
  and an RLVR Comparison'
title_zh: RAG引用的可归因事后合理化问题：可控复现与RLVR对比
authors:
- Mehedi Khan
- Md. Shariful Islam Bhuyan
affiliations:
- Bangladesh University of Engineering and Technology
arxiv_id: '2609.23053'
url: https://arxiv.org/abs/2609.23053
pdf_url: https://arxiv.org/pdf/2609.23053
published: '2026-09-19'
collected: '2026-09-22'
category: RAG
direction: RAG评估 · 引用忠实度优化
tags:
- RAG
- Citation Faithfulness
- RLVR
- Post-Rationalization
- Evaluation
- LLM Agent
one_liner: 提出带无植入对照组的RAG引用测量方法，验证RLVR训练无法改善引用事后合理化问题
practical_value: '- 电商商品咨询、售后答疑等要求信息溯源的RAG场景，不能仅奖励答案正确率，必须单独设计引用忠实度的评测与奖励项，避免引用无关商品参数的错误

  - 做RAG引用忠实度评估时，必须新增无植入对照组，排除模型原生引用偏好的干扰，避免高估事后合理化的比例

  - 用RLVR训练检索类Agent时，可直接将本文的植入探针作为引用忠实度惩罚项加入PPO/GRPO奖励函数，无需额外裁判模型，实现成本极低

  - 7B级模型即可跑出稳定的引用行为结果，小团队用免费T4 GPU就能完成RAG引用质量的全量评估，无需大算力支持'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统普遍存在「答案正确但引用未实际使用的文档」的事后合理化问题，用户仅核查引用内容表面匹配无法发现问题。当前主流RLVR训练的检索Agent仅以答案正确性作为奖励，完全未覆盖引用忠实度，其对引用行为的影响尚未得到验证，且原有引用忠实度测量方法缺乏对照组，结果存在严重偏差。
### 方法关键点
1. 改进植入探针测量方法，新增无植入对照组，通过可归因率（植入答案片段后的引用率减去对照组原生引用率）精准度量事后合理化程度
2. 控制单一变量：所有对比模型均基于Qwen2.5-7B-Instruct底座，包括原生指令微调模型、3个开源RLVR检索Agent（Search-R1、ReSearch、R-Search）
3. 固定检索上下文：所有模型输入相同的BM25召回的5篇文档，排除检索策略差异对引用行为的干扰
4. 以REL-UNCITED探针为核心指标：将答案片段植入未被原回答引用的召回文档，观测模型是否切换引用到该文档
### 关键结果
在4个公开问答数据集上测试：原生底座模型在维基类数据集上的事后合理化率约1/7（9.1%~14.8%），3个RLVR训练的Agent的引用忠实度与底座无显著差异，其中R-Search甚至在Web数据集上显著变差3个百分点，全部实验可在免费T4 GPU上完成。
**最值得记住的一句话**：优化目标只会给到你明确奖励的能力，仅奖励答案正确的训练完全不会带来引用忠实度的提升，后者必须单独设计评测与奖励规则。
