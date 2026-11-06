---
title: 'HeLM: Hierarchical Explicit Language Memory for Non-Markovian Manipulation'
title_zh: HeLM：面向非马尔可夫操作的分层显式语言记忆框架
authors:
- Gyeonghun Kim
- Donghoon Kim
- Minsoo Choi
- Suyun Lee
affiliations:
- Seoul National University
arxiv_id: '2611.02660'
url: https://arxiv.org/abs/2611.02660
pdf_url: https://arxiv.org/pdf/2611.02660
published: '2026-11-02'
collected: '2026-11-06'
category: LLM
direction: 多模态VLA模型 · 分层显式记忆优化
tags:
- VLA
- Explicit Memory
- Non-Markovian
- Hierarchical Memory
- Event Trigger
one_liner: 提出分层显式语言记忆VLA框架，解决非马尔可夫场景长时记忆缺失问题
practical_value: '- 可借鉴事件触发式记忆更新机制，替换全量历史缓存策略，降低长会话推荐、客服Agent的KV cache占用，提升推理响应速度

  - 分层显式语言记忆设计可复用在跨会话用户建模中，用自然语言显式存储用户长期偏好，降低跨任务上下文召回成本

  - 因子化事件检测逻辑可迁移到推荐系统用户行为建模，精准捕捉偏好变化节点，避免无效历史特征的冗余计算'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型普遍基于马尔可夫假设，仅通过当前观测生成动作，无法处理需要长时工作记忆的非马尔可夫场景，在多轮跨任务操作中失败率高。
### 方法关键点
模仿人类「内心独白」机制，提出HeLM分层显式语言记忆框架，通过因子化事件检测识别任务关键节点，仅在事件触发时更新显式语言格式的任务相关历史记忆，无需存储全量观测序列。
### 关键结果
在10类共56种非马尔可夫真实任务（含5类新增跨轮次持久上下文任务）上测试，相比最优基线intra-episode成功率提升12.8个百分点，组合泛化任务子任务成功率达78%；长时序场景下相比关键帧基线内存占用最高降4.5倍，推理速度提升2.5倍。
