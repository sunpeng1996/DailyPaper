---
title: Rethinking Projector Training in Multimodal LLMs
title_zh: 多模态大语言模型投影层训练的重新思考
authors:
- Fabian Gröger
- Naël Ouerghemi
- Shuo Wen
- Maria Brbić
affiliations:
- EPFL
- University of Basel
- HSLU
arxiv_id: '2610.18598'
url: https://arxiv.org/abs/2610.18598
pdf_url: https://arxiv.org/pdf/2610.18598
published: '2026-10-12'
collected: '2026-10-15'
category: Multimodal
direction: 多模态LLM · 无训练投影层初始化
tags:
- Multimodal-LLM
- Projector Alignment
- Optimal Transport
- Training-free
- PCA
one_liner: 提出无需配对数据的PORTAL投影层初始化方案，跳过预训练仍匹配甚至超过标准基线性能
practical_value: '- 做多模态商品理解、商品图文内容生成的业务，可直接用PORTAL跳过投影层配对预训练，省去大量图文配对数据收集成本和训练算力，尤其适合缺乏标注数据的垂类场景

  - 若需进一步微调投影层，采用PORTAL初始化可减少135倍预训练FLOPs，仅需约4k配对样本即可达到558k样本训练的基线性能，大幅降低模型迭代周期和成本

  - 跨模态特征对齐的思路可迁移到搜索推荐场景：将用户行为特征、商品多模态特征对齐到LLM输入空间时，无需配对训练，仅通过统计特征做最优传输映射即可快速上线验证

  - OCR类场景（如商品包装文字识别、小票信息提取、单据解析）不建议完全跳过配对预训练，这类任务依赖细粒度空间特征，PORTAL的统计匹配存在性能缺口，需补充少量配对数据微调'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多模态LLM的标准训练流程需先在大规模图文配对数据集上训练投影层，对齐视觉编码器与LLM的特征空间，但该阶段的实际作用缺乏清晰认知，不同研究结论冲突，且配对数据标注成本高、训练算力消耗大，亟需更高效的对齐方案。
### 方法关键点
- 先通过实验验证投影层训练本质是粗粒度分布对齐：仅需10~20%的标准配对数据即可恢复大部分下游性能，不同数据集训练的投影层线性插值后性能几乎无下降，说明投影层的有效解空间极宽
- 提出PORTAL无训练投影层初始化方案：分别计算视觉特征和LLM输入特征的均值、Top-k PCA主方向与对应方差，通过Bures-Wasserstein最优传输构造闭式映射，直接得到投影层参数，无需任何配对数据和梯度优化
### 关键实验
- 覆盖7组（视觉编码器+LLM）组合（包括LLaMA、Qwen、Vicuna等，参数规模0.5B~8B），在16个下游基准上测试
- 无需任何配对数据的PORTAL平均达到558k配对数据训练基线的98%性能，其中3组配置超过基线，最高达到基线得分的106.2%
- 作为初始化使用时，仅需4k配对样本即可达到558k样本训练的基线性能，减少135倍预训练FLOPs

最值得记住的一句话：多模态LLM的投影层对齐核心是特征分布的几何匹配而非细粒度语义学习，大部分场景下完全可以用无训练的统计匹配替代昂贵的配对预训练。
