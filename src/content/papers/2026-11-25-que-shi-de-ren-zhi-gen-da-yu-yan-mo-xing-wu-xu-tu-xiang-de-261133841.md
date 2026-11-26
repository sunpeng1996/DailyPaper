---
title: 'The Missing Root: Geometric Imagination Without Images in Large Language Models'
title_zh: 缺失的认知根：大语言模型无需图像的几何想象能力实现
authors:
- Loïc Magnan
- Tomasz Kozlowski
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.33841'
url: https://arxiv.org/abs/2611.33841
pdf_url: https://arxiv.org/pdf/2611.33841
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM 非视觉空间推理能力增强
tags:
- LLM
- Spatial Reasoning
- Parameter Efficient Fine-tuning
- Workspace Memory
- Geometric Understanding
one_liner: 为Qwen3-1.7B添加4.4%参数的并行空间流 实现无图像无外部工具的连续空间几何推理
practical_value: '- 做具身Agent/电商虚拟场景搭建（虚拟试搭、直播间布局）时，可复用轻量并行空间流方案，仅加少量参数就为LLM注入空间感知能力，无需依赖复杂多模态模块

  - 做多步推理类任务（长链路商品推荐、用户行为轨迹推理）时，可借鉴<LOOK>注意力掩码机制，强制模型从指定持久化工作区读取信息，避免文本短路径作弊，提升推理可信度

  - 做商品属性理解（形状、尺寸推理）时，可复用从预训练LLM隐式知识挖掘物理属性的方案，仅用少量标注的名词-形状对就能泛化到未见过的商品名词，大幅降低标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM仅处理离散文本，缺乏连续空间的直接表示能力，依赖视觉输入的多模态方案会丢失精确位姿信息，也无法处理纯文本输入的空间推理场景；而人类的空间感知本身不需要视觉成像（先天盲人、失语症患者也可完成空间任务），因此需要为LLM注入不依赖图像的几何理解能力。

### 方法关键点
- 设计连续对象token，融合位姿（坐标、旋转、缩放）与有向距离形状嵌入，和文本token共享Transformer输入序列，实现语言与几何信息双向注意力交互
- 新增5个控制token切换输出模态，配套持久化对象工作区存储连续对象状态；<LOOK>掩码强制推理时屏蔽之前的所有文本，只能从工作区读取空间状态，避免文本短路径作弊
- 仅在Qwen3-1.7B每层旁加256维并行空间流，总新增参数仅4.4%，交叉投影初始化为0，保证原LLM的文本能力不受破坏
- 仅用2840个手工标注的名词-形状对训练，即可利用预训练LLM的隐式知识泛化到未见过的名词的形状推理

### 关键结果数字
- 纯文本无坐标空间布局任务，训练过的名词准确率100%，未见过的名词准确率99%；<LOOK>工作区清零/随机化后准确率降到随机水平（~50%），证明模型确实依赖空间工作区推理
- 未见过的名词形状生成IoU达0.79，基础形状匹配准确率74%
- 多步空间推理任务整体准确率71%，和直接输入正确工作区状态的70%基本持平，多步更新无精度损失
- 原文本能力保留较好，WikiText-2困惑度仅从16.38升到18.72，无控制token误生成

### 最值得记住的一句话
预训练LLM本身已经存储了大量隐式的物理世界知识，仅需添加极少量参数和轻量监督，就能将这些隐性知识显式化为可操作的连续空间表示，不需要依赖大量视觉数据。
