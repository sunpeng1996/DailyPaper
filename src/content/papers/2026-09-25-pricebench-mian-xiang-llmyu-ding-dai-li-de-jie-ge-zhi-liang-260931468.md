---
title: 'PriceBench: A Diagnostic Benchmark for Price, Quality, and Brand Preferences
  in LLM Booking Agents'
title_zh: PriceBench：面向LLM预订代理的价格质量品牌偏好诊断基准
authors:
- Pavel Kireyev
affiliations:
- London School of Economics and Political Science
arxiv_id: '2609.31468'
url: https://arxiv.org/abs/2609.31468
pdf_url: https://arxiv.org/pdf/2609.31468
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: LLM代理偏好诊断·电商预订场景
tags:
- LLM Agent
- Benchmark
- E-commerce
- Preference Modeling
- Discrete Choice
one_liner: 提出LLM预订代理偏好诊断基准，实测28款LLM揭示偏好异质性与位置锁失效模式
practical_value: '- 上线电商导购/预订类LLM Agent前，可复用PriceBench的logit选择模型+正反顺序测试方案，先筛查位置锁问题，避免商品排序权完全被平台控制

  - 针对已上线的导购Agent，可复用其价格-质量 tradeoff 估算方法，校准Agent默认偏好，避免与目标用户群体（性价比/高端用户）的偏好错配

  - 商家侧可参考不同LLM的价格响应曲线（线性/对数/阈值/价格质量信号bump），针对性调整定价与排序策略，适配主流导购Agent的选择逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM电商代理基准仅衡量任务完成率，未量化满足用户约束后的实际选择偏好；当LLM作为 autonomous agent 直接代用户下单时，其隐式的价格、质量、品牌偏好直接决定成交商品与客单价，此类偏好的异质性、偏差均未被系统测量，缺少可落地的诊断工具。
### 方法关键点
- 构建179家纽约真实酒店的属性池，生成1800组二选一、1800组三选一预订任务，每组任务正反排序各测试1次，抵消纯位置偏差对参数估计的干扰
- 基于离散选择logit模型拟合LLM选择结果，拆分出位置截距、价格敏感度、质量权重、品牌溢价等可解释参数，同时测试线性/对数/非参数三种价格响应函数
- 设计位置锁筛查规则：首选项选择率超出[15%,85%]区间判定为位置锁定，该类LLM无稳定可测量的真实消费偏好
### 关键结果
覆盖8家厂商的28款LLM测试：① 5款小参数模型（≤8B）存在位置锁，平台控制商品排序即可决定其88%~100%的成交选择；② 23款有效LLM的价格敏感度跨度超1个数量级，对1分点评分的支付意愿跨度达16倍，相同任务下平均成交客单价从$247到$393，相差$146；③ LLM能力仅与选择一致性正相关，与偏好方向无关，同厂商同系列模型的偏好也可能完全相反；④ 所有LLM的质量溢价均远高于人类历史测量区间。
### 核心结论
LLM代理的消费偏好和其能力、厂商无固定关联，必须单独测量，不能默认与人类偏好一致
