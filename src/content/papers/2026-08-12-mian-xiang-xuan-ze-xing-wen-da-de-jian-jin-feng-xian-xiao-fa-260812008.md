---
title: Asymptotic Risk Calibration for Selective Question Answering
title_zh: 面向选择性问答的渐近风险校准方法
authors:
- Shufan Lin
- Sijin Dong
affiliations:
- Zhejiang University
- Ibaraki University
arxiv_id: '2608.12008'
url: https://arxiv.org/abs/2608.12008
pdf_url: https://arxiv.org/pdf/2608.12008
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: LLM不确定性校准 · 选择性问答
tags:
- Uncertainty Quantification
- Conformal Prediction
- Selective QA
- Risk Calibration
- Post-hoc Calibration
one_liner: 提出模型无关的后校准框架A-CRC-QA，在可控错误率下提升选择性问答的答案保留率
practical_value: '- 电商客服Agent、商品问答场景可直接复用A-CRC-QA框架，基于现有不确定性分数做后校准，无需重训模型即可控制回答错误率，平衡准确率与拒答率

  - 推荐/广告场景的LLM生成文案、个性化query推荐质检环节，可借鉴线性期望约束+经验风险单调化trick，在预设错误容忍度下最大化有效内容通过率

  - Agent系统的输出路由逻辑可复用该阈值校准方法，避免固定阈值在数据分布变化时失效，用小批量校准集即可动态调整拒答阈值'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM生成回答易出现幻觉，现有启发式不确定性分数无法精准区分正确与错误输出，直接使用固定阈值无法对接受答案的错误率提供统计保障，在医疗、电商客服等高风险场景会带来不可控的业务风险。
### 方法关键点
- 将选择条件下的错误率控制重写为线性期望约束，引入实例级线性损失简化校准目标，规避条件概率直接校准的复杂度
- 针对实例损失随阈值非单调的问题，采用经验风险上包络单调化处理，消除校准数据随机波动导致的孤立可行阈值，提升稳定性
- 加入渐近消失的有限样本校正项，选择满足约束的最小可靠性阈值最大化答案接受率，整个流程为后处理模式，无需训练、模型无关，可适配任意标量不确定性估计器
### 关键实验
在CoQA（开放域对话问答）、MedMCQA（医疗多选问答）数据集上测试，覆盖LLaMA-3.1-8B-Instruct、Qwen2.5-7B-Instruct两类开源模型，对比固定阈值、UCB类校准、LEC直接法等基线：目标错误率0.15时，A-CRC-QA在CoQA上平均错误率0.143、接受率46.2%，在MedMCQA上平均错误率0.138、接受率58.7%；相比Hoeffding上界基线接受率提升6.1~7.4个百分点，相比LEC直接法违规率降低11~12个百分点。
### 核心结论
未校准的不确定性阈值即使具备不错的错误区分能力，也无法可靠控制接受答案的错误率，单调化经验风险的后校准是平衡答案保留率和稳定性的高性价比方案。
