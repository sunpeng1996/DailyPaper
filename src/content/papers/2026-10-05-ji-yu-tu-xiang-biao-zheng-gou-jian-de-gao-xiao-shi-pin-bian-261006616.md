---
title: Video Encoders Built on Image Representations
title_zh: 基于图像表征构建的高效视频编码器
authors:
- Jusheng Zhang
- Wenhao Wang
- Longqi Cai
- Liangzhe Yuan
- Yuxiao Wang
- Ming-Hsuan Yang
affiliations:
- Google DeepMind
- Stanford University
- Vast Intelligence Lab
arxiv_id: '2610.06616'
url: https://arxiv.org/abs/2610.06616
pdf_url: https://arxiv.org/pdf/2610.06616
published: '2026-10-05'
collected: '2026-10-06'
category: Multimodal
direction: 多模态 · 视频LLM高效视觉编码
tags:
- Video-LLM
- Visual Token Compression
- Efficient Inference
- Multimodal Encoding
- Temporal Modeling
one_liner: 拆分帧表征、跨帧token分配与时序交互，用28%-35%视觉token达到全图像路径的视频理解性能
practical_value: '- 电商商品短视频理解、直播内容召回场景可复用其压缩逻辑：先逐帧生成独立表征再做query相关token选择，用更少token保留关键信息，降低推理成本

  - 多模态Agent处理长视频/直播流时，可借鉴「先选关键锚点token，再补充相邻帧上下文做残差更新」的架构，平衡性能和时延

  - 视频广告物料打分、短视频标签生成场景，可复用其问题感知的DPP选择策略，同时保证token的相关性和多样性，避免冗余占用预算

  - 工程上可参考其训练方案：仅训练轻量时序精炼模块，冻结图像编码器和大模型，小数据量即可快速适配业务，训练成本极低'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
原生视频编码（如Conv3D）会在编码早期混合相邻帧信息，导致帧级关键证据无法独立选择；全帧独立编码方案虽保留了所有帧信息，但视觉token量过大，会大幅提升视频LLM的推理时延和内存占用，现有压缩方案要么损失关键时序信息，要么性能下降明显，亟需兼顾性能和token效率的视频编码方案。

### 方法关键点
- 拆分三个耦合步骤：先使用冻结的图像编码器生成每帧独立的表征候选，完整保留帧级原始信息
- 问题感知token选择器：结合相关性、多样性、跨帧对应关系，在固定token预算下跨帧分配slot，仅保留和query相关的关键锚点，不修改原始表征
- 轻量时序精炼模块：仅对选中的锚点token读取相邻帧上下文做残差更新，输出token数保持固定，不增加大模型输入长度，仅训练该模块，其余组件全部冻结

### 关键实验
在13个视频理解基准、3个Qwen-VL系列backbone上测试，对比Conv3D、全图像路径及FlashVID、VidCom2等7种SOTA压缩方案：仅用28%-35%的全图像路径视觉token，就达到甚至超过全图像路径的平均性能；在Qwen3-VL-32B上，13个基准平均得分66.28（全图像路径为66.09），端到端推理速度提升2.16倍，GPU内存占用降低1.39GB。

最值得记住的结论：紧凑视频编码不需要在选择前就做时序混合，完全可以先保留帧级独立证据、再联合分配token预算、最后补充时序上下文，在大幅降低token量的同时不损失性能。
