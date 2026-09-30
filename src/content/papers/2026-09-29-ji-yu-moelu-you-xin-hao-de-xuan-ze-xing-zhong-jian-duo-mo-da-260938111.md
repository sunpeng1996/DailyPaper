---
title: 'From Routing Signals to Selective Review: Visual regrounding in MoE VLMs'
title_zh: 基于MoE路由信号的选择性重检：多模态大模型视觉接地优化
authors:
- Hongzhu Guo
- Mohsen Fayyaz
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- Peking University
arxiv_id: '2609.38111'
url: https://arxiv.org/abs/2609.38111
pdf_url: https://arxiv.org/pdf/2609.38111
published: '2026-09-29'
collected: '2026-09-30'
category: Multimodal
direction: 多模态大模型 · MoE路由信号利用
tags:
- MoE
- VLM
- Visual Grounding
- Hallucination Detection
- Selective Review
one_liner: 利用MoE VLM内部路由信号预检测目标缺失，触发选择性重检提升视觉接地准确率
practical_value: '- 电商多模态商品问答、直播内容审核场景可直接复用该思路：无需修改MoE VLM权重，仅通过路由特征的轻量线性探针即可预检测query涉及的目标商品/元素是否缺失，避免编造属性的幻觉问题

  - 选择性干预架构可迁移到高并发推荐/搜索场景：仅对探针判定高风险的样本触发重检prompt，相比全量走校验流程可减少至少40%的额外推理成本，兼顾效果和效率

  - 跨域落地可参考阈值校准方案：路由信号的排序能力跨场景稳定，仅需要少量目标域标注做阈值校准，无需重训探针即可实现业务场景快速冷启动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
MoE架构视觉语言模型（VLM）普遍存在目标缺失接地错误：当用户询问图像中不存在的物体属性时，模型会接受虚假前提编造答案，现有检测方案要么依赖生成后结果、额外视觉校验模型，要么全量触发重检推理成本过高，而MoE路由过程本身产生的计算分配信号尚未被挖掘用于感知校验。
### 方法关键点
- 自动提取query中目标名词短语对应的token跨度，拼接所有MoE层的路由概率得到层-专家维度的特征向量
- 训练L2正则化线性探针做目标存在性二分类，全程不修改VLM任何权重或路由参数
- 探针得分超过阈值时触发目标感知重检prompt，要求模型显式验证目标存在性，否则走标准生成流程
### 关键结果
在GQA-Inpaint数据集上，Qwen3-VL-30B、Gemma-4-26B的路由探针ROC-AUC分别达0.9988、0.9956，跨域到OBER数据集仍保留0.8095、0.7781的AUC；触发选择性重检后，Qwen在两个数据集上的端到端准确率分别提升22.25pp、12.17pp，Gemma对应提升13.42pp、1.39pp，假阳性触发导致的正确回答转错误率低于8%。
### 核心结论
MoE模型内部已有的路由信号编码了丰富的感知状态信息，仅需轻量线性探针即可挖掘高价值风险信号，无需修改模型就能实现低成本性能优化。
