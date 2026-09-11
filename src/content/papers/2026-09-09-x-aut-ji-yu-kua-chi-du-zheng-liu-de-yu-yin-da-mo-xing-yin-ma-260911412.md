---
title: 'X-AuT: Progressive Audio-Encoder Compression for Speech LLMs with Cross-Scale
  Distillation'
title_zh: X-AuT：基于跨尺度蒸馏的语音大模型音频编码器渐进压缩框架
authors:
- Haojun Zhang
- Yi Zou
- Min Chen
- Qize Yu
- Lianrui Fan
- Xini Ding
- Hao Li
- Shuchang Zhou
- Xianming Liu
- Shiyu Huang
affiliations:
- XPeng Inc.
arxiv_id: '2609.11412'
url: https://arxiv.org/abs/2609.11412
pdf_url: https://arxiv.org/pdf/2609.11412
published: '2026-09-09'
collected: '2026-09-11'
category: Training
direction: 语音LLM · 编码器压缩与蒸馏
tags:
- Model Compression
- Knowledge Distillation
- LoRA
- Speech LLM
- Structured Pruning
one_liner: 提出渐进剪枝+跨尺度蒸馏的语音LLM编码器压缩方案，减20.7%参数几乎不降精度
practical_value: '- 端侧/车载Agent的多模态模型压缩可复用「渐进剪枝+短探针筛选可恢复层组合」方案，避免直接剪枝的精度跳水问题

  - 跨尺度蒸馏策略可迁移到小模型对齐大模型场景，用更大规格的teacher替代同规模自蒸馏，可大幅降低压缩后的精度损失

  - 蒸馏训练采用「主干冻结+仅注意力LoRA+输出层微调」的参数配置，可在保留预训练能力的同时大幅降低训练算力开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
语音大模型的音频编码器是端侧（车载、移动设备）推理首包延迟的核心瓶颈，直接剪枝编码器层会导致输入到解码器的嵌入分布偏移，引发提前EOS、识别漏字等严重错误。现有压缩方案要么需要从头训练轻量化编码器，成本极高；要么采用同尺度自蒸馏，精度损失大，亟需低成本的后训练压缩方案。
### 方法关键点
- 渐进式剪枝：分18→16→14层两步剪枝，每步剪前用0.3 epoch的短训练探针筛选可恢复的层组合，解决静态层重要性评分无法捕捉层间交互的问题
- 三阶段恢复训练：Stage0做跨尺度表示对齐，用1.7B大教师的中间层、桥接层输出蒸馏，加MLP投影适配师生维度差；Stage1混合教师强制和调度式学生策略蒸馏，过滤退化生成样本；Stage2仅用目标域数据做LoRA微调，冻结LLM主干和输出层
- 数据过滤：构建9级转录一致性数据集，蒸馏全程用最高一致性的纯净数据，微调阶段重加权目标域样本提升域内性能
### 关键实验
在10个中英ASR公开基准上测试，基线为Qwen3-ASR-0.6B 18层编码器：1. 16层压缩版宏平均错误率从5.61%降至5.27%，精度反超基线；2. 14层压缩版音频塔参数减少20.7%，宏平均错误率仅5.75%，比直接剪枝的6.73%低0.98pp，编码器延迟在车载PPU下降21.4%，H800下降11.4%；3. 跨尺度1.7B教师蒸馏比同规模自蒸馏的平均错误率从8.45%降至5.55%。
### 核心结论
结构化剪枝后的模型恢复效果无法通过单层级重要性评分预测，渐进剪枝+大教师跨尺度蒸馏是低成本压缩预训练多模态模型的高性价比路径。
