---
title: 'DECODE: Diagnosing Interpretability Failures in Automated Interpretation Process'
title_zh: DECODE：诊断LLM自动化解释流程中的可解释性失效问题
authors:
- Dohyun Kim
- Jaeung Lee
- Donghee Hong
- Jaemin Jo
arxiv_id: '2611.17856'
url: https://arxiv.org/abs/2611.17856
pdf_url: https://arxiv.org/pdf/2611.17856
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM可解释性 · 自动化失效诊断
tags:
- LLM Interpretability
- Sparse Autoencoder
- Visual Analytics
- Failure Diagnosis
- Automated Interpretation
one_liner: 推出DECODE可视化分析系统，拆解流程定位LLM自引用式解释的失效来源
practical_value: '- 落地LLM4Rec/Agent的可解释性校验时，可复用独立多解释共识作为无标注场景下的可靠性代理指标，规避自引用校验的固有偏差

  - 大规模特征/规则的人工审核场景，可复用三阶段主动采样协议，优先推荐高风险样本降低人工审核成本

  - 定位LLM应用的解释失效时，可参考三级拆解流程，分层区分是底层特征提取还是上层解释生成环节的问题'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM可解释性工具普遍采用「LLM生成+LLM评估」的自引用自动化流程，缺乏人工监督且无ground truth，既无法验证解释有效性，也难以定位失效来自特征提取环节还是解释生成环节。

### 方法关键点
1. 推出DECODE可视化分析系统，将诊断流程拆解为3个递进阶段，分层隔离从结构缺陷到解释层错位的不同失效来源
2. 借鉴定性分析的编码者共识思路，用独立生成的多解释及评估指标的共识度作为可靠性代理
3. 设计三阶段主动采样协议，智能推荐高优先级样本供人工审核，放大人工检查的覆盖规模

### 关键结果
在16384个稀疏自编码器特征的案例研究中，可高效实现大规模可解释性失效的识别与归因
