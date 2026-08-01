---
title: 'When Derived Measurements Mislead: Quantifying and Mitigating LLM Over-Trust
  with Privileged-Modality Reliability Evidence'
title_zh: 衍生测量误导问题：用特权模态证据量化与缓解LLM过度信任
authors:
- Zongheng Guo
- Tao Chen
- Tianli Li
- Mingzhe Cui
- Yang Jiao
- Lei Xie
- Yi Pan
- Xiao Hu
- Manuela Ferrario
affiliations:
- Politecnico di Milano
- Zhejiang University
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Emory University
- China-Japan Friendship Hospital
arxiv_id: '2607.28421'
url: https://arxiv.org/abs/2607.28421
pdf_url: https://arxiv.org/pdf/2607.28421
published: '2026-07-30'
collected: '2026-08-01'
category: LLM
direction: LLM 可靠性评估与过度信任缓解
tags:
- LLM Reliability
- Over-Trust Mitigation
- Privileged Modality
- Evaluation Framework
- Knowledge Distillation
one_liner: 提出衍生特征过度信任评估框架与特权模态蒸馏方案，量化并降低LLM对衍生测量的过度信任
practical_value: '- 推荐/Agent系统用到CTR预估值、用户标签等衍生特征时，可参考DFOT评估框架量化模型对衍生特征的过度信任程度，避免错误决策

  - 训练阶段可复用特权模态蒸馏思路：用离线高置信ground truth（如实付数据、人工标注）做监督，为线上仅能使用低置信度特征的模型注入可靠性感知能力，降低错误率

  - 可适配文中5类评估指标，搭建业务场景下的过度信任风险量化体系，平衡模型效果与可靠性'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前LLM流水线普遍将衍生测量值直接作为事实输入，但这类特征的有效性随样本波动，LLM易过度信任错误衍生值、超范围使用，缺乏统一的评估与缓解方案。
### 方法关键点
1. 定义衍生特征过度信任（DFOT）问题，设计5类量化指标：冲突过度信任率（COTR）、上下文诱导错误率（CIR）、正确修复率（CRR）、证据特异性修复边际（ESRM）、效用损害率（UHR），覆盖全链路风险。
2. 提出特权模态蒸馏方案，训练阶段用高置信度特权模态（如ECG）做监督，推理阶段仅用低置信度普通模态（如PPG）即可注入可靠性感知能力，无需修改下游LLM架构。
### 关键结果
在5万条PPG-ECG配对数据集测试，特权蒸馏基线将4项修复与特异性指标提升1.82-6.69个百分点，仅带来0.67个百分点的不必要验证率上升（95%CI：-0.4~+1.7，无统计显著性）。
