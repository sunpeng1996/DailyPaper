---
title: 'What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial
  LLM API Migrations'
title_zh: 商用LLM API迁移评估盲区：item级性能变化的量化测量
authors:
- Xiaonan Xu
- Wenjing Wu
affiliations:
- Georgia Institute of Technology
- University of Colorado Boulder
arxiv_id: '2608.17719'
url: https://arxiv.org/abs/2608.17719
pdf_url: https://arxiv.org/pdf/2608.17719
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: LLM评估 · API迁移性能校验
tags:
- LLM evaluation
- API migration
- regression testing
- item-level measurement
- backward compatibility
one_liner: 量化商用LLM API迁移中聚合得分掩盖的双向item级性能波动，提供item级分类评估方案
practical_value: '- 做LLM API版本迭代评估时，不能仅看整体准确率等聚合指标，必须新增item级回归校验，避免商品文案生成、query理解等核心场景效果掉点

  - 评估LLM效果时需设计分层评分规则，对齐业务实际容忍度，区分严格/宽松阈值的结果差异，避免误判迁移价值

  - 对核心业务依赖的LLM调用场景，可复用论文的错误发现率控制+重复采样方法，量化每个item的效果波动置信度，优先保障高优先级item效果稳定'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
商用LLM API厂商会定期下线旧版本，下游系统被迫迁移时通常仅靠聚合benchmark得分做决策，掩盖了异质性的item级性能变化，容易引发核心业务掉点。
### 方法关键点
针对GPT-5.4到GPT-5.6的3次版本升级，对900个涵盖研究生知识、奥赛数学、指令遵循的benchmark item，每个item在每个模型上重复查询50次，在错误发现率控制和实际显著性阈值下，将每个item分类为可靠提升、可靠回归、实际等效、无结论四类。
### 关键结果数字
9组迁移-benchmark测试对中，提升和回归同时存在：聚合得分最高提升7.3pp的版本迭代中仍有最高8.3%的item可靠回归；聚合得分下降的迭代中也有最高10.7%的item可靠提升；指令遵循场景最新迁移中，严格/宽松评分的结果差达3.9pp，严格评分下3.9pp的回归在宽松评分下仅为0.04pp。
