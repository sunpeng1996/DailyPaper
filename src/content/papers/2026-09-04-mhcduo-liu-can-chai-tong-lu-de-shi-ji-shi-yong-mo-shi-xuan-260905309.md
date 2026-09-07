---
title: How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity
  Mixing
title_zh: mHC多流残差通路的实际使用模式：选择性路由与近恒等混合
authors:
- Pengxiang Zhao
- Xing Li
- Xianzhi Yu
- Wei Guo
- Zhenhua Dong
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2609.05309'
url: https://arxiv.org/abs/2609.05309
pdf_url: https://arxiv.org/pdf/2609.05309
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: 大模型架构 · mHC多流残差通路分析
tags:
- mHC
- residual stream
- DeepSeek-V4
- inference optimization
- model efficiency
one_liner: 分析DeepSeek-V4-Flash的mHC多流使用模式，给出推理优化的低损方案
practical_value: '- 业务部署mHC结构大模型时，可直接将模型后半段（如43层模型的22层之后）的残差混合器替换为恒等映射，省去Sinkhorn-Knopp迭代开销，推理延迟降低的同时几乎无损效果

  - 低延迟场景（如电商实时推荐的LLM调用、Agent实时决策）可对读写路由做剪枝，每个token仅保留top3权重，PPL上升不超过2.7%，下游任务掉点不到0.4个百分点，大幅降低计算量

  - 定制多流残差架构的业务小模型时，无需全层配置动态残差混合器，仅在前半层保留动态混合、后半层用恒等映射即可，可同时降低训练开销和推理延迟'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多流残差架构mHC通过约束残差混合器为双随机矩阵，大幅提升了大模型训练稳定性和有效容量，但训练后模型如何实际利用多流能力的机制尚不明确：路由是集中还是分散、跨流混合的强度随深度如何分布、多流表征是否存在冗余，此前小模型上的结论是否适用于大规模工业级mHC模型也未验证，只有实测量化其使用模式才能针对性做架构优化和推理提速。
### 方法关键点
- 分析对象为284B参数的DeepSeek-V4-Flash MoE模型，其骨干采用4流mHC架构，共43层，覆盖86个注意力/FFN观测位点
- 设计三个核心量化指标：有效流数（衡量路由分配的集中度）、残差恒等偏差（衡量跨流混合的强度）、流间余弦相似度（衡量多流表征的独立性）
- 采用无重训推理干预验证功能冗余：路由稀疏化（保留top-k权重后缩放保证总权重不变）、残差混合器替换（替换为恒等矩阵或数据集上的统计均值）
### 关键实验结果
- 数据集：C4语料做困惑度评估，ARC、PIQA、HellaSwag、MMLU、GSM8K等6个零样本任务做下游效果验证
- 典型注意力/FFN层的有效流数仅约2个，87%以上的token共享同层的同一个主导流，流间表征余弦相似度平均仅0.4，不存在表征坍塌
- 22~42层的残差混合器接近恒等，直接替换为恒等矩阵仅提升C4 PPL 1.9%，下游6任务平均得分反而微涨0.04个百分点；0~21层替换为恒等矩阵则PPL上涨41%
- 每层每个token仅保留top3读写路由权重，PPL最多上涨2.7%，下游得分最多下降0.38个百分点；早期残差混合器固定为C4上的统计均值，PPL仅上涨0.2%，下游得分下降0.25个百分点
### 核心结论
mHC多流架构的容量存在结构化冗余而非均匀利用，优化时需按层区分处理，无需盲目保留全部动态计算能力
