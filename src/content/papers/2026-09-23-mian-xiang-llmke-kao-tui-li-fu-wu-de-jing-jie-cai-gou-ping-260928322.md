---
title: Learning the Cost of Reliable Inference
title_zh: 面向LLM可靠推理服务的竞价采购平台与成本优化机制
authors:
- Dimitrios Rontogiannis
- Ander Artola Velasco
- Manuel Gomez Rodriguez
affiliations:
- Max Planck Institute for Software Systems
arxiv_id: '2609.28322'
url: https://arxiv.org/abs/2609.28322
pdf_url: https://arxiv.org/pdf/2609.28322
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM服务 · 竞价定价机制
tags:
- LLM-as-a-Service
- Reverse Auction
- Multi-Armed Bandit
- Dynamic Pricing
- Quality Assurance
one_liner: 结合反向次价拍卖与多臂老虎机的LLM推理采购平台，保障质量阈值下实现最优市场定价
practical_value: '- 对大量调用LLM的电商/Agent业务（如文案生成、智能客服、推理链路），可复用该竞价框架对接多家LLM服务商，自定义任务质量阈值（如答案准确率、文案通顺度），动态选择最低成本的达标服务商，竞争充分场景下可降低10%+推理成本

  - 内部多供应商流量分配场景（如广告素材、UGC内容分发）可复用「质量置信度估计+成本优先分配」的多臂老虎机机制，平衡探索成本与长期ROI

  - 若做LLM路由类To B平台，反向次价拍卖的激励设计可直接复用，能激励服务商真实报价，避免恶意竞价与质量造假，保障供需双方利益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM推理服务市场普遍采用固定token定价模式，无法反映不同任务下各服务商的实际推理成本与输出质量差异，用户要么为达标服务支付超额溢价，要么为了低价牺牲输出质量；现有路由平台仅做性能排名，未引入竞价机制，存在显著的市场效率浪费。
### 方法关键点
- 采用反向次价拍卖机制：最终支付价格由第二低的达标服务商报价决定，与中标方自身报价无关，从机制上激励服务商真实上报自身推理成本，避免报价作弊
- 结合UCB多臂老虎机做服务商筛选：动态计算每个服务商的质量置信上界，仅保留满足用户指定质量阈值的服务商进入竞价池，高概率下不会遗漏合格服务商
- 分阶段路由：探索阶段均匀采样达标服务商积累质量与成本数据，利用阶段选择调整后报价最低的服务商，理论证明非最优服务商的分配占比随请求量增长趋近于0，平均支付价格最终收敛到达标服务商的第二低平均成本
### 关键实验
基于Llama、Qwen两个系列共9个模型，在GSM8K数学推理、GPQA科学问答两个公开基准上测试：竞争充分场景（GPQA）下，用户平均支付价格比公开固定定价低12%，服务商利润率仅10%；竞争不充分场景（GSM8K）下，服务商利润率最高达71%，反映固定定价的溢价空间；最终96%以上的请求会被路由到成本最低的达标服务商。
### 核心结论
当前LLM服务固定定价模式存在显著效率浪费，基于任务自定义质量阈值的动态竞价采购模式，在竞争充分的场景下可帮用户降低10%以上的推理成本。
