---
title: 'FunnelCausalNet: Funnel-aware Joint Conversion-Revenue Uplift for Multi-tier
  Coupon Allocation'
title_zh: FunnelCausalNet：面向多档位优惠券分配的漏斗感知转化-营收联合增益模型
authors:
- Yu Zhang
- Zhihan Wang
- Guanlin Chen
- Min Jiang
- Shuai Li
affiliations:
- AMap Alibaba Group
arxiv_id: '2608.11675'
url: https://arxiv.org/abs/2608.11675
pdf_url: https://arxiv.org/pdf/2608.11675
published: '2026-08-12'
collected: '2026-08-13'
category: RecSys
direction: 因果增益建模 · 多档位优惠券分配
tags:
- uplift_modeling
- causal_inference
- coupon_allocation
- multi_treatment
- conformal_prediction
one_liner: 提出漏斗结构因果增益模型，结合RCT锚定分配与共形审计层，提升多档优惠券投放ROI
practical_value: '- 电商优惠券/补贴分配场景下，若存在明确的转化→营收漏斗结构，可复用硬耦合`μ_gmv = μ_conv * μ_val`的建模方式，相比直接回归GMV最多降低48%的效应估计误差，尤其适配低转化率高零膨胀场景

  - 多档位补贴分配工程落地可复用RCT臂级均值锚定技巧，无需重训模型即可修正GMV预估的系统性偏差，直接提升预算分配ROI

  - 合规要求高的营销场景可复用Bonferroni联合共形区间作为审计层，建议采用宽松的α（0.1~0.2）避免区间过宽导致分配策略过于保守

  - 百万级用户规模的多档资源分配优先选择Lagrangian松弛方案，相比LP求解速度快2个数量级，仅损失极小的ROI精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前优惠券营销增益建模存在三个核心痛点：一是拆分转化、客单价预估忽略GMV=0当且仅当转化=0的漏斗确定性约束，直接回归GMV又在高零膨胀场景下方差过高；二是转化与GMV增益排序不一致，预算有限时直接损失增量营收；三是多档位优惠券的弹性差异未被有效建模，无法支撑预算约束下的最优分配。

### 方法关键点
- 建模层：双分支共享表征，分别预估二元转化概率与非负条件客单价，硬耦合为GMV期望`μ_gmv = μ_conv * μ_val`，训练损失融合转化BCE、客单价对数MSE，可选一致性、单调性正则项
- 校准层：基于RCT臂级均值做加法偏移校准，修正GMV预估系统性偏差；引入边际拆分共形区间+Bonferroni联合覆盖，作为双结果CATE的审计监控带
- 分配层：采用Lagrangian松弛求解百万级用户的多档优惠券预算分配问题，兼顾效果与性能

### 关键结果
- 半合成Criteo-MT7数据集：对比11个基线，硬漏斗耦合相比直接GMV回归降低18%~48%的PEHE_GMV误差，零膨胀率越高收益越明显
- 工业酒店多档优惠券RCT数据集（4.9M曝光样本）：在10%~60%ΔGMV区间的7个锚点上，ΔROI均为最优，相比次优基线高0.18~0.21个单位，策略可覆盖的最大ΔGMV达90.4%，优于所有基线

**最值得记住的一句话**：漏斗耦合建模的收益严格依赖场景的确定性漏斗结构与多档位治疗设计，单激励二元营销场景下反而不如营收导向的排序模型
