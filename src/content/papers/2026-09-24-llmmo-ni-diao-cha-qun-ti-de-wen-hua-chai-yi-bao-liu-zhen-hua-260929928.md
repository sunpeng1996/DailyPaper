---
title: 'Cultural Divergence Preservation: Diagnosing Flattening and Caricature in
  LLM-Simulated Survey Populations'
title_zh: 《LLM模拟调查群体的文化差异保留：诊断扁平化与刻板化》
authors:
- Yeeun Chae
- Yewon Choi
- Seunghyun Lee
- IL Im
affiliations:
- Yonsei University
- NAVER
- Seoul National University Hospital
arxiv_id: '2609.29928'
url: https://arxiv.org/abs/2609.29928
pdf_url: https://arxiv.org/pdf/2609.29928
published: '2026-09-24'
collected: '2026-09-26'
category: Eval
direction: LLM仿真人群跨文化评估
tags:
- Cross-Cultural Evaluation
- Synthetic Population
- LLM Evaluation
- Survey Simulation
- Cultural Divergence
one_liner: 提出仅需一次人工校准的CDP指标，弥补传统指标无法衡量跨文化差异保留度的缺陷
practical_value: '- 跨境电商/跨区域推荐场景做用户画像仿真时，需在单群体分布保真指标外补充类CDP的跨群体差异校验指标，避免不同区域用户画像趋同或过度刻板化，降低推荐适配错误率

  - 用LLM生成不同地域/文化的用户persona做前置AB测试仿真时，可复用CDP的一次人工校准模式，低成本校验生成persona的文化差异合理性，无需全量标注

  - 传统分布距离指标（JSD等）对组间差异变化敏感度低，跨人群仿真效果评估需补充组间差异专项指标，避免被传统指标高分误导'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM被广泛用作合成调查对象估算人群反馈分布，跨文化场景下现有评估指标（如JSD）仅衡量单国家内分布保真度，无法捕捉跨国家文化差异的保留情况，容易出现文化扁平化（差异缩小）或刻板化（差异放大）问题。
### 方法关键点
提出Cultural Divergence Preservation（CDP）轻量诊断指标，仅需一次人工校准即可完成评估，无需大量参考标注，可直接量化跨群体差异的衰减或放大程度。
### 关键结果
实验覆盖4种LLM backbone、3种persona提示方法、2个调查领域（WVS、大五人格测试）：
1. 传统保真指标和CDP结果存在系统性偏差；
2. 跨文化差异缩小时CDP单调下降、放大时单调上升，同期JSD变化幅度极小；
3. 传统指标得分最高的DeepPersona提示法，在所有模型-领域组合下都存在最严重的文化扁平化问题。
