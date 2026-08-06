---
title: Provable Limits and Certified Deferral for Verbalized Uncertainty in Small
  Language Models
title_zh: 小语言模型口语化置信度的可证明校准边界与认证拒识机制
authors:
- Jianru Shen
affiliations:
- University of Montana
arxiv_id: '2608.05064'
url: https://arxiv.org/abs/2608.05064
pdf_url: https://arxiv.org/pdf/2608.05064
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: 小语言模型 · 置信度校准与风险可控拒识
tags:
- Small LM
- Confidence Calibration
- Selective Prediction
- Risk Control
- Verbalized Uncertainty
one_liner: 提出融合口语化置信度提取、事后校准、有限样本风险保证的小模型安全部署拒识框架
practical_value: '- 部署端侧小模型做电商客服、商品属性标注等低时延任务时，可复用这套「口语化置信度提取+Platt校准+Clopper-Pearson阈值选择」的安全pipeline，控制错误率在业务预算内

  - 温度scaling对过自信的小模型校准效果存在理论下界，优先选择Platt scaling做事后校准，可将ECE降至0.02量级

  - 对多选择评测/业务分类任务，可复用基于问题哈希的选项随机置换方法，避免模型位置bias干扰结果准确性

  - 跨任务迁移小模型拒识阈值不可行，必须按「模型+业务场景」单独校准，比如同个小模型用于商品问答和售后咨询要分别训练校准器'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小参数量开源LLM广泛应用于端侧、私有部署等成本敏感场景，但模型能力有限错误率高，现有置信度校准方案缺乏可证明的风险控制机制，且小模型上的口语化置信度可用性、校准效果边界尚未明确。

### 方法关键点
-  pipeline 分三步：通过固定格式prompt提取模型输出的口语化置信度分，用Platt scaling做事后校准（比温度scaling多偏置项，解决过自信问题），最后基于Clopper-Pearson界结合联合界修正，选择满足风险预算的最大覆盖阈值，提供有限样本风险保证
- 证明三个理论结论：严格单调校准不改变风险-覆盖前沿与错误检测AUROC；当模型置信度均>0.5且准确率<0.5时，温度scaling无法校准；200条校准集即可生成i.i.d.场景下的风险证书

### 关键实验结果
在ARC-Challenge、TruthfulQA两个数据集上测试0.5B-14B共11个开源指令微调模型，Platt scaling可将ECE最低降至0.02；20%风险预算下仅3组模型-任务对可获得认证，最高覆盖率99.8%，10%风险预算下无模型满足要求；8/22组模型-任务对触及温度scaling不可行下界，与理论预测误差<1%。

最值得记住的结论：校准只赋予置信度语义，无法提升模型本身的错误检测能力，严格的风险证书才是高风险场景下小模型自主决策的前提。
