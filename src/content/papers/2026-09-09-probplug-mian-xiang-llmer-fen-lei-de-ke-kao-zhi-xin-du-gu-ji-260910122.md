---
title: 'ProbPlug: A Plugin Uncertainty Network for Reliable Confidence in LLM Binary
  Classification'
title_zh: ProbPlug：面向LLM二分类的可靠置信度估计插件网络
authors:
- Jianzong Wang
- Chuhang Liu
- Botao Zhao
- Zuheng Kang
- Xulong Zhang
- Xiaoyang Qu
- Junqing Peng
- Zhiewei Ye
- Yayun He
affiliations:
- Ping An Technology (Shenzhen) Co., Ltd.
- Tsinghua Shenzhen International Graduate School
- Hubei University of Technology
arxiv_id: '2609.10122'
url: https://arxiv.org/abs/2609.10122
pdf_url: https://arxiv.org/pdf/2609.10122
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: LLM 置信度校准与分类优化
tags:
- Confidence Estimation
- LLM Classification
- Lightweight Plugin
- Model Calibration
- Multimodal LLM
one_liner: 无需修改底座LLM，通过抽取内部token特征加轻量注意力模块实现可靠二分类置信度校准
practical_value: '- 电商/广告场景下用LLM做内容审核、用户意向二分类（如是否高转化意向用户）等任务时，可直接复用ProbPlug插件架构，无需微调底座LLM即可获得可靠置信度，灵活调整精度召回
  trade-off 适配业务需求

  - 插件推理开销极低，仅增加极小型自注意力模块计算，对高吞吐的线上推荐、广告分类场景友好，无需额外GPU资源扩容即可落地

  - 跨任务泛化性强，同一预训练的ProbPlug插件可适配多个二分类业务场景，仅需少量样本微调即可适配新任务，降低多业务线的重复开发成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在文本、多模态分类任务上表现突出，但原生输出缺乏可靠置信度，无法支撑精度-召回 trade-off 调整，极大限制了其在风控、审核等高风险业务场景的落地，现有LLM置信度研究对分类场景的校准优化覆盖不足。
### 方法关键点
ProbPlug为完全无侵入的轻量插件：底座LLM全程冻结，仅抽取推理过程中输出层前的token隐藏特征，通过新增的小型自注意力模块聚合特征直接输出分类结果置信度，无需修改原模型推理管线即可快速集成。
### 关键结果
跨12个文本、多模态二分类任务测试，置信度估计可靠性较主流基线平均提升14.7%，分类精度最高提升7.2%，推理额外计算开销<1%，预训练插件支持跨任务迁移，适配新任务仅需<100条样本微调。
