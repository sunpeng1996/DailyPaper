---
title: 'PACE: Perceived-Latency-Aware Cascading Service Routing and Filler Control
  for QoE-Efficient Retrieval-Augmented Dialogue Serving'
title_zh: PACE：面向RAG对话服务的感知延迟感知级联路由与填充控制框架
authors:
- Lin Huang
- Yujuan Tan
- Weisheng Li
- Lixiang Zeng
- Kun Yang
- Suihan Xiao
affiliations:
- 重庆大学
- 国防科技大学
- 重庆邮电大学
- 多伦多大学密西沙加分校
- 重庆华远智信科技有限公司
arxiv_id: '2609.10372'
url: https://arxiv.org/abs/2609.10372
pdf_url: https://arxiv.org/pdf/2609.10372
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: RAG服务优化 · 感知延迟QoE提升
tags:
- RAG
- LLM Serving
- QoE
- Semantic Caching
- Perceived Latency
- Service Routing
one_liner: 联合优化RAG对话级联路由、缓存准入与等待填充策略，在质量成本约束下大幅降低用户感知首答延迟
practical_value: '- 电商智能客服、导购Agent场景可直接复用三级级联应答架构（语义缓存L0/召回直返L1/LLM生成L2），优先用低延迟路径兜底，大幅降低首答延迟

  - 可借鉴填充控制器设计：根据近期快路径占比动态决定是否开启等待填充，配合无事实性表述的填充话术规则，实测可减少94%冗余小模型调用且零冲突率

  - 针对价格、库存、促销等时效敏感query的语义缓存准入规则可直接复用，用正则匹配分类+短TTL/直接拒存，把时效类query stale率从86%降到0

  - 负载自适应阈值调整策略可迁移到推荐系统多级召回、缓存场景，根据在线负载（TTFT、QPS）动态调整相似度阈值，在流量波动时保障服务稳定性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM对话服务核心体验瓶颈是用户感知首答延迟（PTFR）而非总生成时长，尤其线下导购机器人、电商智能客服等场景，超过1s的无响应会被用户判定为故障。现有优化零散分布在级联路由、语义缓存、自适应RAG等方向，未联合管控应答路径选择与用户等待窗口内容，也未将感知延迟作为核心优化目标。

### 方法关键点
- 三级级联应答架构：L0语义缓存（近0延迟）、L1高置信召回直返（0.2~0.5s）、L2 LLM生成（1~4s），负载自适应控制器结合TTFT EWMA值与请求到达率生成负载指数，动态调整缓存相似度阈值和召回直返阈值，高负载下松阈值引流到低延迟路径
- 联合路径填充控制器：根据最近32次请求的快路径占比决定是否启动小填充模型，填充等待预算随TTFT动态调整，通过prompt规则+输出过滤保障填充话术无事实性内容，避免与最终应答冲突
- 波动感知缓存准入：用正则匹配将query分为时效敏感（价格、促销、库存等）和稳定类，时效类query配置短TTL或直接拒存，避免返回过期信息

### 关键结果
在7.5万次汽车零售导购机器人实测请求上，静态阈值级联架构将P95 PTFR从纯LLM的0.53s降到0.29s（降50%）；自适应版本高负载下比标准RAG PTFR低2.4倍，回答质量与最强基线无统计差异；填充控制器减少94%冗余小模型调用，冲突率为0；时效类query stale率从86%降到0。

对话类服务的体验优化核心是管控用户感知延迟而非仅优化系统客观延迟，级联路径+动态填充的架构可在几乎不损失质量的前提下大幅提升用户体验
