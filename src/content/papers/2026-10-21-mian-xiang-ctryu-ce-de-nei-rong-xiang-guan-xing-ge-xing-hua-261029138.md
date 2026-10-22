---
title: Progressive Learning from Content to Relevance to Personalization for CTR Prediction
title_zh: 面向CTR预测的内容-相关性-个性化三阶段渐进式学习框架FineSID
authors:
- Zhiguang Yang
- Yulin Yang
- Fuyu Lv
- Dan Ou
affiliations:
- Alibaba Group
arxiv_id: '2610.29138'
url: https://arxiv.org/abs/2610.29138
pdf_url: https://arxiv.org/pdf/2610.29138
published: '2026-10-21'
collected: '2026-10-22'
category: RecSys
direction: CTR预测 · 多模态语义ID渐进式训练
tags:
- CTR Prediction
- Semantic ID
- Multimodal
- Progressive Learning
- E-commerce Search
one_liner: 提出三阶段渐进式框架FineSID，通过细粒度Semantic ID融合多模态内容提升工业CTR预测效果
practical_value: '- 可复用多尺度视觉tokenizer+分域文本tokenizer的离散化方案，将多模态内容转成与原生ID格式兼容的Semantic
  ID，无需修改现有ID-based CTR模型架构即可融合语义信息，大幅降低落地成本

  - 可迁移三阶段渐进式训练流程：先做内容token化，再用LLM标注的相关性软标签预训练整个CTR backbone，最后微调个性化CTR任务，兼顾语义泛化性与个性化拟合能力，冷启动场景收益尤其显著

  - 多模态token提取可全离线执行，在线仅需新增ID lookup开销，无额外VLM推理延迟，适合工业级高吞吐排序场景落地，实测对推理延迟影响可忽略

  - 对于同品多创意的电商广告/搜索场景，该方案的细粒度语义建模能力可直接用于创意优选，无需额外构建独立的创意排序模型，提升同品下创意点击率'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业电商搜索CTR预测需同时建模物品内容、查询相关性、用户个性化三类信号，传统ID-based模型存在冷启动效果差、无法利用多模态语义信息的问题；现有多模态融合方案要么存在连续特征与稀疏ID空间分布不匹配的问题，要么全局量化的Semantic ID丢失细粒度结构信息，无法支撑细粒度语义匹配与同品创意差异化排序需求。

### 方法关键点
- 阶段I细粒度内容token化：用预训练多尺度VAR视觉tokenizer生成1×1到4×4共30个空间索引的视觉Semantic ID，不同文本域用独立BPE/ngram tokenizer生成文本ID，两类ID均与原生ID共享lookup接口，保留多模态细粒度结构信息
- 阶段II全参数语义预训练：用Qwen3.5微调生成的查询-物品相关性软标签训练整个CTR共享backbone，注入通用语义匹配先验，全参数更新包括ID embedding、交互层在内的所有共享参数
- 阶段III个性化后训练：直接复用阶段II的所有共享参数，替换任务头后用用户点击日志端到端微调，无需额外模态融合或对比损失，适配个性化偏好建模

### 关键实验
在淘宝512亿曝光工业数据集、公开MMCTR数据集上对比HiFormer、COINS等SOTA方案：淘宝离线整体AUC+0.25pt、GAUC+0.26pt，冷启动商品AUC+0.38pt，同品创意排序NSCTR+0.75%，所有指标均显著优于基线；线上7天AB测实现点击IPV+0.21%、GMV+0.85%，无显著推理延迟上升；公开MMCTR数据集上即使去掉相关性预训练阶段，AUC仍比基线高0.77pt，泛化性优异。

### 核心结论
把多模态内容转成与原生ID兼容的细粒度离散表示，再通过渐进式训练注入语义先验，是工业场景低成本融合多模态语义提升CTR效果的可行路径。
