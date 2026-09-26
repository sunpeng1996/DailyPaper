---
title: 'InternW0: A Foundational Physical World Model for Efficient Real-World Interactions'
title_zh: InternW0：面向高效真实世界交互的基础物理世界模型
authors:
- Jisong Cai
- Yao Mu
- Ganlin Yang
- Zhe Cao
- Zhangzheng Tu
- Xing Gao
- Kailin Li
- Xinyu Zhan
- Lixin Yang
- Yangkun Zhu
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2609.27656'
url: https://arxiv.org/abs/2609.27656
pdf_url: https://arxiv.org/pdf/2609.27656
published: '2026-09-22'
collected: '2026-09-26'
category: Agent
direction: 实体Agent · 物理世界基础建模
tags:
- World Model
- Embodied Agent
- KV Cache
- Multimodal Pretraining
- Asynchronous Inference
one_liner: 提出异步双流架构的基础物理世界模型InternW0，实现低延迟高准确率的真实世界实体交互决策
practical_value: '- 异步快慢双专家架构可直接迁移到搜索推荐多时效任务：慢专家建模长周期用户兴趣，快专家响应实时点击/搜索行为，兼顾长期偏好准确性与实时性

  - 分层KV复用+观测条件路由机制可用于优化LLM4Rec、RAG推荐的推理延迟，降低高并发实时推荐请求的计算开销

  - 领域特定软Prompt适配异构任务的思路，可复用在多场景/多品类推荐系统的统一建模，减少不同业务线的重复训练成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有物理世界模型无法兼顾长时序预测精度与实时交互响应速度，难以适配动态变化的真实环境下的可落地决策需求。
### 方法关键点
1. 采用非对称视频-动作双流架构，高容量慢视频专家做长horizon动态预测，轻量快动作专家输出高频控制信号
2. 复用分层KV cache，通过观测条件路由适配新观测状态，避免每轮请求重新生成上下文
3. 支持多模态输入（视觉/力/触觉），通过领域接口+软Prompt适配异构实体，接触感知后训练优化强接触任务表现
4. 在7200小时多源异构机器人/第一人称数据上预训练，含自研275小时真实实验室第一人称数据集EgoLab
### 关键结果数字
- 真实世界任务成功率最高超基线37.6pct，推理速度达基线的3.13倍
- Libero基准测试平均准确率达98.6%，RoboTwin 2.0随机场景准确率达93.04%
