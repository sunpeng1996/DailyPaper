---
title: 'Less from More: Reinforcing Sparse Video Reasoning from Dense References'
title_zh: 少即是多：基于密集参考强化稀疏视频推理能力
authors:
- Wenfang Sun
- Yingjun Du
- Cees G. M. Snoek
affiliations:
- University of Amsterdam
arxiv_id: '2610.10893'
url: https://arxiv.org/abs/2610.10893
pdf_url: https://arxiv.org/pdf/2610.10893
published: '2026-10-06'
collected: '2026-10-12'
category: Multimodal
direction: 多模态视频推理 · 稀疏帧优化
tags:
- VideoReasoning
- SparseInference
- ReinforcementLearning
- MultimodalLLM
- KnowledgeDistillation
one_liner: 提出SAVER稠密到稀疏后训练框架，仅用1250个时序标注实现稀疏帧推理追平稠密帧Qwen3.5基线
practical_value: '- 可复用「稠密帧训练蒸馏到稀疏帧推理」的范式，在电商短视频/直播内容理解场景下，用高FPS样本训练低FPS推理模型，最高可降75%推理算力成本

  - 仅需少量时序定位标注即可迁移到通用视频理解任务的经验，可用于低资源多模态召回特征优化，减少标注成本90%以上

  - 三类奖励联合的强化蒸馏策略，可复用在跨模态小模型蒸馏场景，避免稀疏输入下的任务性能掉点'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频语言模型默认输入时序帧越多推理越可靠，但稠密帧推理算力成本极高，核心瓶颈并非提升稠密帧处理效率，而是如何在有限时序输入下保障推理精度。
### 方法关键点
提出SAVER稠密到稀疏后训练框架，训练阶段用稠密视频帧作为参考，仅需1250个随机采样的时序定位标注样本，无需任何视频QA标注；优化时结合接地奖励、可靠性门控参考奖励，约束稀疏帧预测保留任务相关的时序证据。
### 关键结果数字
在3个时序定位基准、6个视频QA基准上，所有帧预算区间性能均稳定提升；仅用远少于基线的输入帧，即可追平甚至超过稠密帧Qwen3.5基线的性能。
