---
title: 'SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable
  Fine-Grained Specialization'
title_zh: 基于稀疏自编码器（SAE）的MoE大模型专家细粒度分工可解释方法
authors:
- Anyuan Zhuo
- Shaohua Zhang
- Yuan Lin
- Pinyan Lu
affiliations:
- ByteDance Seed
- Shanghai University of Finance and Economics
arxiv_id: '2611.08089'
url: https://arxiv.org/abs/2611.08089
pdf_url: https://arxiv.org/pdf/2611.08089
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: MoE大模型可解释 · SAE特征归因
tags:
- MoE
- Sparse AutoEncoder
- Interpretability
- Expert Specialization
- LLM
one_liner: 通过SAE分解MoE层输出，量化专家特征贡献，发现人类可理解的细粒度专家分工
practical_value: '- 业务侧若采用MoE架构LLM做推荐文案生成、电商Agent推理，可复用这套SAE归因方法，定位不同专家负责的业务场景（如商品属性生成、促销文案、客服应答），优化路由逻辑，降低推理延迟。

  - 训练MoE推荐/广告模型时，可借鉴细粒度专家分工结论，针对性将同业务域的细粒度任务分配给相邻专家，减少路由冲突，提升训练稳定性。

  - 做MoE模型部署剪枝时，可参考本文的贡献占比计算方法，仅保留对业务核心特征贡献高的专家，无需全量部署，有效降低推理成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE专家分工分析依赖人工预设的粗粒度域标签，仅能统计专家被选中的频率，无法衡量专家对输出的实际贡献，也无法发现模型自发学习到的细粒度分工，难以支撑MoE模型的优化、剪枝和可控编辑。

### 方法关键点
- 针对MoE层输出训练TopK SAE，学习模型自发形成的稀疏可解释特征空间，避免人工预设标签的局限
- 利用SAE编码器的仿射特性，将每个latent的激活精确分解为各活跃专家的贡献，聚合全量语料得到每个专家的贡献分布
- 设置阈值构建专家-特征主导关系图，通过大模型自动解释专家主导的latent集合，得到专家的细粒度分工标签

### 关键实验结果
在Qwen3-30B-A3B的第4、30、46层开展实验，每层128个专家，单token激活8个专家，训练SAE隐层维度2^20，验证集1.5B tokens：
1. 专家对latent的贡献集中度远高于路由权重，层30中贡献排名第一的专家占比达51.2%，而路由排名第一的仅23.1%
2. 超过56%的latent仅由1个专家主导，85%以上的latent由不超过2个专家主导；约40%的专家对的主导特征集无重叠，仅0.25%-0.57%的专家对重叠度超过0.05
3. 专家分工粒度远细于常规域标签，比如代码域下存在独立的Java专家、前端web专家，数学域下存在几何专家、算术多项式专家；128个专家自动聚为11个域，仅计算和数学推理两个域就占用了37.5%的专家资源

**最值得记住的一句话：** MoE专家的实际贡献与路由选择相关性很低，分工细粒度远超人工预设的域标签，资源分配与训练数据的域占比强相关。
