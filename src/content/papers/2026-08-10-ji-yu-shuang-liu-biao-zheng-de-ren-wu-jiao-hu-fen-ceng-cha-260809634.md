---
title: 'IntHQ: Task-Interactive Hierarchical Query on Dual-Stream Representations
  for Generative Recommendation'
title_zh: 基于双流表征的任务交互分层查询多任务生成式推荐框架IntHQ
authors:
- Junjie Sun
- Longfei Xu
- Huimin Yan
- Wei Luo
- Kaikui Liu
- Xiangxiang Chu
affiliations:
- Alibaba Group DreamX
arxiv_id: '2608.09634'
url: https://arxiv.org/abs/2608.09634
pdf_url: https://arxiv.org/pdf/2608.09634
published: '2026-08-10'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · 多任务优化
tags:
- Generative Recommendation
- Multi-Task Learning
- Dual-Stream Architecture
- Hierarchical Query
- Industrial Deployment
one_liner: 针对生成式推荐多任务三类坍缩问题，提出双流+任务交互+分层查询的IntHQ框架，上线高德获1.6%相对UVCTR提升
practical_value: '- 多任务生成式推荐场景可复用双流解耦设计，提前将任务标识注入独立任务流，避免任务信号被共享表征稀释，缓解source collapse

  - 无需预定义任务依赖漏斗，可基于注意力显式建模任务间自适应交互，适配不同场景动态变化的任务依赖，缓解relational collapse

  - 不同任务对不同深度表征偏好不同，可复用分层查询机制，让每个任务自适应选取合适层级特征，无需固定单层出头，缓解hierarchical collapse

  - 工程上线可参考其离线预计算用户历史序列存入KV、在线仅做轻量推理的架构，30k QPS下平均延迟仅40ms，适配高并发工业场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐多任务方案普遍基于「共享无偏表征+多任务头」架构，存在三类固有坍缩：一是source collapse，任务信号注入晚、被共享空间稀释；二是relational collapse，任务依赖要么隐式被主干吸收，要么被预定义漏斗静态固定；三是hierarchical collapse，不同任务依赖不同尺度特征、训练阶段偏好不同，固定层级输出无法适配。

### 方法关键点
1. **Dual-Stream Decoupling (DSD)**：分离上下文流（编码用户行为、场景、属性等通用信息）和独立任务流（预定义各任务的可学习token，参数与上下文流完全解耦），任务流提前注入任务标识避免信号稀释
2. **Task-Interactive Modeling (TIM)**：任务流内增加自注意力，显式建模任务间自适应依赖，无需预定义任务漏斗，通过因果掩码避免标签泄露
3. **Hierarchical Querying (HQ)**：每个任务的token作为query，跨主干所有层的表征做注意力，自适应选取适配当前任务、当前训练阶段的多层特征

### 关键结果
离线在阿里公开IntTravel数据集（41亿交互、1.63亿用户、730万POI）上测试，对比IntTravel、OneTrans、HGenPush等SOTA生成式推荐主干，搭配PLE、STAR、DSFNet、HoME四类主流多任务头，所有任务指标均领先；上线高德出行推荐场景，30k QPS下平均延迟40ms，获1.6%相对UVCTR提升。

最值得记住的结论：多任务生成式推荐的优化要把任务信号提前注入编码阶段，而不是仅在输出层做多任务头适配。
