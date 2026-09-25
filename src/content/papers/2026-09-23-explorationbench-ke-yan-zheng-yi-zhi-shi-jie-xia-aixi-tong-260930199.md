---
title: 'ExplorationBench: Measuring AI Systems'' Exploration in Verifiable Alien Worlds'
title_zh: ExplorationBench：可验证异质世界下AI系统探索能力评测基准
authors:
- Ming Zhang
- Zhenghao Xiang
- Peizhong Gao
- Yujiong Shen
- Yuhui Wang
- Zhonghan Yue
- Shihan Dou
- Zhangyue Yin
- Junjie Ye
- Shichun Liu
affiliations:
- Fudan University
- Hunyuan Team, Tencent
- Tsinghua University
arxiv_id: '2609.30199'
url: https://arxiv.org/abs/2609.30199
pdf_url: https://arxiv.org/pdf/2609.30199
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: Agent 未知环境探索能力评测基准
tags:
- Agent
- Exploration
- Benchmark
- Tool Calling
- Knowledge Discovery
one_liner: 构建反常识可验证异质环境基准，实现对AI自主探索与新知识获取能力的客观评测
practical_value: '- 做Agent探索能力评测时，可复用「构造反常识可执行规则环境」的思路，彻底规避预训练记忆对评测结果的干扰

  - 针对电商新类目探索、用户未知偏好挖掘等冷启场景，可参考本基准的多轨迹效果评估逻辑，量化探索策略的稳定性

  - 搭建领域探索型Agent时，可参考沙箱的配套设计：提供残缺领域文档、实时环境反馈、标准化工具调用入口，提升探索效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有AI探索能力评测存在两大核心痛点：一是无法验证全新假设的正确性，二是无法区分结果来自自主探索还是预训练知识记忆，缺乏客观可量化的统一评测框架。
### 方法关键点
1. 构建基于反常识、规则可执行Alien Worlds的评测基准，确保答案可精准校验、仅靠预训练记忆无法完成任务
2. 包含AlienCode（31个探索目标、70个任务）和AlienLogic（24个探索目标、70个任务）两个沙箱，配套残缺手册、任务专属环境反馈、工具调用schema，要求系统自主探索后完成held-out任务
### 关键结果
评测10款主流AI系统发现，最强系统可掌握并应用陌生规则，但不同探索轨迹的性能差异极大，持续探索可能出现性能停滞甚至较前期结果倒退的情况
