---
title: 'How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length
  Generalization'
title_zh: 数据如何塑造RoPE频率使用：从位置尺度匹配到长度泛化
authors:
- Xinyi Wu
- Siyuan Liu
- Ali Jadbabaie
affiliations:
- MIT IDSS
- IIIS, Tsinghua University
arxiv_id: '2607.07678'
url: https://arxiv.org/abs/2607.07678
pdf_url: https://arxiv.org/pdf/2607.07678
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM位置编码 · RoPE长度泛化
tags:
- RoPE
- Position Encoding
- Length Generalization
- Position Interpolation
- Transformer
one_liner: 揭示RoPE频率与数据位置依赖的匹配规律，明确位置插值的生效条件
practical_value: '- 做电商用户长行为序列建模、长商品文案理解时，先统计业务数据的位置依赖宽度W，优先选择RoPE频率与1/W匹配的预训练模型，或调整初始频率，可快速提升长序列任务效果

  - 引入位置插值（PI）做长度扩展前，先判断业务场景的依赖结构是否自相似：用户浏览/搜索序列等依赖随长度同比例扩张的场景，用PI可低成本提升长序列推理性能；固定偏移类任务（如召回用户最近3次点击）使用PI反而会降效

  - 评估生成式推荐长序列方案的收益时，可先计算数据的自相似性，快速预判PI等长度扩展方法的效果，减少无效实验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RoPE是当前Transformer最常用的位置编码方案，但训练后模型对RoPE频率的使用极不均匀，此前高低频分别对应位置/语义的解释无法解释序列长度变化时频率带偏移的现象，且位置插值（PI）的生效机制不清晰，缺乏数据驱动的理论指导。

### 方法关键点
- 定义数据诱导的位置依赖核K(r)，用依赖宽度W刻画任务相关的最大相对距离，量化数据的位置依赖结构
- 形式化RoPE频率的视野-分辨率tradeoff：频率越高，位置分辨率越高但无歧义视野越窄，反之视野越宽分辨率越低
- 证明频率匹配原理：最优RoPE频率与依赖宽度W成反比，θ⋆≈π/W
- 提出PI的本质是频率视野扩张α倍同时分辨率降低α倍，仅当长序列依赖是训练序列依赖的拉伸版本（自相似性）时PI生效

### 关键结果数字
在块结构合成数据上，测得有效频率与块宽度W的拟合系数c=3.02，与理论值π高度吻合；在iGSM数学题数据集上，依赖宽度随运算数从2升到10时，RoPE有效频率持续向低频偏移；合成检索任务验证，自相似场景下PI可将长度泛化准确率提升至接近训练集水平，非自相似算术任务下PI准确率下降超40%。

最值得记住的一句话：RoPE频率选择本质是训练数据位置依赖结构的映射，长度泛化的核心是频率尺度与依赖结构尺度的双重匹配。
