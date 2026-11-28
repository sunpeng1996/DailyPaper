---
title: 'EPPC-CARE: Staged Hierarchical Annotation of Communication Behaviors in Secure
  Patient-Provider Messages'
title_zh: EPPC-CARE：医患安全消息通信行为的分阶段分层标注方法
authors:
- Samah Fodeh
- Sreeraj Ramachandran
- Ganesh Puthiaraju
- Sarah Schellhorn
affiliations:
- Yale School of Medicine Department of Emergency Medicine
- Yale School of Medicine Medical Oncology
arxiv_id: '2611.34539'
url: https://arxiv.org/abs/2611.34539
pdf_url: https://arxiv.org/pdf/2611.34539
published: '2026-11-25'
collected: '2026-11-28'
category: Other
direction: LLM驱动的分层文本标注框架
tags:
- LLM
- Hierarchical Annotation
- Text Span Extraction
- Human-in-the-loop
- Text Classification
one_liner: 提出分阶段分层标注框架EPPC-CARE，可自动提取医患通信行为三元组且性能优于基线
practical_value: '- 分层标注思路可迁移到电商客服会话、用户评论的意图打标：先提取相关文本span，再依次打大类、细类标签，比端到端打标准确率更高

  - 分阶段识别三元组的架构可复用在需要可解释性的文本分类场景，标签结果关联原始span可大幅降低人在回路标注的人工校验成本

  - 开源LLM+分层标注的方案可替代部分人工标注工作，适合大规模非标文本（如用户反馈、商品评价）的批量标注降本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
医患门户消息中通信行为的人工提取标注成本极高，现有方法无法同时输出分类结果和支撑源文本，可解释性差，难以支撑大规模分析和人在回路校验。
### 方法关键点
1. 定义标注三元组结构：通信相关文本span、上层通信类别Code、细分子类Sub-code
2. 采用分阶段顺序识别架构：先抽取关联span，再逐层标注大类、细类标签
3. 跨6个开源LLM验证效果，对比监督微调、EPPC-OASIS等基线方案
### 关键结果
比基线EPPC-OASIS平均Triplet F1提升2.9个百分点，最优得分达64.4%；在100条样本的人工评估集上，与专家标注效果相当，部分指标更优
