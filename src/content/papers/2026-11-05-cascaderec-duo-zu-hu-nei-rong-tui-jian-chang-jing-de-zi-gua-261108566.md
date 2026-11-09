---
title: 'CascadeRec: Deployed Adaptive LLM Compute Allocation for Multi-Tenant Content
  Recommendation'
title_zh: CascadeRec：多租户内容推荐场景的自适应LLM算力分配系统
authors:
- Kai Zhao
- Guilin Zhang
- Xiang Cheng
- Xiquan Cui
- Henry Heng
- Xu Chu
- Alet Blanken
affiliations:
- Workday AI Research
arxiv_id: '2611.08566'
url: https://arxiv.org/abs/2611.08566
pdf_url: https://arxiv.org/pdf/2611.08566
published: '2026-11-05'
collected: '2026-11-09'
category: RecSys
direction: LLM推荐重排 · 自适应算力分配
tags:
- LLM4Rec
- Reranking
- Cost-Optimization
- Multi-Tenant
- Production-Deployment
one_liner: 落地双层LLM重排级联架构，多租户推荐场景降10%推理成本无效果退化
practical_value: '- 架构可复用双层级联重排设计：全量请求走轻量小模型重排，仅按规则路由少部分请求到大模型/多采样推理，既平衡成本效果，还可通过临时下调
  escalation 率应对流量波峰削峰

  - 冷启动用户不要盲目加LLM算力：离线实验证明稀疏历史用户用大模型重排NDCG@10最高降30%，额外推理补不了缺失的偏好数据，优先优化prompt里的偏好信号而非推理步数

  - 工程落地必须加LLM输出容错机制：为不同模型配置专用prompt约束输出格式，单独统计解析失败率，任意LLM环节失败自动降级到前序重排/召回结果，避免用户感知报错

  - AB实验必须做分人群效果评估：不要只看大盘指标，大盘持平可能掩盖冷用户退化、热用户提升的结构差异，路由规则要基于分群效果数据制定，不要拍脑袋给冷用户加算力'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业多租户SaaS推荐场景下，LLM重排是最大的边际成本项，租户间交互历史长度、请求流量差异极大：全量用大模型重排不仅成本高，还会因为冷用户历史稀疏导致效果下降，大租户的流量波峰还会引发全链路 latency 上涨，需要自适应的算力分配方案平衡成本、效果、延迟。

### 方法关键点
- 两层级联架构：Tier1 用轻量LLM对全量请求重排，输出排序结果和置信度，结果按(user, model, seed)缓存降低重复计算成本；Tier2 提供3种高成本推理选项：自一致性采样、多路径推理、大参数模型，仅处理路由过来的请求
- 路由设计：生产落地用零延迟的分群启发式规则，基于不同人群的效果数据动态调整路由阈值，可配置无需修改代码
- 容灾机制：全链路配置超时、输出解析失败降级逻辑，任意LLM环节失败自动回退到前序最优结果（Tier1结果/召回排序），用户无感知

### 关键结果数字
- 生产A/B实验跑满1个月，对比全量用高成本重排的基线，CascadeRec 推理成本降低10%，无效果退化，延迟影响极小
- 公开数据集实验：MovieLens-1M、Amazon-Electronics 上，全量LLM重排对仅1条交互的稀疏历史用户NDCG@10最高降30%，仅20条以上交互的长历史用户有最高27%的提升；错误给冷用户路由到Tier2会进一步放大效果损失，60% escalation率的级联架构比全量Tier2节省40-50%的Tier2 token消耗

### 最值得记住的一句话
LLM重排的效果瓶颈是偏好信号的完备性，不是推理算力，给缺失偏好数据的冷用户加推理算力只会白花钱还降效果
