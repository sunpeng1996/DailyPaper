---
title: 'Squoosh Bench: Evaluating UX-1 on 318 Historical Website A/B Tests'
title_zh: 《Squoosh Bench：基于318组历史网站A/B测试的UX-1模型评估》
authors:
- Rohith Pasula
- Johari Dramiga
- Viraj Shah
- Suzan Halim
- Tyler Dooskin
affiliations:
- Squoosh AI
arxiv_id: '2611.25200'
url: https://arxiv.org/abs/2611.25200
pdf_url: https://arxiv.org/pdf/2611.25200
published: '2026-11-18'
collected: '2026-11-20'
category: Eval
direction: A/B测试效果预评估 大模型基准测试
tags:
- A-B Testing
- Benchmark
- LLM Evaluation
- User Simulation
- Conversion Prediction
one_liner: 基于318组历史A/B测试验证微调的UX-1模拟用户预测A/B结果准确率达84%，远超通用大模型
practical_value: '- 做A/B测试前置筛选时，可基于历史用户浏览数据微调专属模拟用户模型，提前淘汰低概率获胜的迭代方案，节省流量成本

  - 优先测试模拟用户判定的高胜率版本，可覆盖超85%的实际获胜变体，90%以上选中的变体最终线上效果正向，大幅提升迭代效率

  - 不要完全依赖模型预测筛除所有低优先级方案，保留少量测试配额给未被选中的候选，避免遗漏潜在有效迭代，平衡效率与收益'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
电商/网站迭代的A/B测试需要消耗大量流量，实验团队亟需前置预判方案优劣，优先测试高潜力方案，降低试错成本。
### 方法关键点
构建Squoosh Bench评估基准，筛选412组历史网站A/B测试，最终选取运行时长超21天的318组有效样本，对比4套系统的三类A/B结果（原版本胜/变体胜/无结论）预测能力；推理阶段屏蔽页面角色、隐藏真实结果，其中UX-1为在人类浏览数据上微调的专用模型，每测试组模拟1000个用户行为输出预测。
### 关键结果
UX-1预测准确率达84.0%（95% Wilson区间79.5-87.6%），远超最强通用大模型Qwen3 Next 80B的61.6%；UX-1判定为高优先级的126个变体中，118个在线上真实测试中获胜，胜率达93.7%，仅漏判19个真实获胜变体。
