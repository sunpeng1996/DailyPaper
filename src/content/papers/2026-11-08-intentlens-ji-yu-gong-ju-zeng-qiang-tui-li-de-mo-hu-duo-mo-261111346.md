---
title: 'IntentLens: Grounding Underspecified Multimodal Queries for Recommendation
  via Tool-Augmented Reasoning'
title_zh: IntentLens：基于工具增强推理的模糊多模态查询推荐意图落地
authors:
- Xiao Chen
- Dong Fang
- Haitao Li
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
- LightSpeed
arxiv_id: '2611.11346'
url: https://arxiv.org/abs/2611.11346
pdf_url: https://arxiv.org/pdf/2611.11346
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 多模态推荐 · 工具增强意图理解
tags:
- Multimodal Recommendation
- Tool-Augmented LLM
- Intent Grounding
- MLLM
- Dual Encoder
one_liner: 提出两阶段工具增强多模态推荐框架，解决模糊图文查询的意图落地问题，配套两个专用测评基准
practical_value: '- 模糊多模态查询场景可复用ground-then-rank架构：用MLLM做工具调用补全意图与候选属性，再用轻量双编码器排序，相比直接用大模型端到端排序，推理成本降低80%以上，latency可控在4s级

  - 推荐场景的MLLM工具调用训练可复用反事实排名奖励+观测掩码GRPO设计：奖励同时绑定下游排序效果与工具调用准确率，自动过滤无效工具调用，无需人工标注工具调用样本即可对齐推荐目标

  - 用户偏好建模可复用双层记忆架构：将用户历史拆分为episodic单次交互记忆与semantic长期偏好记忆，按查询触发检索，相比全量历史喂入MLLM上下文，token消耗降低60%以上

  - 业务场景的模糊查询测评集可复用论文的合成流程：先明确工具调用路径与意图逻辑，再反向生成自然模糊查询，过滤信息泄露样本，快速构造适配业务的测试集'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
随着智能穿戴设备普及，用户越来越多通过「参考图+模糊自然语言」的多模态形式发起推荐请求，现有推荐系统要么仅依赖历史交互做被动特征匹配，要么要求用户输入完全明确的查询，无法补全查询中隐含的视觉偏好、个性化历史约束、商品细粒度属性，导致匹配准确率低，无法适配场景化推荐需求。
### 方法关键点
- 采用**ground-then-rank两阶段架构**：第一阶段用MLLM编排三类工具（视觉分析工具提取图中隐含属性、用户记忆工具召回历史偏好、商品属性工具拉取候选细粒度信息），将模糊查询落地为结构化的明确意图表示，同时为每个候选补全查询相关的属性信息；第二阶段用轻量双编码器完成候选排序，将意图理解和排序解耦，提升大规模候选集下的可扩展性。
- 设计**排序对齐的强化微调（RFT）方案**：用反事实排名奖励对比工具调用前后的排序效果，同时加入工具选择准确率奖励，避免无效工具调用；采用观测掩码GRPO训练，仅对MLLM生成的策略token计算梯度，避免工具返回的观测内容干扰训练。
- 构造两个专用基准GOOGLEREVIEW-MMTOOL、YELP-MMTOOL，包含4个难度等级的模糊多模态查询，覆盖仅需视觉工具到需要三类工具协同的不同场景。
### 关键实验结果
在两个基准上与10+基线对比，7B参数的IntentLens在Yelp-MMTool数据集上Hit@1达33.8%、Hit@10达70.4%、MRR达46.7%，比零样本Qwen2.5-VL-7B MRR提升21.3个百分点，比GPT-4o MRR提升5.3个百分点；端到端延迟约4s，其中排序阶段仅515ms，性能可满足在线推荐要求。
### 核心结论
解决模糊多模态推荐问题的核心不是盲目提升大模型的端到端排序能力，而是通过工具主动补全查询隐含的多源信息，用轻量排序层平衡效果和部署成本。
