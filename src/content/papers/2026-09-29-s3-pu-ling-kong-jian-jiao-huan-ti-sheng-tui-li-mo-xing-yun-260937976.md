---
title: '$S^3$: Spectral Null-Space Swap Makes Reasoning Models Efficient'
title_zh: S³：谱零空间交换提升推理模型运行效率
authors:
- Hongbo Ma
- Sansheng Cao
- Jiajun Fan
- Bangji Yang
- Ge Liu
affiliations:
- University of Illinois Urbana-Champaign
- Tsinghua University
- Dartmouth College
- Peking University
arxiv_id: '2609.37976'
url: https://arxiv.org/abs/2609.37976
pdf_url: https://arxiv.org/pdf/2609.37976
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM无训练合并 · 高效推理优化
tags:
- Spectral Decomposition
- Model Merging
- Efficient Reasoning
- Chain-of-Thought
- MoE
one_liner: 无需训练的谱零空间交换方法融合基础与推理模型，降低推理token开销同时提升精度
practical_value: '- 针对业务中同时部署通用基础LLM和垂直领域微调LLM的场景，可复用S3的谱分解思路，仅保留微调模型在基础模型零空间的差异分量，无需额外训练即可同时保留基础模型的高效性与微调模型的垂直能力，大幅降低推理token开销

  - 电商/推荐场景下的Agent决策推理、用户意图理解、复杂Query解析模块，可采用该方法对CoT微调后的推理模型做轻量化，平均减少27%左右的token生成量，同时维持甚至提升推理准确率，降低交互延迟与推理成本

  - 注意力熵可作为推理效率的可解释性指标，业务侧可通过监控模型推理时的注意力熵变化，提前判断模型生成冗余token的概率，用于动态截断或推理路由的阈值判定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
CoT训练的推理LLM虽然推理能力突出，但生成token开销极高，现有优化方法多在主谱空间操作，难以兼顾精度与效率，如何在不额外训练的前提下降低推理模型的token开销同时维持精度，是大模型落地电商、Agent等业务场景的核心痛点。

### 方法关键点
- 发现基础非推理模型主谱空间内的微调权重差异参数能量高但功能影响极弱，推理能力核心来自于基础模型主谱空间之外的零空间权重分量
- 提出S3无训练合并方法：对基础模型权重做SVD分解，保留基础模型在主谱空间的权重，零空间部分直接替换为推理模型的对应权重，仅需超参数ρ控制主谱空间占比，默认ρ=0.8效果最优
- 构建探针家族验证分量贡献：仅保留零空间差异的Null模型效果接近全量推理模型，仅保留主谱空间差异的Sub模型效果接近基础模型

### 关键实验
在2B-30B的密集模型与MoE模型上，覆盖文本、多模态、音频等28个推理基准，对比基础模型、全量推理模型、TIES合并、MI-0.8插值等基线：平均比全量推理模型减少27.4%的token开销，同时整体精度提升1个百分点；HMMT25数据集上精度提升8.3%同时token减少33%，MathVista数据集上精度达78.05%同时token减少31.9%。

**最值得记住的一句话**：大模型微调带来的新增能力，绝大多数存在于基础模型的谱零空间中，仅迁移这部分即可实现无训练的高效能力融合。
