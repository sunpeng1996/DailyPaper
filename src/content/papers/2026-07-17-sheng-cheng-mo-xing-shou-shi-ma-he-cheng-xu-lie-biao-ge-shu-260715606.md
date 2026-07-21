---
title: Do Generative Models Keep Time? A Time-Aware Evaluation of Synthetic Sequential
  Tabular Data
title_zh: 生成模型守时吗？合成序列表格数据的时间感知评估
authors:
- Kiwan Kwon
- Kangmin Kim
- Hojin Lee
- Yeseong Jung
- Hyeongwoo Kong
- Vamsi K. Potluru
- Saerom Park
- Yongjae Lee
affiliations:
- UNIST
- HUFS
- JP Morgan AI Research
- LinqAlpha
arxiv_id: '2607.15606'
url: https://arxiv.org/abs/2607.15606
pdf_url: https://arxiv.org/pdf/2607.15606
published: '2026-07-17'
collected: '2026-07-21'
category: Eval
direction: 合成数据 · 时序保真度评估
tags:
- Synthetic Data
- Temporal Fidelity
- Sequential Tabular Data
- Evaluation Protocol
- Benchmark
one_liner: 提出合成序列表格数据的分类引导式时间保真度评估协议，揭示传统静态评估的时序缺陷
practical_value: '- 生成/评估用户行为序列合成数据时，必须加入时序维度校验，避免生成倒序/重复时间戳的无效序列

  - 可直接复用4个时序评估维度：时间戳有效性、对齐时间点截面结构、实体内动态、时变关系结构，替代原有的单条数据校验逻辑

  - 用合成用户行为数据训练推荐模型前，先做时序保真度校验，避免低质量合成数据拉低模型效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
合成序列表格数据广泛用于隐私合规的数据共享，但传统静态评估仅关注全局分布，完全无法发现时间戳倒序/重复、实体行为轨迹不符合真实时序逻辑的问题，生成的序列数据实际可用性差。

### 方法关键点
提出分类引导的时间保真度评估协议：先对数据集按4个属性（时间表示方式、采样是否规律、轨迹是否相互依赖、实体与历史的关联模式）分类，再针对性选择评估维度，覆盖时间戳有效性、对齐时间点截面结构、实体内动态、时变关系结构4个核心维度，将原有的单条记录评估升级为轨迹级评估。

### 关键结果数字
在6个领域13个数据集、8种生成模型上验证，传统评估的模型排名与时序评估排名差异极大，时序缺陷和模型架构强相关而非随机错误，仅用静态分布推断时序保真度完全不可靠。
