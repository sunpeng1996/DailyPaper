---
title: 'MTEB-PT: A Text Embedding Benchmark for Brazilian Portuguese'
title_zh: MTEB-PT：巴西葡萄牙语专用文本嵌入基准数据集
authors:
- Tardelli Ronan Coelho Stekel
affiliations:
- Federal Institute of São Paulo (IFSP)
arxiv_id: '2607.04581'
url: https://arxiv.org/abs/2607.04581
pdf_url: https://arxiv.org/pdf/2607.04581
published: '2026-07-06'
collected: '2026-07-08'
category: Eval
direction: 多语言文本嵌入评测基准构建
tags:
- Text Embedding
- Benchmark
- Multilingual
- Evaluation
- RAG
- Portuguese
one_liner: 构建包含22个原生巴西葡萄牙语任务的文本嵌入基准，评测93款模型并公开榜单与全量资源
practical_value: '- 布局葡语地区电商/搜索/RAG业务时，可直接参考MTEB-PT榜单选型本土适配的开源嵌入模型，无需调用商用API即可达到SOTA效果

  - 构建小语种/区域语言嵌入评测基准时，可复用「全原生语料、覆盖分类/检索/重排全场景、基于项目反应理论做任务区分度分析」的设计范式

  - 跨语言业务选型嵌入模型时，不能直接依赖全球多语言榜单排名，必须补充本土场景验证，避免排名偏差（如全球榜第3的模型在葡语榜排49）'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
巴西葡萄牙语覆盖2亿+原生用户，但此前无专用原生文本嵌入基准，评测依赖翻译语料或多语言基准的少量任务，模型选型可靠性低。

### 方法关键点
构建MTEB-PT基准，覆盖分类、语义相似度、检索、重排等7大类共22个全原生葡语任务，完全排除翻译生成的语料；评测93款参数从23M到27B的模型（73款开源、20款商用API），配套加入bootstrap置信区间、配对显著性检验、基于项目反应理论的任务区分度分析、跨榜单相关性分析等统计层。

### 关键结果数字
基准可清晰划分12个模型性能梯队，前6名性能无统计显著性差异；有开源可自部署模型跻身第一梯队，无需商用API即可获得顶级葡语嵌入效果；全球多语言榜单排名与葡语榜单排名相关性仅为Spearman ρ=0.75，存在明显偏差。
