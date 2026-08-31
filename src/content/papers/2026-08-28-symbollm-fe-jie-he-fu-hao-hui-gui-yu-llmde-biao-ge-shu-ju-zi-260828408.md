---
title: 'SymboLLM-FE: LLM-Accelerated Symbolic Regression for Automated Feature Engineering
  on Tabular Data'
title_zh: SymboLLM-FE：结合符号回归与LLM的表格数据自动特征工程
authors:
- Zi-Jian Cheng
- Zi-Yi Jia
- Zhi Zhou
- Yu-Feng Li
- Lan-Zhe Guo
affiliations:
- National Key Laboratory for Novel Software Technology, Nanjing University
- School of Intelligence Science and Technology, Nanjing University
- School of Artificial Intelligence, Nanjing University
arxiv_id: '2608.28408'
url: https://arxiv.org/abs/2608.28408
pdf_url: https://arxiv.org/pdf/2608.28408
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 表格自动特征工程 · LLM+符号回归
tags:
- AutoFE
- Symbolic Regression
- LLM
- Tabular Data
- Feature Engineering
one_liner: 融合符号回归与LLM，仅需个位数API调用生成高性能可解释的表格特征
practical_value: '- 做电商用户/商品侧特征工程时，可先通过符号回归挖掘统计层面有效的特征公式，再喂给LLM做语义对齐和可解释性优化，大幅减少LLM迭代次数和幻觉问题

  - 高维特征组合搜索可复用Spearman相关性排序+扩展滑动窗口的策略，将搜索复杂度从O(2^n)降到O(n^2)，在保证特征质量的同时大幅降低计算量

  - CVR/点击率预测等需要高可解释性的场景，可直接复用该框架生成既有业务语义可解释、又能提效的特征，避免传统AutoFE生成的黑箱特征难以合规的问题

  - 用LLM做特征优化时，不需要让LLM从零生成，而是基于已有的统计有效特征做重构、去冗余、代码生成，能大幅降低LLM调用成本和出错概率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统AutoFE依赖盲目的数学变换生成特征，预测性能高但完全不可解释，无法满足金融、电商等需要合规、可解释的业务场景；现有LLM-based AutoFE需要多轮迭代验证，API调用成本高，还容易出现幻觉生成无效特征，两者都无法兼顾性能、可解释性和效率。

### 方法关键点
- 两阶段框架：第一阶段用符号回归生成与目标强相关的候选特征公式，第二阶段用LLM注入领域知识做公式的语义优化、可解释性增强和可执行代码生成
- 降本策略：先通过Spearman相关性对特征做重要性排序，再用扩展滑动窗口生成特征子集，将符号回归的搜索复杂度从指数级O(2^n)降到多项式级O(n^2)
- 迭代优化：生成的特征通过下游模型验证后反馈给LLM做迭代调优，同时内置去冗余和过拟合抑制机制，避免特征爆炸

### 关键结果
在6个真实数据集+4个Kaggle竞赛上验证，相比传统AutoFE平均性能提升1.23%，相比LLM-based AutoFE平均准确率高1%，Kaggle竞赛上平均得分提升2.5pp；仅需平均4次LLM API调用即可完成全流程，远低于其他LLM-based AutoFE的几十次调用成本，生成的特征同时具备高预测性能和业务可解释性。

### 最值得记住的一句话
LLM做特征工程时不要从零生成，而是锚定统计层面已经验证有效的特征做语义优化，能同时解决幻觉、效率、可解释性三大问题。
