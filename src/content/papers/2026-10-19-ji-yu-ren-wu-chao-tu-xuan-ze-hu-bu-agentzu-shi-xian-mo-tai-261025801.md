---
title: Learning Complementary Agent Groups via Task Hypergraphs for Next-POI Recommendation
  with Missing Modalities
title_zh: 基于任务超图选择互补Agent组实现模态缺失下的下一跳POI推荐
authors:
- Jinze Wang
- Yuze Liu
- Liang Yuan
- Gaoyuan Du
- Xiaohang Xu
- Yong Xiang
- Jiong Jin
affiliations:
- Swinburne University of Technology
- Australian Catholic University
- University of Tennessee
- University of Tokyo
- Deakin University
arxiv_id: '2610.25801'
url: https://arxiv.org/abs/2610.25801
pdf_url: https://arxiv.org/pdf/2610.25801
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 多Agent推荐 · 模态缺失下POI推荐
tags:
- MultiAgent
- POI-Recommendation
- Hypergraph
- Missing-Modality
- LLM-Agent
one_liner: 提出任务超图驱动的互补Agent组动态选择框架解决多模态缺失下的POI推荐问题
practical_value: '- 多模态缺失场景可复用分角色Agent+动态编组设计：每个Agent对应单一模态/分析能力（如文本、轨迹、偏好），按需编组适配单请求的模态可用情况，比固定多模态融合架构鲁棒性更强

  - 任务超图的编组逻辑可迁移：通过Set Transformer编码已选Agent能力，动态补充互补角色，避免能力重叠浪费算力，同时用PPO优化编组策略兼顾效果和计算成本，适配在线推荐的预算控制需求

  - 多Agent结果融合可参考统一状态更新+共享排序头设计：所有Agent输出统一更新候选表示和请求状态，共享排序头输出最终得分，避免多Agent独立打分的校准问题，降低融合复杂度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
下一跳POI推荐高度依赖用户轨迹、POI文本/图像等多模态信号，但实际场景中POI内容模态经常缺失，传统固定架构的多模态推荐模型性能会出现明显下降；现有LLM-Agent推荐方案多采用单Agent顺序调用或固定专家组，无法根据单请求的可用模态、用户特征动态选择互补的分析能力，存在能力冗余或不足的问题，也难以平衡效果和计算成本。

### 方法关键点
- 设计6个固定角色的Agent：分别负责长期偏好、短期轨迹、时空分析、文本分析、视觉分析、协同检索，每个Agent用冻结LLM+角色专属LoRA实现，降低训练成本
- 提出任务超图表示：每个任务（全池上下文更新、候选对比、模态缺失补偿）对应一条超边，动态选择互补Agent组作为超边节点，基于Set Transformer编码已选Agent能力，逐步补充成员直到满足任务需求
- 执行阶段Agent共享中间结果引导后续操作，完成任务后统一更新候选表示、请求状态和Agent记忆，所有任务结果通过共享排序头输出对基础排序的修正值
- 训练分两阶段：先监督训练执行器和排序头，再冻结执行器用PPO优化任务选择、Agent编组和停止策略，同时加入计算成本惩罚实现效果-成本权衡

### 关键实验
在Gowalla-CA、Foursquare-NYC、Foursquare-TKY三个公开POI数据集自然模态缺失条件下，对比SOTA基线HyperAgent4POI，NDCG@20相对提升8.4%~9.1%；在50%联合模态缺失的极端场景下仍保持2.6pp的NDCG@20绝对提升，可通过预算参数灵活调整效果与latency tradeoff，高预算下p50 latency约156ms。

**最值得记住的一句话**：多Agent推荐的核心不是堆砌Agent能力，而是根据单请求的任务、可用数据动态编组互补能力，通过统一状态共享和融合降低复杂度，同时兼顾性能与成本。
