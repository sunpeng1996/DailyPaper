---
title: 'Winning by Peeking: Unenforced Budgets and Test-Set Selection Inflate Short-Budget
  AutoML Comparisons'
title_zh: 短预算AutoML对比结果虚高原因：测试集泄露与预算约束失效
authors:
- Guilin Zhang
- Kai Zhao
affiliations:
- Independent Researcher
arxiv_id: '2608.07303'
url: https://arxiv.org/abs/2608.07303
pdf_url: https://arxiv.org/pdf/2608.07303
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: AutoML基准测试评估规范
tags:
- AutoML
- Benchmark
- Evaluation
- Bias Analysis
- Budget Control
one_liner: 揭示短预算AutoML对比的两类实验漏洞，给出公平对比的可落地检查清单
practical_value: '- 做低延时算法（如实时召回、轻量微调）离线对比时，严禁在测试集上选优，测试集仅用于最终性能校验，候选选优必须用独立验证集

  - 对比不同框架/策略的性能时，必须从外部强制统一时间/算力配额，不能依赖框架自身的预算检查，避免实际算力不均导致结果偏差

  - 多候选在同一份测试集上选优会引入约0.27精度点的虚高，可作为离线对比结果的校正参考'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
短预算（数十秒级）AutoML对比广泛出现在工具README、workshop论文中，实验设计漏洞普遍存在，导致结果虚高不可信。
### 方法关键点
针对简单AutoML引擎Orcetra在513个OpenML数据集上看似优于FLAML、AutoGluon的异常结果溯源，定位两类核心实验漏洞：1）所有候选模型直接在测试集打分选最优，而基线仅使用一次测试集；2）仅在启动候选前检查预算、不中途强制终止，实际运行耗时远超标称值。重新做对照实验：改用验证集选优、外部强制统一预算、各框架算力均分。
### 关键结果
修正实验设计后，Orcetra的胜率从59.4%降至34.3%，与两个竞品均无显著性能差异；其中测试集选优带来4.8个百分点的胜率虚高，实测选择偏差仅0.27精度点，远低于理论上的σ√(2lnK)界。
