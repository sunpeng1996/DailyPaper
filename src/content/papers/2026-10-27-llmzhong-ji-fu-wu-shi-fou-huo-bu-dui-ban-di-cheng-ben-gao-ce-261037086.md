---
title: Is Your LLM Relay Serving What It Claims? A low-cost and high-power test for
  LLM Relay Auditing
title_zh: LLM中继服务是否货不对板？低成本高检测力的LLM中继审计方法
authors:
- Fangran Miao
- Shengjie Niu
- Jian Huang
- Ting Li
affiliations:
- The Hong Kong Polytechnic University
- Southern University of Science and Technology
arxiv_id: '2610.37086'
url: https://arxiv.org/abs/2610.37086
pdf_url: https://arxiv.org/pdf/2610.37086
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: LLM服务审计 · 黑盒分布指纹校验
tags:
- LLM Auditing
- Black-box Testing
- Distributional Fingerprint
- LLM Relay
- Statistical Testing
one_liner: 提出基于分布指纹的黑盒LLM中继审计方案，低成本实现模型真伪校验与混配比例估算
practical_value: '- 业务侧采购第三方LLM API服务时，可复用DFA方案构建低成本校验流程，避免服务商降配替换模型、混合路由低性能模型造成的业务效果下降

  - 自研Agent/GenRec系统的多LLM路由模块，可基于分布指纹构建轻量校验逻辑，验证动态路由的模型命中是否符合预期，避免路由逻辑Bug导致的效果波动

  - 黑盒LLM效果对齐时，可复用「有限选择探针+响应分布统计」的思路，低成本区分不同基座模型的输出特性差异，减少冗余AB测试成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM中转/转售API已成为企业调用大模型的主流方式，但用户无法校验服务商返回的模型是否与付费购买的规格一致，现有审计方案无法同时满足黑盒访问下的低成本、抗部署配置干扰、统计可解释三个要求。

### 方法关键点
提出分布指纹审计（DFA）方法，仅需黑盒获取待测端点与可信参考端点的文本响应即可完成校验：1. 构造语义简单的有限选择探针批量请求，基于分类响应分布构建端点指纹；2. 逐探针比对待测与参考指纹，用Cauchy combination test聚合证据，输出预设显著性水平下的审计p值；3. 支持全量替换下的模型归因、固定比例混合路由下的替换模型身份与替换比例联合估算。

### 关键结果数字
在10个模型家族的16款闭源/开源LLM基准测试中，α=0.05显著性水平下，仅需5个探针、单次审计调用250次中继接口，240组全量替换对的检测率达到极高水平；混合路由场景下替换比例估算误差随审计预算提升显著降低。
