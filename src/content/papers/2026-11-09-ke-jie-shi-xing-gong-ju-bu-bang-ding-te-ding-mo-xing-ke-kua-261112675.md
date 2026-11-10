---
title: Interpretability Is Not Model-Specific
title_zh: 可解释性工具不绑定特定模型 可跨架构参数规模迁移
authors:
- Marcus Armstrong
- Navid Ayoobi
- Pradham Mummaleti
- Alexander Chulzhanov
- Arjun Mukherjee
affiliations:
- Department of Computer Science, University of Houston
arxiv_id: '2611.12675'
url: https://arxiv.org/abs/2611.12675
pdf_url: https://arxiv.org/pdf/2611.12675
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: LLM可解释性 · 跨模型工具迁移
tags:
- Interpretability
- Cross-Model Transfer
- Residual Stream
- LLM Probe
- Steering Vector
one_liner: 通过无标注prompt拟合残差流映射，实现LLM可解释性工具跨架构、参数规模高效迁移
practical_value: '- 跨LLM迭代对齐时，可复用已有拒绝、正确性探测等可解释工具，仅需少量业务场景无标注prompt拟合残差流映射，无需重新标注数据，大幅降低大模型换版成本

  - 电商/推荐场景用到的LLM语义探测、内容合规steering等能力，换用新基座时配合业务无标注数据即可达到90%+的原有效果，无需重新训练探测头

  - 可复用本文提出的无标注覆盖率评分，提前预判跨模型工具迁移的效果，避免无效的工具重构尝试'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM可解释性工具（拒绝方向、真实性探测、steering向量等）均为单模型定制，依赖标注数据训练，切换模型时需从零重建，成本极高。
### 方法关键点
通过仅输入无标注prompt拟合不同模型残差流的线性映射，将源模型训练完成的可解释性工具直接迁移到目标模型，覆盖拒绝方向、正确性方向、情感探测三类工具，同时设计无标注覆盖率评分预判迁移效果。
### 关键结果
在110组跨模型对（覆盖5个模型家族、1B-72B参数、基座/指令微调模型）测试：仅用普通问题拟合映射时可恢复54%的拒绝steering效果、16%-77%的正确性增益；补充工具适用场景的无标注prompt后，两项指标分别提升至102%、88%-98%，对照组方向恢复率最高仅1%，迁移后工具效果优于目标模型无标注表征训练的任意工具。
