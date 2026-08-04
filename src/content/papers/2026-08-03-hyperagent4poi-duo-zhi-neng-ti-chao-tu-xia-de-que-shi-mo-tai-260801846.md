---
title: 'HyperAgent4POI: Dynamic Semantic Message Passing on Multi-Agent Hypergraphs
  for Missing-Modality Recommendation'
title_zh: HyperAgent4POI：多智能体超图下的缺失模态POI推荐框架
authors:
- Jinze Wang
- Yuze Liu
- Tiehua Zhang
- Jiong Jin
- Zhu Sun
affiliations:
- Swinburne University of Technology
- Tongji University
- Singapore University of Technology and Design
arxiv_id: '2608.01846'
url: https://arxiv.org/abs/2608.01846
pdf_url: https://arxiv.org/pdf/2608.01846
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: POI推荐 · 多智能体超图 缺失模态补全
tags:
- POI Recommendation
- Hypergraph
- Missing Modality
- LoRA
- Multi-Agent
one_liner: 基于冻结LLM+角色LoRA的超图动态语义传递，解决缺失模态下的POI推荐问题
practical_value: '- 可复用「冻结大模型+角色专属LoRA」架构，同一基座支持语义聚合、拓扑打分、模态补全多任务，大幅降低多任务推荐场景的训练部署成本

  - 模态补全可与图/超图消息传递迭代执行，每层用更新后的拓扑上下文重新补全缺失模态，在电商商品图文缺失场景下可显著提升表征质量

  - 所有LLM计算放在离线阶段完成，最终节点表征缓存后线上仅用点积打分，兼顾LLM语义能力和线上低延迟要求，可无缝适配现有推荐serving架构

  - 超图拓扑可基于语义匹配做软修正，不局限于原始交互硬关联，能挖掘更多高阶用户-物品共现模式，对session类推荐效果提升明显'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现实场景中POI的文本、图像等模态信息往往缺失，传统补全方法与超图消息传递解耦，表征误差会逐层传播导致推荐效果下降；现有动态超图方法依赖不完整初始表征，拓扑优化与模态补全未联合建模，效果瓶颈明显。

### 方法关键点
- 每个用户/POI节点对应一个持久化智能体，共享冻结Llama-3-8B基座，配备3个角色专属LoRA适配器，分别实现语义聚合、拓扑演化、模态推断三类任务
- 动态语义消息传递(DSMP)流程：每层先将节点消息聚合为超边语义motif，再基于motif修正超边软关联权重，最后用修正后的拓扑上下文补全POI缺失模态，更新节点状态进入下一层
- 训练阶段仅更新LoRA、投影层等少量参数，LLM计算仅在训练和离线表征刷新时执行，最终节点表征缓存后线上无需调用LLM，直接点积打分

### 关键结果
在Yelp-2018、FSQ-NYC、FSQ-TKY三个真实LBSN数据集上，对比15个基线：60%模态缺失率下NDCG@20平均比最强基线提升8.2%；80%模态缺失率下NDCG@20下降幅度仅17%~18%，远低于基线的25%~27%；线上单千次查询耗时仅14.7ms，与传统图推荐性能相当。

最值得记住的一句话：把大模型的语义能力嵌入到图消息传递的每层流程中，同时将大模型计算完全隔离在离线阶段，是兼顾推荐效果和线上性能的可行路径
