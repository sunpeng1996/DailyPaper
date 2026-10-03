---
title: Counterfactual Auditing of Bias in Open-Source Large Language Models for Clinical
  Triage
title_zh: 开源大语言模型临床分诊场景的偏差反事实审计
authors:
- Manar Aljohani
- Brandon Ho
- Kenneth McKinley
- Dennis Ren
- Xuan Wang
affiliations:
- Virginia Tech
- University of Washington
- Seattle Children’s Hospital
- Children’s National Hospital
arxiv_id: '2610.01963'
url: https://arxiv.org/abs/2610.01963
pdf_url: https://arxiv.org/pdf/2610.01963
published: '2026-10-01'
collected: '2026-10-03'
category: Eval
direction: LLM 公平性评估与偏差优化
tags:
- LLM Bias
- Counterfactual Audit
- QLoRA
- Fairness Evaluation
- Domain Fine-tuning
one_liner: 对比10款开源LLM的临床分诊反事实偏差，证实QLoRA微调可降偏差，反事实审计可作为预部署公平性校验方案
practical_value: '- 可复用反事实偏差审计方法，在推荐/搜索场景构造仅修改用户属性、其余特征固定的配对样本，校验模型对敏感属性的鲁棒性

  - 业务场景微调LLM时可优先尝试QLoRA轻量微调方案，不仅适配隐私场景，还可显著降低模型对非核心特征的敏感性

  - 模型效果评估不能只看整体指标，需做分层分析挖掘聚合指标隐藏的方向性偏差和共性失败case，规避业务风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：高风险临床分诊场景中，LLM易受人口统计学、社会经济等非临床特征干扰产生决策偏差，不同开源LLM的反事实偏差分布规律尚未明确，缺乏可解释的预部署公平性校验方案。
**方法**：基于真实临床病例构造配对反事实样本，仅修改单维度非临床特征、固定核心临床症状，对10款不同大小、不同领域预训练的开源LLM开展分诊预测偏差审计，覆盖任意偏移率、漏分诊/过分诊率、平均绝对偏移等指标。
**结果**：反事实敏感度与模型大小、医疗领域预训练无显著负相关；QLoRA微调的Qwen2.5-7B任意偏移率仅5.27%、平均绝对偏移0.0534，较底座模型分别下降67%、69%，表现最优；聚合指标易隐藏方向性偏差与共性失败模式，反事实审计是轻量可解释的公平性校验框架
