---
title: 'Attention Function as an Intrinsic Inductive Bias: How Models'' Behavior Diverges
  in Novel Contexts'
title_zh: 注意力函数作为内在归纳偏置：分布偏移场景下模型行为的分化规律
authors:
- Dong Gyun Kang
- Megha Thukral
- Kwangsoo Kim
affiliations:
- Georgia Institute of Technology
- Seoul National University Hospital
arxiv_id: '2609.39188'
url: https://arxiv.org/abs/2609.39188
pdf_url: https://arxiv.org/pdf/2609.39188
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: LLM架构优化 · 混合注意力激活
tags:
- Transformer
- Attention
- Inductive Bias
- Distribution Shift
- OOD Generalization
one_liner: 提出无参数混合函数注意力MoFA，验证注意力激活配比的归纳偏置仅在分布偏移下显现
practical_value: '- 做跨域推荐/多场景Agent时，可引入MoFA混合softmax/sigmoid注意力头，3个sigmoid头的配比域内效果与纯softmax完全一致，无性能损失即可提升OOD场景泛化能力

  - 业务场景可根据文本特征选激活配比：短文本搜索/用户评论理解保留高softmax占比，长商品说明书/法律条款/代码类内容理解提升sigmoid头占比，可获得最高28点perplexity下降

  - 多模态推荐场景下，可扩展MoFA思路给不同注意力头分配适配不同模态的激活函数，无需增加参数即可获得模态专属归纳偏置'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer的注意力激活函数默认全模型统一，现有研究普遍忽略不同激活的归纳偏置差异，且域内训练通常会掩盖架构偏置的效果，导致分布偏移（OOD）场景下泛化性能波动无规律，需明确激活选择对泛化能力的影响规律。

### 方法关键点
- 提出无参数的混合函数注意力（MoFA），训练前固定softmax和sigmoid注意力头的配比，无需新增参数，仅修改头级激活分配
- sigmoid头采用`-log t`偏移归一化保证输出量级与softmax对齐，所有头共享同一QKV投影矩阵，输出直接拼接后投影
- 头分配规则固定：每层前N个头为softmax，剩余为sigmoid，跨层统一配置，训练过程不调整

### 关键实验
- 训练124M参数GPT-2，预训练数据为OpenWebText，验证集为同分布OpenWebText，OOD测试覆盖15个领域（代码、学术文献、社交媒体、对话等）
- 基线为纯softmax注意力（12个softmax头），对比5种sigmoid头配比（0/3/6/9/12个）
- 域内效果：3个sigmoid头的配置与基线PPL完全一致（21.26），全sigmoid配置域内PPL仅上升0.53
- OOD效果：不同配比的PPL差异较域内放大10倍以上，学术文献领域全sigmoid配置较纯softmaxPPL下降28点；78.3%的领域性能差异可被「短非正式文本偏好softmax，长技术文本偏好sigmoid」单轴解释

### 核心结论
注意力激活函数的归纳偏置在域内训练时会被掩盖，仅在分布偏移场景下才会显著影响模型性能，没有通用最优的激活配比，需匹配下游场景的文本结构选择。
