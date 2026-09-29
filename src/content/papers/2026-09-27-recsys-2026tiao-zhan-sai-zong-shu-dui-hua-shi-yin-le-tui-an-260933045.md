---
title: 'Overview and Analysis of the RecSys Challenge 2026: Conversational Music Recommendation'
title_zh: RecSys 2026挑战赛综述：对话式音乐推荐方案分析
authors:
- Seungheon Doh
- Sergio Oramas
- Bruno Sguerra
- Abhinav Bohra
- Claudio Pomo
- Francesco Barile
affiliations:
- Sony Group Corporation
- SiriusXM
- Deezer Research
- Amazon
- Politecnico di Bari
arxiv_id: '2609.33045'
url: https://arxiv.org/abs/2609.33045
pdf_url: https://arxiv.org/pdf/2609.33045
published: '2026-09-27'
collected: '2026-09-29'
category: RecSys
direction: 对话式推荐 · 赛事方案拆解
tags:
- Conversational-RecSys
- Music-Recommendation
- Retrieval-Rerank
- LLM-Judge
- RecSys-Challenge
one_liner: 梳理RecSys 2026对话式音乐推荐赛的参赛方案，提炼可落地的系统设计原则
practical_value: '- 对话式推荐系统可直接复用「多源召回+保留源侧特征的树模型重排」架构，无训练资源时用Weighted RRF做融合 fallback，比单路召回+端到端排序的效果更稳定、迭代效率更高

  - 冷启动场景优先基于对话上下文、item本身属性做检索，用户ID/profile/CF信号设为可选分支，避免冷启动时因缺失用户特征导致效果暴跌

  - 无需搭建复杂的全量意图分类体系，仅针对高置信可触发特定动作的意图（比如精确商品查找、续听/换新需求）做规则+小模型检测，歧义时直接走通用链路，性价比更高

  - 对话场景的召回必须覆盖完整多轮上下文，仅用当前query做检索会损失10%以上的相关信号，可做「当前query+全对话上下文」双路召回融合补全信息'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话式推荐支持用户通过多轮自然语言交互迭代表达偏好，比传统静态单轮推荐体验更灵活，但此前缺乏统一的任务基准、评测体系和可复用的工程范式，行业落地成本极高。RecSys 2026挑战赛首次将对话式音乐推荐定义为「曲目召回排序+事实 grounded 回复生成」联合任务，为该领域提供了标准化的验证框架。
### 方法关键点
- 发布1.6万+合成多轮对话数据集TalkPlayData，覆盖4.7万首多模态曲目、8700+用户，预置多模态Embedding、用户属性等特征，评测指标加权融合nDCG@20、多样性、LLM-as-a-Judge回复打分
- 拆解16个获奖方案的共性架构，主流均采用「多源召回-树模型重排-解耦回复生成」的三级模块化设计
- 提炼4条可落地设计原则：多源召回后保留各源的rank/score/命中特征输入重排、冷启动场景优先依赖对话上下文和item信号、仅做窄域高置信意图检测、建模完整多轮上下文而非仅当前query
### 关键实验
- 评测集Blind-B包含40个冷启动（无用户profile）、40个暖启动样本，基线方案为Random+模板、BM25+Llama-1B
- 最优非数据泄露方案nDCG@20达0.493，比BM25基线高268%，LLM Judge最高得分4.9/5
- 模糊单目标请求的nDCG比精确查找低43%，建模完整多轮上下文比仅用当前query的nDCG提升约2%
### 核心结论
对话式推荐的核心是用多源信息对冲交互不确定性，解耦的模块化架构在效果、迭代效率上远优于复杂端到端方案
