---
title: EVEREST:Endogenous Vision-Language Reinforcement Reasoning Exploration for
  Urban Socio-Semantic Segmentation
title_zh: EVEREST：面向城市社会语义分割的内生视觉语言强化推理模型
authors:
- Qixiu Li
- Zhongzhi He
- Xiang Zhu
- Xiaoyong Li
- Jiarun Lin
- Weifeng Xu
affiliations:
- National University of Defense Technology
- Changchun University of Science and Technology
arxiv_id: '2608.24640'
url: https://arxiv.org/abs/2608.24640
pdf_url: https://arxiv.org/pdf/2608.24640
published: '2026-08-25'
collected: '2026-08-30'
category: Other
direction: 多模态语义分割·强化推理
tags:
- Vision-Language Model
- Reinforcement Learning
- Semantic Segmentation
- Multimodal Reasoning
- Active Exploration
one_liner: 提出融合主动边界探索、伪代码规则、强化学习的跨模态语义分割模型，解决边界识别不准问题
practical_value: '- 可借鉴将离散自然语言prompt转伪代码的思路，规范化LLM执行逻辑，降低推理结果随机性，可用于推荐场景prompt工程、Agent执行规则定义

  - 主动探索难例+自修正的强化学习框架可迁移到推荐/广告的边界样本（如冷启item、低质内容）识别优化场景，提升bad case处理能力

  - 跨模态信息被动聚合转主动探索的思路可用于多模态推荐的用户兴趣挖掘，提升细粒度兴趣边界的识别精度'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有城市社会语义分割方法依赖被动聚合的全局跨模态线索，缺乏环境主动探索能力，存在目标边界划分不准确的缺陷，无法支撑城市资源分配、AOI管理、15分钟城市规划等下游场景对高精度实体边界的需求。
### 方法关键点
1. 采用以自我为中心的探索策略，支持模型主动挖掘边界线索并完成自修正；
2. 将离散自然语言prompt封装为伪代码，约束模型执行逻辑，降低推理过程的随机性；
3. 引入强化学习实现完整推理流程，激发模型结构化推理能力。
### 关键结果数字
在真实城市社会语义分割数据集上所有评估指标均达到最优，性能显著超过现有基线方法。
