---
title: Watermarkable Multi-Draft Speculative Sampling via Poisson Processes
title_zh: 基于泊松过程的可加水印多草稿推测采样算法
authors:
- Yanxiao Liu
- Sicheng Wan
- Zhan Gao
- Deniz Gündüz
affiliations:
- Imperial College London
- University of Washington
arxiv_id: '2609.21858'
url: https://arxiv.org/abs/2609.21858
pdf_url: https://arxiv.org/pdf/2609.21858
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM推理优化 · 可水印推测采样
tags:
- Speculative Sampling
- LLM Watermarking
- Poisson Process
- Inference Acceleration
- Drafter Invariant
one_liner: 提出基于泊松过程的多草稿推测采样方案，同时保推理效率、水印强度和输出分布无偏
practical_value: '- 电商场景用LLM生成商品文案、客服回复时，可直接复用该方案，加合规水印的同时不会损失Speculative Sampling的推理加速效果，无需额外平衡速度和溯源需求

  - 多版本小草稿模型迭代场景，利用其drafter invariant特性，替换草稿模型时大模型输出分布不变，避免业务侧生成效果波动，减少回归测试成本

  - 现有LLM生成内容管控链路可替换该方案，替换不同草稿模型时水印TPR@1%FPR漂移<1%，远优于现有方案的6%~22%漂移，溯源稳定性大幅提升

  - 做Agent服务部署时，该方案的无偏水印不影响生成内容质量，无需额外做内容通顺度校正，可直接对接现有推测采样部署架构'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM部署同时需要**Speculative Sampling**提升推理效率、**水印**实现输出可溯源，但现有研究证明二者存在固有trade-off：加水印会显著降低推测采样的token接受率，保效率则会削弱水印可检测性，且替换草稿模型时还会出现输出分布变化、水印信号漂移的问题，无法满足业务同时对速度、合规、稳定性的要求。
### 方法关键点
- 基于泊松函数表示（PFR）设计耦合采样逻辑，将水印嵌入耦合层而非后处理，保证输出分布和原生采样完全一致，无偏性不受水印影响
- 扩展为多草稿版本MPFR，利用泊松过程映射定理生成多个候选草稿并行验证，大幅提升token接受率
- 天然具备停止时间级drafter invariant特性：草稿模型仅影响生成速度，不影响最终输出的token分布和水印信号
- 水印基于密钥生成的泊松随机数嵌入，检测仅需密钥和输出序列，无需依赖草稿侧的中间信息
### 关键实验
在Qwen2.5-7B、Llama3.1-8B作为目标模型，同系列小尺寸模型作为草稿的配置下，在CNN/DAILYMAIL、ELI5数据集测试：
- 相同水印强度下，每步平均接受token数（AATPS）比现有基线高15%以上；多草稿B=8时AATPS最高达3.749，接近无水印原生多草稿推测采样的效率
- 替换不同尺寸/温度的草稿模型时，水印TPR@1%FPR漂移<1个百分点，远低于现有基线的6~22个百分点
- 水印强度和无推测采样的基础水印方案几乎一致，生成内容的困惑度、ROUGE-L无明显下降
### 核心结论
基于泊松过程的耦合采样可以打破推测采样和水印的固有trade-off，同时实现高推理效率、强水印可检测性和输出分布稳定性
