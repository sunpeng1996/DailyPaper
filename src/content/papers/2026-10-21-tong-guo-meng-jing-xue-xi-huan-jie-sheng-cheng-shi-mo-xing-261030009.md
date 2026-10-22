---
title: Mitigating Model Collapse through Dreaming Learning
title_zh: 通过梦境学习缓解生成式模型自训练的模型坍塌问题
authors:
- Matteo Benati
- Alessandro Londei
- Denise Lanzieri
- Raffaello Mastromarino
- Vittorio Loreto
affiliations:
- Sapienza University of Rome
- Sony CSL Rome
- CREF
- University of Copenhagen
- Complexity Science Hub Vienna
arxiv_id: '2610.30009'
url: https://arxiv.org/abs/2610.30009
pdf_url: https://arxiv.org/pdf/2610.30009
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: 大模型训练 · 模型坍塌缓解
tags:
- Model Collapse
- Dreaming Learning
- Spectral Analysis
- Regularization
- LLM Training
one_liner: 从转移算子谱特性视角验证高温度采样辅助的梦境学习正则可缓解自训练模型坍塌
practical_value: '- 生成式推荐/电商文案生成场景自迭代训练时，可引入Td>1的高温度自样本作为正则项，降低输出多样性丢失风险，避免推荐结果/文案趋同

  - 训练LLM驱动的电商Agent时，若需复用模型自生成的交互数据迭代，可加入梦境学习正则，缓解多轮迭代后的能力退化

  - 可复用谱分析方法监控生成式推荐模型的转移算子特征值变化，提前感知模型坍塌风险，无需等线上业务指标恶化

  - 参考调优范围：Td选1~3之间，正则系数α选0.3~1，小流量/小模型先做网格搜索再上全量，降低调参成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前网络合成数据占比持续升高，生成式模型常需在自身产出的合成数据上迭代训练，极易出现模型坍塌：输出多样性下降、性能退化。现有缓解方法以混合真实数据为主，但无法适配推理阶段常用的低于1的采样温度场景，也无法解决真实/合成数据无法区分的问题，且缺少从生成过程结构层面的坍塌机制解释。

### 方法关键点
- 从马尔可夫转移算子的谱特性切入分析坍塌：次主特征值越接近1、谱间隙越窄，模型探索状态空间的能力越差，越容易发生坍塌
- 梦境学习作为正则项：训练时并行加入模型自身在Td>1高温度下采样生成样本的交叉熵损失，总损失为常规真实数据损失加α倍的梦境损失
- 高温度采样可拉平模型输出分布，避免转移矩阵元素趋近于0，从而约束次主特征值远离1，维持谱间隙稳定

### 关键实验
覆盖三类场景：10状态马尔可夫链、4层LSTM语言模型、124M参数GPT-2，对比无梦境正则的vanilla自训练基线：
- 马尔可夫链场景：5000代训练后，最优参数（Td=1.5, α=0.8）下真实与重建分布的KL散度比基线低2个数量级，次主特征值无漂移
- GPT-2场景：15代自训练后，梦境学习组（Td=1.1, α=0.5）的验证困惑度为980，仅为基线1960的一半

### 核心结论
自训练时采样温度低于1是模型坍塌的核心诱因之一，引入高温度自样本正则可低成本维持生成多样性，大幅缓解退化
