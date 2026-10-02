---
title: 'Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation'
title_zh: 邻域在线策略自蒸馏：挖掘参数邻域的互补监督信号
authors:
- Xincheng Wei
- Yifan Ding
- Yoshua Li
- Yuquan Lu
- Ziheng Li
- Yi Lu
- Dongsheng Ma
- Rongxiang Weng
- Xunliang Cai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Meituan
- Peking University
- University of Toronto
arxiv_id: '2609.39687'
url: https://arxiv.org/abs/2609.39687
pdf_url: https://arxiv.org/pdf/2609.39687
published: '2026-09-29'
collected: '2026-10-02'
category: Training
direction: LLM蒸馏 · 在线自蒸馏优化
tags:
- Self-Distillation
- On-Policy Training
- Knowledge Distillation
- Perturbation Expert
- LLM Reasoning
one_liner: 构建参数扰动专家池与状态级路由，无需额外推理成本提升OPSD的数学推理性能
practical_value: '- 做LLM微调/蒸馏场景（如生成式推荐prompt微调、Agent推理模型蒸馏）时，可直接复用扰动专家池思路：无需引入异构大模型作为教师，仅对单一base模型施加小参数扰动即可生成互补监督信号，推理仅用学生模型无额外成本

  - 多专家路由方法可迁移到多专家推荐、多工具Agent调度场景：先选最高置信度的锚定方向，再在该方向的匹配专家中选择合适分位的输出，平衡信号强度与泛化性

  - SCGate低置信过滤trick可直接落地：蒸馏/SFT时仅对模型输出置信度低于阈值的位置施加监督，既节省训练资源，又避免过拟合高置信的正确样本

  - 专家选择优先考虑边际增益而非独立排名：做召回池构建、多专家融合时，优先选择能补充现有池子覆盖盲区的候选，而非单独效果最优的候选，提升整体性价比'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
标准OPSD仅使用单一固定参数的特权教师提供监督，无法挖掘同一base模型参数邻域内的互补监督信号，限制了蒸馏效果上限；现有多教师蒸馏方法多依赖异构大模型或独立排名选专家，未考虑专家冗余，训练成本高且增益有限。
### 方法关键点
- 离线专家选择：对base特权教师施加小高斯扰动生成大量候选专家，基于参考前缀的过滤后正教师优势（PTA），用贪心算法选择边际增益最高的K个专家构建紧凑池，通过SCGate过滤高置信位置、裁剪过强峰值，避免无效监督
- 在线动态路由：对每个学生访问的状态，用MaxPeak取所有专家输出的最高概率token为锚，在top1输出与锚一致的专家中选择q分位的专家，用其全词表分布作为监督信号
- 训练优化：配合SCGate仅对学生低置信位置计算裁剪后的正向KL损失，推理仅使用蒸馏后的学生模型，无额外开销
### 关键结果
在AIME2024、AIME2025、HMMT 2025三个数学推理benchmark上测试，对比OPSD、EOPD、PW-OPSD等基线，N-OPSD在Qwen3-1.7B、4B、8B上的三数据集Average@12分别提升2.75、1.67、1.94个百分点；K=25的专家池仅带来42%的训练步长增加，无推理开销。
> 最值得记住的话：单一base模型的参数邻域内天然存在大量互补监督信号，无需引入额外大模型即可通过蒸馏大幅提升学生性能，且无推理额外成本
