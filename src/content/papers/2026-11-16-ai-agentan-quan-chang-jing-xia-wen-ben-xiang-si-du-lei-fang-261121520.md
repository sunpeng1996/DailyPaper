---
title: 'Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails
  for AI Agent Safety'
title_zh: AI Agent安全场景下文本相似度类防护护栏的效果边界研究
authors:
- Charles Xiao
arxiv_id: '2611.21520'
url: https://arxiv.org/abs/2611.21520
pdf_url: https://arxiv.org/pdf/2611.21520
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent安全 · 间接Prompt注入防护
tags:
- Agent Safety
- Prompt Injection
- Guardrail
- Text Similarity
- Behavioral Evaluation
one_liner: 实测文本相似度类Agent安全护栏高漏检高误报，证明纯文本观测无法解决授权判定歧义
practical_value: '- 搭建多Agent链路的安全护栏不能仅依赖文本相似度特征，需追加下游行为校验、权限上下文校验：例如电商多Agent服务链路中，不能因文本重叠拦截合法的工单模板复用，也不能漏过改写表述的恶意指令

  - 评估Guardrail的实际效果时，禁止用ROC插值计算阈值，必须直接基于实际决策阈值计算混淆矩阵：例如推荐系统内容审核护栏的阈值校准，必须用真实业务样本的实际判定结果做验证，避免上线后FPR/TPR与预期偏差过大

  - 多Agent交互场景的安全评估要做端到端行为观测，不能仅依赖单步文本特征：例如电商导购、支付、售后Agent的全链路安全测试，要跟踪恶意指令是否在多Agent间持续生效，而非仅校验单步输出的特征匹配度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多Agent交互场景下，间接Prompt注入的恶意指令可在Agent间传播，即使表述被改写仍能触发下游执行；而合法的模板复用、内容引用又会产生高文本重叠，现有基于文本相似度的安全护栏极易混淆两类场景，过往评估未结合下游行为与授权上下文，效果可信度不足。

### 方法关键点
- 测试对象为公开的DonkeyRail相似度护栏，是融合BLEU、ROUGE-L、METEOR特征的分类器，部署在三Agent邮件转发链路中
- 定义独立于相似度得分的功能性判定规则：输出能让后续两个Agent均执行注入指令即判定为功能生效，与文本改动程度无关
- 合法对照组覆盖4类真实高重叠场景：普通回复、原文引用、内容转述、模板复用，均有明确授权
- 同步分析现有护栏阈值计算的ROC插值误差，以及纯文本观测的授权不可识别性问题

### 关键结果
- 默认阈值下，护栏漏检19个功能生效的恶意输出中的8个（漏检率42%），同时误拦192个合法回复中的70个（误报率36%），所有完成的引用、模板复用回复全部触发误报
- 针对模板集校准阈值降低误报后，仅能检测到1个恶意输出，对新模板仍存在15个误报
- 理论证明纯观测的文本分类器无法区分相同文本对应不同授权的场景，高文本相似度AUC完全不保证实际行为检测的AUC

**最值得记住的一句话**：Agent安全防护不能仅依赖文本特征，必须结合下游行为观测和显式权限策略上下文，才能平衡安全要求与业务可用性。
