---
title: 'Beyond wheelchairs and blindfolds: Investigating disability stereotypes in
  T2I models with INCLUDE-BENCH'
title_zh: 超越轮椅与眼罩：用INCLUDE-BENCH评测文生图模型的残疾刻板印象
authors:
- Sophia Lichtenberg
- Albert Gatt
- Judith Masthoff
affiliations:
- Utrecht University
arxiv_id: '2607.08515'
url: https://arxiv.org/abs/2607.08515
pdf_url: https://arxiv.org/pdf/2607.08515
published: '2026-07-09'
collected: '2026-07-12'
category: Eval
direction: 文生图公平性 · 偏见评测
tags:
- T2I
- Bias Evaluation
- Stereotype Detection
- Benchmark
- Fairness
one_liner: 推出首个大规模文生图模型残疾相关偏见评测基准INCLUDE-BENCH及SCM刻板印象评分指标
practical_value: '- 电商场景生成营销物料（模特图、场景图等）时，可复用SCM Score检测残疾相关刻板印象，规避合规风险

  - 构建多群体友好内容生成的内部评测集时，可参考INCLUDE-BENCH的prompt设计框架，覆盖多维度、动静态场景测试用例

  - 需适配残障群体宣传合规要求的业务，可基于该研究结论针对性优化训练数据中残障群体的表示多样性，减少刻板输出'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有T2I模型偏见研究多聚焦性别、肤色、文化维度，残疾相关偏见长期被忽视，且现有评测方法未对齐社会学刻板印象定义，无法系统化评估对残障群体的表征伤害。

### 方法关键点
推出首个大规模残疾偏见评测基准INCLUDE-BENCH，覆盖多偏见维度、动静态场景，共生成11.9万张图像作为测试集；配套提出基于社会学刻板印象内容模型的SCM Score，量化刻板印象程度；完成15个开源、2个闭源T2I模型的全量评测。

### 关键结果数字
1. 所有模型对 mobility 障碍、默认残疾提示词的输出90%+为轮椅形象；2. 带残疾条件的生成内容多样性比基准低42%；3. 刻板印象类刻画的文本-图像对齐度比非刻板类高28%；4. T2I模型输出与真实世界刻板印象关联的匹配度达87%
