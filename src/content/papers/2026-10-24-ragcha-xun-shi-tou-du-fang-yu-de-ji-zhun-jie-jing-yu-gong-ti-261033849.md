---
title: 'Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse
  in Query-Time RAG Poisoning Defenses'
title_zh: RAG查询时投毒防御的基准捷径与工作点崩溃问题研究
authors:
- Pushkal Kumar
- Arvin Sahaym
affiliations:
- North Creek High School
- Washington State University
arxiv_id: '2610.33849'
url: https://arxiv.org/abs/2610.33849
pdf_url: https://arxiv.org/pdf/2610.33849
published: '2026-10-24'
collected: '2026-10-27'
category: RAG
direction: RAG安全 · 投毒防御评测有效性
tags:
- RAG
- Data Poisoning
- Benchmark
- Security
- Evaluation
one_liner: 提出无需防御参与的投毒数据集两指标轮廓，揭示现有RAG防御评测的shortcut和工作点失效问题
practical_value: '- 业务中上线RAG防御（如电商商品问答、客服RAG）时，不能仅用AUROC评估效果，必须同时披露部署阈值下的FPR和FNR，避免上线后漏检率过高

  - 自研或评测RAG投毒防御前，先校验投毒样本的两个shortcut：是否带目标query原文前缀、长度是否与正常样本分布一致，避免测出虚高的准确率

  - 现有开源RAG投毒防御方案（RAGuard、TrustRAG等）在绕过构造捷径后漏检率最高可达0.986，业务使用时必须做适配改造，不能直接照搬

  - 做电商/搜索的恶意内容过滤时，不要依赖样本长度、query是否出现在文本中这类易被绕过的特征，需结合内容语义、来源可信度做多维校验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG查询时投毒防御是对抗检索知识库污染的主流方案，公开评测中普遍报告接近完美的检测效果，但实际部署时性能往往暴跌，核心原因是评测用的投毒数据集存在构造捷径，防御模型拟合捷径特征而非真实内容差异，业界缺乏统一的投毒数据集有效性校验方法，也没有规范的防御评测指标要求。

### 方法关键点
- 两个无需防御参与、无需标注即可计算的投毒数据集轮廓指标：①containment：投毒文本逐字包含目标query的比例；②length overlap：投毒文本长度落在正常文本长度5%~95%分位区间的比例
- 设计5阶payload保留的攻击编辑梯子：从原始模板、移除query前缀、对齐长度、双特征移除到风格模仿，逐层消除构造捷径，验证防御真实鲁棒性
- 评测体系同时采集三类指标：部署工作点下的FPR/FNR、固定5%FPR下的FNR、AUROC，明确区分排序性能和实际部署的决策性能

### 关键实验结果
覆盖通用（NQ）、医疗、金融、法律4个语料，4类主流RAG投毒攻击，10种已发表的投毒防御方案：①移除PoisonedRAG默认添加的query前缀后，RAGuard的AUROC从0.953降至0.758，部署漏检率从0.191升至0.763；②将医疗领域投毒样本长度对齐到正常分布后，TrustRAG的漏检率从0.000升至0.827，自研学习式打分器漏检率升至0.986但AUROC仍维持0.953；③调研21篇已发表的防御评测工作，8篇使用自带query前缀的投毒样本，12篇未报告部署工作点的FPR。

最值得记住的一句话：Ranking is not deciding，仅靠AUROC无法区分可通过阈值校准修复的校准崩溃，和决策层完全无法修复的信号崩溃，防御评测必须同时披露投毒数据集构造轮廓和部署阈值下的FPR。
