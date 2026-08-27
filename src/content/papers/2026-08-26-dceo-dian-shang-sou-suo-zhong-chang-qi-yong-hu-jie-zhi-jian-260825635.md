---
title: 'DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling
  in E-commerce Search'
title_zh: DCEO：电商搜索中长期用户价值建模的直接因果效应优化
authors:
- Junzhao Zhang
- Tao Zhang
- Liren Yu
- Feiyi Dong
- Zhixuan Zhang
- Dan Ou
- Haihong Tang
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.25635'
url: https://arxiv.org/abs/2608.25635
pdf_url: https://arxiv.org/pdf/2608.25635
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 电商搜索排序 · 长期用户价值优化
tags:
- e-commerce search
- multi-objective fusion
- causal inference
- long-term user value
- learning to rank
one_liner: 提出DCEO因果优化框架，跨粒度对齐商品排序与用户长期价值，上线GMV提升0.36%
practical_value: '- 多目标融合可替代人工调权方案，通过actor生成上下文动态权重，直接对齐GMV等长期用户级目标，大幅降低A/B测试试错成本

  - 优化目标放弃传统的预测关联，改用相对因果效应（RCE）作为优化目标，可保证proxy指标提升时真的能带动最终业务目标上涨

  - 架构兼容性极强，仅需部署轻量actor模型，无需修改原有多目标融合链路，直接新增proxy得分项即可快速上线

  - 长期价值建模可扩展上游特征池，纳入点击/加购/支付各转化阶段、不同客单价区间的预估值，可显著提升最终效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索的核心长期目标（如n天累计GMV、用户复购）是用户粒度的，但排序环节基于商品粒度打分，存在天然的粒度差。现有方案依赖人工调整多目标融合的全局权重，无法实现细粒度个性化，反复A/B测试成本极高；且传统优化proxy与目标的预测关联，无法保证提升proxy就能带动最终目标上涨，容易导致次优结果。

### 方法关键点
- 采用actor-critic架构：actor根据用户、请求特征生成请求级的动态融合权重，加权上游多维度预估值得到商品级proxy得分，再聚合校准为固定曝光量下的用户级proxy metric
- 提出相对因果效应（RCE）作为对齐度指标：critic拟合用户特征+proxy metric到长期目标的映射，以干预proxy提升δ后的目标差值作为actor的训练信号，直接优化因果效应而非预测关联
- 新增条件归一化排序损失作为正则，解决因果效应损失非凸难优化的问题；离线训练完成后仅需部署actor模块，将proxy得分直接加入原有多目标融合公式即可

### 关键结果
基于阿里淘宝搜索14天日志训练，离线对比传统预测关联优化方案，RCE提升140.9%；对比仅用GMV单特征的方案，RCE提升96.3%。线上41天A/B测试，相比传统GMV proxy，GMV提升0.36%，点击量提升0.36%，购买量提升0.12%。

> 最值得记住：优化长期用户价值时，提升proxy与目标的因果效应，比优化两者的预测关联效果好得多
