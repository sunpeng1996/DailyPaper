---
title: 'DPMA: Learning to Compress Mixture-of-Experts Models'
title_zh: DPMA：面向混合专家模型的可学习压缩框架
authors:
- Jon Irureta
- Jon Imaz
- Philipp Wiesner
- Gorka Azkune
- Javier Fernandez-Marques
- Alex Iacob
- Andrej Jovanović
- Aizea Lojo
- Nicholas D. Lane
affiliations:
- Ikerlan Technology Research Center
- University of the Basque Country UPV/EHU
- University of Cambridge
- HiTZ Basque Center for Language Technology
- Flower Labs
arxiv_id: '2611.27759'
url: https://arxiv.org/abs/2611.27759
pdf_url: https://arxiv.org/pdf/2611.27759
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: MoE压缩 · 免重训梯度优化
tags:
- MoE
- Model Compression
- Pruning
- Merging
- Gradient Descent
one_liner: 免重训联合优化剪枝/合并/吸收操作与跨层专家预算，实现MoE高效高精度压缩
practical_value: '- 业务中使用MoE架构LLM做推荐文案生成、用户意图理解、搜索Query改写时，可直接复用DPMA做免重训压缩，75%专家削减下精度领先基线最高6.7pp，适配端侧/边缘部署需求

  - 压缩架构设计可借鉴：放弃传统每层固定压缩比的思路，采用全局专家预算分配+梯度自动选择剪枝/合并/吸收操作组合，适配不同层的压缩敏感度，降低精度损失

  - 校准成本极低，仅需32条1024token的通用语料即可完成优化，无需业务域标注数据，落地门槛低

  - 实时推荐等低延迟场景可选择DPMAhard变体，保证单token激活专家数不超过原模型，精度仍优于所有现有压缩基线'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE架构可在单token计算量恒定的前提下大幅提升模型容量，是当前大模型落地的主流选择之一，但所有专家需全部驻留显存，极大限制了其在资源受限硬件上的部署；现有免重训MoE压缩方法普遍提前固定采用剪枝或合并操作，且采用每层统一压缩比，未考虑不同层的压缩敏感度差异，精度损失较高。
### 方法关键点
- 定义三种可组合的压缩操作：剪枝（丢弃专家参数与路由槽）、合并（将专家参数合并至保留专家后丢弃原参数）、吸收（丢弃专家参数但保留路由槽，路由权重转发至保留专家）
- 通过可学习系数编码操作选择，采用梯度下降联合优化操作组合、跨层专家预算分配，全程冻结原模型权重，仅优化少量系数与分配矩阵参数
- 提供两种导出变体：DPMAhard将被移除专家的路由权重转发至单个保留专家，单token激活专家数不超过原模型；DPMAsoft转发至top3保留专家，精度更高
### 关键结果
在4个主流开源MoE模型（OLMoE-1B-7B、Qwen1.5-MoE-A2.7B、Qwen3-30B-A3B、DeepSeek-MoE-16B）上测试，对比7种现有压缩基线，覆盖5种压缩比、8个多选择基准任务：平均精度优于所有基线，75%专家削减下精度领先最强基线最高6.7个百分点，仅需32条1024token的C4通用语料即可完成校准。
### 核心结论
梯度下降可以同时学习MoE模型的压缩操作选择与压缩位置分配，免重训下即可实现远超人工设计策略的压缩效果。
