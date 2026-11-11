---
title: Can the Confidence and Decisions of System 1 Models Be Trusted? An Explainability
  and Perturbation Audit of Jev-Style Decision Models
title_zh: System1模型置信度与决策可信吗？Jev式决策模型的可解释性与扰动审计
authors:
- Julien Delaunay
affiliations:
- Independent Researcher
arxiv_id: '2611.12521'
url: https://arxiv.org/abs/2611.12521
pdf_url: https://arxiv.org/pdf/2611.12521
published: '2026-11-09'
collected: '2026-11-11'
category: Eval
direction: 大模型可信性审计 · System1决策模型
tags:
- System1 Model
- Model Calibration
- XAI
- Perturbation Audit
- Prompt Injection Defense
one_liner: 提出公开确定性审计基准，评测Jev式System1决策模型的校准、抗干扰与可解释性，给出5项实证结论
practical_value: '- 低延迟决策场景（如实时推荐路由、广告流量分级、prompt攻击拦截）可选用4B+参数System1模型，校准度远高于logprob/JSON生成基线，延迟仅48-60ms

  - System1模型置信度可直接用闭式离散度变换计算，无需额外拟合准确率映射，可直接用于低置信case转人工/兜底策略

  - 单步决策模型可解释性归因可采用logit空间S1-SHAP方法，避免softmax饱和导致的归因偏差，提升特征贡献判断准确率

  - 4B以下参数System1模型不建议多query打包调用，0.8B模型多query时决策翻转率高达11.7%-22.4%'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
Jev风格System1决策模型用单前向传播替代自回归生成输出结构化概率分布，已落地低延迟路由、自动分诊等场景，但校准性、可解释性未被系统性验证，缺乏统一审计标准。
### 方法关键点
提出公开确定性审计基准，从标签保留扰动下的校准度、多query交叉干扰、事后归因忠实度三个维度，评测5个0.8B-27B参数量开源System1模型，对比单token logprob打分、结构化JSON/CoT解码两类System2基线，覆盖NLI、对抗句法捷径、临床分诊、prompt注入防御、逻辑门触发5类任务。
### 关键结果数字
①4B+参数System1模型句法偏移下加权ECE为0.030-0.087，远优于logprob基线的0.144和JSON基线的0.378；②prompt注入防御任务AUROC达0.988-0.998，最高95.2%召回率零误报；③S1-SHAP对或门的恢复率达89.3%-100%，较概率空间方法提升最多32.2个百分点；④0.8B参数System1模型多query打包时决策翻转率达11.7%-22.4%，4B版本仅为0.1%-0.2%
