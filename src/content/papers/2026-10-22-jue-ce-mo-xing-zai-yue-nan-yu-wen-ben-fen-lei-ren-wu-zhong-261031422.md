---
title: How Well Do Decision Models Transfer to Vietnamese? An Empirical Study of Text
  Classification
title_zh: 决策模型在越南语文本分类任务中的迁移效果实证研究
authors:
- Phat Huu Ha
- Nguyen Xuan Phuc
- Nong Nhut Quy
- Trinh Tran Tran
- Nguyen Minh Triet
- Dang Van Thin
affiliations:
- University of Information Technology, Ho Chi Minh City, Vietnam
- Vietnam National University HoChiMinh City, Vietnam
arxiv_id: '2610.31422'
url: https://arxiv.org/abs/2610.31422
pdf_url: https://arxiv.org/pdf/2610.31422
published: '2026-10-22'
collected: '2026-10-25'
category: Eval
direction: 小语种零样本分类模型评测
tags:
- Zero-Shot Classification
- Cross-Lingual Transfer
- Text Classification
- Model Evaluation
- Low-Resource NLP
one_liner: 系统评测4种决策模型在越南语零样本文本分类场景下的性能、标签语言敏感度及语言变异鲁棒性
practical_value: '- 布局东南亚越南语市场做零样本意图识别、商品分类、舆情分析时，优先测试JEV搭配英文标签描述，性能更稳定

  - 处理越南语UGC、搜索query、用户评论时，优先修复变音符号缺失问题，对分类效果提升远高于治理teencode、拼写错误

  - 多语言分类场景不要盲目复用双语标签描述方案，不同模型适配性差异大，需通过AB测试验证实际收益'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有零样本专用决策模型的小语种迁移效果研究不足，越南语场景下的分类性能、鲁棒性边界尚不明确。
### 方法关键点
覆盖6类任务共13种分类设置，评测4种专用决策模型；对比英文、越南语、双语三类标签描述的效果差异；同时测试teencode、拼写错误、变音符号删除三类越南语常见语言扰动下的模型鲁棒性。
### 关键结果
- 英文标签描述下JEV整体性能最优，在11个分类设置中排名第一
- 双语标签描述无统一增益，效果随模型、数据集差异波动
- 变音符号删除对性能影响最大，可使平均macro-F1下降9.51~15.47个百分点，远高于teencode、拼写错误的影响
