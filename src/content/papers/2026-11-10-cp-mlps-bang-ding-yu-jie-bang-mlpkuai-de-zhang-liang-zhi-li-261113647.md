---
title: 'CP-MLPs: A Tensor-Rank Theory of Tied and Untied MLP Blocks'
title_zh: CP-MLPs：绑定与解绑MLP块的张量秩理论
authors:
- Md Rifat Arefin
- Farzaneh Heidari
- Irina Rish
- Guillaume Rabusseau
affiliations:
- Mila – Quebec AI Institute
- Université de Montréal
arxiv_id: '2611.13647'
url: https://arxiv.org/abs/2611.13647
pdf_url: https://arxiv.org/pdf/2611.13647
published: '2026-11-10'
collected: '2026-11-12'
category: LLM
direction: LLM基础架构 · MLP块设计理论
tags:
- MLP
- Transformer FFN
- Tensor Rank
- Model Efficiency
- Structure Design
one_liner: 提出CP-MLP张量框架，量化绑定/解绑MLP块的表达效率差异与适用场景
practical_value: '- 推荐/广告模型FFN优化：针对用户-商品匹配等非对称特征交互场景，优先选用SwiGLU等解绑MLP块，相同参数预算下提升表达效率

  - 特征交互建模选型：用户购买力、商品热度等对称纯幂次特征场景，可选用ReLU²等绑定MLP块，降低参数冗余

  - 小参数模型优化参考：参数预算有限时，先分析业务特征交互的对称/非对称属性，选择匹配的MLP结构，避免盲目堆叠宽度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
Transformer FFN块占大模型约2/3参数，现有设计（平方激活、门控、参数绑定/解绑）的表达性贡献缺乏量化理论支撑，不同场景下的结构选型无明确依据。

### 方法关键点
提出CP-MLP张量框架，将每个乘法单元拆解为特征检测、值读取、输出写入3个秩1交互角色：绑定块（如ReLU²）强制检测与值角色共享方向，解绑块（如ReGLU、SwiGLU）允许二者独立。

### 关键结果
- 解绑单元对非对称单项式、不定二次交互的宽度效率显著更高，绑定单元更适配对称纯幂次目标
- 相同输入投影预算下，解绑块在指定任务上效果更优
- 低于精确表示宽度时的损失平台不代表存在近似gap，任意精度近似由边界秩决定
