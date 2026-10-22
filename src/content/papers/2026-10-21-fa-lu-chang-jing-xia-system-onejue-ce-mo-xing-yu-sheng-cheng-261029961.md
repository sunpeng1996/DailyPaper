---
title: Commit or Abstain? System One Decision Models, LLMs, and Missing Legal Authority
title_zh: 法律场景下System One决策模型与生成式LLM的弃权行为对比研究
authors:
- M. Mikail Demir
affiliations:
- University at Albany, SUNY
arxiv_id: '2610.29961'
url: https://arxiv.org/abs/2610.29961
pdf_url: https://arxiv.org/pdf/2610.29961
published: '2026-10-21'
collected: '2026-10-22'
category: Eval
direction: 大模型评估 · 决策模型校验与蒸馏
tags:
- Decision Model
- Abstention
- Calibration
- Knowledge Distillation
- Legal AI
one_liner: 对比System One决策模型与生成式LLM的法律引证错误率，给出低成本校验与本地蒸馏方案
practical_value: '- 高风险业务场景（如电商合规校验、广告素材审核、Agent工具调用结果校验）可引入低成本System One决策模型作为前置校验门，仅当决策模型与生成式LLM结果一致时放行，可将错误率减半，额外成本仅1%左右

  - 无标注或标注成本高的场景，可通过蒸馏黑盒决策模型的输出概率，低成本得到可本地部署的小模型，校准效果优于直接用少量标注训练

  - 业务评估不要只看准确率，要区分不同错误的成本（如误判合规风险vs漏判违规内容），通过调整决策模型的置信阈值适配不同风险等级的业务场景

  - 多模型级联架构中，用小参数决策模型做路由/校验，大模型处理难例，可在效果下降极小的情况下大幅降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有生成式LLM在法律引证场景 hallucination 严重，法院已出现大量因AI生成虚假法律依据被处罚的案例，常规评估只看准确率，不对「无正确选项时强行选择」和「有正确选项时弃权」两种错误做成本区分，而前者的业务代价远高于后者，亟需低成本、高可靠性的校验方案。

### 方法关键点
- 扩展CaseHOLD数据集，将1670条样本的正确法律持有替换为相似错误样本，新增「无正确选项」的弃权选项，总测试样本5314条
- 对比4款System One决策模型（输出各选项置信概率）和6款主流生成式LLM的表现，核心指标为无正确选项时的错误选择率、有正确选项时的错误弃权率、推理成本
- 测试三种模型组合策略：否决制（决策模型置信度不足时拒答）、一致门限（仅两类模型结果一致时放行）、决策模型优先（高置信直接输出，低置信调用大模型）
- 验证无标注蒸馏方案：用决策模型的输出概率作为监督，LoRA微调Qwen3-8B得到本地部署模型

### 关键实验
- 无正确选项时，生成式LLM错误选择率为38%~86%，最优System One模型仅30%；标准CaseHOLD任务上决策模型准确率与最优生成式LLM相当（88.1% vs 88.2%），成本仅为1/55
- 采用一致门限策略，将pplx-decider与Gemini 3.8 Flash组合，可将错误引证率减半，仅增加1%左右的成本
- 无标注蒸馏得到的Qwen3-8B表现与教师Jev几乎一致，准确率63.8% vs 63.9%，校准误差甚至优于教师（0.025 vs 0.056）

### 核心结论
高风险场景下模型评估不能只看准确率，要根据不同错误的业务成本设计考核指标，可通过校准的小决策模型大幅降低错误率与推理成本。
