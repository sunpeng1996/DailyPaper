---
title: 'Artificial Societies Benchmark: A Validation Framework for Synthetic Research'
title_zh: 人工社会基准：面向合成人口研究的验证框架
authors:
- Edoardo Chidichimo
- Min Jun Jung
- Felix P. S. Wallis
- James K. He
affiliations:
- University of Oxford, UK
- Artificial Societies
arxiv_id: '2609.30030'
url: https://arxiv.org/abs/2609.30030
pdf_url: https://arxiv.org/pdf/2609.30030
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: 合成人口仿真 · LLM输出效度评估
tags:
- Synthetic Population
- LLM Validation
- Benchmark
- Artificial Society
- Survey Simulation
one_liner: 提出覆盖三类效度的11项测试基准，评估LLM构建的合成人口的分析可用性
practical_value: '- 做用户仿真Agent群测试时，可复用内部/构念/外部三类效度的评估逻辑，避免只看平均指标忽略群体差异、特征关联的拟合度

  - 用LLM模拟用户行为做推荐/广告AB仿真实验时，可参考11项测试的设计思路，提前验证仿真人口效度，避免得出错误结论

  - 针对LLM生成用户回答一致性过高、响应尺度压缩的共性问题，做用户模拟时可加入随机性校正规则，提升仿真真实性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有合成调研仅能复刻平均回答，无法准确还原人群差异、答案关联关系、条件变动下的用户响应，缺少体系化的合成人口效度验证框架，易导致基于合成人口的分析结论失真。
### 方法关键点
提出人工社会基准验证框架，覆盖内部、构念、外部三类效度，共设计11项测试，基于20份真实人类数据源，对比9款LLM生成的合成人口表现，同时验证受访者画像信息丰富度对仿真结果的影响。
### 关键结果
单域表现优异不代表其他域保真；LLM普遍存在回答一致性过高、响应尺度压缩、特征关联关系偏移的共性问题；更丰富的用户画像对部分模型预测效果有提升，对另一部分模型反而有负向作用，最终输出的评分卡可明确合成人口适用的分析场景。
