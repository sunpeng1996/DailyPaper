---
title: On-the-go Forgetting without Explicit Unlearning via ERASE
title_zh: 基于ERASE的无需显式卸载的推理时动态遗忘方法
authors:
- Kushal Chakrabarti
- Mayank Baranwal
affiliations:
- Tata Consultancy Services Research, Mumbai
- Indian Institute of Technology Bombay
arxiv_id: '2609.05966'
url: https://arxiv.org/abs/2609.05966
pdf_url: https://arxiv.org/pdf/2609.05966
published: '2026-09-05'
collected: '2026-09-09'
category: Training
direction: 模型隐私合规 · 推理时无卸载遗忘
tags:
- Unlearning
- Data Privacy
- Inference Optimization
- Adversarial Perturbation
- Regulation Compliance
one_liner: 提出基于类条件输入扰动的ERASE框架，无需修改模型权重即可在推理时实现指定数据的选择性遗忘
practical_value: '- 电商推荐场景处理用户隐私删除请求时，可借鉴推理时扰动思路，无需重训模型即可快速消除指定用户/商品数据的影响，大幅降低合规响应成本

  - 会话Agent的历史敏感信息遗忘需求，可复用类条件扰动方案，无需修改LLM权重即可快速抹去指定话题/用户的历史记忆，避免重训带来的性能波动

  - 动态迭代的推荐系统中，对过时/违规内容的快速下线需求，可参考ERASE的选择性遗忘逻辑，在排序模块输入层加定向扰动快速生效，时效性远优于重训方案'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有模型卸载（Unlearning）方案依赖事后权重调整、蒸馏或多副本存储，存在内存开销高、泛化性下降、扩展性差的问题，无法满足电商、社交等场景快速响应隐私删除合规的需求。
### 方法关键点
1. 提出ERASE（Erasure via Reconstructive Adversarial Signal Editing）框架，采用类条件结构化输入扰动策略，在推理阶段诱导模型选择性遗忘指定子类数据，完全不需要重训、微调或保存多份模型副本
2. 理论证明了在温和正则假设下，ERASE可实现指定子类的功能性遗忘，同时保留同大类下其他子类的预测效果，为推理时遗忘提供了可解释的理论支撑
### 关键结果
在多架构、多基准数据集上的测试表明，ERASE在遗忘有效性、计算效率、留存数据预测保真度三者的平衡表现优于近年所有基于显式卸载的遗忘方法，无额外模型存储开销，推理额外耗时可忽略。
